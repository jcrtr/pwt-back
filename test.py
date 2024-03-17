import sqlite3
import uuid

data = {
    "Напряжение": "220 В",
    "Частота": "50/60 Гц",
    "Мощность": "250 Вт",
    "Температура нагрева": "600 °C",
    "Режим работы": "1/4 мин-нагревание, 3/4 мин-остывание",
    "В комплекте": "кейс, лезвие (250мм), шестигранный ключ, металлическая щетка, комплект документов",
    "Вес": "576 гр."
}


def main():
    print('OK')
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cur = sqliteConnection.cursor()

        ch_sql = cur.execute("SELECT * FROM product_сharacteristic")
        ch = ch_sql.fetchall()

        pr_sql = cur.execute("SELECT * FROM product_product WHERE slug='PWTSG-004'")
        pr_sql_rows = pr_sql.fetchall()
        pr_id = pr_sql_rows[0][0]

        for i in data:
            for row in ch:
                if row[1] == i:
                    ch_name = row[1]
                    ch_id = row[0]

                    sqlite_insert_with_param = """INSERT INTO product_сharacteristicitem
                    (id, value, characteristic_id, product_id)
                    VALUES
                    (?, ?, ?, ?)
                    """

                    data_tuple = (str(uuid.uuid4().hex), data[i], str(ch_id), str(pr_id))

                    cur.execute(sqlite_insert_with_param, data_tuple)
                    sqliteConnection.commit()

                    print(ch_name, data[i])

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

main()
