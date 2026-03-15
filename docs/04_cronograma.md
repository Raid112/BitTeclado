# 04 - Cronograma

## Visao Geral

- **Inicio**: 15/03/2026 (sabado)
- **Entrega**: 22/03/2026 (sabado)
- **Duracao**: 8 dias
- **Abordagem**: Refinamentos sucessivos — modulos desenvolvidos em paralelo por diferentes integrantes, integrados progressivamente

## Diagrama Gantt

```
                    15/03  16/03  17/03  18/03  19/03  20/03  21/03  22/03
                    SAB    DOM    SEG    TER    QUA    QUI    SEX    SAB
─────────────────────────────────────────────────────────────────────────────
Fase 1: Setup e Pesquisa
  Repo + docs        ████▌
  Pesquisa musical         ████▌
  Estudo BitDogLab         ████▌

Fase 2: Desenvolvimento dos Modulos
  notas.py                        ████▌
  buzzer.py                       ████▌
  controles.py                    ████▌
  display.py                             ████▌

Fase 3: Integracao e Testes
  main.py (integ.)                              ████▌
  Testes unitarios                              ████▌
  Testes na placa                                      ████▌
  Ajuste deadzone/UX                                   ████▌

Fase 4: Finalizacao
  Doc. final                                                  ████▌
  Apresentacao                                                ████▌
  Revisao e entrega                                                 ████▌
─────────────────────────────────────────────────────────────────────────────
```

## Divisao de Tarefas por Integrante

### Caio Cezar Pagliarani (248118) — Arquitetura e Integracao

| Tarefa | Inicio | Fim | Status |
|--------|--------|-----|--------|
| Criar repositorio GitHub e estrutura de pastas | 15/03 | 15/03 | Concluido |
| Documentacao inicial (problema, requisitos, conceito) | 15/03 | 16/03 | Concluido |
| Modulo `notas.py` — tabela de frequencias e bancos | 17/03 | 17/03 | Pendente |
| Integracao `main.py` — loop principal | 19/03 | 19/03 | Pendente |
| Testes integrados na placa (sistema completo) | 20/03 | 20/03 | Pendente |
| Revisao final do codigo e documentacao | 21/03 | 22/03 | Pendente |

### Vitor Goncalves Costa (240043) — Hardware e Controles

| Tarefa | Inicio | Fim | Status |
|--------|--------|-----|--------|
| Estudo do pinout da BitDogLab V7 e perifericos | 15/03 | 16/03 | Pendente |
| Modulo `buzzer.py` — controle PWM do buzzer | 17/03 | 17/03 | Pendente |
| Modulo `controles.py` — leitura de botoes e joystick | 17/03 | 18/03 | Pendente |
| Testes unitarios: buzzer, botoes, joystick | 19/03 | 19/03 | Pendente |
| Calibracao de deadzone do joystick na placa | 20/03 | 20/03 | Pendente |
| Documentacao de hardware (`pinout.md`) e testes | 21/03 | 21/03 | Pendente |

### Lucas Bernardino de Oliveira (182199) — Display e Documentacao

| Tarefa | Inicio | Fim | Status |
|--------|--------|-----|--------|
| Pesquisa sobre escalas musicais e frequencias | 15/03 | 16/03 | Pendente |
| Modulo `display.py` — painel OLED (layout e renderizacao) | 17/03 | 18/03 | Pendente |
| Teste unitario do display OLED | 19/03 | 19/03 | Pendente |
| Refinamento visual do display (fontes, posicionamento) | 20/03 | 20/03 | Pendente |
| Documentacao de especificacoes e arquitetura | 21/03 | 21/03 | Pendente |
| Preparacao dos slides da apresentacao | 21/03 | 22/03 | Pendente |

## Marcos (Milestones)

| Data | Marco | Criterio de Aceitacao |
|------|-------|----------------------|
| 16/03 | **M1 — Repo e documentacao prontos** | Repo no GitHub com docs iniciais preenchidos |
| 18/03 | **M2 — Modulos individuais prontos** | notas.py, buzzer.py, controles.py, display.py codificados |
| 19/03 | **M3 — Integracao completa** | main.py funcional, todos os modulos conectados |
| 20/03 | **M4 — Validacao na placa** | Sistema testado na BitDogLab, deadzone calibrada |
| 22/03 | **M5 — Entrega final** | Documentacao completa, apresentacao pronta, codigo revisado |

## Reunioes

| Data | Tipo | Pauta |
|------|------|-------|
| 15/03 (SAB) | Kickoff | Divisao de tarefas, alinhamento de escopo, setup do repo |
| 17/03 (SEG) | Sync | Status dos modulos individuais, duvidas de implementacao |
| 19/03 (QUA) | Integracao | Juntar modulos, resolver conflitos, primeiros testes |
| 21/03 (SEX) | Pre-entrega | Revisao da documentacao, dry-run da apresentacao |

- **Formato**: Chamada de 15-20min ou presencial no lab
- **Registro**: Decisoes documentadas via commits no repositorio

## Gestao de Riscos

| Risco | Probabilidade | Impacto | Mitigacao |
|-------|--------------|---------|-----------|
| Driver ssd1306.py incompativel com a placa | Baixa | Alto | Testar no dia 17/03, ter driver alternativo (sh1107) |
| Deadzone do joystick imprecisa | Media | Medio | Calibrar empiricamente na placa no dia 20/03 |
| Buzzer com som muito baixo/distorcido | Baixa | Medio | Testar diferentes duty cycles e frequencias |
| Conflitos de merge entre integrantes | Media | Baixo | Cada integrante trabalha em modulo separado |
| Falta de tempo para apresentacao | Baixa | Alto | Lucas comeca slides no dia 21/03, template pronto antes |
