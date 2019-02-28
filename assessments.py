from questions_pattern import questions
from utils import utils


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
        utils.clear()
        print('{}{} ## Avaliação multidimensional do idoso: {} \n'.
              format(utils.Color.BOLD, utils.Color.CYAN, utils.Color.END))

    @staticmethod
    def call_tests_score(title, question):
        test = MultidimensionalEvaluationTest(title, question)
        return test.issues()
