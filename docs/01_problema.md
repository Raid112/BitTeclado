# 01 - Definicao do Problema

## Contexto

Instrumentos musicais tradicionais sao caros, volumosos e exigem anos de pratica para dominar. Em ambientes educacionais de sistemas embarcados, existe a oportunidade de criar instrumentos digitais simples que permitem exploracao musical imediata usando componentes eletronicos basicos.

## Problema

Como criar um instrumento musical interativo e acessivel utilizando apenas os recursos on-board de uma placa de prototipagem (BitDogLab V7), que seja funcional, intuitivo e extensivel para aplicacoes futuras?

## Escopo

- **Inclui**: Teclado musical com 3 botoes, navegacao por joystick, feedback visual em display OLED, emissao de som por buzzer
- **Nao inclui**: Gravacao de melodias, polifonia (multiplas notas simultaneas), conexao com dispositivos externos, uso de microfone ou matriz NeoPixel

## Recorte

O projeto foca na interacao humano-maquina (IHM) musical:
- Entrada: botoes discretos + joystick analogico
- Processamento: mapeamento de entradas para frequencias musicais
- Saida: som (buzzer PWM) + visual (display OLED)

## Visao de Longo Prazo

Este projeto e a base de uma progressao de 3 projetos:

1. **Projeto 1 (atual)**: Teclado musical on-board
2. **Projeto 2**: Integracao de sensor ultrasonico para gerar sons baseados em distancia (theremin digital)
3. **Projeto 3**: Adaptacao para bengala assistiva para deficientes visuais (feedback sonoro de proximidade)

A arquitetura modular do Projeto 1 permite a reutilizacao direta dos modulos de buzzer, display e controles nos projetos seguintes.
