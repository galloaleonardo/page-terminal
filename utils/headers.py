from utils import utils


class Headers:

    @staticmethod
    def title_header():
        utils.clear()
        print('{}{}- - - - - - - - - - - - - - - -'.format(utils.Color.CYAN, utils.Color.BOLD))
        print('Plano de Atenção Gerontológica')
        print('- - - - - - - - - - - - - - - -')
        print('v.0.1{}'.format(utils.Color.END))
        utils.line_break()
