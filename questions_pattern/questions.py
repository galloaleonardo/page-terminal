class QuestionsAttitudesAging:
    questions_answers_attitudes_agging = {
        '1. Que idade o(a) senhor(a) sente ter? Por quê? ': None,
        '2. Existe pontos positivos e negativos presentes nessa fase da vida? Quais? ': None,
        '3. Você gerontologo(a), como classificaria as respostas acima? \n' +
        '[0] Ruim | [1] Mediana | [2] Boa: ': None
    }


class QuestionsQualityLife:
    questions_answers_quality_life = {
        '1. Em geral, o(a) senhor(a) se considera uma pessoa: \n' +
        '[0] = Infeliz | [1] = Não muito feliz | [2] = Feliz | [3] = Muito Feliz: ': None,

        '2. Em geral, o(a) senhor(a) diria que sua saúde é: \n' +
        '[0] = Muito ruim | [1] = Ruim | [2] = Boa | [3] = Muito boa: ': None,

        '2.1. Por quê? ': None,

        '3. Como o(a) senhor(a) avalia sua qualidade de vida? \n' +
        '[0] = Muito ruim | [1] = Ruim | [2] = Boa | [3] = Muito boa: ': None,

        '3.1. Por quê? ': None,

        '4. O(a) senhor(a) se sente capaz de fazer coisas/atividades ' +
        'tão bem quanto a maioria das outras pessoas? \n' +
        '[0] = Nunca | [1] = Raramente | [2] = A maioria das vezes | [3] = Sempre: ': None,
    
        '5. Quanta dor no corpo o(a) senhor(a) sentiu nas últimas quatro semanas? \n' +
        '[0] = Intensa | [1] = Moderada | [2] = Leve | [3] = Nenhuma: ': None,

        '5.1. Onde? \n': None,

        '6. Durante o último mês, como o(a) senhor(a) classificaria a ' +
        'qualidade do seu sono de uma maneira geral? \n' +
        '[0] = Muito ruim | [1] = Ruim | [2] = Boa | [3] = Muito boa: ': None,

        '7. O(a) senhor(a) é sexualmente ativo(a)? \n'
        '[0] = Não | [1] = Sim: ': None,

        '7.1. Quão satisfeito o(a) senhor(a) está com o seu relacionamento afetivo? \n' +
        '[0] = Muito insatisfeito | [1] = Insatisfeito | [2] = Satisfeito | [3] = Muito satisfeito: ': None,

        '8. Como o(a) senhor(a) ocupa o seu tempo (investigar sobre sua rotina)? \n': None,

        '9. O(a) senhor(a) está satisfeito com a forma que ocupa o seu tempo/rotina? \n' +
        '[0] Não | [1] Sim: ': None,

        '10. O(a) senhor(a) realiza alguma atividade prazerosa e/ou de lazer? \n' +
        '[0] Não | [1] Sim: ': None,

        '10.1. Se sim, qual(is): ': None,

        '10.2. Frequência: ': None,

        '11. De todos os aspectos perguntados anteriormente (saúde, dor, sono, ' +
        'capacidade de fazer atividades, relacionamento afetivo, ocupação do tempo, ' +
        'atividades de lazer,outros), qual o(a) senhor(a) considera mais importante ' +
        'para a sua qualidade de vida? [1] a [10]: ': None
    }


class QuestionsDirections:
    questions_answers_directions = {
        '1. O(a) senhor(a) tem dificuldade para ver TV, ler jornal ou fazer qualquer outra ' +
        'atividade devido a problemas visuais? Se sim, por quê? ' +
        '(investigar se necessita de óculos ou cirurgia de catarata). \n' +
        '[0] = Sim | [1] = Não: ': None,

        '2. O(a) senhor(a) tem dificuldade para ouvir o que as pessoas falam? Se sim, por quê? ' +
        '(investigar a necessidade de aparelho auditivo) \n' +
        '[0] = Sim | [1] = Não: ': None,

        '3. O(a) senhor(a) tem feridas ou lesões na língua, bochecha, céu da boca ou lábios, presentes ' +
        'há mais de 1 mês? Se sim, por quê? (investigar a presença de prótese e se a mesma encontra-se ajustada)?\n' +
        '[0] = Sim | [1] = Não: ': None,

        '4. Como o(a) senhor(a) avaliaria o funcionamento dos seus sentidos ' +
        '(por exemplo, audição, visão, paladar, olfato, tato)? \n' +
        '[0] = Muito ruim | [1] = Ruim | [2] = Boa | [3] = Muito boa: ': None,

        '5. Até que ponto o funcionamento dos seus sentidos (por exemplo, audição, visão, paladar, olfato, tato) ' +
        'afeta a sua capacidade de participar em atividade e de interagir com outras pessoas? \n' +
        '[0] = Completamente | [1] = Muito | [2] = Muito pouco | [3] = Nada: ': None
    }


