import numpy as np
import pandas as pd
import sqlalchemy


# Create a connection
def create_engine(database='TheVoice'):
   engine = sqlalchemy.create_engine(f"mssql+pyodbc://LAPTOP-S6MHQN3G/{database}?driver=SQL+Server+Native+Client+11.0")
   #conn = engine.connect()
   
   return engine #, conn

def close_engine():
    #global conn 
    global engine
    #conn.close()
    engine.dispose()

# Start Data Manipulations
engine = create_engine()

                            # MRR
##############################################################


# Load into dataframes
mrr_call_type =         pd.read_sql_table(table_name= 'call_type', con= engine)
mrr_countries =         pd.read_sql_table(table_name= 'countries', con= engine)
mrr_customer =          pd.read_sql_table(table_name= 'customer', con= engine)
mrr_customer_invoice =  pd.read_sql_table(table_name= 'CUSTOMER_INVOICE', con= engine)
mrr_customer_lines =    pd.read_sql_table(table_name= 'customer_lines', con= engine)
mrr_opfileopp =         pd.read_sql_table(table_name= 'customer_lines', con= engine)
mrr_opfileopp =         pd.read_sql_table(table_name= 'OPFILEOPP', con= engine)
mrr_package_catalog =   pd.read_sql_table(table_name= 'Package_Catalog', con= engine)
mrr_usage_main =        pd.read_sql_table(table_name= 'USAGE_MAIN', con= engine)
mrr_xxCountryType =     pd.read_sql_table(table_name= 'XXCOUNTRYPRE', con= engine)


mrr_dict = {
    'MRR_CALL_TYPE': mrr_call_type,
    'MRR_COUNTRIES': mrr_countries,
    'MRR_CUSTOMER': mrr_customer,
    'MRR_CUSTOMER_INVOICE': mrr_customer_invoice,
    'MRR_CUSTOMER_LINES': mrr_customer_lines,
    'MRR_OPFILEOPP': mrr_opfileopp,
    'MRR_PACKAGE_CATALOG': mrr_package_catalog,
    'MRR_USAGE_MAIN': mrr_usage_main,
    'MRR_XXCOUNTRY_PRE': mrr_xxCountryType
}

# Load into MRR_TheVoice
def process_mrr(engine):

    for tb,df in mrr_dict.items():
        try:
            df.to_sql(name= tb, con= engine, schema= 'dbo', if_exists= 'replace', index= False)
            print(f'{tb} was loaded successfully')
        except Exception as e:
            print(f'Error loading {tb}')
            print(e)




                            # STG
##############################################################

                ### STG_DimCallType ###

price_per_minute_var = 0.5

# Create dataframe
stg_DimCallType =  mrr_call_type[['call_type_code','call_type_desc','call_type']].rename(columns = {
    'call_type_code': 'DescCallTypeCode','call_type_desc':'DescCallType','call_type':'DescCallTypeCategory'})

# calculated columns
stg_DimCallType['KeyCallType'] = mrr_call_type.index
stg_DimCallType['DescCallTypePriceCategory'] = np.where(mrr_call_type.priceperminuter > price_per_minute_var, 'Discounted Price', 'Normal Price')
stg_DimCallType['DescFullCallType'] = mrr_call_type['call_type_code'] + mrr_call_type['call_type_desc']


                ### STG_DimCountries ###

# # Create dataframe
stg_DimCountries = mrr_xxCountryType.merge(mrr_countries, how = 'inner', on = 'COUNTRY_CODE')[['COUNTRY_PRE', 'COUNTRY_CODE', 'REGION', 'AREA']].rename(columns = {
    'COUNTRY_PRE': 'KeyCountry', 'COUNTRY_CODE': 'DescCountry', 'REGION': 'DescRegion', 'AREA': 'DescArea'
})

stg_DimCountries['KeyCountry'] = stg_DimCountries.KeyCountry.astype(int)


                ### STG_DimPackageCatalog ###

