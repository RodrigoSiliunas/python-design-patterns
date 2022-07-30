"""
    O conceito de metaclasses é algo avançado em qualquer linguagem de programação.
    Esse código tem a pretenção de utilizar uma metaclasse chamada MetaSingleton para definir o
    comportamento de criação de outras classes, transformando-as em Singletons;
"""

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs) -> None:
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Singleton(metaclass=MetaSingleton):
    pass


singleton_one = Singleton()
singleton_two = Singleton()

print(
    f'A primeira chamada o objeto possui um ID de: {id(singleton_two)}\n'
    f'A segunda chamada o objeto possui um id de: {id(singleton_two)}')

"""
    Os mesmos identificadores são exibidos para cada instância criada do Singleton, provando que
    nossa metaclasse está definindo o comportamento de criação de outras classes.
"""
