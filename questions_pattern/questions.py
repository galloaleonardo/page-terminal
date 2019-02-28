class QuestionsAttitudesAging:
    TITLE = 'A) Atitudes em relação a velhice e envelhecimento: '

    questions_answers_attitudes_agging = {
        '1. Que idade o(a) senhor(a) sente ter? Por quê? ': None,
        '2. Existe pontos positivos e negativos presentes nessa fase da vida? Quais? ': None,
        '3. Você gerontologo(a), como classificaria as respostas acima? \n' +
        '[0] Ruim | [1] Mediana | [2] Boa: ': None
    }


class QuestionsQualityLife:
    TITLE = 'B) Qualidade de vida: '

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
    TITLE = 'C) Sentidos: '

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
    TITLE = 'D) Desnutrição: '

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
    TITLE = 'E) Capacidade funcional: '

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
    TITLE = 'F) Depressão: '

    questions_answers_depression = {
        '1. De modo geral o(a) senhor(a) está satisfeito com a vida? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '1.1. Se não, por quê? <Enter> se resposta anterior for [Sim]': None,

        '2. O(a) senhor (a) se sente triste com frequência? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '2.1. Se não, por quê? <Enter> se resposta anterior for [Sim]': None,

        '3. O(a) senhor(a) abandonou muitas das coisas que fazia ou gostava de fazer? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '3.1. Se não, por quê? <Enter> se resposta anterior for [Sim]': None,

        '4. O(a) senhor(a) tem medo de que algum mal vá lhe acontecer? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '4.1. Se não, por quê? <Enter> se resposta anterior for [Sim]': None,

        '5. O(a) Sr.(a) se sente impaciente e agitado(a) com frequência? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '5.1. Se não, por quê? <Enter> se resposta anterior for [Sim]': None,

        '6. O O(a) Sr.(a) tem dificuldades em concentrar-se? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '6.1. Se não, por quê? <Enter> se resposta anterior for [Sim]': None
    }


class QuestionsCardiovascularFactors:
    TITLE = 'G) Fatores cardiovasculares: '

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


class QuesntionsMedicationAdministration:
    TITLE = 'H) Administração de medicamentos: '

    questions_answers_medication_administration = {
        '1. Nos últimos 5 anos, algum médico já disse que o(a) senhor(a) tem as seguintes doenças/problemas? \n' +
        'a. Doença do coração (angina, infarto ou ataque cardíaco): \n' +
        '[0] = Sim | [1] = Não: ': None,

        'b. Pressão alta/hipertensão (ver RCV): \n' +
        '[0] = Sim | [1] = Não: ': None,

        'c. Derrame / AVC / Isquemia: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'd. Diabetes Mellitus (ver RCV): \n' +
        '[0] = Sim | [1] = Não: ': None,

        'e. Tumor maligno / Câncer: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'f. Doenças do pulmão, como bronquite e enfisema: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'g. Depressão: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'h. Incontinência urinária/perda de urina \n' +
        '[0] = Sim | [1] = Não: ': None,

        'i. Outras? ': None,

        '2. Quantidade de doenças crônicas: ': None,

        '3. Quais são os medicamentos utilizados pelo(a) senhor(a)? ' +
        '(Solicitar bulas e registrar com letra legível): ': None,

        '4. Quantidade de medicamentos? \n' +
        '[0] = ≥ 5 | [1] = < 5 | [1] Não se aplica: ': None,

        '5. O(a) senhor(a) sabe para que serve todos os medicamentos que utiliza? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '6. Todos os medicamentos foram prescritos pelo mesmo médico? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '7. O(a) senhor(a) toma os medicamentos de acordo com as orientações médicas? Por quê? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '8. O(a) senhor(a) alguma vez já deixou de tomar os medicamentos? Por quê? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '9. O(a) senhor(a) tem o costume de tomar remédios por conta própria (automedicação)? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '10. Verificar na lista dos critérios de Beers (anexada ao PAGe) ' +
        'se o(a) idoso(a) toma algum medicamento inapropriado \n' +
        '[0] = Sim | [1] = Não: ': None,

        'Para calcular o risco para reações adversas, circule e cruze ' +
        'as informações acima na seguinte tabela: \n \n'

        '╔═════════════════════════════════╗ \n' +
        '║ USO DE MEDICAMENTO INAPROPRIADO ║ \n' +
        '╠═════════════════╦═══════╦═══════╣ \n' +
        '║      Nro de     ║  Não  ║  Sim  ║ \n' +
        '║   diagnósticos  ║       ║       ║ \n' +
        '╠═════════════════╬═══════╬═══════╣ \n' +
        '║        1        ║   18  ║   9   ║ \n' +
        '╠═════════════════╬═══════╬═══════╣ \n' +
        '║        2        ║   15  ║   6   ║ \n' +
        '╠═════════════════╬═══════╬═══════╣ \n' +
        '║        3        ║   11  ║   2   ║ \n' +
        '╠═════════════════╬═══════╬═══════╣ \n' +
        '║        4        ║   7   ║   0   ║ \n' +
        '╠═════════════════╬═══════╬═══════╣ \n' +
        '║        5        ║   4   ║   0   ║ \n' +
        '╚═════════════════╩═══════╩═══════╝ \n' +
        'Pressione <Enter> para continuar...': None,

        '10.  O(a) idoso(a) utiliza uma quantidade de medicamentos ' +
        'superior ao valor indicado/circulado na tabela acima? \n' +
        '[0] = Sim | [1] = Não: ': None
    }


