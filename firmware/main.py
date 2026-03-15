# main.py — Loop principal do BitTeclado
# Projeto 1 - Lab de Sistemas Embarcados (FEEC/UNICAMP)
# Plataforma: BitDogLab V7 (RP2040)

import time
from buzzer import Buzzer
from controles import Controles
from display import Display
from notas import frequencia, nomes_banco, NUM_BANCOS, OITAVA_MIN, OITAVA_MAX

# Inicializacao
bz = Buzzer()
ctrl = Controles()
disp = Display()

# Estado inicial
banco = 0
oitava = 4
ultimo_joy_x = 0
ultimo_joy_y = 0
cooldown_x = 0  # evita mudanca rapida demais
cooldown_y = 0

COOLDOWN_MS = 200  # tempo minimo entre mudancas de banco/oitava

# Tela de boas-vindas
disp.mostrar_inicio()
time.sleep_ms(1500)

# Loop principal
while True:
    # 1. Ler joystick X — mudar banco
    joy_x = ctrl.ler_joystick_x()
    if joy_x != 0 and cooldown_x <= 0:
        banco = (banco + joy_x) % NUM_BANCOS
        cooldown_x = COOLDOWN_MS
    elif joy_x == 0:
        cooldown_x = 0

    # 2. Ler joystick Y — mudar oitava
    joy_y = ctrl.ler_joystick_y()
    if joy_y != 0 and cooldown_y <= 0:
        oitava = max(OITAVA_MIN, min(OITAVA_MAX, oitava + joy_y))
        cooldown_y = COOLDOWN_MS
    elif joy_y == 0:
        cooldown_y = 0

    # 3. Ler botoes
    a, b, c = ctrl.ler_botoes()
    botao_ativo = None

    if a:
        botao_ativo = 0
    elif b:
        botao_ativo = 1
    elif c:
        botao_ativo = 2

    # 4. Tocar ou parar
    if botao_ativo is not None:
        freq = frequencia(banco, oitava, botao_ativo)
        bz.tocar(freq)
    else:
        bz.parar()

    # 5. Atualizar display (so se mudou)
    nomes = nomes_banco(banco)
    disp.atualizar(banco, oitava, nomes, botao_ativo)

    # 6. Sleep e cooldown
    time.sleep_ms(20)
    if cooldown_x > 0:
        cooldown_x -= 20
    if cooldown_y > 0:
        cooldown_y -= 20