# Create dataframe
stg_DimPackageCatalog = mrr_package_catalog[['PACKAGE_NUM','pack_desc','enddate','createdate']].rename(columns = {
    'PACKAGE_NUM': 'KeyPackage', 'pack_desc': 'DescPackage', 'enddate': 'DatePackageEnd', 'createdate': 'DatePackageCreation'
})

# calculated columns
stg_DimPackageCatalog['CodePackageActivitiesDays'] = stg_DimPackageCatalog.DatePackageEnd - stg_DimPackageCatalog.DatePackageCreation
stg_DimPackageCatalog['DescPackageStatus'] = np.where(mrr_package_catalog.status == 1, 'Active', 'Inactive')


                ### STG_DimOperators ###

# Create dataframe
stg_DimOperators = mrr_opfileopp[['OPCCC','prepre','OPDDD']].rename(columns = {'OPCCC': 'KeyOperator', 'prepre': 'DescKeyPrefix'})

# Calculated columns
stg_DimOperators['DescOperator'] = stg_DimOperators.DescKeyPrefix.astype(str) + '-' + stg_DimOperators.OPDDD

# Final stage
stg_DimOperators = stg_DimOperators[['KeyOperator', 'DescKeyPrefix', 'DescOperator']]
stg_DimOperators.KeyOperator = stg_DimOperators.KeyOperator.astype(int)


                ### STG_DimCustomers ###

# Create dataframe
stg_DimCustomers = mrr_customer.merge(mrr_customer_lines, how = 'inner', left_on = 'CUST_NUMBER', right_on = 'PHONE_NO')[['customer_id','PHONE_NO','cust_name','address','DESC']]

# Get operator code and name
stg_DimCustomers['PHONE_NO'] = stg_DimCustomers['PHONE_NO'].map(str)
stg_DimCustomers['Operator_code'] = np.where(stg_DimCustomers.PHONE_NO.str.len() == 12, stg_DimCustomers.PHONE_NO.str[2:5], stg_DimCustomers.PHONE_NO.str[4:6]).astype(int)

# Join opifileopp
stg_DimCustomers = stg_DimCustomers.merge(mrr_opfileopp, how = 'left', left_on = 'Operator_code', right_on = mrr_opfileopp.prepre.astype(int))
stg_DimCustomers['Operator_name'] = np.where(stg_DimCustomers.OPDDD.isna(), 'Unknown', stg_DimCustomers.OPDDD)

# Get country code
stg_DimCustomers['country_code'] = np.where(stg_DimCustomers.PHONE_NO.str.len() == 12, stg_DimCustomers.PHONE_NO.str[3:4], stg_DimCustomers.PHONE_NO.str[1:4]).astype(int)
stg_DimCustomers['country_code'] = np.where(stg_DimCustomers.country_code.isna(), -1, stg_DimCustomers.country_code)

# Join xxCountryType
stg_DimCustomers = stg_DimCustomers.merge(mrr_xxCountryType, how = 'left', left_on = 'country_code', right_on = mrr_xxCountryType.COUNTRY_PRE.astype(int))

# Final stage dataframe
stg_DimCustomers = stg_DimCustomers[['customer_id', 'Operator_code', 'Operator_name','country_code','COUNTRY_CODE','cust_name'
                                     ,'address','DESC']].rename(columns = {
    'customer_id': 'KeyCustomer',
    'Operator_code': 'KeyOperator',
    'Operator_name': 'DescCustomerLineOperator',
    'country_code': 'KeyCountry',
    'COUNTRY_CODE': 'DescCustomerLineCountry',
    'cust_name': 'DescCustomerName',
    'address': 'DescCustomerAddress',
    'DESC': 'DescCusomterPackage'
})



                ### STG_DimCallOriginType ###

