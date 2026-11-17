# Frames, posição e reconstrução de clipes

## Três contagens diferentes

1. **Arquivo de imagem:** 153 arquivos.
2. **Quadro codificado no arquivo:** todos têm um; inclusive os 24 GIFs, medidos com Pillow.
3. **Célula/pose desenhada na folha:** muitas por arquivo; quantidade depende de ação, vista, equipamento e organização da exportação.

Não há uma contagem semântica validada de todas as 153 folhas. Nenhum documento deste repositório deve converter largura × altura em quantidade de frames sem conhecer margens, separadores, tamanhos de célula e blocos. O inventário traz `semantic_frame_count: null` onde o mapeamento integral está pendente. Isso é dado desconhecido, não zero.

## Exemplos contados na imagem original

| Folha / bloco | Organização observada | Células |
|---|---|---:|
| Bird / walk | 8 fases por linha × 8 vistas | 64 |
| Bird / idle | Uma pose por vista × 8 vistas | 8 |
| Rat / idle | 6 fases × 8 vistas | 48 |
| Rat / walk | 4 fases × 8 vistas | 32 |
| Rat / die | Uma pose por vista × 8 vistas; células menores | 8 |
| Fire Large / fire 1 | Uma faixa, 20 fases | 20 |
| Fire Large / fire 2 | Uma faixa, 20 fases | 20 |
| Fire Large / fire 3 | Uma faixa, 20 fases | 20 |
| Charsi / smith | 6 linhas completas de 20 + 9 células na sétima; uma sequência quebrada | 129 |
| Amazon Light / Town Neutral | 16 fases × 16 vistas no primeiro bloco | 256 |

Bird totaliza **72**, Rat **88** e Fire Large **60** células nos blocos listados, que cobrem suas folhas visuais. Charsi e Amazon têm outros blocos: 129 e 256 **não** são o total dessas folhas. “Uma pose die por vista” no Rat não é uma animação de morte com oito fases: oito orientações distintas não devem ser reproduzidas em sequência.

Os exemplos JSON cobrem Bird, Rat, Fire Large e smith de Charsi; Town Neutral foi contado visualmente e não faz parte do extrator. Direção absoluta, timing nativo e eventos não foram recuperados de nenhuma dessas contagens.

## Coordenadas dos exemplos

Sistema: pixels, origem no canto superior esquerdo, `x` cresce à direita, `y` para baixo. Retângulo `[x,y,w,h]` representa `[x,x+w) × [y,y+h)`; índices de linha/coluna iniciam em zero. Bordas/legendas ficam fora do recorte.

| Bloco | Primeiro x,y | Célula w,h | Passo x,y | Organização |
|---|---|---|---|---|
| Bird walk | 1,17 | 22,16 | 23,17 | 8 colunas × 8 linhas |
| Bird idle | 188,17 | 22,9 | 23,10 | 1 × 8 |
| Rat idle | 0,11 | 28,15 | 29,16 | 6 × 8 |
| Rat walk | 0,149 | 28,15 | 29,16 | 4 × 8 |
| Rat die | Ver [layouts.json](../examples/layouts.json) | Célula própria | Passo próprio | 1 pose × 8 vistas |
| Fire Large 1 | 1,17 | 46,76 | 47,77 | 20 × 1 |
| Fire Large 2 | 1,110 | 69,101 | 70,102 | 20 × 1 |
| Fire Large 3 | 1,228 | 118,187 | 119,188 | 20 × 1 |
| Charsi smith | 1,13 | 44,73 | 45,74 | Linhas quebradas de até 20; 129 células válidas |

Para uma grade, `x = x0 + coluna × passo_x`, `y = y0 + linha × passo_y`. No smith, índice temporal = `linha × 20 + coluna`; parar em 128. Em Bird walk, linha seleciona vista e coluna seleciona fase; **não** usar `linha × 8 + coluna` para um único clipe de voo.

O JSON inclui hash de origem e cada retângulo expandido. É a fonte executável dos exemplos, não uma inferência aplicada a todas as folhas. O extrator rejeita origem alterada e coordenadas fora da imagem. A cor-chave só é aplicada aos blocos selecionados; não há tratamento global de todas as imagens.

## Como anotar o restante sem perder informação

1. Abrir a folha nativa e identificar texto, créditos, fundo e cada bloco.
2. Distinguir tempo, direção, variante e peça. Registrar o rótulo original e uma descrição normalizada.
3. Contar linhas/colunas e células finais parciais; anotar exceções em vez de completar retângulos vazios.
4. Medir retângulos e separadores. Uma folha pode ter vários tamanhos de célula e múltiplos fundos.
5. Reconstruir um clipe por ação/vista. Examinar começo, fim, continuidade e poses repetidas.
6. Mapear ângulos por inspeção; registrar incerteza. Não aplicar a ordem padrão de outro arquivo.
7. Fixar origem comum. Preservar offset de cada recorte e espaço de arma/efeito.
8. Revisar alpha e contornos sobre três fundos. Registrar pixels apagados, não destruir a origem.
9. Rotular timing/eventos como desconhecidos até ter evidência específica. Preview artificial não vira dado histórico.
10. Publicar manifesto, preview, folha numerada e revisão de qualidade antes de liberar para dataset.

## Armadilhas concretas

- GIF estático: iterar `n_frames` não extrai as poses dentro da folha.
- Fundo magenta varia: aqui há `#FF0099` e `#FF00CC`; vários arquivos têm fundo RGB opaco. Remover apenas `#FF00FF` falha.
- Fundo cinza: pode conter legenda/crédito; não assumir que todas as regiões cinzas sejam células ou que todo cinza seja descartável.
- Grade: contar retângulos vazios como poses gera negativos falsos; em peças modulares, porém, vazios podem representar oclusão válida.
- Charsi smith: cada linha não equivale a uma vista.
- Amazon Town Neutral: há 16 vistas, não oito por conveniência.
- Rat die: morte estática multivista não é um ciclo de oito frames.
- Fire Large: três escalas/ciclos, não uma chama que cresce em 60 frames.
- Tiles: a sequência espacial não é timeline; cada peça requer metadados de mapa.

## Timing e eventos

Os arquivos não fornecem o timing nativo por célula, os pontos de dano/disparo ou offsets originais. A velocidade usada pelo script é **100 ms por quadro para estudo**. Pode ser modificada para inspeção; não representa a velocidade do Diablo II.

A origem lógica precisa ser definida conforme ação/entidade. O centro do retângulo não é automaticamente o pé, e o centro da caixa do personagem muda durante ataque. Hitbox, alcance, instante do disparo e colisão são trilhas separadas. Um frame visual “agressivo” não comprova o frame em que o jogo calcula dano.
