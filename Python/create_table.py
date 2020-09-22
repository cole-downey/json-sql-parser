import psycopg2


def createTable(connectString, tableName, columnNames, columnTypes, addPM=False):
    # Connect to 315 database
    conn = psycopg2.connect(connectString)
    cur = conn.cursor()

    tableString = "CREATE TABLE IF NOT EXISTS " + tableName + "(\n"
    endLine = ",\n"
    if addPM:
        tableString += "id int PRIMARY KEY" + endLine
    for i in range(len(columnNames)):
        if i == len(columnNames) - 1:
            endLine = "\n)"
        tableString += columnNames[i] + " " + columnTypes[i] + endLine

    cur.execute(tableString)

    # Commit everything to the database
    conn.commit()
    print("Table Created: " + tableName)
