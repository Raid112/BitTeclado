# controles.py — Leitura de botoes e joystick com debounce
# BitTeclado - Projeto 1 Lab Embarcados

from machine import Pin, ADC


# Deadzone: 25% do range (centro ~32768, range 0-65535)
DEADZONE_MIN = 24576   # 32768 - 8192
DEADZONE_MAX = 40960   # 32768 + 8192


class Controles:
    def __init__(self):
        # Botoes (ativo LOW, pull-up interno)
        self.btn_a = Pin(5, Pin.IN, Pin.PULL_UP)
        self.btn_b = Pin(6, Pin.IN, Pin.PULL_UP)
        self.btn_c = Pin(10, Pin.IN, Pin.PULL_UP)

        # Joystick
        self.adc_x = ADC(Pin(27))  # eixo X — selecao de banco
        self.adc_y = ADC(Pin(26))  # eixo Y — selecao de oitava
        self.joy_sw = Pin(22, Pin.IN, Pin.PULL_UP)

    def ler_botoes(self):
        """Retorna tupla (a, b, c) com True se pressionado."""
        return (
            self.btn_a.value() == 0,
            self.btn_b.value() == 0,
            self.btn_c.value() == 0,
        )

    def ler_joystick_x(self):
        """Retorna direcao do eixo X: -1 (esquerda), 0 (centro), +1 (direita)."""
        val = self.adc_x.read_u16()
        if val < DEADZONE_MIN:
            return -1
        elif val > DEADZONE_MAX:
            return 1
        return 0

    def ler_joystick_y(self):
        """Retorna direcao do eixo Y: -1 (baixo), 0 (centro), +1 (cima)."""
        val = self.adc_y.read_u16()
        if val < DEADZONE_MIN:
            return -1
        elif val > DEADZONE_MAX:
            return 1
        return 0
