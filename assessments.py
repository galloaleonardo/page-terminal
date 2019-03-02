from questions_pattern import questions
from utils import utils
import time


class MultidimensionalEvaluationTest:
    def __init__(self, title, question):
        self.title = title
        self.question = question

    def issues(self):
        utils.clear()
        print('{}{}%s{}'.format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END) % self.title)
        count_score = 0

        for key, value in self.question.items():
            answer = input(key)
            utils.line_break()
            setattr(questions, key, answer)

            try:
                count_score += int(answer)
            except ValueError:
                pass

        return count_score


class MultidimensionalEvaluation:
    def __init__(self):
        self._attitudes_aging_score = []
        self._quality_life_score = []
        self._directions_score = []
        self._malnutrition_score = []
        self._functional_capacity_score = []
        self._depression_score = []
        self._cardiovascular_factors_score = []
        self._medication_administration_score = []
        self._environment_score = []
        self._falls_score = []
        self._violence_score = []
        self._social_vulnerability_score = []
        self._fragility_score = []
        self._gerontologist_evaluation_score = []
        self._planning_actions_score = []

    def set_categories(self):
        utils.clear()
        print('{}{} ## Avaliação multidimensional do idoso: {} \n'.
              format(utils.Color.BOLD, utils.Color.CYAN, utils.Color.END))
        time.sleep(0.5)
        
        self._attitudes_aging_score.append(self.call_tests_score(questions.QuestionsAttitudesAging.TITLE,
                                                                 questions.QuestionsAttitudesAging.
                                                                 questions_answers_attitudes_agging))

        self._quality_life_score.append(self.call_tests_score(questions.QuestionsQualityLife.TITLE,
                                                              questions.QuestionsQualityLife.
                                                              questions_answers_quality_life))

        self._directions_score.append(self.call_tests_score(questions.QuestionsDirections.TITLE,
                                                            questions.QuestionsDirections.
                                                            questions_answers_directions))

        self._malnutrition_score.append(self.call_tests_score(questions.QuestionsMalnutrition.TITLE,
                                                              questions.QuestionsMalnutrition.
                                                              questions_answers_malnutrition))

        self._functional_capacity_score.append(self.call_tests_score(questions.QuestionsFunctionalCapacity.TITLE,
                                                                     questions.QuestionsFunctionalCapacity.
                                                                     questions_answers_functional_capacity))

        self._depression_score.append(self.call_tests_score(questions.QuestionsDepression.TITLE,
                                                            questions.QuestionsDepression.
                                                            questions_answers_depression))

        self._cardiovascular_factors_score.append(self.call_tests_score(questions.QuestionsCardiovascularFactors.TITLE,
                                                                        questions.QuestionsCardiovascularFactors.
                                                                        questions_answers_cardiovascular_factors))

        self._medication_administration_score.append(self.call_tests_score(questions.
                                                                           QuesntionsMedicationAdministration.TITLE,
                                                                           questions.QuesntionsMedicationAdministration.
                                                                           questions_answers_medication_administration))

        self._environment_score.append(self.call_tests_score(questions.QuestionsEnvironment.TITLE,
                                                             questions.QuestionsEnvironment.
                                                             questions_answers_environment))

        self._falls_score.append(self.call_tests_score(questions.QuestionsFalls.TITLE,
                                                       questions.QuestionsFalls.questions_answers_falls))

        self._violence_score.append(self.call_tests_score(questions.QuestionsViolence.TITLE,
                                                          questions.QuestionsViolence.questions_answers_violence))

        self._social_vulnerability_score.append(self.call_tests_score(questions.QuestionsSocialVulnerability.TITLE,
                                                                      questions.QuestionsSocialVulnerability.
                                                                      questions_answers_social_vulnerability))

        self._fragility_score.append(self.call_tests_score(questions.QuestionsFragility.TITLE,
                                                           questions.QuestionsFragility.questions_answers_fragility))

        self._gerontologist_evaluation_score.append(self.call_tests_score(questions.QuestionsGerontologistEvaluation.
                                                                          TITLE,
                                                                          questions.QuestionsGerontologistEvaluation.
                                                                          questions_answers_gerontologist_evaluation))

        self._planning_actions_score.append(self.call_tests_score(questions.QuestionsPlanningActions.TITLE,
                                                                  questions.QuestionsPlanningActions.
                                                                  questions_answers_planning_actions))

    def set_gategory_need_investigation(self):
        self._attitudes_aging_score.append(input('Atitudes em relação a velhice e envelhecimento: {}'
                                                 .format(self._attitudes_aging_score[0]) +
                                                 'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._quality_life_score.append(input('Qualidade de vida: {}. A máxima é de 23 pontos.'
                                              .format(self._quality_life_score[0]) +
                                              'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._directions_score.append(input('Sentidos: {}. A máxima é de 9 pontos. '
                                            .format(self._directions_score[0]) +
                                            'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._malnutrition_score.append(input('Desnutrição: {}. A máxima é de 14/12 pontos. '
                                              .format(self._malnutrition_score[0]) +
                                              'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._functional_capacity_score.append(input('Capacidade funcional: {}. A máxima é de 6 pontos. '
                                                     .format(self._functional_capacity_score[0]) +
                                                     'Paciente possui necessidade de investigação? ' +
                                                     '[0] Sim | [1] Não: '))

        self._depression_score.append(input('Depressão: {}. A máxima é de 6 pontos. '
                                            .format(self._depression_score[0]) +
                                            'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._cardiovascular_factors_score.append(input('Fatores cardiovasculares: {}. A máxima é de 14 pontos. '
                                                        .format(self._cardiovascular_factors_score[0]) +
                                                        'Paciente possui necessidade de investigação? ' +
                                                        '[0] Sim | [1] Não: '))

        self._medication_administration_score.append(input('Administraçåo de medicamentos: {}. '
                                                           .format(self._medication_administration_score[0]) +
                                                           'A máxima é de 7 pontos. ' +
                                                           'Paciente possui necessidade de investigação? ' +
                                                           '[0] Sim | [1] Não: '))

        self._environment_score.append(input('Ambiente: {}. A máxima é de 18 pontos. '
                                             .format(self._environment_score[0]) +
                                             'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._falls_score.append(input('Quedas: {}. A máxima é de 17 pontos. '.format(self._falls_score[0]) +
                                       'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._violence_score.append(input('Violência: {}. A máxima é de 6 pontos. '.format(self._violence_score[0]) +
                                          'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

        self._social_vulnerability_score.append(input('Vulnerabilidade social: {}. A máxima é de 24 pontos. '.
                                                      format(self._social_vulnerability_score[0]) +
                                                      'Paciente possui necessidade de investigação? ' +
                                                      '[0] Sim | [1] Não: '))

        self._fragility_score.append(input('Fragilidade: {}. A máxima é de 10 pontos. '
                                           .format(self._fragility_score[0]) +
                                           'Paciente possui necessidade de investigação? [0] Sim | [1] Não: '))

    @staticmethod
    def call_tests_score(title, question):
        test = MultidimensionalEvaluationTest(title, question)
        return test.issues()
