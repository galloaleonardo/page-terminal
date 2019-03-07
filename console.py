from persons import Gerontologian, Patient

from utils.headers import Headers
from utils.utils import Color, clear
from assessments import MultidimensionalEvaluation
from questions_pattern import questions
from bullet import Bullet, ScrollBar
import time


class StartApplication:
    @staticmethod
    def init_app():
        Headers.title_header()
        StartApplication.register_people()

    @staticmethod
    def register_people():
        gerontologist = GerontologianPeople.input_gerontologist()
        patient = PatientPeople.input_patient()
        StartApplication.call_multidimensional_test()

    @staticmethod
    def call_multidimensional_test():
        test = MultidimensionalEvaluation()
        test.set_categories()
        print("{}{}Relação da pontuação obtida: {}".format(Color.BOLD, Color.GREEN, Color.END))
        test.set_gategory_need_investigation()


class GerontologianPeople:
    @staticmethod
    def input_gerontologist():
        print('{}{}## Ficha cadastral: {} \n'.format(Color.BOLD, Color.CYAN, Color.END))
        inpt_primary_name = input('Gerontólogo(a), digite o seu nome: ').capitalize()
        inpt_last_name = input('Último nome: ').capitalize()
        inpt_num_membership_abg = input('Número de associação ABG (Associação Brasileira de Gerontologia): ')
        inpt_service_institution = input('Serviço/Instituíção: ').capitalize()

        inpt_is_elderly_interviewee_aux = ScrollBar('O entrevistado é o próprio idoso?: ', choices=['Sim', 'Não'],
                                                    indent=0, margin=2, pointer="★", pad_right=5)

        inpt_is_elderly_interviewee = inpt_is_elderly_interviewee_aux.launch()

        inpt_evaluation_date = time.strftime("%d/%m/%Y")

        inpt_is_elderly_interviewee = (1 if (inpt_is_elderly_interviewee.upper() == 'S') else 0)

        gerontologist = Gerontologian(inpt_primary_name, inpt_last_name, inpt_num_membership_abg,
                                      inpt_service_institution, inpt_is_elderly_interviewee, inpt_evaluation_date)

        print('Bem vindo(a), %s. \n' % gerontologist.full_name)
        time.sleep(1)
        return gerontologist


class PatientPeople:
    @staticmethod
    def input_patient():
        clear()
        print('{}{}## Dados de identificação do paciente: {} \n'.format(Color.BOLD, Color.CYAN, Color.END))
        inpt_first_name = input('Primeiro nome: ').capitalize()
        inpt_last_name = input('Segundo nome: ').capitalize()
        inpt_adress = input('Endereço: ').capitalize()
        inpt_telephone = input('Telefone: ')
        inpt_date_birth = input('Data de nascimento (DD/MM/AAAA): ')
        inpt_age = input('Idade: ').capitalize()

        inpt_genre_aux = ScrollBar(prompt='Gênero: ', choices=['Feminino', 'Masculino', 'Prefiro não dizer'],
                                   indent=0, margin=2, pointer="★", pad_right=5)

        inpt_genre = inpt_genre_aux.launch()

        inpt_marital_status = input('Estado civíl: ').capitalize()
        inpt_scholarity = input('Escolaridade: ').capitalize()
        inpt_years_scholarity = input('De acordo com sua escolaridade, o(a) senhor(a) estudou,'
                                      ' formalmente durante quantos anos? ')
        inpt_retired = input('O(a) Sr(a) é aposentado? Se não, qual é a sua profissão atual? ')
        inpt_retired_pensioner = input('Caso seja aposentado ou pensionista,'
                                       ' qual a profissão que exerceu por mais tempo? ')
        inpt_paid_work = input('Exerce atualmente algum tipo de trabalho remunerado? Se sim, qual? ')
        inpt_individual_income = input('Renda individual: ')
        inpt_family_income = input('Renda familiar (se houver): ')
        inpt_live_with = input('Com quem mora: ').capitalize()
        inpt_have_relegion = input('Possui religião - Sim (S) | Não (N): ')

        inpt_have_relegion = (1 if (inpt_have_relegion.upper() == 'S') else 0)

        patient = Patient(inpt_first_name, inpt_last_name, inpt_adress, inpt_telephone,
                          inpt_date_birth, inpt_age, inpt_genre, inpt_marital_status,
                          inpt_scholarity, inpt_years_scholarity, inpt_retired,
                          inpt_retired_pensioner, inpt_paid_work, inpt_individual_income,
                          inpt_family_income, inpt_live_with, inpt_have_relegion)

        print('Iniciando a avaliação de %s... \n' % patient.full_name)
        return patient
