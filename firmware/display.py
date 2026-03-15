# display.py — Painel OLED para o BitTeclado
# BitTeclado - Projeto 1 Lab Embarcados

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C


class Display:
    def __init__(self):
        i2c = SoftI2C(scl=Pin(3), sda=Pin(2))
        self.oled = SSD1306_I2C(128, 64, i2c)
        self._estado_anterior = None

    def atualizar(self, banco, oitava, nomes, botao_ativo=None):
        """Atualiza o display com informacoes do estado atual.

        Args:
            banco: numero do banco ativo (0-3)
            oitava: oitava atual (3-7)
            nomes: tupla com 3 nomes de notas
            botao_ativo: indice do botao ativo (0, 1, 2) ou None
        """
        estado = (banco, oitava, nomes, botao_ativo)
        if estado == self._estado_anterior:
            return  # sem mudanca, nao redesenha
        self._estado_anterior = estado

        self.oled.fill(0)

        # Linha 1: Oitava
        self.oled.text("Oitava: {}".format(oitava), 0, 0)

        # Linha 3-4: Notas com destaque na ativa
        y_notas = 24
        y_labels = 36
        x_positions = [4, 44, 84]  # posicoes X para 3 colunas

        for i, nome in enumerate(nomes):
            if botao_ativo == i:
                texto = "[{}]".format(nome)
            else:
                texto = " {} ".format(nome)
            self.oled.text(texto, x_positions[i], y_notas)

        # Labels dos botoes
        self.oled.text("  A", x_positions[0], y_labels)
        self.oled.text("  B", x_positions[1], y_labels)
        self.oled.text("  C", x_positions[2], y_labels)

        # Linha 6: Banco
        self.oled.text("Banco: {}/4".format(banco + 1), 0, 56)

        self.oled.show()

    def mostrar_inicio(self):
        """Tela de boas-vindas ao ligar."""
        self.oled.fill(0)
        self.oled.text("BitTeclado", 24, 8)
        self.oled.text("Lab Embarcados", 8, 28)
        self.oled.text("FEEC/UNICAMP", 16, 48)
        self.oled.show()
