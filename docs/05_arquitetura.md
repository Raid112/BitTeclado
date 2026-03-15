# 05 - Arquitetura

## Diagrama de Blocos

```
┌──────────────┐     ┌───────────────┐     ┌──────────────┐
│ Botoes A/B/C │────>│               │────>│  Buzzer PWM  │
│ (GP5/6/10)   │     │               │     │  (GP21)      │
└──────────────┘     │    main.py    │     └──────────────┘
                     │   (RP2040)    │
┌──────────────┐     │               │     ┌──────────────┐
│  Joystick    │────>│               │────>│ OLED 128x64  │
│  X/Y + SW    │     │               │     │ (I2C GP2/3)  │
└──────────────┘     └───────────────┘     └──────────────┘
```

## Modulos de Software

```
firmware/
├── main.py          # Loop principal e inicializacao
├── notas.py         # Tabela de frequencias, bancos, escalas
├── buzzer.py        # Controle PWM do buzzer (tocar/parar nota)
├── display.py       # Desenho do painel OLED
├── controles.py     # Leitura de botoes e joystick (debounce)
└── ssd1306.py       # Driver do display (lib externa)
```

### Dependencias entre Modulos

```
main.py
├── controles.py     # le entradas
├── notas.py         # consulta frequencia da nota
├── buzzer.py        # emite som
└── display.py       # atualiza tela
    └── ssd1306.py   # driver I2C do OLED
```

## Fluxo de Dados

```
[Joystick X] ──> banco_atual (0-3)
[Joystick Y] ──> oitava_atual (3-7)
                        │
                        v
              ┌──────────────────┐
              │    notas.py      │
              │ banco + oitava   │──> frequencia (Hz)
              │ + botao          │
              └──────────────────┘
                        │
              ┌─────────┴─────────┐
              v                   v
        ┌──────────┐       ┌──────────┐
        │ buzzer   │       │ display  │
        │ PWM freq │       │ OLED info│
        └──────────┘       └──────────┘
```

## Loop Principal (main.py)

```
while True:
    1. controles.ler_joystick() → atualizar banco e oitava
    2. controles.ler_botoes() → identificar botao pressionado
    3. Se botao ativo: buzzer.tocar(notas.frequencia(banco, oitava, botao))
    4. Se nenhum botao: buzzer.parar()
    5. Se estado mudou: display.atualizar(banco, oitava, botao_ativo)
    6. time.sleep_ms(20)
```

## Extensibilidade

Os modulos `buzzer.py` e `display.py` possuem interfaces genericas:
- `buzzer.tocar(frequencia_hz)` e `buzzer.parar()` — qualquer fonte pode fornecer a frequencia
- `display.atualizar(...)` — pode receber novos modos de visualizacao

No Projeto 2, um modulo `sensor_dist.py` fornecera frequencias ao `buzzer.py` baseado em distancia, sem alterar o modulo do buzzer.
