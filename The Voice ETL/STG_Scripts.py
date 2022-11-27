                    # CREATE TABLES #
################################################################
try:
    create_stg_dim_call_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        CREATE TABLE STG_DimCallType (
            KeyCallType int
            ,DescCallTypeCode varchar(100)
            ,DescCallType varchar(100)
            ,DescFullCallType varchar(100)
            ,DescCallTypePriceCategory varchar(100)
            ,DescCallTypeCategory varchar(100)
        )
    """
except Exception as e:
    print('Error creating STG_DimCallType')
    print(e)


try:
    create_stg_dim_countries = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        CREATE TABLE STG_DimCountries (
            KeyCountry int 
            ,DescCountry varchar(100)
            ,DescRegion	varchar(100)
            ,DescArea varchar(100)
        )
    """
except Exception as e:
    print('Error creating STG_DimCountries')
    print(e)


try:
    create_stg_dim_package_catalog = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        CREATE TABLE STG_DimPackageCatalog (
            KeyPackage	int 
            ,DescPackage varchar(120)
            ,DatePackageCreation date
            ,DatePackageEnd	date
            ,DescPackageStatus varchar(100)
            ,CodePackageActivitiesDays int
        )
    """
except Exception as e:
    print('Error creating STG_DimPackageCatalog')
    print(e)



try:
    create_stg_dim_operators = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        CREATE TABLE STG_DimOperators (
            KeyOperator	int 
            ,DescOperator varchar(50)
            ,DescKeyPrefix varchar(3)
        )
    """
except Exception as e:
    print('Error creating STG_DimOperators')
    print(e)


try:
    create_stg_dim_customers = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        CREATE TABLE STG_DimCustomers(
            KeyCustomer int
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
    print('Error creating STG_DimCustomers')
    print(e)


try:
    create_stg_dim_call_origin_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        CREATE TABLE STG_DimCallOriginType (
            KeyCallOriginType int 
            ,DescCallOriginType varchar(100)
        )
    """
except Exception as e:
    print('Error creating STG_DimCallOriginType')
    print(e)


try:
    create_stg_fact_usage = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        CREATE TABLE STG_FactUsage (
            CallId	int 
            ,KeyCustomer int
            ,KeyCallType int
            ,KeyOriginCountry int
            ,KeyDestinationCountry int
            ,KeyOriginOperator int
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
    print('Error creating STG_FactUsage')
    print(e)


try:
    create_stg_dim_date = """
    IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimDate')
    CREATE TABLE STG_DimDate (
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
    print('Error creating STG_DimTime')
    print(e)

                    # TRUNCATE TABLES #
################################################################

try:
    truncate_stg_dim_call_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallType')
        TRUNCATE TABLE STG_DimCallType
    """
except Exception as e:
    print('Error truncating STG_DimCallType')
    print(e)


try:
    truncate_stg_dim_countries = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCountries')
        TRUNCATE TABLE STG_DimCountries
    """
except Exception as e:
    print('Error truncating STG_DimCountries')
    print(e)


try:
    truncate_stg_dim_package_catalog = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimPackageCatalog')
        TRUNCATE TABLE STG_DimPackageCatalog
    """
except Exception as e:
    print('Error truncating STG_DimPackageCatalog')
    print(e)


try:
    truncate_stg_dim_operators = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimOperators')
        TRUNCATE TABLE STG_DimOperators
    """
except Exception as e:
    print('Error truncating STG_DimOperators')
    print(e) 
    

try:
    truncate_stg_dim_customers = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCustomers')
        TRUNCATE TABLE STG_DimCustomers
    """
except Exception as e:
    print('Error truncating STG_DimCustomers')
    print(e) 


try:
    truncate_stg_dim_call_origin_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimCallOriginType')
        TRUNCATE TABLE STG_DimCallOriginType
    """
except Exception as e:
    print('Error truncating STG_DimCallOriginType')
    print(e) 


try:
    truncate_stg_fact_usage = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_FactUsage')
        TRUNCATE TABLE STG_FactUsage
    """
except Exception as e:
    print('Error truncating STG_FactUsage')
    print(e) 


try:
    truncate_stg_dim_date = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'STG_DimDate')
        TRUNCATE TABLE STG_DimDate
    """
except Exception as e:
    print('Error truncating STG_DimDate')
    print(e)
   
 
################################################################


stg_create = [
    create_stg_dim_call_type,
    create_stg_dim_countries,
    create_stg_dim_package_catalog,
    create_stg_dim_operators,
    create_stg_dim_customers,
    create_stg_dim_call_origin_type,
    create_stg_fact_usage,
    create_stg_dim_date
]

stg_truncate = [
    truncate_stg_dim_call_type,
    truncate_stg_dim_countries,
    truncate_stg_dim_package_catalog,
    truncate_stg_dim_operators,
    truncate_stg_dim_customers,
    truncate_stg_dim_call_origin_type,
    truncate_stg_fact_usage,
    truncate_stg_dim_date
]
