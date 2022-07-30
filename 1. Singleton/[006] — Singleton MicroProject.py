import sqlite3


class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs) -> None:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]


class DatabaseManager(metaclass=MetaSingleton):
    conn = None

    def connect(self):
        """
            Aqui nós verificamos se a conexão é inexistente; caso for, então criamos uma nova conexão.
            Se a conexão for existente então retornamos essa conexão;
        """

        # Essa instrução 'if' é executada apenas uma vez, assim que o método connect é chamado;
        if self.conn is None:
            self.conn = sqlite3.connect('db.singleton')
            self.cursor = self.conn.cursor()
            print("We don't have a connection. Creating a new one...")

        return self.cursor


database_one = DatabaseManager().connect()
database_two = DatabaseManager().connect()
