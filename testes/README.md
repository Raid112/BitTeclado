# Testes

Scripts de teste para validacao individual de cada modulo.

## Estrutura

```
testes/
├── teste_buzzer.py      # Toca La4 (440Hz) por 1 segundo
├── teste_botoes.py      # Imprime estado dos botoes no terminal
├── teste_joystick.py    # Imprime valores ADC do joystick
├── teste_display.py     # Mostra texto de teste no OLED
└── teste_notas.py       # Valida tabela de frequencias
```

## Como Executar

1. Conectar BitDogLab via USB
2. Abrir Thonny, selecionar interpreter "MicroPython (Raspberry Pi Pico)"
3. Abrir o script de teste desejado
4. Clicar em "Run" (F5)
5. Observar resultado no terminal e/ou hardware
