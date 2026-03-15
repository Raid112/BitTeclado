# buzzer.py — Controle PWM do buzzer
# BitTeclado - Projeto 1 Lab Embarcados

from machine import Pin, PWM


class Buzzer:
    def __init__(self, pin=21):
        self.pwm = PWM(Pin(pin))
        self.pwm.duty_u16(0)
        self._tocando = False

    def tocar(self, freq_hz):
        """Toca uma nota na frequencia especificada (Hz)."""
        if freq_hz > 0:
            self.pwm.freq(int(freq_hz))
            self.pwm.duty_u16(32768)  # 50% duty cycle
            self._tocando = True

    def parar(self):
        """Para o som imediatamente."""
        self.pwm.duty_u16(0)
        self._tocando = False

    @property
    def tocando(self):
        return self._tocando
