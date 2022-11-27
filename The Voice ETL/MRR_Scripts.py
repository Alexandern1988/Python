                    # CREATE TABLES #
################################################################

try:
    mrr_create_call_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CALL_TYPE')
        CREATE TABLE MRR_CALL_TYPE (
            call_type_code varchar(10) not null
            ,call_type_desc varchar(100)
            ,price_per_minute decimal(10,2)
            ,call_type varchar(50)
        )
    """
except Exception as e:
    print('Error creating MRR_CALL_TYPE')
    print(e)


try:
    mrr_create_countries = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_COUNTRIES')
        CREATE TABLE MRR_COUNTRIES (
            country_code varchar(100) not null
            ,description varchar(100)
            ,region varchar(100)
            ,area varchar(100)
            ,insert_date datetime
            ,update_date datetime
        )
    """
except Exception as e:
    print('Error creating MRR_COUNTRIES')
    print(e)


try:
    mrr_create_customer = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CUSTOMER')
        CREATE TABLE MRR_CUSTOMER (
            customer_id int not null
            ,cust_number varchar(20) not null
            ,cust_name varchar(100)
            ,address varchar(100)
            ,insert_date datetime
            ,update_date datetime
        )
    """
except Exception as e:
    print('Error creating MRR_CUSTOMER')
    print(e)


try:
    mrr_create_customer_invoice ="""
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CUSTOMER_INVOICE')
        CREATE TABLE MRR_CUSTOMER_INVOICE (
            invoice_num int not null
            ,phone_num varchar(20) not null
            ,invoice_type varchar(10)
            ,invoice_date datetime
            ,invoice_ind int
            ,invoice_desc varchar(100)
            ,invoice_currency varchar(10)
            ,invoice_amount decimal(10,4)
            ,insert_date datetime
            ,update_date datetime
        )
    """
except Exception as e:
    print('Error creating MRR_CUSTOMER_INVOICE')
    print(e)


try:
    mrr_create_customer_lines = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CUSTOMER_LINES')
        CREATE TABLE MRR_CUSTOMER_LINES (
            phone_no varchar(20) not null
            ,create_date datetime not null
            ,end_date datetime
            ,status varchar(4)
            ,type varchar(10)
            ,description varchar(100)
            ,insert_date datetime
            ,update_date datetime
            ,discount_pct int
            ,number_of_free_minutes decimal(10,4)
        )
    """
except Exception as e:
    print('Error creating MRR_CUSTOMER_LINES')
    print(e)


try:
    mrr_create_opfileopp = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_OPFILEOPP')
        CREATE TABLE MRR_OPFILEOPP (
            opccc varchar(10)
            ,opddd varchar(100)
            ,prepre varchar(3)
        )
    """
except Exception as e:
    print('Error creating MRR_OPFILEOPP')
    print(e)


try:
    mrr_create_package_catalog = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_PACKAGE_CATALOG')
        CREATE TABLE MRR_PACKAGE_CATALOG (
            package_num int not null
            ,create_date datetime
            ,end_date datetime
            ,status varchar(10)
            ,pack_type varchar(10)
            ,pack_desc varchar(100)
            ,insert_date datetime
            ,update_date datetime
        )
    """
except Exception as e:
    print('Error creating MRR_PACKAGE_CATALOG')
    print(e)


try:
    mrr_create_usage_main = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_USAGE_MAIN')
        CREATE TABLE MRR_USAGE_MAIN (
            call_no int not null
            ,answer_time datetime not null
            ,seized_time datetime not null
            ,disconnect_time datetime not null
            ,call_datetime datetime
            ,calling_no varchar(18)
            ,called_no varchar(18)
            ,des_no varchar(25)
            ,duration int
            ,cust_id int
            ,call_type varchar(20)
            ,prod_type varchar(20)
            ,rated_amnt int
            ,rated_curr_code varchar(20)
            ,cell int
            ,cell_origin int
            ,high_low_rate int
            ,insert_date datetime
            ,update_date datetime
        )
    """
except Exception as e:
    print('Error creating MRR_USAGE_MAIN')
    print(e)


try:
    mrr_create_xxcountry_pre = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_XXCOUNTRY_PRE')
        CREATE TABLE MRR_XXCOUNTRY_PRE (
            country_code varchar(100) not null
            ,country_pre varchar(3)
        )
    """
except Exception as e:
    print('Error creating MRR_XXCOUNTRY_PRE')
    print(e)


                    # TRUNCATE TABLES #
################################################################

try:
    mrr_truncate_call_type = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CALL_TYPE')
        TRUNCATE TABLE MRR_CALL_TYPE
    """
except Exception as e:
    print('Error truncating MRR_CALL_TYPE')
    print(e)


try:
    mrr_truncate_countries = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_COUNTRIES')
        TRUNCATE TABLE MRR_COUNTRIES
    """
except Exception as e:
    print('Error truncating MRR_COUNTRIES')
    print(e)


try:
    mrr_truncate_customer = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CUSTOMER')
        TRUNCATE TABLE MRR_CUSTOMER
    """
except Exception as e:
    print('Error truncating MRR_CUSTOMER')
    print(e)


try:
    mrr_truncate_customer_invoice ="""
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CUSTOMER_INVOICE')
        TRUNCATE TABLE MRR_CUSTOMER_INVOICE
    """
except Exception as e:
    print('Error truncating MRR_CUSTOMER_INVOICE')
    print(e)


try:
    mrr_truncate_customer_lines = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_CUSTOMER_LINES')
        TRUNCATE TABLE MRR_CUSTOMER_LINES
    """
except Exception as e:
    print('Error truncating MRR_CUSTOMER_LINES')
    print(e)


try:
    mrr_truncate_opfileopp = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_OPFILEOPP')
        TRUNCATE TABLE MRR_OPFILEOPP
    """
except Exception as e:
    print('Error truncating MRR_OPFILEOPP')
    print(e)


try:
    mrr_truncate_package_catalog = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_PACKAGE_CATALOG')
        TRUNCATE TABLE MRR_PACKAGE_CATALOG
    """
except Exception as e:
    print('Error truncating MRR_PACKAGE_CATALOG')
    print(e)


try:
    mrr_truncate_usage_main = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_USAGE_MAIN')
        TRUNCATE TABLE MRR_USAGE_MAIN
    """
except Exception as e:
    print('Error truncating MRR_USAGE_MAIN')
    print(e)


try:
    mrr_truncate_xxcountry_pre = """
        IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'MRR_XXCOUNTRY_PRE')
        TRUNCATE TABLE MRR_XXCOUNTRY_PRE
    """
except Exception as e:
    print('Error truncating MRR_XXCOUNTRY_PRE')
    print(e)



################################################################


mrr_create = [
    mrr_create_call_type,
    mrr_create_countries,
    mrr_create_customer,
    mrr_create_customer_invoice,
    mrr_create_customer_lines,
    mrr_create_opfileopp,
    mrr_create_package_catalog,
    mrr_create_usage_main,
    mrr_create_xxcountry_pre
    ]
mrr_truncate = [
    mrr_truncate_call_type,
    mrr_truncate_countries,
    mrr_truncate_customer,
    mrr_truncate_customer_invoice,
    mrr_truncate_customer_lines,
    mrr_truncate_opfileopp,
    mrr_truncate_package_catalog,
    mrr_truncate_usage_main,
    mrr_truncate_xxcountry_pre
    ]
