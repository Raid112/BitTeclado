# 03 - Conceito Preliminar

## Abordagem Escolhida: Refinamentos Sucessivos

Optamos pela abordagem de **refinamentos sucessivos** (prototipo simples que ganha features incrementalmente) porque:

1. Os requisitos sao exploratórios — ajustes na interacao (deadzone, mapeamento) serao refinados com testes praticos
2. O projeto faz parte de uma progressao de 3 projetos, entao o codigo do Projeto 1 sera estendido naturalmente
3. Permite ter algo funcional rapidamente e iterar sobre a experiencia de uso

## Conceito da Solucao

### Sistema de Bancos de Notas

A escala cromatica (12 notas) e dividida em 4 bancos de 3 notas:

| Banco | Botao A | Botao B | Botao C |
|-------|---------|---------|---------|
| 0 | Do | Do# | Re |
| 1 | Re# | Mi | Fa |
| 2 | Fa# | Sol | Sol# |
| 3 | La | La# | Si |

O joystick eixo X navega entre bancos. O eixo Y seleciona oitavas (3 a 7).

### Interacao

1. Ao ligar, o sistema inicia no Banco 0, Oitava 4 (Do central)
2. O usuario move o joystick horizontalmente para escolher o banco
3. O display atualiza mostrando as 3 notas disponiveis
4. O usuario pressiona A, B ou C para tocar a nota
5. O buzzer emite a frequencia correspondente via PWM
6. Ao soltar, o som para imediatamente

### Layout do Display OLED

```
┌──────────────────────┐
│  Oitava: 4           │
│                      │
│  [Do]  Do#   Re      │
│   A     B     C      │
│                      │
│  Banco: 1/4          │
└──────────────────────┘
```

A nota ativa e destacada com colchetes. Notas inativas aparecem sem destaque.

## Alternativas Consideradas

| Alternativa | Motivo da Rejeicao |
|-------------|-------------------|
| Cada botao toca nota fixa + joystick so muda oitava | Limitado a 3 notas por oitava, sem acesso a escala completa |
| Modo escala (joystick navega nota a nota) | Menos intuitivo, mais lento para tocar melodias |
| Usar matriz NeoPixel como feedback | Display OLED e mais informativo; NeoPixel reservada para projetos futuros |
