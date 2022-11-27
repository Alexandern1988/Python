                    # CREATE TABLES #
################################################################
try:
    create_dwh_dim_call_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_DimCallType')
        CREATE TABLE DWH_DimCallType (
            KeyCallType int
            ,DescCallTypeCode varchar(100)
            ,DescCallType varchar(100)
            ,DescFullCallType varchar(100)
            ,DescCallTypePriceCategory varchar(100)
            ,DescCallTypeCategory varchar(100)
        )
    """
except Exception as e:
    print('Error creating DWH_DimCallType')
    print(e)


try:
    create_dwh_dim_countries = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_DimCountries')
        CREATE TABLE DWH_DimCountries (
            KeyCountry int 
            ,DescCountry varchar(100)
            ,DescRegion	varchar(100)
            ,DescArea varchar(100)
        )
    """
except Exception as e:
    print('Error creating DWH_DimCountries')
    print(e)


try:
    create_dwh_dim_package_catalog = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_DimPackageCatalog')
        CREATE TABLE DWH_DimPackageCatalog (
            KeyPackage	int 
            ,DescPackage varchar(120)
            ,DatePackageCreation date
            ,DatePackageEnd	date
            ,DescPackageStatus varchar(100)
            ,CodePackageActivitiesDays int
        )
    """
except Exception as e:
    print('Error creating DWH_DimPackageCatalog')
    print(e)



try:
    create_dwh_dim_operators = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_DimOperators')
        CREATE TABLE DWH_DimOperators (
            KeyOperator	int 
            ,DescOperator varchar(50)
            ,DescKeyPrefix varchar(3)
        )
    """
except Exception as e:
    print('Error creating DWH_DimOperators')
    print(e)


try:
    create_dwh_dim_customers = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_DimCustomers')
        CREATE TABLE DWH_DimCustomers (
            ,KeyCustomer int
            ,KeyOperator int 
            ,DescCustomerLineOperator varchar(50)
            ,KeyCountry int
            ,DescCustomerLineCountry varchar(100)
            ,DescCustomerName varchar(100)
            ,DescCustomerAddress varchar(100)
            ,DescCusomterPackage varchar(100)
        )
    """
except Exception as e:
    print('Error creating DWH_DimCustomers')
    print(e)


try:
    create_dwh_dim_call_origin_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_DimCallOriginType')
        CREATE TABLE DWH_DimCallOriginType (
            KeyCallOriginType int 
            ,DescCallOriginType varchar(100)
        )
    """
except Exception as e:
    print('Error creating DWH_DimCallOriginType')
    print(e)


try:
    create_dwh_fact_usage = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_FactUsage')
        CREATE TABLE DWH_FactUsage (
            CallId	int 
            ,KeyCustomer int
            ,KeyCallType int
            ,KeyOriginCountry int
            ,KeyDestinationCountry int
            ,KeyOriginOperator int
            ,KeyDestinationCountry
            ,KeyDestinationOperator int
            ,DestinationCountry varchar(100)
            ,DestinationOperator varchar(100)
            ,KeyPackage	int
            ,KeyCallOriginType int
            ,KeyCallDate int
            ,Duration int
            ,BillableDuration int
            ,Amount	float
            ,BillableAmount	float
        )
    """
except Exception as e:
    print('Error creating DWH_FactUsage')
    print(e)


try:
    create_dwh_dim_date = """
    IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'DWH_DimDate')
    CREATE TABLE DWH_DimDate (
        FullDate datetime
        ,KeyDate int
        ,KeyMonth int
        ,CodeYear int
        ,CodeQuarter int
        ,CodeMonth int
        ,DescMonth varchar(10)
        ,CodeDayInWeek int
        ,DescDayInWeek varchar(10)
    )
    """
except Exception as e:
    print('Error creating DWH_DimDate')
    print(e)



################################################################


dwh_create = [
    create_dwh_dim_call_type,
    create_dwh_dim_countries,
    create_dwh_dim_package_catalog,
    create_dwh_dim_operators,
    create_dwh_dim_customers,
    create_dwh_dim_call_origin_type,
    create_dwh_fact_usage,
    create_dwh_dim_date
]


