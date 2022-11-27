
from Data_Manipulation import create_engine, close_engine, process_mrr, process_stg, process_dwh
from Create_Databases import create_db
from MRR_Scripts import *
from STG_Scripts import *
from DWH_Scripts import *


                    # Db 
##############################################

# Create database
def create_databases(engine):
    for query in create_db:
        engine.execute(query)


                    # MRR
##############################################

# Create MRR tables
def create_mrr_tables(engine):
    for query in mrr_create:
        engine.execute(query)

# Truncate MRR tables
def truncate_mrr_tables(engine):
    for query in mrr_truncate:
        engine.execute(query)


                    # STG
##############################################

# Create STG tables
def create_stg_tables(engine):
    for query in stg_create:
        engine.execute(query)

# Truncate STG tables
def truncate_stg_tables(engine):
    for query in stg_truncate:
        engine.execute(query)


                    # DWH
##############################################

# Create DWH tables
def create_dwh_tables(engine):
    for query in stg_create:
        engine.execute(query)


def main():
    
    engine = create_engine()
    create_databases(engine)
    close_engine()

    engine = create_engine('MRR_TheVoice')
    create_mrr_tables(engine)
    truncate_mrr_tables(engine)
    process_mrr(engine)
    close_engine()
    
    engine = create_engine('STG_TheVoice')
    create_stg_tables(engine)
    truncate_stg_tables(engine)
    process_stg(engine)
    close_engine()

    engine = create_engine('DWH_TheVoice')
    create_dwh_tables(engine)
    process_dwh(engine)
    close_engine()
    

if __name__ == "__main__":
    main()
    close_engine()