# Create dataframe 
stg_DimCallOriginType = pd.DataFrame(mrr_usage_main.CELL_ORIGIN)

# Calculated columns
stg_DimCallOriginType['DescCallOriginType'] = np.where(stg_DimCallOriginType.CELL_ORIGIN == 1, 'Cellular Call',np.where(stg_DimCallOriginType.CELL_ORIGIN == 0, 'Line Call', 'Unknown'))

# Final staging dataframe
stg_DimCallOriginType = stg_DimCallOriginType.rename(columns = {'CELL_ORIGIN': 'KeyCallOriginType'})



                ### STG_FactUsage ###

# Create dataframe
stg_FactUsage = mrr_usage_main.merge(mrr_customer,        how ='left', left_on= 'CALL_NO',    right_on= 'customer_id')\
                              .merge(stg_DimCallType,     how= 'left', left_on= 'CALL_TYPE',  right_on= 'DescCallTypeCode')\
                              .merge(mrr_customer_lines,  how= 'left', left_on= 'CALLING_NO', right_on= 'PHONE_NO')\
                              .merge(mrr_package_catalog, how= 'left', left_on= 'TYPE',       right_on= 'pack_type')[['CALL_NO','CALLING_NO', 'CUST_ID', 'CALL_TYPE', 'DES_NO', 
                              'CELL_ORIGIN','CALL_DATETIME', 'DURATION', 'RATED_AMNT', 'KeyCallType', 'numberoffreeminutes', 'discountpct', 'TYPE', 'PACKAGE_NUM']]

# Extract origin country and operator code 
stg_FactUsage['KeyOriginCountry'] =  np.where(stg_FactUsage.CALLING_NO.str.len() == 13, stg_FactUsage.CALLING_NO.str[1:4], stg_FactUsage.CALLING_NO.str[1:2])
stg_FactUsage['KeyOriginCountry'] = np.where(stg_FactUsage.KeyOriginCountry.isna(), -1, stg_FactUsage.KeyOriginCountry).astype(int)

stg_FactUsage['KeyOriginOperator'] = np.where(stg_FactUsage.CALLING_NO.str.len() == 13, stg_FactUsage.CALLING_NO.str[4:6], stg_FactUsage.CALLING_NO.str[2:5])
stg_FactUsage['KeyOriginOperator'] = np.where(stg_FactUsage.KeyOriginOperator.isna(), -1, stg_FactUsage.KeyOriginOperator).astype(int)


# Lookup origin country and operator name
stg_FactUsage['OriginCountry'] = np.dot(stg_FactUsage.KeyOriginCountry.values[:, None] == mrr_xxCountryType.COUNTRY_PRE.values, mrr_xxCountryType.COUNTRY_CODE.values)
stg_FactUsage['OriginCountry'] = np.where(stg_FactUsage.OriginCountry == '', 'Unknown', stg_FactUsage.OriginCountry)

stg_FactUsage['OriginOperator'] = np.dot(stg_FactUsage.KeyOriginOperator.astype(int).values[:,None] == mrr_opfileopp.prepre.astype(int).values, mrr_opfileopp.OPDDD.values)
stg_FactUsage['OriginOperator'] = np.where(stg_FactUsage.OriginOperator == '', 'Unknown', stg_FactUsage.OriginOperator)


# Extract destination country and operator code
stg_FactUsage['KeyDestinationCountry'] = np.where(stg_FactUsage.DES_NO.str.len() == 13, stg_FactUsage.DES_NO.str[1:4], stg_FactUsage.DES_NO.str[1:2])
stg_FactUsage['KeyDestinationCountry'] = np.where(stg_FactUsage.KeyDestinationCountry.isna(), -1, stg_FactUsage.KeyDestinationCountry).astype(int)

