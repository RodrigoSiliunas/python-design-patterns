class MetaSingleton:
    __instances = {}

    def __new__(cls, *args, **kwargs) -> None:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(
                MetaSingleton, cls).__new__(cls, *args, **kwargs)

        return cls.__instances[cls]


class SanityCheck:
    __instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls.__instance is None:
            cls.__instance = super(SanityCheck, cls).__new__(
                cls, *args, **kwargs)

        return cls.__instance

    def __init__(self) -> None:
        self.__servers = []

    def verify_server(self, server: int) -> None:
        print(f'Verificando o {self.__servers[server]}...')

    def add_server(self) -> None:
        self.__servers.append('server um')
        self.__servers.append('server dois')
        self.__servers.append('server três')
        self.__servers.append('server quatro')
        self.__servers.append('server cinco')

    def change_server(self) -> None:
        self.__servers.pop()
        self.__servers.append('server seis')


sanity_check_one = SanityCheck()
sanity_check_two = SanityCheck()

sanity_check_one.add_server()
print(
    f'Executando verificação de sanidade dos servidores A...')

for server in range(5):
    sanity_check_one.verify_server(server)

sanity_check_two.change_server()
print(
    f'Executando verificação de sanidade dos servidores B...')

for server in range(5):
    sanity_check_two.verify_server(server)
