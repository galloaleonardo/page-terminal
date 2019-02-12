from utils import utils


class AttitudesAging:
    @staticmethod
    def attitude_issues():
        utils.line_break()
        print('A) ATITUDES EM RELAÇÄO A VELHICE E ENVELHECIMENTO.')
        q_1 = input('1. Que idade o(a) senhor(a) sente ter? Por quê? ')
        q_2 = input('2. Existe pontos positivos e negativos presentes nessa fase da vida? Quais? ')


class QualityLife:
    @staticmethod
    def quality_issues():
        utils.line_break()
        print('B) QUALIDADE DE VIDA.')
        q_question_1 = input('1. Em geral, o(a) senhor(a) se considera uma pessoa: \n'
                             '0 = Infeliz | 1 = Não muito feliz | 2 = Feliz | 3 = Muito Feliz -> ')
        q_question_1_1 = input('1.1. Por quê? ')

        utils.line_break()

        q_question_2 = input('2. Em geral, o(a) senhor(a) diria que sua saúde é: \n'
                             '0 = Muito ruim | 1 = Ruim | 2 = Boa | 3 = Muito boa -> ')
        q_question_2_1 = input('2.1. Por quê? ')

        utils.line_break()

        q_question_3 = input('3. Como o(a) senhor(a) avalia sua qualidade de vida? \n'
                             '0 = Muito ruim | 1 = Ruim | 2 = Boa | 3 = Muito boa -> ')
        q_question_3_1 = input('3.1. Por quê? ')

        utils.line_break()

        q_question_4 = input('4. O(a) senhor(a) se sente capaz de fazer coisas/atividades '
                             'tão bem quanto a maioria das pessoas? \n'
                             '0 = Nunca | 1 = Raramente | 2 = A maioria das vezes | 3 = Sempre -> ')

        utils.line_break()

        q_question_5 = input('5. Quanta dor no corpo o(a) senhor(a) sentiu nas últimas quatro semanas? \n'
                             '0 = Intensa | 1 = Moderada | 2 = Leve | 3 = Nenhuma -> ')
        q_question_5_1 = input('5.1. Onde? ')

        utils.line_break()

        q_question_6 = input('6. Durante o último mês, como o(a) senhor(a) classificaria '
                             'a qualidade do seu sono de uma maneira geral? \n'
                             '0 = Muito ruim | 1 = Ruim | 2 = Boa | 3 = Muito boa -> ')

        utils.line_break()

        q_question_7 = input('7. O(a) senhor(a) é sexualmente ativo(a)? (0) NÃO | (1) SIM -> ')

        if q_question_7.upper() == 1:
            utils.line_break()
            q_question_7_1 = input('Quão satisfeito o(a) senhor(a) está com o seu relacionamento afetivo? \n'
                                   '0 = Muito insatisfeito | 1 = Insatisfeito | '
                                   '2 = Satisfeito | 3 = Muito satisfeito -> ')

        utils.line_break()

        q_question_8 = input('8. Como o(a) senhor(a) ocupa o seu tempo (investigar sobre sua rotina)? \n')

        utils.line_break()

        q_question_9 = input('9. O(a) senhor(a) está satisfeito com a forma que '
                             'ocupa o seu tempo/rotina? (0) NÃO | (1) SIM -> ')

        utils.line_break()

        q_question_10 = input('10. O(a) senhor(a) realiza alguma atividade '
                              'prazerosa e/ou de lazer? (0) NÃO | (1) SIM -> ')

        if q_question_10 == 1:
            q_question_10_1 = input('10.1. Qual(is)?: ')
            q_question_10_2 = input('10.2. Frequência: ')

        utils.line_break()

        q_question_11 = input('11. De todos os aspectos perguntados anteriormente (saúde, dor, sono, '
                              'capacidade de fazer atividades, relacionamento afetivo, ocupação do tempo, '
                              'atividades de lazer,outros), qual o(a) senhor(a) considera mais importante '
                              'para a sua qualidade de vida? ')

        quality_life_questions = [int(q_question_1), int(q_question_2), int(q_question_3), int(q_question_4),
                                  int(q_question_5), int(q_question_7), int(q_question_9), int(q_question_10)]

        quality_life_final_anwser = sum(quality_life_questions)

        utils.line_break()

        quality_life_need_research = input('PONTUAÇÂO OBTIDA: %s. A MÁXIMA PARA ESTA CATEGORIA É DE [23 PONTOS]. \n'
                                           'EXISTE A NECESSIDADE DE INVESTIGAÇÃO? (0) NÃO | (1) SIM -> '
                                           % str(quality_life_final_anwser)).upper()

        return quality_life_need_research


class MultidimensionalEvaluation:
    @staticmethod
    def questions_and_answers():
        AttitudesAging.attitude_issues()
        quality_life = QualityLife
        quality_life_score = quality_life.quality_issues()

        return quality_life_score
