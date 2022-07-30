"""
    Por padrão o Python transforma módulos em Singletons. Então não importa realmente quantas vezes você
    importa um módulo, o Python sempre retornará a mesma instância desse módulo para você.

    Para provar isso temos esse módulo com duas funções e uma execução, pela lógica não importa quantas
    vezes executemos esse arquívo, ele sempre iria exibir na tela a informação que foi importado.

    No entanto, quando importamos esse módulo mais de uma vez, ele só exibe a instrução uma única vez,
    realmente não importando quantas vezes ele é importado, ele sempre retornará a mesma istância.
"""
NAME = 'Rodrigo Siliunas'


def singleton_function():
    print('Hello World! This is a singleton anti pattern! Funtion one!')


def singleton_function_two():
    print('Hello World! This is a singleton anti pattern! Function two!')


print('The module has been imported with success!')
