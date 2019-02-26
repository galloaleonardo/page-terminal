from questions_pattern import questions
from utils import utils


class AttitudesAging:
    @staticmethod
    def attitude_issues():
        print('{}{}A) Atitudes em relação a velhice e envelhecimento: {}'.
              format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END))
        count_score = 0

        for key, value in questions.QuestionsAttitudesAging.questions_answers_attitudes_agging.items():
            answer = input(key)
            utils.line_break()
            questions.QuestionsAttitudesAging.questions_answers_attitudes_agging[key] = answer

            try:
                count_score += int(answer)
            except ValueError:
                pass

        return count_score


class QualityLife:
    @staticmethod
    def quality_issues():
        utils.clear()
        print('{}{}B) Qualidade de vida: {}'.
              format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END))
        count_score = 0

        for key, value in questions.QuestionsQualityLife.questions_answers_quality_life.items():
            answer = input(key)
            utils.line_break()
            questions.QuestionsQualityLife.questions_answers_quality_life[key] = answer

            try:
                count_score += int(answer)
            except ValueError:
                pass

        return count_score


class Directions:
    @staticmethod
    def directions_issues():
        utils.clear()
        print('{}{}C) Sentidos: {}'.
              format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END))
        count_score = 0

        for key, value in questions.QuestionsDirections.questions_answers_directions.items():
            answer = input(key)
            utils.line_break()
            questions.QuestionsDirections.questions_answers_directions[key] = answer

            try:
                count_score += int(answer)
            except ValueError:
                pass

        return count_score


class Malnutrition:
    @staticmethod
    def malnutrition_issues():
        utils.clear()
        print('{}{}D) Desnutrição: {}' .
              format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END))
        count_score = 0

        for key, value in questions.QuestionsMalnutrition.questions_answers_malnutrition.items():
            answer = input(key)
            utils.line_break()
            questions.QuestionsMalnutrition.questions_answers_malnutrition[key] = answer

            try:
                count_score += int(answer)
            except ValueError:
                pass

        return count_score


class MultidimensionalEvaluation:
    def __init__(self):
        utils.clear()
        print('{}{} ## Avaliação multidimensional do idoso: {} \n'.
              format(utils.Color.BOLD, utils.Color.CYAN, utils.Color.END))

    @staticmethod
    def call_attitudes_aging_score():
        attitudes_aging = AttitudesAging()
        return attitudes_aging.attitude_issues()

    @staticmethod
    def call_quality_life_score():
        quality_life = QualityLife()
        return quality_life.quality_issues()

    @staticmethod
    def call_directions_score():
        directions = Directions()
        return directions.directions_issues()

    @staticmethod
    def call_malnutrition_score():
        malnutrition = Malnutrition()
        return malnutrition.malnutrition_issues()
