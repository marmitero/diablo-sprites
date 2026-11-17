# Contrato de animação v1

## Espaço e vistas

Câmera alvo: projeção ortográfica elevada oblíqua, cerca de 30° olhando para baixo; escala e luz consistentes. A geração raster pode divergir desse alvo: a revisão deve registrar a diferença, sem chamar o desenho de câmera calibrada. Luz principal no alto à esquerda da tela.

| Índice | Vista | Leitura na tela |
|---:|---|---|
| 0 | S | Frente, focinho voltado ao observador |
| 1 | SW | Frente/esquerda |
| 2 | W | Perfil olhando para a esquerda |
| 3 | NW | Costas/esquerda |
| 4 | N | Costas |
| 5 | NE | Costas/direita |
| 6 | E | Perfil olhando para a direita |
| 7 | SE | Frente/direita |

Na folha de identidade, quatro colunas × duas linhas contêm as oito vistas, sem dimensão temporal. Nas folhas multivista, cada linha é uma vista e as colunas são fases da mesma ação. Na folha de ações piloto, cada linha é uma ação na vista E; não se deve interpretar linha como direção.

## Matriz planejada para esta primeira versão

| Ação | Vistas alvo v1 | Fases solicitadas | Loop | Cobertura posterior |
|---|---|---:|---|---|
| Neutral / turnaround | 8 | 1 | Não | Refinar câmera/escala conforme aprovação |
| Idle | 8 | 4 por vista | Sim | Expandir fases se necessário, sem interpolação automática |
| Walk | 8 | 8 por vista | Sim | Refinar apoios e eventualmente ampliar a 16 quadros |
| Run | E | 8 | Sim | Expandir para as outras 7 vistas |
| Claw | E | 8 | Não | Expandir direções e segundo ataque |
| Bite | E | 8 | Não | Expandir direções |
| Howl | E | 8 | Não | Expandir direções e efeito separado |
| Hit | E | 8 | Não | Refinar duração e expandir direções |
| Death | E | 8 | Não; segurar último | Expandir direções e conferir corpo final |

As quantidades da tabela são o contrato de geração, não uma medição antecipada de resultado. O inventário registra a contagem observada e o estado da revisão. V1 é um conjunto piloto utilizável para revisão, não a classe inteira com todas as ações em oito vistas e aprovação final.

## Biomecânica

Idle: patas plantadas, respiração no tórax, movimento discreto de mãos/orelhas/juba; não deslocar o corpo inteiro para simular respiração.

Walk: duas passadas alternadas, uma de cada perna, em oito fases: contato A, carga A, passagem B, saída A, contato B, carga B, passagem A, saída B. Braços contrabalançam as pernas; cabeça e cauda estabilizam. Pata de apoio deve manter contato até o push-off. É caminhada bípede, não quadrúpede, moonwalk ou corrida com as duas patas sempre suspensas.

Run: maior inclinação e amplitude, com fase aérea curta; não acelerar o GIF de walk como substituição da ação.

Claw: 0–1 preparação, 2–3 execução, 4 passagem/extensão, 5–7 recuperação. Bite: 0–2 carga, 3–4 avanço e fechamento, 5–7 retorno. Howl: 0–2 inspirar, 3–5 uivar, 6–7 baixar a cabeça. Hit: receber, absorver e recuperar. Death: colapso irreversível e corpo final, sem levantar no último quadro.

Essas fases são alvos de direção de animação e devem ser confrontadas com a imagem gerada. Não são eventos de dano já validados. `events` permanece vazio até escolher precisamente o instante com revisão e integração.

## Exportação e execução

Guardar a folha fonte, cada retângulo XYWH e um índice ordenado por clipe. A divisão da folha em células preserva pixels e fundo; não recorta/centraliza cada silhueta independentemente. O pivô lógico comum fica no chão do canvas; offsets medidos ou ajustes precisam estar no manifesto, sem fingir que a IA posicionou todos os apoios perfeitamente.

Os previews usam tempos de inspeção definidos pelo projeto. Não são tempos do Diablo II nem prova de fluidez final. Clipes one-shot não devem repetir no jogo; a ferramenta pode gerar preview de revisão com pausa final. Hitbox e alcance são externos à caixa do sprite.
