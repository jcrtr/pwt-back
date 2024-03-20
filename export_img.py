import csv
import sqlite3
import urllib.request
import uuid


# def text_format(i):
#     pattern = r'\[[^\[\]]*\]'
#     format_text = bleach.clean(i, tags=[], strip=True)
#     text = re.sub(pattern, '', format_text)
#     text = re.sub("^\s+|\n|\n\n|\r|\s+$", '', text)
#     return text


def main():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        with open('wc.csv', mode='r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            сount_id = 1
            for row in csvreader:
                count = 1
                art = row[2]
                img = row[29]
                img_list = list(img.split(","))
                print(art)
                pr_sql = cursor.execute("SELECT * FROM product_product WHERE slug=?", (art,))
                pr_sql_rows = pr_sql.fetchall()
                try:
                    pr_id = pr_sql_rows[0][0]
                except Exception as e:
                    continue

                print(pr_id)

                for i in img_list:
                    print(i)
                    name = f'{art}-{count}'
                    urllib.request.urlretrieve(i, f"./media/public/img/product/{name}.png")

                    img_file = f'public/img/product/{art}-{count}.png'

                    _uuid = str(uuid.uuid4().hex)

                    sqlite_insert_with_param_img = """INSERT INTO product_productimage (id, name, image)
                    VALUES (?, ?, ?)"""
                    data_tuple = (_uuid, name, img_file)
                    cursor.execute(sqlite_insert_with_param_img, data_tuple)
                    sqliteConnection.commit()

                    sqlite_insert_with_param = """INSERT INTO product_product_images (id, product_id, productimage_id)
                    VALUES (?, ?, ?)"""
                    data_tuple = (сount_id, pr_id, _uuid)
                    cursor.execute(sqlite_insert_with_param, data_tuple)
                    sqliteConnection.commit()

                    count = count + 1
                    сount_id = сount_id + 1

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


if __name__ == "__main__":
    main()
