import fill_table as ft
import create_table as ct

connectString = "host=csce-315-db.engr.tamu.edu dbname=db908_group16_project2 user=USERNAME password=PASSWORD"

tableName = "business_1"
jsonName = '..\Data\\business.json'
columnNames = ['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars',
               'review_count', 'is_open', 'attributes', 'categories', 'hours']
columnTypes = ['text PRIMARY KEY', 'text', 'text', 'text', 'text', 'text', 'float', 'float', 'float', 'int', 'bool',
               'json', 'text[]', 'json']

try:
    ct.createTable(connectString, tableName, columnNames, columnTypes)
    ft.fillTable(connectString, tableName,
                    jsonName, columnNames, columnTypes)
except Exception as e:
    print(e)


tableName = "Tip_1"
jsonName = '..\Data\\tip.json'
columnNames = ['user_id', 'business_id', 'text', 'date', 'compliment_count']
columnTypes = ['text', 'text', 'text', 'text', 'int']

try:
    ct.createTable(connectString, tableName, columnNames, columnTypes)
    ft.fillTable(connectString, tableName, jsonName,
                    columnNames, columnTypes, 10000)
except Exception as e:
    print(e)


tableName = "User_6"
jsonName = '..\Data\\user.json'
columnNames = ['user_id', 'name', 'review_count', 'yelping_since', 'useful', 'funny', 'cool', 'elite', 'friends',
               'fans', 'average_stars', 'compliment_hot', 'compliment_more', 'compliment_profile', 'compliment_cute',
               'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool', 'compliment_funny',
               'compliment_writer', 'compliment_photos']
columnTypes = ['text PRIMARY KEY', 'text', 'int', 'text', 'int', 'int', 'int', 'text', 'text[]',
               'int', 'float', 'int', 'int', 'int', 'int',
               'int', 'int', 'int', 'int', 'int',
               'int', 'int', ]

try:
    ct.createTable(connectString, tableName, columnNames, columnTypes)
    ft.fillTable(connectString, tableName, jsonName,
                    columnNames, columnTypes, 1000, 1968703)
except Exception as e:
    print(e)


tableName = "Checkin_2"
jsonName = '..\Data\\checkin.json'
columnNames = ['business_id', 'date']
columnTypes = ['text PRIMARY KEY', 'text[]']

try:
    ct.createTable(connectString, tableName, columnNames, columnTypes)
    ft.fillTable(connectString, tableName,
                    jsonName, columnNames, columnTypes)
except Exception as e:
    print(e)


tableName = "Review_1"
jsonName = '..\Data\\review.json'
columnNames = ['review_id', 'user_id', 'business_id',
               'stars', 'useful', 'funny', 'cool', 'text', 'date']
columnTypes = ['text PRIMARY KEY', 'text', 'text',
               'float', 'int', 'int', 'int', 'text', 'text']

try:
    ct.createTable(connectString, tableName, columnNames, columnTypes)
    ft.fillTable(connectString, tableName,
                    jsonName, columnNames, columnTypes)
except Exception as e:
    print(e)