class QuestionsMalnutrition:
    questions_answers_malnutrition = {
        '1. O(a) senhor(a) acredita ter algum problema nutricional? \n' +
        '[0] = Sim, estou desnutrido | [1] = Não sei dizer | [2] = Não tenho problemas: ': None,

        '2. Quantas vezes por dia o(a) senhor(a) come alguma coisa? \n' +
        '[0] Uma refeição | [1] = Duas refeições | [2] = Três ou mais refeições: ': None,

        '3. Nos últimos 3 meses houve diminuição involuntária da ingesta alimentar? \n' +
        '[0] = Grave | [1] = Moderada | [2] = Leve [3] = Sem diminuição: ': None,

        '4. O(a) senhor(a) perdeu peso sem motivo aparente nos últimos 3 meses? \n' +
        '[0] = 3KG | [1] = Não sabe informar | [2] = Entre 1 e 3KG | [3] = Não: ': None,

        '5. O(a) Sr(a) passou por algum estresse psicológico, ' +
        'doença aguda e/ou internações nos últimos 3 meses? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '6. Índice de Massa Corporal (IMC = peso ______ [kg] / estatura ______ [m2]) \n' +
        '[0] = IMC < 19 | [1] =19 ≤ IMC < 21 | [2] = 21 ≤ IMC < 23 | [3] =I MC ≥ 23: ': None,

        '7. Caso não seja possível aferir a estatura e o peso do idoso, substitua a questão 4 pela questão 5.' +
        'Perímetro da Perna (PP) em cm: \n' +
        '[0] = PP < 31 | [1] = PP ≥ 31: ': None
    }


class QuestionsFunctionalCapacity:
    questions_answers_functional_capacity = {
        '1. O(a) senhor(a) necessita de ajuda para: ' +
        '1.1. Verstir-se? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '1.2. Tomar banho? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '1.3. Usar o telefone? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '1.4. Preparar a própria comida? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '1.5. Fazer compras? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '1.6. Usar meios de transporte? \n' +
        '[0] = Sim | [1] = Não: ': None
    }


class QuestionsDepression:
    questions_answers_depression = {
        '1. De modo geral o(a) senhor(a) está satisfeito com a vida? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '1.1. Se não, por quê? <ENTER> se resposta anterior for [Sim]': None,

        '2. O(a) senhor (a) se sente triste com frequência? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '2.1. Se não, por quê? <ENTER> se resposta anterior for [Sim]': None,

        '3. O(a) senhor(a) abandonou muitas das coisas que fazia ou gostava de fazer? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '3.1. Se não, por quê? <ENTER> se resposta anterior for [Sim]': None,

        '4. O(a) senhor(a) tem medo de que algum mal vá lhe acontecer? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '4.1. Se não, por quê? <ENTER> se resposta anterior for [Sim]': None,

        '5. O(a) Sr.(a) se sente impaciente e agitado(a) com frequência? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '5.1. Se não, por quê? <ENTER> se resposta anterior for [Sim]': None,

        '6. O O(a) Sr.(a) tem dificuldades em concentrar-se? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '6.1. Se não, por quê? <ENTER> se resposta anterior for [Sim]': None
    }


class QuestionsCardiovascularFactors:
    questions_answers_cardiovascular_factors = {
        '1. O(a) senhor(a) tem histórico familiar (primeiro grau) de DCV (infarto, derrame, angina)? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '2. O(a) senhor(a) tem hipertensão arterial? \n' +
        '[0] = Sim, mas desconhece os valores de PA | [0] = Sim, mas não controlada (PA>140/90 mmHg), \n' +
        '[1] = Sim, mas controlada (PA<140/90 mmHg) | [2] = Não: ': None,

        '3. O(a) senhor(a) tem diabetes? \n' +
        '[0] = Sim, mas desconhece os valores de glicemia | \n' +
        '[0] = Sim, e não controlada (glicemia jejum > 100 mg/dL) | \n' +
        '[1] = Sim, mas controlada (glicemia jejum < 100 mg/dL) | [2] = Não: ': None,

        '4. O(a) senhor(a) tem colesterol alterado? \n' +
        '[0] = Sim, mas desconhece os valores de CT e HDL | \n' +
        '[0] = Sim, mas não controlado(CT>200 e/ou HDL<60 mg/dL) | \n' +
        '[1] = Sim, mascontrolado (CT<200 e/ou HDL>60 mg/dL) | [2] = Não: ': None,

        '5. Índice de massa corporal (KG/m2) - Adicione o prefixo [IMC] antes: ': None,

        '6. O(a) senhor(a) é fumante? \n' +
        '[0] = Sim | [1] = Não, mas já fumou antes | [2] - Não: ': None,

        '7. Na última semana, o(a) senhor(a) ingeriu bebidas alcoólicas? \n' +
        '[0] = Sim (>2 doses de destilado, 1 taça de vinho ou 2 latas de cerveja por dia) | ' +
        '[1] = sim (>2 doses de destilado, ou 1 taça de vinho ou 2 latas de cerveja por dia) | [2] = Não': None,

        '8. O(a) senhor(a) pratica exercícios físicos? \n' +
        '[0] = Não | [1] = Sim (<150min/semana) |  [2] = Sim (>150min/semana): ': None
    }
