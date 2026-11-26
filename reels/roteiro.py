"""Roteiro de cada Reel.

cenas: (clipe, início no bruto em s, duração no bruto em s, velocidade). Velocidade 0.6 = câmera lenta.
textos: de/até em segundos do vídeo final; pos = 'alto', 'baixo' ou 'centro'.
Cada cena começa 0,4 s antes do fim da anterior (transição suave).
"""

REELS = {
    'shabat': {
        'arquivo': '01-shabat-shalom',
        'cenas': [
            ('L461', 3.4, 3.3, 0.6),   # acende a vela no castiçal dourado
            ('L462', 0.4, 2.0, 0.7),   # as duas velas acesas
            ('L467', 1.2, 3.0, 0.75),  # castiçal na mão
            ('L473', 0.1, 2.4, 0.8),   # castiçal turquesa, de baixo para cima
            ('L482', 1.8, 3.0, 0.7),   # acende a vela no castiçal turquesa
            ('L438', 1.0, 3.5, 0.8),   # detalhe da travessa de chalá
            ('L450', 0.3, 2.4, 0.8),   # detalhe do cálice
            ('L445', 0.5, 2.4, 0.8),   # cálice inteiro
        ],
        'textos': [
            {'de': 0.2, 'ate': 4.9, 'pos': 'alto', 'eyebrow': 'Judaica pintada à mão', 'titulo': 'Shabat <em>Shalom</em>'},
            {'de': 7.8, 'ate': 11.3, 'pos': 'baixo', 'tam': 'm', 'titulo': 'Cada letra, cada flor,<br><em>pintada à mão.</em>'},
            {'de': 17.9, 'ate': 21.8, 'pos': 'alto', 'tam': 'm', 'titulo': 'Para a mesa do Shabat:<br><em>travessa, cálice e castiçais.</em>'},
        ],
        'fim': {'titulo': 'Peças que atravessam<br><em>gerações.</em>', 'texto': 'Judaica pintada à mão, sob encomenda.',
                'chamada': 'Encomende pelo link na bio'},
        'capa': 1.6,
    },
    'detalhes': {
        'arquivo': '02-detalhes-que-so-a-mao-faz',
        'xf': 0.25,
        'cenas': [
            ('L486', 1.0, 1.5, 0.75),  # manta do Elefante Real
            ('L501', 0.2, 1.4, 0.7),   # Relógio Imari
            ('L547', 0.6, 1.6, 0.8),   # araras da jardineira
            ('L567', 0.1, 1.6, 0.8),   # garça da placa
            ('L438', 1.5, 1.6, 0.8),   # prato de Shabat
            ('L533', 0.3, 1.6, 0.8),   # tampa vista de cima
            ('L581', 1.0, 1.6, 0.8),   # aparelho Horta
            ('L473', 0.4, 1.6, 0.8),   # castiçal turquesa
        ],
        'textos': [
            {'cena': 0, 'mais': 0.1, 'dur': 3.3, 'pos': 'centro', 'titulo': 'Detalhes que só<br><em>a mão</em> faz.'},
        ],
        'fim': {'titulo': 'Cada peça,<br><em>uma obra única.</em>', 'texto': 'Porcelana pintada à mão, sob encomenda.',
                'chamada': 'Encomende pelo link na bio', 'dur': 3.0},
        'capa': 1.0,
    },
    'elefante': {
        'arquivo': '03-elefante-real',
        'cenas': [
            ('L484', 0.3, 3.8, 0.75),  # de lado, passeando pela peça
            ('L486', 0.2, 3.3, 0.7),   # a manta de perto
            ('L485', 0.2, 2.6, 0.75),  # tromba e presas
            ('L483', 0.2, 3.1, 0.8),   # três quartos
        ],
        'textos': [
            {'cena': 0, 'mais': 0.2, 'dur': 4.0, 'pos': 'alto', 'eyebrow': 'Acervo Pituá', 'titulo': 'Elefante <em>Real</em>'},
            {'cena': 1, 'mais': 0.4, 'dur': 3.6, 'pos': 'baixo', 'tam': 'm', 'titulo': 'Relevo, dourado<br>e mandalas,<br><em>pintados à mão.</em>'},
        ],
        'fim': {'titulo': 'Uma peça única.<br><em>A sua também pode ser.</em>', 'texto': 'Arte sob encomenda.',
                'chamada': 'Encomende pelo link na bio'},
        'capa': 1.6,
    },
    'relogio': {
        'arquivo': '04-relogio-imari',
        'cenas': [
            # L490P e L492P: os mesmos clipes com os ponteiros acrescentados (reels/ponteiros.py)
            ('L490P', 0.2, 3.5, 0.7),  # do detalhe para a peça inteira
            ('L500', 0.2, 3.6, 0.8),   # a paisagem da base
            ('L501', 0.1, 1.7, 0.6),   # detalhe da lateral
            ('L492P', 0.2, 3.2, 0.8),  # de frente
        ],
        'textos': [
            {'cena': 0, 'mais': 0.2, 'dur': 4.2, 'pos': 'alto', 'eyebrow': 'Acervo Pituá', 'titulo': 'Relógio <em>Imari</em>'},
            {'cena': 1, 'mais': 0.4, 'dur': 3.6, 'pos': 'baixo', 'tam': 'm', 'titulo': 'Inspirado na<br>porcelana japonesa,<br><em>pintado traço a traço.</em>'},
        ],
        'fim': {'titulo': 'Uma peça única.<br><em>A sua também pode ser.</em>', 'texto': 'Arte sob encomenda.',
                'chamada': 'Encomende pelo link na bio'},
        'capa': 2.0,
    },
    'mesa': {
        'arquivo': '05-arte-tambem-vai-a-mesa',
        'cenas': [
            ('L506', 1.0, 2.6, 0.7),   # Queijeira Hibisco: abre a tampa
            ('L511', 3.0, 4.0, 0.8),   # a tampa na mão
            ('L512', 0.6, 2.0, 0.8),   # Manteigueira Borboletas chegando à mesa
            ('L519', 6.5, 3.6, 0.8),   # passando manteiga no pão
            ('L523', 19.5, 4.0, 0.8),  # Latinhas Sardinha & Atum
            ('L529', 0.3, 3.0, 0.7),   # pote com tampa: abre e aparece o homus
            ('L541', 8.0, 4.0, 1.0),   # petisqueira com queijo e uvas
        ],
        'textos': [
            {'cena': 0, 'mais': 0.1, 'dur': 3.6, 'pos': 'alto', 'eyebrow': 'Feitas para usar', 'titulo': 'Arte também<br>vai <em>à mesa.</em>'},
            {'cena': 3, 'mais': 0.3, 'dur': 3.6, 'pos': 'alto', 'tam': 'm', 'titulo': 'Manteigueira,<br>queijeira,<br><em>petisqueira…</em>'},
            {'cena': 5, 'mais': 0.3, 'dur': 3.6, 'pos': 'baixo', 'tam': 'm', 'titulo': 'Peças únicas para os<br><em>momentos de todo dia.</em>'},
        ],
        'fim': {'titulo': 'Sua mesa,<br><em>do seu jeito.</em>', 'texto': 'Peças pintadas à mão, sob encomenda.',
                'chamada': 'Encomende pelo link na bio'},
        'capa': 1.2,
    },
    'jardineira': {
        'arquivo': '06-jardineira-mata-atlantica',
        'cenas': [
            ('L544', 0.1, 1.5, 0.6),   # a jardineira inteira
            ('L546', 0.2, 3.3, 0.8),   # tucano
            ('L547', 0.2, 2.4, 0.7),   # araras
            ('L548', 0.2, 2.9, 0.8),   # papagaio
            ('L551', 0.2, 3.4, 0.8),   # tucano de bico colorido
        ],
        'textos': [
            {'cena': 0, 'mais': 0.2, 'dur': 4.8, 'pos': 'alto', 'eyebrow': 'Acervo Pituá', 'titulo': 'Jardineira<br><em>Mata Atlântica</em>'},
            {'cena': 3, 'mais': 0.3, 'dur': 3.2, 'pos': 'baixo', 'tam': 'm', 'titulo': 'Tucanos, araras<br>e papagaios,<br><em>pintados à mão.</em>'},
        ],
        'fim': {'titulo': 'A natureza brasileira<br><em>em porcelana.</em>', 'texto': 'Arte sob encomenda.',
                'chamada': 'Encomende pelo link na bio'},
        'capa': 3.5,
    },
    'mezuza': {
        'arquivo': '07-mezuza',
        'cenas': [
            ('L555', 0.0, 2.4, 0.6),   # a mão toca a mezuzá
            ('L558', 0.2, 1.8, 0.6),   # na porta de casa
            ('L563', 0.4, 2.2, 0.7),   # outra mezuzá
            ('L562', 0.3, 1.6, 0.7),   # a porta aberta
        ],
        'textos': [
            {'cena': 0, 'mais': 0.2, 'dur': 3.6, 'pos': 'baixo', 'eyebrow': 'Mezuzá pintada à mão', 'tam': 'm', 'titulo': 'A bênção<br><em>na porta de casa.</em>'},
        ],
        'fim': {'titulo': 'Para proteger<br>e <em>receber bem.</em>', 'texto': 'Mezuzás pintadas à mão, sob encomenda.',
                'chamada': 'Encomende pelo link na bio'},
        'capa': 3.2,
    },
    'jantar': {
        'arquivo': '08-mesa-posta',
        'cenas': [
            ('L576', 0.5, 3.0, 0.75),  # pratos chegando à mesa
            ('L577', 0.2, 2.5, 0.75),  # detalhe dos tomates e cogumelos
            ('L581', 0.3, 3.6, 0.8),   # Aparelho para Risoto Horta
            ('L583', 0.3, 3.6, 0.8),   # a mesa posta
            ('L586', 2.6, 2.0, 0.75),  # servindo na travessa
        ],
        'textos': [
            {'cena': 0, 'mais': 0.2, 'dur': 3.4, 'pos': 'alto', 'eyebrow': 'Mesa posta', 'titulo': 'Para receber<br><em>com arte.</em>'},
            {'cena': 2, 'mais': 0.3, 'dur': 3.8, 'pos': 'alto', 'tam': 'm', 'eyebrow': 'Aparelho para Risoto', 'titulo': 'Uma horta inteira,<br><em>pintada à mão.</em>'},
        ],
        'fim': {'titulo': 'Uma mesa que<br><em>ninguém esquece.</em>', 'texto': 'Aparelhos e travessas pintados à mão, sob encomenda.',
                'chamada': 'Encomende pelo link na bio'},
        'capa': 1.6,
    },
}
