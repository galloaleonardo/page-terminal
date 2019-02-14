from persons import Gerontologian, Patient
from utils.headers import Headers
from assessments import MultidimensionalEvaluation
import time


class StartApplication:
    @staticmethod
    def init_app():
        Headers.title_header()
        gerontologian = GerontologianPeople.input_gerontologian()
        print('Vamos iniciar com o cadastro do paciente... \n')
        time.sleep(1)
        patient = PatientPeople.get_patient()
        MultidimensionalEvaluation.questions_and_answers(patient)


class GerontologianPeople:
    @staticmethod
    def input_gerontologian():
        name = input('Olá gerontologo(a), digite o seu nome: ')
        abg = input('%s, qual seu númedo da ABG? ' % name)
        confirm = input('Nome: %s | Num. ABG: %s. Podemos confirmar o cadastro (S / N)? ' % (name, abg))
        if confirm.upper() == 'S':
            gerontologian = Gerontologian(name, abg)
            print('Bem vindo(a), %s.' % gerontologian.g_name)
            return gerontologian
        else:
            exit()


class PatientPeople:
    @staticmethod
    def get_patient():
        name = input('Nome: ')
        birth = input('Data de nascimento: ')
        sex = input('Sexo - Feminino (F) | Masculino (M) | Prefiro não dizer (O): ')
        marital_status = input('Estado civíl: ')
        schooling = input('Escolaridade: ')
        ocupation = input('Ocupação: ')
        home_with = input('Com quem mora: ')
        income = input('Renda individual ou familiar: ')
        bpc = input('BPC - Sim (S) | Não (N) | Não se aplica (O): ')
        b_religion = input('Possui religião - Sim (S) | Não (N):')
        religion_name = input('Se sim, qual: ')

        patient = Patient(name, birth, sex, marital_status, schooling, ocupation, home_with,
                          income, bpc, b_religion, religion_name)
        confirm = input('Ficha de %s, confirmar? (S / N)' % patient.p_name)

        if confirm.upper() == 'S':
            return patient
        else:
            exit()
