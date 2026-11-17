# Como os recursos participam do Diablo II

## Escopo da interpretação

Distinguimos três níveis: **observado na folha**, **função do personagem/objeto no jogo documentada por fonte** e **contrato recomendado para produção futura**. O nome amigável de uma exportação não é um ID nativo. Sem token/caminho DCC, tabelas e versão do jogo, não se pode prometer equivalência exata de cada variante. Casos ambíguos estão marcados no inventário, em vez de receber uma identidade inventada.

## A imagem não contém o comportamento

| Grupo do acervo | Papel em execução | Dados externos necessários |
|---|---|---|
| Classes | Aparência da unidade controlada pelo jogador; estado de cidade/combate, armas e animação | Estado, equipamento, direção, velocidade, habilidade e eventos |
| Inimigos | Apresentação dos estados da unidade hostil | IA, alcance, pathfinding, colisão, hit recovery, dano e morte |
| NPCs nomeados | Presença no mundo, gestos, conversa e atividade | Menus, missões, recompensas e serviços |
| Figurantes/fauna | Ambientação e movimento autônomo | Regra de deslocamento, presença e reação |
| Rogue Mercenary | Unidade aliada contratada, arqueira | Alvo, trajetória do projétil, dano, equipamento e contratação |
| Valkyrie | Unidade invocada pela Amazon | Duração/estado da invocação, alvo e atributos |
| Objetos | Estados como íntegro, ativando, ativo e destruído | Interação, destino de portal, loot, flags de missão |
| Efeitos | Apresentação transitória ou contínua | Instante de criação, posição, duração, mistura de cor e vínculo |
| Tiles | Desenho do ambiente, pisos, paredes e adereços | Layout, conectividade, bloqueio e ordem espacial |

Exemplo: Charsi trabalha em uma bigorna na apresentação de ferreira, mas a função imbuir exige estado de missão e transformação de item. Copiar o gesto não recria o serviço. Blood Hawk Nest requer um evento de geração da ave; um ciclo do ninho sem esse evento continua apenas visual. Um portal precisa de origem/destino e restrições de uso; seu arco luminoso não teletransporta sozinho.

## Anatomia dos recursos nativos

Resumo técnico baseado no tutorial de Paul Siramy e na implementação OpenDiablo2; referências em [SOURCES.md](SOURCES.md). Não são arquivos encontrados neste pacote.

| Recurso | Responsabilidade |
|---|---|
| DCC | Imagens comprimidas, direções, frames e offsets de componentes animados |
| COF | Composição: componentes participantes e prioridade de desenho por direção/frame |
| DC6 | Imagens usadas em vários recursos, incluindo interface; existem exceções animadas ao fluxo DCC |
| Paletas/colormaps | Interpretação e variação de cores; cor exportada pode estar já resolvida |
| AnimData.d2 / tabelas | Metadados de animação; velocidade e eventos dependem do tipo e do estado |
| DT1 / DS1 | Tiles e estrutura de mapas; exportar imagens perde semântica espacial |

As folhas aqui são representações exportadas: não permitem recuperar automaticamente os identificadores, offsets, blend modes e eventos originais.

## Modos e direções

Rótulos como neutral, walk, run, attack, cast, hit e death descrevem estados visuais diferentes. Town Neutral/Town Walk distinguem a apresentação de cidade. Nas folhas de classe há blocos de ação, mas não se deve assumir cobertura uniforme de todos os modos ou todas as armas.

Uma linha costuma reunir o tempo e outra linha muda a orientação **dentro de um bloco específico**. Há exceções: sequências longas quebram em várias linhas, efeitos ficam em faixas próprias e mosaicos de cenário nem sequer representam tempo. O caso `Charsi/smith` demonstra essa diferença em [FRAMES.md](FRAMES.md).

Oito e dezesseis vistas são observáveis em exemplos diferentes. O índice de direção exportado não é automaticamente uma rosa dos ventos S, SW, W... e a ordem não deve ser transplantada de um decodificador para uma folha montada por terceiros. Comece com `view_00`, `view_01` etc.; só converta para ângulo após revisão visual. Não deduza orientação pelo lado em que uma arma aparece: oclusão pode escondê-la.

## Modularidade e equipamento

Os 14 arquivos de Rogue Parts ilustram a decomposição: quatro corpos (dois marcados Unused), duas cabeças, duas mãos, quatro ombreiras e dois arcos. Não são 14 personagens. É necessário alinhar a mesma ação, vista e fase temporal de cada componente. Coordenadas locais da folha e origem no mundo são conceitos separados.

Uma composição robusta precisa de uma tabela de ordem por vista/frame. “Mão esquerda sempre atrás do corpo” falha quando a personagem gira ou quando o arco cruza o tronco. Uma peça pode estar totalmente ocluída em determinada vista sem estar faltando. As folhas não trazem os COFs correspondentes: não existe neste pacote uma ordem nativa verificada para cada frame.

Balrog aparece em cinco variantes de arma; Paladin Heavy aparece com dois escudos. Esses pares são referências de variação controlada, mas não garantem alinhamento de células entre arquivos. Medir e comparar antes de misturar partes. Também não separar automaticamente a arma de uma imagem já composta: regiões atrás do corpo podem não existir na imagem.

## Estados e efeitos

- Fogo: observar mudança de contorno, núcleo quente, língua de chama e perda de material na ponta. Um ciclo visual não implica dano.
- Lareira: separar corpo do braseiro, transição de ligar e chama contínua; o corpo não deve oscilar quando só o fogo se move.
- Teleportador: animação de abertura/atividade e a regra de transporte são trilhas distintas.
- Barril: íntegro → quebra → estado final; fragmentos e recompensa não devem ocorrer novamente a cada repetição.
- Espírito: surgimento/deslocamento/dissipação são eventos transitórios; não forçar um loop circular.
- Chefe: pose de ataque, disparo, trajetória, impacto e reação do alvo precisam de sincronização, ainda que exportados em recursos diferentes.

Não há no acervo especificação de física, IA, hitboxes ou shaders originais. Blur/bloom/partículas podem ser estudados ou criados no projeto futuro; não são uma explicação comprovada para todos os pixels das folhas.

## Cenários

`Tiles/Act 1` contém conjuntos de barracks, catacombs, cathedral, caves, court, crypt, graveyard, monastery, outdoor, town e Tristram. Piso não é animação: variantes permitem composição espacial. Paredes precisam de pé/base, altura visual e regra de oclusão. A colisão geralmente corresponde à ocupação no mundo, não ao retângulo inteiro que inclui altura da parede.

No projeto futuro, construir uma sala de teste com piso, quinas, portas, paredes e personagem andando à frente/atrás é mais útil do que avaliar tiles isolados. Os PNGs não guardam os dados de bloqueio, subtile ou conexão do original. Não atribuir walkability a uma peça apenas por ser escura ou clara.
