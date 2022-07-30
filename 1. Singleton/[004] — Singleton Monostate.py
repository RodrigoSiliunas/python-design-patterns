"""
    A principal diferença entre monostate e singleton é que o Singleton sempre retorna a mesma instância;
    elas tem o mesmo identificador;

    O monostate diferente do singleton gera uma nova instância a cada vez que é chamada; No entanto o estado dessa instância é compartilhada por todas as outras instâncias.
"""

class Monostate:
    _state = {}

    def __new__(cls, *args, **kwargs) -> None:
        _monostate = super(Monostate, cls).__new__(cls, *args, **kwargs)
        _monostate.__dict__ = cls._state

        return _monostate


first_appears = Monostate()
print(f'A primeira aparição da classe ela recebe um ID: {id(first_appears)}')
print(f'Primeira aparição da classe para dicionário: {first_appears.__dict__}\n')

second_appears = Monostate()
print(f'A segunda aparição da classe ela recebe um ID: {id(second_appears)}')
print(f'Segunda aparição da classe para dicionário: {second_appears.__dict__}')

first_appears.name = 'Alucard'

print(
    f'Primeira aparição da classe para dicionário: {first_appears.__dict__}\n'
    f'Segunda aparição da classe para dicionário: {second_appears.__dict__}'
)
