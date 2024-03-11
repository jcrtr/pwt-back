import csv
import re
import sqlite3
import uuid

import bleach


def text_format(i):
    pattern = r'\[[^\[\]]*\]'
    format_text = bleach.clean(i, tags=[], strip=True)
    text = re.sub(pattern, '', format_text)
    text = re.sub("^\s+|\n|\n\n|\r|\s+$", '', text)
    return text


def main():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        with open('wc.csv', mode='r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                art = text_format(row[2])
                name = text_format(row[3])

                short_description = text_format(row[7])
                description = text_format(row[8])
                price = row[25]

                print(art, name, description, price)
                sqlite_insert_with_param = """INSERT INTO product_product (id, is_active, priority, name, short_description, description, price, slug) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                data_tuple = (str(uuid.uuid4().hex), True, 0, name, short_description, description, price, art)
                cursor.execute(sqlite_insert_with_param, data_tuple)
                sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


if __name__ == "__main__":
    main()