stg_FactUsage['KeyDestinationOperator'] = np.where(stg_FactUsage.DES_NO.str.len() == 13, stg_FactUsage.DES_NO.str[4:6], stg_FactUsage.DES_NO.str[2:5])
stg_FactUsage['KeyDestinationOperator'] = np.where(stg_FactUsage.KeyDestinationOperator.isna(), -1, stg_FactUsage.KeyDestinationOperator).astype(int)


# Lookup destination country and operator
stg_FactUsage['DestinationCountry'] = np.dot(stg_FactUsage.KeyDestinationCountry.values[:,None] == mrr_xxCountryType.COUNTRY_PRE.values, mrr_xxCountryType.COUNTRY_CODE.values)
stg_FactUsage['DestinationCountry'] = np.where(stg_FactUsage.DestinationCountry == '', 'Unknown', stg_FactUsage.DestinationCountry)

stg_FactUsage['DestinationOperator'] = np.dot(stg_FactUsage.KeyDestinationOperator.values[:, None] == mrr_opfileopp.prepre.astype(int).values, mrr_opfileopp.OPDDD.values)
stg_FactUsage['DestinationOperator'] = np.where(stg_FactUsage.DestinationOperator == '', 'Unknown', stg_FactUsage.DestinationOperator)


# Calculated columns
stg_FactUsage['BillableDuration'] = stg_FactUsage.DURATION - stg_FactUsage.numberoffreeminutes
stg_FactUsage['discountpct'] = np.where(stg_FactUsage.discountpct.isna() | stg_FactUsage.discountpct == 0, stg_FactUsage.RATED_AMNT, stg_FactUsage.discountpct)
stg_FactUsage['BillableAmount'] = stg_FactUsage.RATED_AMNT * stg_FactUsage.discountpct
stg_FactUsage['KeyCallDate'] = (pd.DatetimeIndex(stg_FactUsage.CALL_DATETIME).year.astype(str) + \
                                np.where(pd.DatetimeIndex(stg_FactUsage.CALL_DATETIME).month.astype(str).str.len() == 1, 
                                '0' + pd.DatetimeIndex(stg_FactUsage.CALL_DATETIME).month.astype(str),
                                pd.DatetimeIndex(stg_FactUsage.CALL_DATETIME).month.astype(str)) + \
                                np.where(pd.DatetimeIndex(stg_FactUsage.CALL_DATETIME).day_of_week.astype(str).str.len() == 1, 
                                '0' + pd.DatetimeIndex(stg_FactUsage.CALL_DATETIME).day_of_week.astype(str),
                                pd.DatetimeIndex(stg_FactUsage.CALL_DATETIME).day_of_week.astype(str))).astype(int)

# Final stage dataframe
stg_FactUsage = stg_FactUsage[['CALL_NO','CUST_ID','KeyCallType', 'KeyOriginCountry', 'KeyOriginOperator', 'OriginCountry','OriginOperator', 'KeyDestinationCountry', 
                               'KeyDestinationOperator','DestinationCountry', 'DestinationOperator','CELL_ORIGIN', 'KeyCallDate', 'DURATION', 'BillableDuration', 'RATED_AMNT', 'BillableAmount']].rename(columns={
    'CALL_NO': 'CallId',
    'CUST_ID': 'KeyCustomer',
    'CELL_ORIGIN': 'KeyCallOriginType',
    'DURATION': 'Duration',
    'RATED_AMNT': 'Amount',
})



                ### STG_FactUsage ###

start = mrr_usage_main.CALL_DATETIME.min()
end = mrr_usage_main.CALL_DATETIME.max()

# Create dataframe
stg_DimDate = pd.DataFrame({'FullDate': pd.date_range(start= start, end= end)})

