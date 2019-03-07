import urllib.request
import json

HAVE_CHOICE = 1
DONT_HAVE_CHOICE = 0


class ReadJSONFile:
    request = urllib.request.Request('https://api.myjson.com/bins/t5l2u')
    reader = urllib.request.urlopen(request).read()
    json_file = json.loads(reader.decode('utf-8'))


class QuestionsAttitudesAging:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsAttitudesAging.TITLE = ReadJSONFile.json_file['QuestionsAttitudesAging']['title']
        for item in ReadJSONFile.json_file['QuestionsAttitudesAging']['questions_answers']:
            QuestionsAttitudesAging.questions_answers.append(item)


class QuestionsQualityLife:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsQualityLife.TITLE = ReadJSONFile.json_file['QuestionsQualityLife']['title']
        for item in ReadJSONFile.json_file['QuestionsQualityLife']['questions_answers']:
            QuestionsQualityLife.questions_answers.append(item)


class QuestionsDirections:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsDirections.TITLE = ReadJSONFile.json_file['QuestionsDirections']['title']
        for item in ReadJSONFile.json_file['QuestionsDirections']['questions_answers']:
            QuestionsDirections.questions_answers.append(item)


class QuestionsMalnutrition:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsMalnutrition.TITLE = ReadJSONFile.json_file['QuestionsMalnutrition']['title']
        for item in ReadJSONFile.json_file['QuestionsMalnutrition']['questions_answers']:
            QuestionsMalnutrition.questions_answers.append(item)


class QuestionsFunctionalCapacity:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsFunctionalCapacity.TITLE = ReadJSONFile.json_file['QuestionsFunctionalCapacity']['title']
        for item in ReadJSONFile.json_file['QuestionsFunctionalCapacity']['questions_answers']:
            QuestionsFunctionalCapacity.questions_answers.append(item)


class QuestionsDepression:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsDepression.TITLE = ReadJSONFile.json_file['QuestionsDepression']['title']
        for item in ReadJSONFile.json_file['QuestionsDepression']['questions_answers']:
            QuestionsDepression.questions_answers.append(item)


class QuestionsCardiovascularFactors:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsCardiovascularFactors.TITLE = ReadJSONFile.json_file['QuestionsCardiovascularFactors']['title']

        for item in ReadJSONFile.json_file['QuestionsCardiovascularFactors']['questions_answers']:
            QuestionsCardiovascularFactors.questions_answers.append(item)


class QuesntionsMedicationAdministration:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuesntionsMedicationAdministration.TITLE = ReadJSONFile.json_file['QuesntionsMedicationAdministration']['title']
        for item in ReadJSONFile.json_file['QuesntionsMedicationAdministration']['questions_answers']:
            QuesntionsMedicationAdministration.questions_answers.append(item)


class QuestionsEnvironment:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsEnvironment.TITLE = ReadJSONFile.json_file['QuestionsEnvironment']['title']
        for item in ReadJSONFile.json_file['QuestionsEnvironment']['questions_answers']:
            QuestionsEnvironment.questions_answers.append(item)


class QuestionsFalls:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsFalls.TITLE = ReadJSONFile.json_file['QuestionsFalls']['title']
        for item in ReadJSONFile.json_file['QuestionsFalls']['questions_answers']:
            QuestionsFalls.questions_answers.append(item)


class QuestionsViolence:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsViolence.TITLE = ReadJSONFile.json_file['QuestionsViolence']['title']

        for item in ReadJSONFile.json_file['QuestionsViolence']['questions_answers']:
            QuestionsViolence.questions_answers.append(item)


class QuestionsSocialVulnerability:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsSocialVulnerability.TITLE = ReadJSONFile.json_file['QuestionsSocialVulnerability']['title']

        for item in ReadJSONFile.json_file['QuestionsSocialVulnerability']['questions_answers']:
            QuestionsSocialVulnerability.questions_answers.append(item)


class QuestionsFragility:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsFragility.TITLE = ReadJSONFile.json_file['QuestionsFragility']['title']
        for item in ReadJSONFile.json_file['QuestionsFragility']['questions_answers']:
            QuestionsFragility.questions_answers.append(item)


class QuestionsGerontologistEvaluation:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsGerontologistEvaluation.TITLE = ReadJSONFile.json_file['QuestionsGerontologistEvaluation']['title']
        for item in ReadJSONFile.json_file['QuestionsGerontologistEvaluation']['questions_answers']:
            QuestionsGerontologistEvaluation.questions_answers.append(item)


class QuestionsPlanningActions:
    TITLE = ''
    questions_answers = []

    @staticmethod
    def load():
        QuestionsPlanningActions.TITLE = ReadJSONFile.json_file['QuestionsPlanningActions']['title']
        for item in ReadJSONFile.json_file['QuestionsPlanningActions']['questions_answers']:
            QuestionsPlanningActions.questions_answers.append(item)
