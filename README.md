# json-sql-parser
#### Takes JSON file as input and converts to sql query form, and uploads to database
#### Must have psycopg2 installed in python to work

This project has 2 main functions: createTable and fillTable
See example-main.py for example of use
Parameters are as follows:

createTable(connectString, tableName, columnNames, columnTypes, addPK=false):

    connectString: string, inputted into psycopg2.connect()
    tableName: string, name of desired table
    columnNames: string[], each item will correspond to a new column, ordered
    columnTypes: string[], each item will correspond to the data type of the columns in columnNames
                 make sure each index lines up with columnNames
                 PRIMARY KEY can also be added, ex: "text PRIMARY KEY"
    addPK: bool, if true will add a primary key int named "id" to column list
           optional, default is false
           for use when data set doesn't have primay key already


fillTable(connectString, tableName, jsonName, columnNames, columnTypes, executeAfter=1000, fileLength=-1):

    connectString: string, inputted into psycopg2.connect()
    tableName: string, name of table
    jsonName: string, file name of selected json
    columnNames: string[], each item will correspond to a column, ordered
    columnTypes: string[], each item will correspond to the data type of the columns in columnNames
                 make sure each index lines up with columnNames
    executeAfter: int, will change the number of lines parsed before running the cursor.execute(), saving the data to psycopg2
                  optional, default is 1000
                  only change for performance reasons
                  increase this number when each item in a json is short in size
    fileLength: int, only used for progress display
                optional, default is -1
                if changed from -1, the step used to check file length will be skipped, instead using this value in the progress display
