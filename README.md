# BitTeclado - Teclado Musical Interativo

**Disciplina**: FEE-246 — Laboratorio de Sistemas Embarcados
**Instituicao**: FEEC / UNICAMP
**Plataforma**: BitDogLab V7 (RP2040)

## Integrantes

| Nome | RA |
|------|-----|
| Caio Cezar Pagliarani | 248118 |
| Vitor Goncalves Costa | 240043 |
| Lucas Bernardino de Oliveira | 182199 |

## Descricao

Teclado musical interativo utilizando os recursos on-board da BitDogLab V7. Tres botoes (A, B, C) tocam notas musicais no buzzer, o joystick seleciona bancos de notas (eixo X) e muda a oitava (eixo Y), enquanto o display OLED exibe em tempo real as notas mapeadas, oitava atual e nota ativa.

O projeto foi concebido com arquitetura modular para ser estendido nos projetos seguintes:
- **Projeto 2**: Integracao com sensor ultrasonico (theremin / sons por distancia)
- **Projeto 3**: Adaptacao para bengala assistiva para deficientes visuais

## Objetivos

1. Criar um instrumento musical funcional com interface intuitiva
2. Permitir acesso a todas as notas da escala cromatica via sistema de bancos
3. Exibir feedback visual em tempo real no display OLED
4. Manter codigo modular e extensivel para projetos futuros

## Componentes Utilizados

| Componente | GPIO | Funcao |
|-----------|------|--------|
| Botao A | GP5 | Toca nota 1 do banco |
| Botao B | GP6 | Toca nota 2 do banco |
| Botao C | GP10 | Toca nota 3 do banco |
| Joystick eixo X | GP27 (ADC1) | Seleciona banco de notas |
| Joystick eixo Y | GP26 (ADC0) | Muda oitava |
| Joystick SW | GP22 | Reservado (extensibilidade) |
| Buzzer | GP21 (PWM) | Emite som da nota |
| Display OLED SSD1306 | GP2/GP3 (I2C1) | Painel de informacoes |

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

## Resultados Esperados

1. Apertar botao A/B/C toca a nota correspondente ao banco ativo imediatamente
2. Mover joystick X muda o banco de notas, display atualiza as 3 notas
3. Mover joystick Y sobe/desce a oitava, display atualiza
4. Display mostra em tempo real: oitava, 3 notas do banco, nota ativa destacada
5. Latencia perceptivel < 50ms
6. Codigo modular pronto para receber sensor ultrasonico no Projeto 2

## Documentacao

| Documento | Descricao |
|-----------|-----------|
| [01 - Problema](docs/01_problema.md) | Definicao do problema e contexto |
| [02 - Requisitos](docs/02_requisitos.md) | Requisitos funcionais e nao-funcionais |
| [03 - Conceito](docs/03_conceito.md) | Conceito preliminar e abordagem |
| [04 - Cronograma](docs/04_cronograma.md) | Cronograma com responsaveis |
| [05 - Arquitetura](docs/05_arquitetura.md) | Diagrama de blocos e modulos |
| [06 - Especificacoes](docs/06_especificacoes.md) | BOM e especificacoes tecnicas |
| [07 - Prototipagem](docs/07_prototipagem.md) | Registro de testes e prototipagem |
| [08 - Validacao](docs/08_validacao.md) | Validacao contra requisitos |
| [09 - Conclusao](docs/09_conclusao.md) | Conclusoes e licoes aprendidas |

## Estrutura do Repositorio

```
1-Projeto-BitTeclado/
├── README.md              # Este arquivo
├── docs/                  # Documentacao do projeto (8 etapas)
├── firmware/              # Codigo MicroPython
│   ├── main.py            # Loop principal
│   ├── notas.py           # Tabela de frequencias e bancos
│   ├── buzzer.py          # Controle PWM do buzzer
│   ├── display.py         # Desenho do painel OLED
│   ├── controles.py       # Leitura de botoes e joystick
│   └── ssd1306.py         # Driver OLED (lib externa)
├── hardware/              # Documentacao de hardware e pinout
├── testes/                # Scripts e logs de teste
├── imagens/               # Fotos, diagramas, prints
└── apresentacao/          # Slides da apresentacao
```
