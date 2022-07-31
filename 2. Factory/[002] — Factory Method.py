from abc import ABCMeta, abstractmethod


class Profile(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self) -> None:
        pass

    def get_sections(self) -> list:
        return self._sections

    def add_section(self, section) -> None:
        self._sections.append(section)


class Section(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self) -> str:
        pass


class PersonalSection(Section):
    def __repr__(self) -> str:
        return 'Seção Pessoal'


class AlbumSection(Section):
    def __repr__(self) -> str:
        return 'Seção de Album'


class ProjectSection(Section):
    def __repr__(self) -> str:
        return 'Seção de Projeto'


class PublicationSection(Section):
    def __repr__(self) -> str:
        return 'Seção de Publicação'


class LinkedIn(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PublicationSection())
        self.add_section(ProjectSection())


class Tinder(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PublicationSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    social = input(
        'Em qual rede social deseja criar um perfil?\n[LinkedIn, Tinder, Facebook]\nEscolha: ')
    social_network = eval(social)()

    sections = social_network.get_sections()

    print(
        f'\nA rede social {type(social_network).__name__} é constituida pelas seções {sections};')
