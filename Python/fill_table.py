import psycopg2
import json


def fillTable(connectString, tableName, jsonName, columnNames, columnTypes, executeAfter=1000, fileLength=-1):
    # Connect to 315 database
    # Use an environment variable too access db password
    conn = psycopg2.connect(connectString)
    cur = conn.cursor()
    print("Connected to table: " + tableName)
    # Read in json data
    file_length = 0
    if fileLength == -1:
        with open(jsonName, encoding='utf-8') as f:
            for line in f:
                print('\r', "File loading: " + str(file_length), end='')
                file_length += 1
                # data.append(json.loads(line))
            print()
    else:
        file_length = fileLength
    with open(jsonName, encoding='utf-8') as f:
        # Iterate over each line of the data, which in this case is a separate json data entry
        progress = 0
        execute_string = ""
        for LINE in f:
            line = json.loads(LINE)
            # Messy, but don't attempt to insert if a data field isn't read properly
            missing_data = False
            tableEntry = "insert into " + tableName + " values (\n"
            endLine = ",\n"

            for i in range(len(columnNames)):
                if columnNames[i] in line:
                    value = line[columnNames[i]]
                    ctype = columnTypes[i]
                    if 'text' in ctype:
                        value = str(value).replace("'", "''")
                        if 'text[]' in ctype:
                            array = value.split(",")
                            value = ""
                            value += "{"
                            for j in range(len(array)):
                                value += "\"" + str(array[j]) + "\""
                                if j != len(array) - 1:
                                    value += ", "
                            value += "}"
                        tableEntry += "\'" + str(value) + "\'"
                    elif 'json' in ctype:
                        if str(value) == 'None':
                            value = 'NULL'
                            tableEntry += value
                        else:
                            jsonLine = str(value)
                            # This whole block accounts for misc error when using json as column type
                            # Messy, but works for business.json file
                            jsonLine = jsonLine.replace("\"", "?")
                            jsonLine = jsonLine.replace("\'", "\"")
                            jsonLine = jsonLine.replace("?", "\'")

                            jsonLine = jsonLine.replace(" False", " \"False\"")
                            jsonLine = jsonLine.replace(" True", " \"True\"")
                            jsonLine = jsonLine.replace(" None", " \"None\"")

                            dj = jsonLine.find("\'u\"")
                            while dj != -1:
                                jsonLine = jsonLine[:dj] + \
                                    "\"u_" + jsonLine[dj + 3:]
                                dk = jsonLine.find("\"\'", dj)
                                jsonLine = jsonLine[:dk +
                                                    1] + "" + jsonLine[dk + 2:]
                                dj = jsonLine.find("\'u\"")
                            jsonLine = jsonLine.replace("\'u\"", "\"uno\"")

                            jsonLine = jsonLine.replace("'{", "{")
                            jsonLine = jsonLine.replace("}'", "}")
                            jsonLine = jsonLine.replace("'\"", "\"")
                            jsonLine = jsonLine.replace("\"'", "\"")
                            tableEntry += "\'" + jsonLine + "\'"
                    elif 'bool' in ctype:
                        if value == 1:
                            value = True
                        elif value == 0:
                            value = False
                        tableEntry += str(value)
                    else:
                        tableEntry += str(value)
                    if i == len(columnNames) - 1:
                        endLine = "\n);\n"
                    tableEntry += endLine
                else:
                    missing_data = True
                    print("Data missing: " +
                          columnNames[i] + " in line " + str(progress))

            # Only insert the values to test if they are all present
            if not missing_data:
                # WARNING: Will halt operation if there is a duplicate PRIMARY_KEY
                execute_string += tableEntry

            if progress % (file_length // 1000) == 0:
                percent_progress = int(100 * progress / file_length)
                print('\r', "Progress: " + str(progress) + " lines out of " + str(file_length) +
                      " (" + str(percent_progress) + " %)", end='')
            if progress % executeAfter == 0:
                # print(execute_string)
                cur.execute(execute_string)
                execute_string = ""
            progress += 1
        cur.execute(execute_string)
    # Commit everything to the database
    print('\r', "Progress: " + str(file_length) +
          " lines out of " + str(file_length) + " (100 %)", end='')
    conn.commit()
    print("\nTable filled: " + tableName)
