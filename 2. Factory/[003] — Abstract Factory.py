from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, btn_name, btn_type) -> None:
        self.create_button(btn_name, btn_type)

    @abstractmethod
    def create_button(self) -> None:
        pass

    def get_btn_name(self) -> None:
        return self.btn_name

    def set_btn_name(self, btn_name) -> None:
        self.btn_name = btn_name

    def get_btn_type(self) -> None:
        return self.btn_type

    def set_btn_type(self, btn_type) -> None:
        self.btn_type = btn_type


class ButtonWindows(Button):
    def create_button(self, btn_name, btn_type):
        self.set_btn_name(btn_name)
        self.set_btn_type(btn_type)


class ButtonLinux(Button):
    def create_button(self, btn_name, btn_type):
        self.set_btn_name(btn_name)
        self.set_btn_type(btn_type)


class Form(ABC):
    def __init__(self, form_name, form_type) -> None:
        self.create_form(form_name, form_type)

    @abstractmethod
    def create_form(self, form_name, form_type) -> None:
        pass

    def get_form_name(self) -> None:
        return self.form_name

    def set_form_name(self, form_name) -> None:
        self.form_name = form_name

    def get_form_type(self) -> None:
        return self.form_type

    def set_form_type(self, form_type) -> None:
        self.form_type = form_type


class FormWindows(Form):
    def create_form(self, form_name, form_type):
        self.set_form_name(form_name)
        self.set_form_type(form_type)


class FormLinux(Form):
    def create_form(self, form_name, form_type):
        self.set_form_name(form_name)
        self.set_form_type(form_type)


class UIElementFactory(ABC):
    @abstractmethod
    def create_button(self, btn_name, btn_type) -> None:
        pass

    @abstractmethod
    def create_form(self, form_name, form_type) -> None:
        pass


class UIElementFactoryWindows(UIElementFactory):
    def create_form(
            self, form_name='DefaultFormName', form_type='DefaultFormType') -> FormWindows:
        return FormWindows(form_name, form_type)

    def create_button(self, btn_name, btn_type) -> ButtonWindows:
        return ButtonWindows(btn_name, btn_type)


class UIElementFactoryLinux(UIElementFactory):
    def create_form(self, form_name, form_type) -> FormLinux:
        return FormLinux(form_name, form_type)

    def create_button(
            self, btn_name='DefaultButtonName', btn_type='DefaultButtonType') -> ButtonLinux:
        return ButtonLinux(btn_name, btn_type)


def client_code(
    factory: UIElementFactory,
    form_name='DefaultFormName', form_type='DefaultFormType',
    btn_name='DefaultButtonName', btn_type='DefaultButtonType'
) -> None:
    form = factory.create_form(form_name, form_type)
    button = factory.create_button(btn_name, btn_type)

    print(
        f'O tipo da interface é igual a {type(factory).__name__}')

    print(
        f'O nome do formulário é: {form.get_form_name()}')
    print(
        f'O tipo do formulário é: {form.get_form_type()}')

    print(
        f'O nome do botão é {button.get_btn_name()}')
    print(
        f'O tipo do botão é: {button.get_btn_type()}')


if __name__ == '__main__':
    print("Client: Testing client code with the first factory type:")
    client_code(UIElementFactoryWindows(), 'Gerador de PDF',
                'POST', 'Gerar PDF', 'Submit')

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(UIElementFactoryLinux())