stg_DimDate['KeyDate'] = (pd.DatetimeIndex(stg_DimDate.FullDate).year.astype(str) + \
                          np.where(pd.DatetimeIndex(stg_DimDate.FullDate).month.astype(str).str.len() == 1, 
                          '0' + pd.DatetimeIndex(stg_DimDate.FullDate).month.astype(str),
                          pd.DatetimeIndex(stg_DimDate.FullDate).month.astype(str)) + \
                          np.where(pd.DatetimeIndex(stg_DimDate.FullDate).day_of_week.astype(str).str.len() == 1, 
                          '0' + pd.DatetimeIndex(stg_DimDate.FullDate).day_of_week.astype(str),
                          pd.DatetimeIndex(stg_DimDate.FullDate).day_of_week.astype(str))).astype(int)

stg_DimDate['KeyMonth'] = (pd.DatetimeIndex(stg_DimDate.FullDate).year.astype(str) + \
                           np.where(pd.DatetimeIndex(stg_DimDate.FullDate).month.astype(str).str.len() == 1, 
                           '0' + pd.DatetimeIndex(stg_DimDate.FullDate).month.astype(str),
                           pd.DatetimeIndex(stg_DimDate.FullDate).month.astype(str))).astype(int)
 
stg_DimDate['CodeYear'] = pd.DatetimeIndex(stg_DimDate.FullDate).year
stg_DimDate['CodeQuarter'] = pd.DatetimeIndex(stg_DimDate.FullDate).quarter
stg_DimDate['CodeMonth'] = pd.DatetimeIndex(stg_DimDate.FullDate).month
stg_DimDate['DescMonth'] = pd.DatetimeIndex(stg_DimDate.FullDate).month_name()
stg_DimDate['CodeDayInWeek'] = pd.DatetimeIndex(stg_DimDate.FullDate).day_of_week
stg_DimDate['DescDayInWeek'] = pd.DatetimeIndex(stg_DimDate.FullDate).day_name()


stg_dict = {
    'STG_DimCallType': stg_DimCallType,
    'STG_DimCountries': stg_DimCountries,
    'STG_DimPackageCatalog': stg_DimPackageCatalog,
    'STG_DimOperators': stg_DimOperators,
    'STG_DimCustomers': stg_DimCustomers,
    'STG_DimCallOriginType': stg_DimCallOriginType,
    'STG_FactUsage' : stg_FactUsage,
    'STG_DimDate': stg_DimDate
}

# Load into STG_TheVoice
def process_stg(engine):

    for tb,df in stg_dict.items():
        try:
            df.to_sql(name= tb, con= engine, schema= 'dbo', if_exists= 'replace' , index= False)
            print(f'{tb} was loaded successfully')
        except Exception as e:
            print(f'Error loading {tb}')
            print(e)



                            # DWH
##############################################################


dwh_DimCallType = stg_DimCallType.copy()
dwh_DimCountries = stg_DimCountries.copy()
dwh_DimPackageCatalog = stg_DimPackageCatalog.copy()
dwh_DimOperators = stg_DimOperators.copy()
dwh_DimCustomers = stg_DimCustomers.copy()
dwh_DimCallOriginType = stg_DimCallOriginType.copy()
dwh_FactUsage = stg_FactUsage.copy()
dwh_DimDate = stg_DimDate.copy()

dwh_dict = {
    'DWH_DimCallType': dwh_DimCallType,
    'DWH_DimCountries': dwh_DimCountries,
    'DWH_DimPackageCatalog': dwh_DimPackageCatalog,
    'DWH_DimOperators': dwh_DimOperators,
    'DWH_DimCustomers': dwh_DimCustomers,
    'DWH_DimCallOriginType': dwh_DimCallOriginType,
    'DWH_FactUsage' : dwh_FactUsage,
    'DWH_DimDate': dwh_DimDate
}

# Load into DWH_TheVoice
def process_dwh(engine):

    for tb,df in dwh_dict.items():
        try:
            df.to_sql(name= tb, con= engine, schema= 'dbo', if_exists= 'append' , index= False)
            print(f'{tb} was loaded successfully')
        except Exception as e:
            print(f'Error loading {tb}')
            print(e)


# Close connection
close_engine()
