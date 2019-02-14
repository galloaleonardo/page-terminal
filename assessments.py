from utils import utils
from questions_pattern import questions
from assessments_writer import AssessmentsWriterFile


class AttitudesAging:
    a_question_1 = None
    a_question_2 = None
    a_question_3 = None

    def attitude_issues(self):
        utils.line_break()
        print('A) ATITUDES EM RELAÇÄO A VELHICE E ENVELHECIMENTO.')
        self.a_question_1 = input(questions.QuestionsAttitudesAging.QUESTION_1)
        self.a_question_2 = input(questions.QuestionsAttitudesAging.QUESTION_2)
        self.a_question_3 = input(questions.QuestionsAttitudesAging.QUESTION_3)
        return self.a_question_3


class QualityLife:
    @staticmethod
    def quality_issues(patient):
        utils.line_break()

        print('B) QUALIDADE DE VIDA.')
        q_question_1 = input(questions.QuestionsQualityLife.QUESTION_1)
        q_question_1_1 = input(questions.QuestionsQualityLife.QUESTION_1_1)
        utils.line_break()
        q_question_2 = input(questions.QuestionsQualityLife.QUESTION_2)
        q_question_2_1 = input(questions.QuestionsQualityLife.QUESTION_2_1)
        utils.line_break()
        q_question_3 = input(questions.QuestionsQualityLife.QUESTION_3)
        q_question_3_1 = input(questions.QuestionsQualityLife.QUESTION_3_1)
        utils.line_break()
        q_question_4 = input(questions.QuestionsQualityLife.QUESTION_4)
        utils.line_break()
        q_question_5 = input(questions.QuestionsQualityLife.QUESTION_5)
        q_question_5_1 = input(questions.QuestionsQualityLife.QUESTION_5_1)
        utils.line_break()
        q_question_6 = input(questions.QuestionsQualityLife.QUESTION_6)
        utils.line_break()
        q_question_7 = input(questions.QuestionsQualityLife.QUESTION_7)

        if q_question_7 == 1:
            utils.line_break()
            q_question_7_1 = input(questions.QuestionsQualityLife.QUESTION_7_1)

        utils.line_break()
        q_question_8 = input(questions.QuestionsQualityLife.QUESTION_8)
        utils.line_break()
        q_question_9 = input(questions.QuestionsQualityLife.QUESTION_9)
        utils.line_break()
        q_question_10 = input(questions.QuestionsQualityLife.QUESTION_10)

        if q_question_10 == 1:
            q_question_10_1 = input(questions.QuestionsQualityLife.QUESTION_10_1)
            q_question_10_2 = input(questions.QuestionsQualityLife.QUESTION_10_2)

        utils.line_break()
        q_question_11 = input(questions.QuestionsQualityLife.QUESTION_11)

        quality_life_questions = [int(q_question_1), int(q_question_2), int(q_question_3), int(q_question_4),
                                  int(q_question_5), int(q_question_7), int(q_question_9), int(q_question_10)]

        quality_life_final_anwser = sum(quality_life_questions)
        utils.line_break()
        quality_life_need_research = input('PONTUAÇÂO OBTIDA: %s. A MÁXIMA PARA ESTA CATEGORIA É DE [23 PONTOS]. \n'
                                           'EXISTE A NECESSIDADE DE INVESTIGAÇÃO? (0) NÃO | (1) SIM -> '
                                           % str(quality_life_final_anwser))

        patient.p_score_quality_life = [quality_life_final_anwser, quality_life_need_research]


class MultidimensionalEvaluation:
    @staticmethod
    def questions_and_answers(gerontologian, patient):
        report = AssessmentsWriterFile()
        report.inicializate_write(gerontologian, patient)
        report.header_file_gerontologian(gerontologian)
        report.header_file_patient(patient)

        attitudes = AttitudesAging()
        attitudes.attitude_issues(patient)

        patient.p_score_attitudes_aging = attitudes.a_question_3
        quality_life = QualityLife()
        quality_life.quality_issues(patient)
