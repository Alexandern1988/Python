<b>Introduction</b>

The motivation for this project is to develop an ETL process using python and SSMS to create a DWH.
TheVoice is an OLTP call center db, we want to collect the data, transform it and load it into an analytical db.
The final aim is togive the analytical team a db for their analytical needs.


<b>Project Description </b>

In this project, I have to model data with SSMS and build and ETL pipeline using Python. On the database side, I have to define fact and dimension tables for a Star Schema for a specific focus according to our S2T mapping. On the other hand, ETL pipeline would transfer data from the original OLTP db using 3 different databases for each stage MRR, STG and finally DWH.
The original bak file is included with the files.


<b>Schema for Song Play Analysis</b>

<b>Fact Table</b> Records in the log of calling center

<b> FactUsage: </b> 


<b>Dimension Tables</b>

<b> DimCallTypes: </b> Descries call types

<b> DimCountries: </b> Describes Origin\Target countries

<b> DimPackageCatalog: </b> Describes packages offered

<b> DimDate: </b> Date dimention

<b> DimOperators: </b> Describes all providng operators

<b> DimCustomers: </b> Customer information

<b> DimCallOriginType: </b> Describes origin


<b>Project Design</b>

The goal of the database design is to create an optimized db for the analysis needs of the oranization.
 
<b>Files Description</b>

<b>*</b> Create_Databases.py - A script to create all three databases using SQL for each stage MRR, STG and DWH and assign it to python variables.

<b>*</b> MRR_Scripts.py - Use SQL queries to create and truncate for all the tables from the original OLTP db and assign it to python variables.

<b>*</b> STG_Scripts.py - Use SQL queries to create and truncate for all target tables in the final DWH and assign it to python variables.

<b>*</b> DWH_Scripts.py - Use SQL queries to create all target tables in the final DWH and assign it to python variables.

<b>*</b> Data_Manipulation.py - Use python pandas to perform all the data manipulation according to the S2T mapping file

<b>*</b> Process_ETL.py - This is the main file which is used to run the project
    
