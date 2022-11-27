
# create mirror database
try:
    mirror_db = """
        IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'MRR_TheVoice')
        CREATE DATABASE MRR_TheVoice
    """
except Exception as e:
    print('Error creating mirror database')
    print(e)

# create staging database
try:
    staging_db = """
        IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'STG_TheVoice')
        CREATE DATABASE STG_TheVoice
    """
except Exception as e:
    print('Error creating staging database')
    print(e)

# create dwh database
try:
    dwh_db = """
        IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'DWH_TheVoice')
        CREATE DATABASE DWH_TheVoice
    """
except Exception as e:
    print('Error creating dwh database')
    print(e)


create_db = [mirror_db,staging_db,dwh_db]
