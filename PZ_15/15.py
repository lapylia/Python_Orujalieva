import sqlite3 as sq
from prettytable import PrettyTable

DATABASE = 'notary_services.db'
TABLE_NAME = 'services'

def create_table(cur):
    cur.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME}
                    (surname_klient varchar(20) not null,
                    name_klient varchar(20) not null,
                    lastname_klient varchar(20) not null,
                    notary_type varchar(30) not null,
                    sum_of_transaction decimal(10,2) not null,
                    dohod decimal(10,2) not null)""")

def insert_data(cur, data):
    cur.executemany(f"INSERT INTO {TABLE_NAME} VALUES (?, ?, ?, ?, ?, ?)", data)

def display_table(cur):
    cur.execute(f"SELECT * FROM {TABLE_NAME}")
    table = PrettyTable(["Фамилия", "Имя", "Отчество", "Тип услуги", "Сумма сделки", "Доход"])
    for row in cur.fetchall():
        table.add_row(row)
    print("Таблица с данными:")
    print(table)

def execute_select(cur, query, params=()):
    cur.execute(query, params)
    print(f"{query} {params}:", cur.fetchall())

def execute_delete(cur, query, params=()):
    cur.execute(query, params)
    print(f"{query} {params}: Deleted.")

def execute_update(cur, query, params=()):
    cur.execute(query, params)
    print(f"{query} {params}: Updated.")

try:
    with sq.connect(DATABASE) as con:
        cur = con.cursor()

        # Create table and insert data
        create_table(cur)
        information = [
            ("Куц", "Сергей", "Сергеевич", "Договор купли-продажи квартиры", 3200, 1100),
            ("Манушкина", "Анна", "Владимировна", "Доверенность на имущество", 2500, 800),
            ("Алиев", "Борис", "Алексеевич", "Дарение автомобиля", 3800, 1400),
            ("Гродь", "Елена", "Николаевна", "Свидетельство о наследстве", 3000, 1000),
            ("Попов", "Руслан", "Игоревич", "Брачный договор", 2800, 900),
            ("Дмитриева", "Ольга", "Викторовна", "Продажа дачного участка", 3500, 1200),
            ("Александров", "Артемий", "Романович", "Доверенность на представительство", 2200, 700),
            ("Голубенко", "Татьяна", "Михайловна", "Оформление завещания", 2600, 850),
            ("Коновалов", "Алексей", "Викторович", "Договор займа", 3100, 1050),
            ("Пороро", "Аврора", "Сергееевна", "Продажа коммерческой недвижимости", 3400, 1300)
        ]
        insert_data(cur, information)
        con.commit()

        # Display the table
        display_table(cur)

        # SELECT examples
        execute_select(cur, f"SELECT * FROM {TABLE_NAME} WHERE surname_klient = ?", ("Дмитриев",))
        execute_select(cur, f"SELECT * FROM {TABLE_NAME} WHERE notary_type = ?", ("Договор купли-продажи квартиры",))
        execute_select(cur, f"SELECT surname_klient, notary_type, sum_of_transaction, dohod FROM {TABLE_NAME} WHERE dohod > ?", (1000,))

        # DELETE examples
        execute_delete(cur, f"DELETE FROM {TABLE_NAME} WHERE surname_klient = ?", ("Гродь",))
        con.commit()

        execute_delete(cur, f"DELETE FROM {TABLE_NAME} WHERE sum_of_transaction < ?", (2600,))
        con.commit()

        execute_delete(cur, f"DELETE FROM {TABLE_NAME} WHERE dohod > ?", (1000,))
        con.commit()

        # UPDATE examples
        execute_update(cur, f"UPDATE {TABLE_NAME} SET notary_type = ? WHERE surname_klient = ? AND name_klient = ? AND lastname_klient = ?",("Продажа дачного участка", "Пороро", "Аврора", "Сергееевна"))
        con.commit()

        execute_update(cur, f"UPDATE {TABLE_NAME} SET sum_of_transaction = ? WHERE surname_klient = ? AND name_klient = ? AND lastname_klient = ?",(3500, "Манушкина", "Анна", "Владимировна"))
        con.commit()

        execute_update(cur, f"UPDATE {TABLE_NAME} SET dohod = ? WHERE notary_type = ?", (1300, "Продажа коммерческой недвижимости"))
        con.commit()


except sq.Error as e:
    print(f"Произошла ошибка: {e}")
