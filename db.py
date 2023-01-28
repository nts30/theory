import sqlite3


class Database:
    def __init__(self, db_file: str):
        self.con = sqlite3.connect(db_file)  # Создает подключение
        self.cursor = self.con.cursor()  # Объект курсора

    def create_table_users(self):
        with self.con:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users "
                                "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                "name TEXT, "
                                "age INTEGER)")

    def add_users(self, user: tuple):
        with self.con:
            self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", user)

    def add_many_users(self, users: list):
        """Множественная вставка

        :param users:
        :return:
        """
        with self.con:
            self.cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)

    def  __get_formatted_users(self, users: list):
        """
        Возвращает отформатированных пользователей
        :return:
        """
        for user in users:
            id_ = user[0]
            username = user[1]
            age = user[2]
            print(f'id: {id_}\nusername: {username}\nage: {age}')

    def get_users(self):
        """
        Получение данных из БД

        :return:
        """
        with self.con:
            all_data = self.cursor.execute("SELECT * FROM users")
            self.__get_formatted_users(all_data.fetchall())

    def get_user(self):
        with self.con:
            all_data = self.cursor.execute("SELECT * FROM users").fetchone()
            id_ = all_data[0]
            username = all_data[1]
            age = all_data[2]
            print(f'id: {id_}\nusername: {username}\nage: {age}')

    def get_some_users(self, count: int):
        with self.con:
            all_data = self.cursor.execute("SELECT * FROM users")
            self.__get_formatted_users(all_data.fetchmany(count))

    def update_user(self, name:str, new_name:str):
        with self.con:
            self.cursor.execute("UPDATE users SET name = ? WHERE name = ?", (new_name, name))

    def delete_user(self, id_:int):
        with self.con:
            self.cursor.execute("DELETE FROM users WHERE id = ?", (id_,))

    def clear_table(self):
        with self.con:
            self.cursor.execute("DELETE FROM users")



if __name__ == '__main__':
    database = Database('test.db')
    database.create_table_users()

    peoples = [
        ('user_1', 20), ('user_2', 30), ('user_3', 40)
    ]
    #database.add_many_users(users=peoples)
    #database.get_users()
    #database.get_user()
    #database.get_some_users(2)
    #database.update_user(name='user_2', new_name='Vasya')
    #database.delete_user(id_=33)
    # database.clear_table()
    # database.get_users()
