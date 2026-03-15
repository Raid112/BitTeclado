# notas.py — Tabela de frequencias e sistema de bancos
# BitTeclado - Projeto 1 Lab Embarcados

# Notas da escala cromatica (nome, frequencia base na oitava 4)
NOTAS = [
    ("Do",  261.63),
    ("Do#", 277.18),
    ("Re",  293.66),
    ("Re#", 311.13),
    ("Mi",  329.63),
    ("Fa",  349.23),
    ("Fa#", 369.99),
    ("Sol", 392.00),
    ("Sol#",415.30),
    ("La",  440.00),
    ("La#", 466.16),
    ("Si",  493.88),
]

# Bancos de 3 notas (indices em NOTAS)
BANCOS = [
    (0, 1, 2),    # Banco 0: Do, Do#, Re
    (3, 4, 5),    # Banco 1: Re#, Mi, Fa
    (6, 7, 8),    # Banco 2: Fa#, Sol, Sol#
    (9, 10, 11),  # Banco 3: La, La#, Si
]

NUM_BANCOS = len(BANCOS)
OITAVA_MIN = 3
OITAVA_MAX = 7
OITAVA_REF = 4  # oitava de referencia (frequencias base)


def frequencia(banco, oitava, botao):
    """Retorna a frequencia em Hz para o banco, oitava e botao (0-2) dados."""
    idx_nota = BANCOS[banco][botao]
    _, freq_base = NOTAS[idx_nota]
    # Ajustar oitava: cada oitava acima dobra a frequencia
    fator = 2 ** (oitava - OITAVA_REF)
    return freq_base * fator


def nomes_banco(banco):
    """Retorna tupla com os 3 nomes das notas do banco."""
    return tuple(NOTAS[i][0] for i in BANCOS[banco])
