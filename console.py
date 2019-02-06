from persons import Gerontologian
from utils.headers import Headers


class StartApplication:
    @staticmethod
    def init_app():
        Headers.title_header()
        GerontologianPeople.get_gerontologian()


class GerontologianPeople:
    @staticmethod
    def get_gerontologian():
        name = input('Olá gerontologo(a), qual o seu nome? ')
        abg = input('Certo, e qual é o número do seu cadastro na ABG? ')
        confirm = input('Nome: %s | Num. ABG: %s. Podemos confirmar o cadastro (Y/N)? ' % (name, abg))
        if confirm.upper() == 'Y':
            geronto = Gerontologian()
            geronto.set_gerontologian(name, abg)
            print('Bem vindo(a), %s.' % geronto.geronto_name)
        else:
            pass
