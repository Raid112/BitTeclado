# 07 - Prototipagem e Testes

## Estrategia de Testes

Seguindo a abordagem de refinamentos sucessivos, os testes serao feitos por modulo antes da integracao.

### Fase 1 — Testes Unitarios por Componente

| # | Teste | Modulo | Criterio de Sucesso |
|---|-------|--------|-------------------|
| T1 | Buzzer toca frequencia fixa (440 Hz = La4) | buzzer.py | Som audivel e estavel |
| T2 | Buzzer para ao chamar parar() | buzzer.py | Silencio imediato |
| T3 | Leitura de botoes retorna estado correto | controles.py | Detecta press/release dos 3 botoes |
| T4 | Leitura do joystick retorna valores na faixa | controles.py | ADC 0-65535, centro ~32768 |
| T5 | Deadzone do joystick funciona | controles.py | Sem mudanca com joystick em repouso |
| T6 | Display inicializa e mostra texto | display.py | Texto visivel no OLED |
| T7 | Tabela de frequencias retorna valores corretos | notas.py | La4 = 440.0 Hz |

### Fase 2 — Testes Integrados

| # | Teste | Criterio de Sucesso |
|---|-------|-------------------|
| T8 | Botao A toca nota correta do banco 0 | Do4 = 261.63 Hz |
| T9 | Mudar banco via joystick X altera notas dos botoes | Display e som mudam corretamente |
| T10 | Mudar oitava via joystick Y altera pitch | Mesma nota, frequencia dobra/metade |
| T11 | Display atualiza ao mudar banco/oitava | Informacao correta sem flicker |
| T12 | Loop completo funciona por 5 minutos sem travamento | Sistema estavel |

## Registro de Testes

_A preencher durante a execucao dos testes. Formato sugerido:_

### Teste T1 — Buzzer frequencia fixa
- **Data**: _A preencher_
- **Resultado**: _Passou / Falhou_
- **Observacoes**: _Detalhes_

_(Repetir para cada teste)_