class QuestionsEnvironment:
    TITLE = 'I) Ambiente: '

    questions_answers_environment = {
        '1. Ambiente Interno: Na casa do(a) senhor(a)... \n' +
        'a. Os móveis são estáveis? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'b. Há móveis/objetos/fios/tapetes/animais nas áreas de circulação? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'c. O piso é escorregadio (ex. encerado)? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'd. A casa do(a) senhor(a) possui escadas/degraus? Se sim, ' +
        'há corrimãos em ambos os lados da escada? (Pontue 1, caso não tenha escadas/degraus na casa). \n' +
        '[0] = Sim | [1] = Não: ': None,

        'e. As escadas/degraus são iluminados adequadamente durante a noite? (idem) \n' +
        '[0] = Sim | [1] = Não: ': None,

        'f. Os degraus são adequados (tamanho, rebordos, largura e padronagem etc)? (Idem) \n' +
        '[0] = Sim | [1] = Não: ': None,

        'g. Há tapetes antiderrapantes (fora e dentro do box)? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '2. Comportamento de Risco... \n' +
        'a. O(a) senhor(a) costuma subir em banquetas para alcançar objetos altos? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'b. O(a) senhor(a) acende as luzes quando levanta-se à noite? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'c. O(a) senhor(a) utiliza calçados seguros e adequados ' +
        '(solado antiderrapante, bem ajustados e firmes no pé, sem saltos etc) \n' +
        '[0] = Sim | [1] = Não: ': None,

        '3. Ambiente Externo: O(a) senhor(a) está satisfeito com.. \n' +
        'a. O acesso ao transporte público no seu bairro? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'b. O tempo de transporte entre casa/trabalho/escola/hospital? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'c. O acesso ao comércio no seu bairro? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'd. A facilidade e prazer em andar a pé nele/com cadeira de rodas/bengala/andador? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'e. O acesso à diversão no seu bairro (restaurantes, cinema, clubes etc.) \n' +
        '[0] = Sim | [1] = Não: ': None,

        'f. A segurança quanto à ameaça da criminalidade no seu bairro? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'g. O barulho do tráfego no seu bairro? \n' +
        '[0] = Sim | [1] = Não: ': None,

        'h. O local (bairro) que tem para viver? \n' +
        '[0] = Sim | [1] = Não: ': None
    }


class QuestionsFalls:
    TITLE = 'J) Quedas: '

    questions_answers_falls = {
        '1. Histórico de quedas: O(a) senhor(a) sofreu alguma queda nos últimos 12 meses? ' +
        '(se não, vá para a questão 3). Quantas? \n' +
        '[0] = Sim | [1] = Não: ': None,

        '2. O que o (a) senhor(a) estava fazendo quando sofreu essa(s) queda(s) ' +
        '(investigar atividade realizada, local, horário do dia, tipo de calçado, riscos ambientais etc)?': None,

        '3. Força (MMII): Avalie se o(a) idoso(a) consegue levantar-se de uma cadeira sem ajuda \n' +
        '[0] = Sim | [1] = Não: ': None,

        '4. Equilíbrio: Avalie se o(a) idoso(a) consegue permanecer em 1 perna, ' +
        'sem apoio dos membros superiores, durante 5 segundos. \n' +
        '[0] = Sim | [1] = Não: ': None,

        '5. Baseado nos itens anteriores preenchidos neste e em todos os ' +
        'outros domínios, identifique se o idoso apresenta/utiliza: \n' +
        'a. Idade > 80 anos: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'b. Sexo feminino: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'c. Histórico de quedas: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'd. Histórico de fraturas: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'e. ↓ equilíbrio: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'f. ↓ força (MMII): \n' +
        '[0] = Sim | [1] = Não: ': None,

        'g. Comprometimento AVDs: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'h. Alterações cognitivas: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'i. Riscos domésticos/comportamento de risco: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'j. AVE prévio: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'k. Déficit visual: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'l. Inatividade: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'm. Dispositivo de auxílio de marcha: \n' +
        '[0] = Sim | [1] = Não: ': None,

        'n. Medicamentos em uso: anestésicos, anti-histamínicos, catárticos, diuréticos,  anti-hipertensivos, ' +
        'anticonvulsivantes, benzodiazepínicos, hipoglicemiantes, psicotrópicos, sedativos/hipnóticos \n' +
        '[2] = Nenhum | [1] = De 1 = De 1 a 2 | [0] = ≥ 3: ': None,

        'o. Outras doenças predisponentes: hipertensão, tontura/vertigem, Parkinson, amputação de membros ' +
        'inferiores, convulsões, artrite, osteoporose, incontinência, diabetes, neuropatia, hipotensão postural \n' +
        '[2] = Nenhum | [1] = De 1 = De 1 a 2 | [0] = ≥ 3: ': None
    }
