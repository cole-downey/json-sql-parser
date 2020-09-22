import psycopg2
import csv

csv_filename = "..\Data\\Example Data\example-business.csv"

with open(csv_filename) as csvfile:
    row1 = next(csv.reader(csvfile, delimiter=','))

    tableString = "CREATE TABLE test4(\n"
    tableString += "business_id text PRIMARY KEY,\n"
    data_type = ""
    endLine = ",\n"

    floatNames = ["stars", "latitude", "longitude"]
    intNames = ["review_count"]
    boolNames = ["is_open"]
    for i in range(1, len(row1)):
        col = row1[i]
        if col in floatNames:
            data_type = "float"
        elif col in intNames:
            data_type = "int"
        elif col in boolNames:
            data_type = "bool"
        else:
            data_type = "text"

        col = col.replace(".", "_")
        col = col.replace("-", "_")
        if i == len(row1) - 1:
            endLine = "\n)"
        tableString += col + " " + data_type + endLine
    print(tableString)

# Connect to 315 database
# Use an environment variable too access db password
conn = psycopg2.connect("host=csce-315-db.engr.tamu.edu dbname=db908_group16_project2 user=coledowney password=327003165")
cur = conn.cursor()

# Create a test table in the database
cur.execute(tableString)

# Commit everything to the database
conn.commit()