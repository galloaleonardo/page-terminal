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


class FunctionalCapacity:
    @staticmethod
    def functional_capacity_issues():
        utils.clear()
        print('{}{}E) Capacidade funcional: {}' .
              format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END))
        count_score = 0

        for key, value in questions.QuestionsFunctionalCapacity.questions_answers_functional_capacity.items():
            answer = input(key)
            utils.line_break()
            questions.QuestionsFunctionalCapacity.questions_answers_functional_capacity[key] = answer

            try:
                count_score += int(answer)
            except ValueError:
                pass

        return count_score


class Depression:
    @staticmethod
    def depression_issues():
        utils.clear()
        print('{}{}F) Depressão: {}' .
              format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END))
        count_score = 0

        for key, value in questions.QuestionsDepression.questions_answers_depression.items():
            answer = input(key)
            utils.line_break()
            questions.QuestionsDepression.questions_answers_depression[key] = answer

            try:
                count_score += int(answer)
            except ValueError:
                pass

        return count_score


class CardiovascularFactors:
    @staticmethod
    def cardiovascular_factors_issues():
        utils.clear()
        print('{}{}G) Fatores cardiovasculares: {}' .
              format(utils.Color.BOLD, utils.Color.BLUE, utils.Color.END))
        count_score = 0

        for key, value in questions.QuestionsCardiovascularFactors.questions_answers_cardiovascular_factors.items():
            answer = input(key)
            utils.line_break()
            questions.QuestionsCardiovascularFactors.questions_answers_cardiovascular_factors[key] = answer

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

    @staticmethod
    def call_functional_capacity():
        functional_capacity = FunctionalCapacity()
        return functional_capacity.functional_capacity_issues()

    @staticmethod
    def call_depression():
        depression = Depression()
        return depression.depression_issues()

    @staticmethod
    def call_cardiocascular_factors():
        cardiovascular_factors = CardiovascularFactors()
        return cardiovascular_factors.cardiovascular_factors_issues()
