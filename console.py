from persons import Gerontologian, Patient
from utils.headers import Headers
from assessments import MultidimensionalEvaluation
import time


class StartApplication:
    @staticmethod
    def init_app():
        Headers.title_header()
        StartApplication.register_people()
        # MultidimensionalEvaluation.questions_and_answers(patient)

    @staticmethod
    def register_people():
        gerontologist = GerontologianPeople.input_gerontologist()
        patient = PatientPeople.input_patient()


class GerontologianPeople:
    @staticmethod
    def input_gerontologist():
        print('## Ficha cadastral: \n')
        inpt_primary_name = input('Gerontólogo(a), digite o seu nome: ').capitalize()
        inpt_last_name = input('Último nome: ').capitalize()
        inpt_num_membership_abg = input('Número de associação ABG (Associação Brasileira de Gerontologia): ')
        inpt_service_institution = input('Serviço/Instituíção: ').capitalize()
        inpt_is_elderly_interviewee = input('O entrevistado é o próprio idoso? (S)/(N): ')
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
        print('## Dados de identificação do paciente: \n')
        inpt_first_name = input('Primeiro nome: ').capitalize()
        inpt_last_name = input('Segundo nome: ').capitalize()
        inpt_adress = input('Endereço: ').capitalize()
        inpt_telephone = input('Telefone: ')
        inpt_date_birth = input('Data de nascimento: ')
        inpt_age = input('Idade: ')
        inpt_genre = input('Gênero - Feminino (F) | Masculino (M) | Prefiro não dizer (O): ')
        inpt_marital_status = input('Estado civíl: ').capitalize()
        inpt_scholarity = input('Escolaridade: ').capitalize()
        inpt_individual_income = input('Renda individual: ')
        inpt_family_income = input('Renda familiar (se houver): ')
        inpt_live_with = input('Com quem mora: ').capitalize()
        inpt_have_relegion = input('Possui religião - Sim (S) | Não (N): ')

        inpt_have_relegion = (1 if (inpt_have_relegion.upper() == 'S') else 0)

        patient = Patient(inpt_first_name, inpt_last_name, inpt_adress, inpt_telephone,
                          inpt_date_birth, inpt_age, inpt_genre, inpt_marital_status,
                          inpt_scholarity, inpt_individual_income, inpt_family_income,
                          inpt_live_with, inpt_have_relegion)

        print('Iniciando a avaliação de %s... \n' % patient.full_name)
        return patient
