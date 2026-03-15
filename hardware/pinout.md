# Pinout — BitTeclado (BitDogLab V7)

## Perifericos Utilizados

| Componente | GPIO | Tipo | Configuracao |
|-----------|------|------|-------------|
| Botao A | GP5 | Digital IN | Pull-up interno, ativo LOW |
| Botao B | GP6 | Digital IN | Pull-up interno, ativo LOW |
| Botao C | GP10 | Digital IN | Pull-up interno, ativo LOW |
| Joystick VRx | GP27 | ADC1 | 16-bit (0-65535) |
| Joystick VRy | GP26 | ADC0 | 16-bit (0-65535) |
| Joystick SW | GP22 | Digital IN | Pull-up interno, ativo LOW |
| Buzzer A | GP21 | PWM | Via transistor, passivo |
| OLED SDA | GP2 | I2C1 | SSD1306, addr 0x3C |
| OLED SCL | GP3 | I2C1 | SSD1306, addr 0x3C |

## Perifericos Nao Utilizados (disponiveis para projetos futuros)

| Componente | GPIO |
|-----------|------|
| LED Vermelho | GP13 |
| LED Verde | GP11 |
| LED Azul | GP12 |
| NeoPixel 5x5 | GP7 |
| Microfone | GP28 |
