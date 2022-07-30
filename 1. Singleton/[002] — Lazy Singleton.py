class LazySingleton:
    _instance = None

    def __init__(self, *args, **kwargs) -> None:
        if LazySingleton._instance is None:
            print('O método __init__ foi chamado;')
        else:
            print(f'A instância já foi criada. {self.get_instance()}')

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = LazySingleton(*args, **kwargs)

        return cls._instance


# A classe é inicializada entretando o objeto não é criado;
lazy_singleton = LazySingleton()

# O objeto só passa a ser criado quando chamamos o classmethod get_instance;
lazy_singleton.get_instance()

"""
    A instância já foi criada, então não importa quantas vezes chamamos sempre receberemos como retorno o
    objeto criado quando chamamos get_instance() pela primeira vez;

    Na prática isso significa que lazy_singleton é igual a new_lazy_singleton_instance.
"""
new_lazy_singleton_instance = LazySingleton()
