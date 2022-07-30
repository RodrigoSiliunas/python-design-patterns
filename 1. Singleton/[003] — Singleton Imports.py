"""
    O objetivo desse código foi explicado em modules/Singleton.py;

    * Python transforma importações de módulos em Singleton;
    * Não importa quantas vezes é importado em um arquivo, ele sempre tem o mesmo efeito;
"""

from modules.Singleton import singleton_function
# A linha de cima irá chamar; print('The module has been imported with success!')

singleton_function()

print(
    'Não importa se importamos novamente, o Python vai chamar a mesma instância então não irá exibir na tela a instrução.')

from modules.Singleton import singleton_function_two
# Essa nova importação chamará o mesmo objeto então não irá exibir na tela o: print('The module has been imported with success!').

singleton_function_two()
