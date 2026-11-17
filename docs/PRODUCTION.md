# Como construir um pacote original a partir deste estudo

## Contrato antes da geração

Escolha plataforma visual (isométrica ou lateral), resolução nativa, projeção, escala, direções, ações, política de equipamento, timing, pivô, alpha, câmera e luz. Registre tudo em uma ficha imutável de personagem. O acervo é a referência de complexidade e movimento; o desenho novo precisa de identidade própria.

| Decisão | Exemplo de contrato novo, não dado do Diablo II |
|---|---|
| Identidade | Uma aventureira original, roupa e arma aprovadas em vistas estáticas |
| Direções | Oito vistas nomeadas e mapeadas explicitamente para ângulos |
| Locomoção piloto | Walk de 16 quadros por vista, 8 por passo, somente se adequado ao projeto |
| Canvas | Tamanho comum suficiente para ação/arma mais ampla, definido após medir o piloto |
| Pivô | Origem no plano do chão; offset próprio de cada recorte, preservado ao empacotar |
| Eventos | Frame de disparo/impacto e regra de repetição explícitos |
| Exportação | PNG RGBA, atlas + JSON, preview e registro de aprovação |

O exemplo de 16 quadros é uma opção de desenvolvimento, não uma contagem universal do acervo. Attack, hurt, death e VFX podem exigir durações e números diferentes.

## Rota de produção com controle geométrico

1. Concept e turnaround: silhueta, frente/costas/perfis, equipamento e cores aprovados.
2. Modelo e rig próprios, ou outro método que preserve geometria entre poses; não existe rig original neste repositório.
3. Animação em cena comum: marcadores de apoio dos pés e pontos de empunhadura; separar root motion e pose.
4. Câmera/luz fixas e giros de direção controlados; renderizar as mesmas fases para todas as vistas.
5. Redução à resolução alvo, tratamento de paleta/contraste e limpeza; comparar em tamanho nativo.
6. Renderizar componentes no mesmo sistema de origem; registrar ordem e oclusão por vista/frame.
7. Produzir efeitos em trilhas independentes; registrar spawn, âncora, blend e tempo.
8. Empacotar atlas, JSON de animações, offsets, eventos e previews; validar na engine.

Uma rota por geração 2D/IA pode substituir etapas, mas precisa satisfazer os mesmos contratos. Uma imagem de referência não resolve automaticamente anatomia de costas, articulação ou geometria escondida. Fixar seed não garante identidade temporal: usar referências estruturais e avaliação de clipe inteiro.

## Pacote mínimo útil

Para uma unidade móvel: vistas estáticas, idle, walk, ataque principal, hit/hurt, death e estado final quando aplicável. Acrescentar run, block, cast e skills conforme a função. Para NPC fixo: idle, talk e ofício, com transições. Para objeto: idle, ativação, ativo e desligamento/destruição quando existentes. Para efeito: aparecimento, corpo e dissipação. Para tiles: cantos, segmentos, encontros, variações e mapa de demonstração.

Uma entrega deve conter imagens, manifests e documentação; `nome_01.png` sem direção, fase e origem não é um pacote completo.

```text
assets/<family>/<entity>/<variant>/
  source/             # fontes próprias, quando disponíveis
  frames/<action>/<view>/
  atlas.png
  atlas.json
  animations.json
  previews/
  provenance.json
  README.md
```

Essa árvore é proposta para o projeto novo. Não renomear os originais para encaixá-los nela; preservar rastreabilidade por hash e caminho.

## Contrato de frame

Cada frame precisa de `source_path`, hash, entidade/família/variante, ação, vista, índice temporal, retângulo de recorte, tamanho original, posição da origem, duração e eventos. `rect` é geometria da folha; `pivot` é a origem de desenho; `hitbox` é mecânica de jogo. Não derivar um do outro sem revisão.

Quando aparar pixels vazios, armazene o deslocamento do recorte dentro do canvas lógico. A posição desenhada deve ser `posição_no_mundo - pivô + offset_do_recorte`; uma peça pequena não deve ser recentralizada independentemente do corpo. O atlas pode rotacionar retângulos apenas se a engine e o manifesto suportarem isso; para o piloto, proibir rotação simplifica a revisão.

Para modularidade, manter o índice temporal e a vista comuns. Definir um `draw_order` por frame ou intervalo; oclusão não se resolve com uma ordem fixa universal. Imagens vazias intencionais são válidas para peças ocluídas e não devem ser eliminadas automaticamente.

## Integração em engines

| Destino | Preparação e integração |
|---|---|
| Godot | AtlasTexture/SpriteFrames ou animações com regiões; offsets preservados; AnimationPlayer/trilha lógica para eventos; ordenar pelo chão |
| Unity | Sprite Editor/retângulos e pivôs; AnimationClips; eventos ou tabela de gameplay; material próprio para VFX |
| Canvas/WebGL | Carregar atlas+JSON; usar sourceRect/destRect e duração; ordenar unidades pelo pé; efeitos em passagens adequadas |
| Mod clássico de Diablo II | Exige conversão e metadados nativos compatíveis com versão/mod; PNG/GIF deste pacote não são substituições diretas de DCC/COF/DT1 |

Essas são orientações conceituais, sem código de integração dependente de versão. A engine deve conseguir escolher estado/vista sem modificar a origem do personagem. Eventos de dano não devem depender da taxa de atualização do render.

## Aprovação e regressão

Entregar por marcos: identidade → piloto de movimento → oito vistas → segunda ação → equipamento → efeitos → integração → pacote completo. Em cada marco: folha numerada, preview em tamanho nativo, contato de chão, comparação com referência própria aprovada e lista de defeitos. Registrar positivo/negativo de cada iteração para evitar repetir erros.

Reprovar: membro que encolhe, arma que troca de mão, pivô que salta, frames duplicados para esconder falhas, contorno contaminado, impacto fora do evento ou mudança de câmera. Um bom loop em uma vista não aprova automaticamente as outras.
