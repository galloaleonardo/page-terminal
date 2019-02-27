from persons import Gerontologian, Patient
from utils.headers import Headers
from utils.utils import Color, clear
from assessments import MultidimensionalEvaluation
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
        StartApplication.call_multidimensional_test(gerontologist, patient)

    @staticmethod
    def call_multidimensional_test(gerontologist, patient):
        test = MultidimensionalEvaluation()
        patient._attitudes_aging_score = test.call_attitudes_aging_score()
        patient._quality_life_score = test.call_quality_life_score()
        patient._directions_score = test.call_directions_score()
        patient._malnutrition_score = test.call_malnutrition_score()
        patient._functional_capacity_score = test.call_functional_capacity()
        patient._depression = test.call_depression()
        patient._cardiovascular_factors = test.call_cardiocascular_factors()
        patient._medication_administration = test.call_medication_administration()

        print("{}{}Relação da pontuação obtida: {}".format(Color.BOLD, Color.GREEN, Color.END))

        patient._is_attitudes_aging_score_need_score = \
            input('Atitudes em relação a velhice e envelhecimento: {}'.format(patient._attitudes_aging_score) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')

        patient._is_quality_life_score_need_investigation = \
            input('Qualidade de vida: {}. A máxima é de 23 pontos.'.format(patient._quality_life_score) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')

        patient._is_directions_score_need_investigation = \
            input('Sentidos: {}. A máxima é de 9 pontos. '.format(patient._directions_score) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')

        patient._is_malnutrition_score_need_investigation = \
            input('Desnutrição: {}. A máxima é de 14/12 pontos. '.format(patient._malnutrition_score) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')

        patient._is_functional_capacity_score_need_investigation = \
            input('Capacidade funcional: {}. A máxima é de 6 pontos. '.format(patient._functional_capacity_score) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')

        patient._is_depression_score_need_investigation = \
            input('Depressão: {}. A máxima é de 6 pontos. '.format(patient._depression) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')

        patient._is_cardiovascular_factors_score_need_investigation = \
            input('Fatores cardiovasculares: {}. A máxima é de 14 pontos. '.format(patient._cardiovascular_factors) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')

        patient._is_medication_administration_score_need_investigation = \
            input('Administraçåo de medicamentos: {}. A máxima é de 7 pontos. '.
                  format(patient._medication_administration) +
                  'Paciente possui necessidade de investigação? [0] Sim | [1] Não: ')


class GerontologianPeople:
    @staticmethod
    def input_gerontologist():
        print('{}{} ## Ficha cadastral: {} \n'.format(Color.BOLD, Color.CYAN, Color.END))
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
        clear()
        print('{}{} ## Dados de identificação do paciente: {} \n'.format(Color.BOLD, Color.CYAN, Color.END))
        inpt_first_name = input('Primeiro nome: ').capitalize()
        inpt_last_name = input('Segundo nome: ').capitalize()
        inpt_adress = input('Endereço: ').capitalize()
        inpt_telephone = input('Telefone: ')
        inpt_date_birth = input('Data de nascimento (DD/MM/AAAA): ')
        inpt_age = input('Idade: ').capitalize()
        inpt_genre = input('Gênero - Feminino (F) | Masculino (M) | Prefiro não dizer (O): ')
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
