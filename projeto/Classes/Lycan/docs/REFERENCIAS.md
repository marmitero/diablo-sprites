# Referências utilizadas e o que foi aprendido

Base documental: commit `0d4093740aa4ec15eb2aab858c2b1b2560e414f8` do acervo auditado.

| Referência real | Aprendizado aplicado | O que não foi copiado |
|---|---|---|
| [Abominable](../../../../sprites/Inimigos/Abominable.png) | Volume de criatura peluda, material, vistas, separação entre direção e tempo | Corpo, proporções e poses específicas do monstro |
| [Barbarian Light](../../../../sprites/Classes/Barbarian%20%28Light%29.gif) | Diferença entre estados neutros e locomoção; silhueta corporal em vistas rotacionais | Corpo humano, equipamentos e grade de exportação |
| [Balrog Weaponless](../../../../sprites/Inimigos/Balrog%20%28Weaponless%29.png) | Corpo consistente e oclusão de membros numa criatura | Anatomia alada, identidade e ataques do original |
| [Rogue Parts](../../../../docs/DIABLO2.md) | Origem comum e necessidade de ordem de desenho por fase/vista | Peças da Rogue; o Lycan v1 é composto, não um rig modular |
| [Frames e layouts](../../../../docs/FRAMES.md) | Linhas podem representar vistas ou sequência quebrada; não existe quantidade universal | Direção de bússola inferida do original |
| [Arte](../../../../docs/ART.md) | Silhueta, luz, material, contato de patas e continuidade temporal | Alegação de que qualquer imagem detalhada equivale a sprite final |
| [Produção](../../../../docs/PRODUCTION.md) | Canvas, pivô, eventos e aprovação separados | Offsets e timings “nativos” inexistentes na referência |

Abominable e Barbarian foram inspecionados em recortes de resolução nativa nesta etapa. A geração foi conduzida por descrição; a própria folha de identidade do Lycan é a referência visual das gerações seguintes. Os sprites originais da Blizzard não foram enviados como alvo para editar nem recortados para montar o corpo novo.

## Decisões assumidas para a classe

Oito vistas explícitas em vez de presumir a ordem de uma folha exportada. Idle curto, caminhada bípede digitígrada, combate com garras/mordida e uivo. A sequência de vistas usa `S, SW, W, NW, N, NE, E, SE`, definida pelo sentido de orientação na tela. Esse mapeamento é nosso contrato; não é afirmado como ordem universal do Diablo II.

O fundo magenta existe para inspeção e organização. Não é parte do material do personagem nem garante transparência. As imagens geradas podem conter variação no magenta/antialias; uma conversão de alpha deve ser feita e revisada em etapa própria.
