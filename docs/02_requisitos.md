# 02 - Requisitos

## Requisitos Funcionais

| ID | Requisito | Criterio de Aceitacao |
|----|-----------|----------------------|
| RF01 | O sistema deve emitir som ao pressionar os botoes A, B ou C | Buzzer toca nota correspondente ao banco ativo enquanto botao estiver pressionado |
| RF02 | O joystick eixo X deve selecionar o banco de notas ativo | Mover joystick para esquerda/direita altera banco entre 0-3 |
| RF03 | O joystick eixo Y deve alterar a oitava | Mover joystick para cima/baixo altera oitava entre 3-7 |
| RF04 | O display OLED deve mostrar a oitava atual | Numero da oitava visivel no topo do display |
| RF05 | O display OLED deve mostrar as 3 notas do banco ativo | Nomes das notas visiveis no centro do display com labels A/B/C |
| RF06 | O display OLED deve destacar a nota sendo tocada | Nota ativa aparece com destaque visual (inversa ou entre colchetes) |
| RF07 | O display OLED deve mostrar o numero do banco ativo | Indicador "Banco: X/4" visivel no rodape |
| RF08 | O sistema deve cobrir todas as notas da escala cromatica | 12 notas distribuidas em 4 bancos de 3 notas |

## Requisitos Nao-Funcionais

| ID | Requisito | Criterio de Aceitacao |
|----|-----------|----------------------|
| RNF01 | Latencia entre pressionar botao e emitir som < 50ms | Resposta percebida como imediata pelo usuario |
| RNF02 | Joystick deve ter deadzone para evitar mudancas acidentais | Sem mudanca de banco/oitava com joystick em repouso |
| RNF03 | Display deve atualizar sem flicker perceptivel | Atualizacao somente quando ha mudanca de estado |
| RNF04 | Codigo deve ser modular e extensivel | Modulos separados por funcionalidade (buzzer, display, controles, notas) |
| RNF05 | Consumo energetico compativel com alimentacao USB | Funcionar alimentado pela porta USB da BitDogLab |
| RNF06 | O buzzer deve ser desligado ao soltar o botao | duty_u16(0) quando nenhum botao pressionado |

## Restricoes

- Utilizar apenas componentes on-board da BitDogLab V7
- Linguagem: MicroPython
- IDE: Thonny
- Sem bibliotecas externas alem do driver ssd1306.py
