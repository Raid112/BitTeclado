# 06 - Especificacoes Tecnicas

## Plataforma

| Item | Especificacao |
|------|--------------|
| Placa | BitDogLab V7 |
| Microcontrolador | RP2040 (Dual Cortex-M0+ @ 133 MHz) |
| RAM | 264 KB SRAM |
| Flash | 2 MB |
| Linguagem | MicroPython |
| IDE | Thonny |
| Alimentacao | USB (5V) |

**Justificativa**: A BitDogLab V7 e a plataforma da disciplina. Todos os componentes necessarios (botoes, joystick, buzzer, OLED) sao on-board, eliminando necessidade de prototipagem em breadboard.

## BOM (Bill of Materials)

| # | Componente | Qtd | Modelo/Spec | Custo |
|---|-----------|-----|-------------|-------|
| 1 | BitDogLab V7 | 1 | RP2040, on-board | Fornecida pela disciplina |
| 2 | Cabo USB | 1 | Micro-USB | Fornecido |

**Nota**: Todos os componentes utilizados (botoes, joystick, buzzer, OLED) sao on-board da BitDogLab V7. Nao ha componentes externos neste projeto.

## Especificacoes dos Perifericos

### Buzzer (GP21)

- Tipo: Passivo, acionado via transistor
- Controle: PWM com `duty_u16(32768)` (50% duty cycle)
- Faixa de frequencias: 130.8 Hz (Do3) a 3951 Hz (Si7)
- Desligamento: `duty_u16(0)`

### Display OLED (I2C1 — GP2/GP3)

- Modelo: SSD1306
- Resolucao: 128x64 pixels
- Endereco I2C: 0x3C
- Driver: ssd1306.py (MicroPython)

### Botoes (GP5, GP6, GP10)

- Tipo: Push-button, ativo LOW
- Configuracao: Pull-up interno habilitado
- Debounce: ~50ms por software (polling a cada 20ms)

### Joystick KY023

- Eixo X: GP27 (ADC1) — selecao de banco
- Eixo Y: GP26 (ADC0) — selecao de oitava
- Botao SW: GP22 — reservado
- Resolucao ADC: 16-bit (0-65535)
- Centro: ~32768
- Deadzone: 25% (valores entre ~24576 e ~40960 ignorados)

## Tabela de Frequencias (Hz)

| Nota | Oitava 3 | Oitava 4 | Oitava 5 | Oitava 6 | Oitava 7 |
|------|----------|----------|----------|----------|----------|
| Do   | 130.81 | 261.63 | 523.25 | 1046.50 | 2093.00 |
| Do#  | 138.59 | 277.18 | 554.37 | 1108.73 | 2217.46 |
| Re   | 146.83 | 293.66 | 587.33 | 1174.66 | 2349.32 |
| Re#  | 155.56 | 311.13 | 622.25 | 1244.51 | 2489.02 |
| Mi   | 164.81 | 329.63 | 659.26 | 1318.51 | 2637.02 |
| Fa   | 174.61 | 349.23 | 698.46 | 1396.91 | 2793.83 |
| Fa#  | 185.00 | 369.99 | 739.99 | 1479.98 | 2959.96 |
| Sol  | 196.00 | 392.00 | 783.99 | 1567.98 | 3135.96 |
| Sol# | 207.65 | 415.30 | 830.61 | 1661.22 | 3322.44 |
| La   | 220.00 | 440.00 | 880.00 | 1760.00 | 3520.00 |
| La#  | 233.08 | 466.16 | 932.33 | 1864.66 | 3729.31 |
| Si   | 246.94 | 493.88 | 987.77 | 1975.53 | 3951.07 |
