# Inventário integral do acervo

Snapshot: `da3fd762ee2f5463e652d820e69ab1e12662aae6`, auditado em 17/11/2026. Cada linha corresponde a um arquivo real. Dimensões são da **folha**, não de um sprite. Todos os GIFs contêm um único quadro de arquivo. “Quadros de arquivo = 1” não significa uma pose desenhada: uma folha contém muitas poses. Contagem semântica global não foi inventada a partir das dimensões. Bird: 72 células; Rat: 88; Fire (Large): 60. Os demais totais semânticos permanecem não anotados integralmente.

Metadados e hashes: [inventory.json](data/inventory.json). Layouts com recortes verificados: [FRAMES.md](FRAMES.md). A função descrita não significa que todas as ações daquele personagem estejam exportadas nesta folha.

## Animais — 16 imagens

| Arquivo | Folha (px) | Formato / modo | Quadros de arquivo | Uso no jogo / estudo |
|---|---:|---|---:|---|
| [Bat.png](../sprites/Animais/Bat.png) | 311 × 271 | PNG / RGBA | 1 | Morcego de ambientação; voo multivista. Não confundir automaticamente com família hostil Desert Wing. |
| [Bird.png](../sprites/Animais/Bird.png) | 223 × 152 | PNG / RGBA | 1 | Pássaro de ambientação; bloco walk corresponde visualmente ao voo; preservar rótulo original e adicionar descrição semântica. |
| [Camel.png](../sprites/Animais/Camel.png) | 1512 × 2746 | PNG / RGB | 1 | Camelo de ambientação associado ao cenário desértico; não é montaria controlável do jogador. |
| [Chicken.png](../sprites/Animais/Chicken.png) | 576 × 1190 | PNG / RGB | 1 | Galinha de ambientação de cidade/acampamento; movimento e estados da folha não implicam combate de monstro. |
| [Cobra.png](../sprites/Animais/Cobra.png) | 722 × 214 | PNG / RGB | 1 | Serpente pequena de ambientação; não confundir com Claw Viper hostil. |
| [Cow.png](../sprites/Animais/Cow.png) | 1230 × 2290 | PNG / RGBA | 1 | Vaca comum de ambientação; não é Hell Bovine armado do Secret Cow Level. |
| [Crab.png](../sprites/Animais/Crab.png) | 405 × 519 | PNG / RGBA | 1 | Caranguejo de ambientação; três variantes de idle/walk aparecem na folha, separar identidade visual e ação. |
| [Fly.png](../sprites/Animais/Fly.png) | 493 × 47 | PNG / RGBA | 1 | Inseto voador/ambientação, sequência pequena; não rotular como enxame hostil pelo nome. |
| [Larvae.png](../sprites/Animais/Larvae.png) | 820 × 784 | PNG / RGBA | 1 | Larvas de ambientação; distinção exata de entidade/ato não recuperável só pela folha. |
| [Maggot.png](../sprites/Animais/Maggot.png) | 343 × 532 | PNG / RGBA | 1 | Pequeno verme de ambientação desta pasta; não equivale automaticamente ao Sand Maggot hostil que gera ovos. |
| [Parrot.png](../sprites/Animais/Parrot.png) | 575 × 330 | PNG / RGBA | 1 | Papagaio de ambientação tropical; blocos walk/idle, walk visualmente voo. |
| [Rabbit.png](../sprites/Animais/Rabbit.png) | 327 × 180 | PNG / RGBA | 1 | Coelho de ambientação; idle, special e walk, gesto especial separado do ciclo locomotor. |
| [Rat.png](../sprites/Animais/Rat.png) | 173 × 276 | PNG / RGBA | 1 | Rato de ambientação; idle, walk e die; oito linhas de orientação nos blocos mapeados. |
| [Scarabs.png](../sprites/Animais/Scarabs.png) | 404 × 156 | PNG / RGBA | 1 | Besouros pequenos de ambientação; idle, walk 1, special, walk 2 e die. Não confundir com Scarab Demon que libera raios. |
| [Scorpion.png](../sprites/Animais/Scorpion.png) | 296 × 174 | PNG / RGBA | 1 | Escorpião pequeno de ambientação; idle/walk/die, não inferir dano por veneno. |
| [Spider.png](../sprites/Animais/Spider.png) | 355 × 376 | PNG / RGBA | 1 | Aranha de ambientação; walk/idle/death. Não é automaticamente a família Giant Spider hostil. |

## Classes — 20 imagens

| Arquivo | Folha (px) | Formato / modo | Quadros de arquivo | Uso no jogo / estudo |
|---|---:|---|---:|---|
| [Amazon (Heavy).gif](../sprites/Classes/Amazon%20%28Heavy%29.gif) | 2255 × 5987 | GIF / P | 1 | Amazon: classe de arco, lança e javelin; esta aparência não comprova todas as armas/habilidades. Variante Heavy. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Amazon (Light).gif](../sprites/Classes/Amazon%20%28Light%29.gif) | 2578 × 6403 | GIF / P | 1 | Amazon: classe de arco, lança e javelin; esta aparência não comprova todas as armas/habilidades. Variante Light. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Assassin (Heavy).gif](../sprites/Classes/Assassin%20%28Heavy%29.gif) | 1410 × 12404 | GIF / P | 1 | Assassin: classe da expansão, artes marciais e armadilhas; separar gesto corporal de projéteis/traps. Variante Heavy. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Assassin (Light).gif](../sprites/Classes/Assassin%20%28Light%29.gif) | 1350 × 11972 | GIF / P | 1 | Assassin: classe da expansão, artes marciais e armadilhas; separar gesto corporal de projéteis/traps. Variante Light. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Assassin (Medium).gif](../sprites/Classes/Assassin%20%28Medium%29.gif) | 1682 × 9617 | GIF / P | 1 | Assassin: classe da expansão, artes marciais e armadilhas; separar gesto corporal de projéteis/traps. Variante Medium. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Barbarian (Heavy).gif](../sprites/Classes/Barbarian%20%28Heavy%29.gif) | 4189 × 10496 | GIF / P | 1 | Barbarian: combatente com múltiplas configurações de armas; equipamento e oclusão são centrais. Variante Heavy. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Barbarian (Light).gif](../sprites/Classes/Barbarian%20%28Light%29.gif) | 3357 × 11645 | GIF / P | 1 | Barbarian: combatente com múltiplas configurações de armas; equipamento e oclusão são centrais. Variante Light. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Barbarian (Medium).gif](../sprites/Classes/Barbarian%20%28Medium%29.gif) | 3987 × 8627 | GIF / P | 1 | Barbarian: combatente com múltiplas configurações de armas; equipamento e oclusão são centrais. Variante Medium. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Druid (Heavy).gif](../sprites/Classes/Druid%20%28Heavy%29.gif) | 3384 × 7172 | GIF / P | 1 | Druid: classe da expansão; folhas humanoides não comprovam formas de lobo/urso ou invocações. Variante Heavy. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Druid (Light).gif](../sprites/Classes/Druid%20%28Light%29.gif) | 2807 × 4328 | GIF / P | 1 | Druid: classe da expansão; folhas humanoides não comprovam formas de lobo/urso ou invocações. Variante Light. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Druid (Medium).gif](../sprites/Classes/Druid%20%28Medium%29.gif) | 2993 × 6132 | GIF / P | 1 | Druid: classe da expansão; folhas humanoides não comprovam formas de lobo/urso ou invocações. Variante Medium. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Necromancer (Heavy).gif](../sprites/Classes/Necromancer%20%28Heavy%29.gif) | 3940 × 9264 | GIF / P | 1 | Necromancer: conjurador; esqueletos, golem e maldições não estão garantidos por esta folha corporal. Variante Heavy. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Necromancer (Light).gif](../sprites/Classes/Necromancer%20%28Light%29.gif) | 3258 × 6019 | GIF / P | 1 | Necromancer: conjurador; esqueletos, golem e maldições não estão garantidos por esta folha corporal. Variante Light. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Necromancer (Medium).gif](../sprites/Classes/Necromancer%20%28Medium%29.gif) | 3054 × 7616 | GIF / P | 1 | Necromancer: conjurador; esqueletos, golem e maldições não estão garantidos por esta folha corporal. Variante Medium. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Paladin (Heavy, Heraldic Shield).gif](../sprites/Classes/Paladin%20%28Heavy%2C%20Heraldic%20Shield%29.gif) | 2700 × 11357 | GIF / P | 1 | Paladin: combatente com escudo; variantes Heraldic/Tower mudam silhueta, não o personagem. Variante Heavy, Heraldic Shield. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Paladin (Heavy, Tower Shield).gif](../sprites/Classes/Paladin%20%28Heavy%2C%20Tower%20Shield%29.gif) | 2700 × 11437 | GIF / P | 1 | Paladin: combatente com escudo; variantes Heraldic/Tower mudam silhueta, não o personagem. Variante Heavy, Tower Shield. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Paladin (Light).gif](../sprites/Classes/Paladin%20%28Light%29.gif) | 2370 × 10221 | GIF / P | 1 | Paladin: combatente com escudo; variantes Heraldic/Tower mudam silhueta, não o personagem. Variante Light. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Paladin (Medium).gif](../sprites/Classes/Paladin%20%28Medium%29.gif) | 2700 × 11277 | GIF / P | 1 | Paladin: combatente com escudo; variantes Heraldic/Tower mudam silhueta, não o personagem. Variante Medium. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Sorceress (Heavy).gif](../sprites/Classes/Sorceress%20%28Heavy%29.gif) | 3179 × 6739 | GIF / P | 1 | Sorceress: conjuradora elemental; corpo em cast não é a animação integral da magia. Variante Heavy. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |
| [Sorceress (Light).gif](../sprites/Classes/Sorceress%20%28Light%29.gif) | 2605 × 6736 | GIF / P | 1 | Sorceress: conjuradora elemental; corpo em cast não é a animação integral da magia. Variante Light. Light/Medium/Heavy são aparências de armadura da extração, não níveis de poder. |

## Inimigos — 24 imagens

| Arquivo | Folha (px) | Formato / modo | Quadros de arquivo | Uso no jogo / estudo |
|---|---:|---|---:|---|
| [Abominable.png](../sprites/Inimigos/Abominable.png) | 3616 × 4552 | PNG / RGBA | 1 | Família de criaturas grandes tipo yeti; referência para massa, braços e ataque corporal. Nome da extração não determina variante de MonStats ou ato único. |
| [Altar.png](../sprites/Inimigos/Altar.png) | 5861 × 1789 | PNG / RGBA | 1 | Entidade/altar animado armazenado em Inimigos. A folha mostra sequência de objeto e efeitos; associação exata a altar hostil/missionário não confirmada. Não atribuir IA de monstro pelo diretório. |
| [Andariel.png](../sprites/Inimigos/Andariel.png) | 5282 × 8127 | PNG / RGBA | 1 | Chefe final do Ato I nas Catacombs; combate corporal e veneno. Efeitos da folha devem ser separados do corpo; dano e área não se deduzem do desenho. |
| [Baal's Minion (Light Weaponless).png](../sprites/Inimigos/Baal%27s%20Minion%20%28Light%20Weaponless%29.png) | 4045 × 4929 | PNG / RGBA | 1 | Família de servos do Ato V, variante light sem arma; não é Baal nem prova cobertura de todos os seus servos especiais. |
| [Baboon Demon.gif](../sprites/Inimigos/Baboon%20Demon.gif) | 3374 × 4259 | GIF / P | 1 | Família de demônios símios; movimentação e combate corporal multivista. O arquivo GIF é uma folha estática. |
| [Balrog (Saber).png](../sprites/Inimigos/Balrog%20%28Saber%29.png) | 7855 × 4880 | PNG / RGBA | 1 | Família de demônios alados, variante com sabre; parear com as outras quatro variantes para estudar equipamento. |
| [Balrog (Sickle Sword).png](../sprites/Inimigos/Balrog%20%28Sickle%20Sword%29.png) | 7855 × 4880 | PNG / RGBA | 1 | Mesma família visual, variante com espada curva; não é ação diferente só porque a arma muda. |
| [Balrog (Sword).png](../sprites/Inimigos/Balrog%20%28Sword%29.png) | 7855 × 4880 | PNG / RGBA | 1 | Mesma família visual, variante com espada; preservar coerência do corpo e pontos de empunhadura. |
| [Balrog (Weaponless).png](../sprites/Inimigos/Balrog%20%28Weaponless%29.png) | 7855 × 4880 | PNG / RGB | 1 | Variante sem arma; útil como comparação visual, não constitui necessariamente camada limpa separada de todas as demais variantes. |
| [Balrog (Wide Sword).png](../sprites/Inimigos/Balrog%20%28Wide%20Sword%29.png) | 7855 × 4880 | PNG / RGBA | 1 | Variante com espada larga; largura altera silhueta/oclusão e exige validação por direção. |
| [Blood Hawk Nest.png](../sprites/Inimigos/Blood%20Hawk%20Nest.png) | 4348 × 804 | PNG / RGBA | 1 | Ninho que gera aves hostis; objeto/entidade estacionária atacável. Nascimento de aves é evento de gameplay separado da animação do ninho. |
| [Blood Hawk.gif](../sprites/Inimigos/Blood%20Hawk.gif) | 2714 × 1911 | GIF / P | 1 | Ave hostil da família Blood Hawk; voo, ataque e morte; distinguir da fauna Bird/Parrot. |
| [Blood Lord.png](../sprites/Inimigos/Blood%20Lord.png) | 9219 × 3733 | PNG / RGBA | 1 | Família de grandes combatentes do Ato V; movimento pesado e ataques. Não confundir apenas pelo nome com qualquer vampiro de nome similar. |
| [Blunderbore.gif](../sprites/Inimigos/Blunderbore.gif) | 8540 × 3401 | GIF / P | 1 | Família de brutamontes de combate próximo; estudar peso, antecipação e alcance, sem inferir hitbox do contorno. |
| [Bone Fetish (Knife).png](../sprites/Inimigos/Bone%20Fetish%20%28Knife%29.png) | 2246 × 2240 | PNG / RGBA | 1 | Fetiche esquelético, variante com faca; no jogo a família é conhecida pelo perigo da explosão na morte. Não inferir que a folha incorpora toda a explosão. |
| [Bone Fetish (Spear).png](../sprites/Inimigos/Bone%20Fetish%20%28Spear%29.png) | 2246 × 2240 | PNG / RGBA | 1 | Variante com lança; deve pertencer ao mesmo grupo de família no split de dados que a variante com faca. |
| [Carniflower.png](../sprites/Inimigos/Carniflower.png) | 3437 × 2661 | PNG / RGBA | 1 | Planta/monstro rotulada Carniflower pela extração. Presença efetiva no jogo lançado, nome de entidade e habilidades não confirmados; manter como referência visual não validada. |
| [Catapult.png](../sprites/Inimigos/Catapult.png) | 7895 × 1969 | PNG / RGBA | 1 | Catapulta do Ato V, artilharia estacionária; separar máquina, disparo, projétil e impacto. A folha não fornece balística nem área de dano. |
| [Council Member.gif](../sprites/Inimigos/Council%20Member.gif) | 3610 × 3038 | GIF / P | 1 | Membros do Conselho Zakarum, associados a Travincal e Durance of Hate; combate e magia. Não atribuir variante única/estatísticas a toda a folha. |
| [Death Mauler.png](../sprites/Inimigos/Death%20Mauler.png) | 5269 × 4417 | PNG / RGBA | 1 | Família do Ato V que ataca com membros/tentáculos pelo solo; sincronizar antecipação com surgimento do ataque, não apenas reproduzir loop de caminhada. |
| [Demon Imp.png](../sprites/Inimigos/Demon%20Imp.png) | 3840 × 8820 | PNG / RGBA | 1 | Diabrete do Ato V; conjuração/ataque à distância e mobilidade especial. Efeitos e eventos exigem trilhas próprias. |
| [Desert Wing.png](../sprites/Inimigos/Desert%20Wing.png) | 2577 × 10544 | PNG / RGBA | 1 | Família de demônios alados hostis; não confundir com Bat ambiental. A folha não prova quais variantes elementais estão representadas. |
| [Diablo.png](../sprites/Inimigos/Diablo.png) | 6798 × 18841 | PNG / P | 1 | Chefe do Ato IV no Chaos Sanctuary; múltiplos ataques corpo a corpo e mágicos. A folha não substitui a implementação de raio, fogo, colisão e padrões de IA. |
| [Duriel.png](../sprites/Inimigos/Duriel.png) | 6651 × 6865 | PNG / RGBA | 1 | Chefe do Ato II em Tal Rasha's Chamber; grande corpo, combate próximo e investida. A aura Holy Freeze é mecânica separada; não inferir alcance da área pela largura dos frames. |

## Npcs — 39 imagens

| Arquivo | Folha (px) | Formato / modo | Quadros de arquivo | Uso no jogo / estudo |
|---|---:|---|---:|---|
| [Akara.png](../sprites/Npcs/Akara.png) | 352 × 1225 | PNG / RGBA | 1 | Ato I, Acampamento das Rogues: sacerdotisa, cura, comércio de suprimentos mágicos e missões; a animação de conversa não executa a cura por si. |
| [Alkor.png](../sprites/Npcs/Alkor.png) | 978 × 1860 | PNG / RGBA | 1 | Ato III, Docas de Kurast: alquimista, poções, apostas e missões; estudo de gestos e atividade de NPC. |
| [Anya.png](../sprites/Npcs/Anya.png) | 919 × 758 | PNG / RGBA | 1 | Ato V, Harrogath: NPC resgatada, comércio e recompensas de missões; estado congelado/resgatado depende da lógica de missão, não do nome da folha. |
| [Asheara.png](../sprites/Npcs/Asheara.png) | 3339 × 1185 | PNG / RGBA | 1 | Ato III, Docas de Kurast: líder dos Iron Wolves, contratação de mercenários e comércio. |
| [Atma.png](../sprites/Npcs/Atma.png) | 2916 × 685 | PNG / RGBA | 1 | Ato II, Lut Gholein: taverneira ligada à missão de Radament; também restaura recursos. |
| [Cameos.png](../sprites/Npcs/Cameos.png) | 757 × 735 | PNG / RGBA | 1 | Folha coletiva de figuras/cameos. Não representa um único NPC. Identidades individuais e condição de aparição não confirmadas pelo material fornecido; separar subgrupos antes de rotular. |
| [Charsi.png](../sprites/Npcs/Charsi.png) | 900 × 1130 | PNG / RGBA | 1 | Ato I: ferreira, comércio, reparo e recompensa de imbuir. A folha distingue smith, walk e idle; smith é uma sequência longa com quebra de linha, não uma linha por direção. |
| [Deckard Cain.png](../sprites/Npcs/Deckard%20Cain.png) | 1329 × 702 | PNG / RGBA | 1 | Sábio recorrente nos atos: identificação de itens, diálogos e missões. Uma única folha não comprova todas as variantes por ato. |
| [Drognan.png](../sprites/Npcs/Drognan.png) | 841 × 1849 | PNG / RGBA | 1 | Ato II: mago comerciante de equipamento e suprimentos mágicos; diálogos de progressão. |
| [Elzix.png](../sprites/Npcs/Elzix.png) | 337 × 1393 | PNG / RGBA | 1 | Ato II: comerciante de armas/armaduras e apostas; preservar o nome e o caminho originais da extração. |
| [Fara.png](../sprites/Npcs/Fara.png) | 821 × 1697 | PNG / RGBA | 1 | Ato II: ferreira, comércio, reparos e cura; gestos de profissão e conversa. |
| [Geglash.png](../sprites/Npcs/Geglash.png) | 920 × 724 | PNG / RGBA | 1 | Ato II: personagem de ambientação e diálogos na taverna; não é um mercenário contratável. |
| [Gheed.png](../sprites/Npcs/Gheed.png) | 551 × 564 | PNG / RGBA | 1 | Ato I: comerciante e apostas; o pacote não contém o sistema de geração de itens. |
| [Greiz.png](../sprites/Npcs/Greiz.png) | 393 × 1449 | PNG / RGBA | 1 | Ato II: contratação de mercenários do deserto; a folha do contratante não substitui a dos combatentes. |
| [Hadriel.png](../sprites/Npcs/Hadriel.png) | 1873 × 228 | PNG / RGBA | 1 | Ato IV: anjo que guarda o acesso ao Chaos Sanctuary; personagem de diálogo, não o chefe Izual. |
| [Halbu.png](../sprites/Npcs/Halbu.png) | 1020 × 1164 | PNG / RGBA | 1 | Ato IV, Pandemonium Fortress: comércio e reparo de equipamento. |
| [Hratli.png](../sprites/Npcs/Hratli.png) | 465 × 1145 | PNG / RGBA | 1 | Ato III: ferreiro/comerciante, reparos e diálogos; deslocamento e animação de ofício são responsabilidades distintas. |
| [Izual's Spirit.png](../sprites/Npcs/Izual%27s%20Spirit.png) | 4661 × 835 | PNG / RGBA | 1 | Ato IV: espírito liberado após derrotar Izual, usado no diálogo de missão; não é a forma demoníaca combatente. |
| [Jamella.png](../sprites/Npcs/Jamella.png) | 1361 × 3040 | PNG / RGBA | 1 | Ato IV: comércio, apostas e cura; efeitos visuais presentes devem ser anotados como camadas/sequências próprias. |
| [Jerhyn.png](../sprites/Npcs/Jerhyn.png) | 502 × 580 | PNG / RGBA | 1 | Ato II: governante de Lut Gholein; diálogo e acesso ao palácio ligados à progressão. |
| [Kashya.png](../sprites/Npcs/Kashya.png) | 361 × 1257 | PNG / RGBA | 1 | Ato I: comandante das Rogues; contratação e missão de Blood Raven. |
| [Kurast Docks Men.png](../sprites/Npcs/Kurast%20Docks%20Men.png) | 3341 × 7896 | PNG / RGBA | 1 | Figurantes masculinos das Docas de Kurast, Ato III; separar cada personagem/variante, sem atribuir serviços de NPC nomeado. |
| [Larzuk.png](../sprites/Npcs/Larzuk.png) | 1619 × 1056 | PNG / RGBA | 1 | Ato V: ferreiro, comércio, reparo e recompensa de engastes; gestos de trabalho não codificam a recompensa. |
| [Lut Gholein Guard (Light).png](../sprites/Npcs/Lut%20Gholein%20Guard%20%28Light%29.png) | 4853 × 6156 | PNG / RGBA | 1 | Guarda de Lut Gholein, Ato II, variante visual light; não identificar automaticamente como Kaelan sem comparação específica. |
| [Lut Gholein Men.png](../sprites/Npcs/Lut%20Gholein%20Men.png) | 2925 × 3947 | PNG / RGBA | 1 | Figurantes masculinos de Lut Gholein, Ato II; folha coletiva com variantes. |
| [Lut Gholein Women.png](../sprites/Npcs/Lut%20Gholein%20Women.png) | 2188 × 2962 | PNG / RGBA | 1 | Figurantes femininos de Lut Gholein, Ato II; folha coletiva, não uma classe jogável. |
| [Lysander.png](../sprites/Npcs/Lysander.png) | 473 × 1417 | PNG / RGBA | 1 | Ato II: vendedor de poções e suprimentos; NPC de cidade. |
| [Malah.png](../sprites/Npcs/Malah.png) | 529 × 1386 | PNG / RGBA | 1 | Ato V: curandeira e comerciante de suprimentos, participante da missão de resgate de Anya. |
| [Man in Coat (Black & Brown).png](../sprites/Npcs/Man%20in%20Coat%20%28Black%20%26%20Brown%29.png) | 509 × 261 | PNG / RGBA | 1 | Homem encapuzado com variantes preta e marrom; legendas idle/talk. Identidade e uso exato no jogo não confirmados; não rotular como Dark Wanderer por semelhança. |
| [Meshif.png](../sprites/Npcs/Meshif.png) | 752 × 668 | PNG / RGBA | 1 | Ato II/III: capitão que transporta entre Lut Gholein e Kurast e participa de missão no Ato III; transporte é transição lógica, não movimento do sprite. |
| [Nihlathak.png](../sprites/Npcs/Nihlathak.png) | 497 × 1549 | PNG / RGBA | 1 | Ato V: personagem inicialmente de cidade e posteriormente inimigo de missão. Esta folha na pasta Npcs não comprova todas as animações da forma hostil. |
| [Ormus.png](../sprites/Npcs/Ormus.png) | 2558 × 960 | PNG / RGBA | 1 | Ato III: mago, cura e comércio de suprimentos mágicos; diálogo e recompensas de missão. |
| [Qual-Kehk.png](../sprites/Npcs/Qual-Kehk.png) | 1001 × 1679 | PNG / RGBA | 1 | Ato V: comandante, contratação de mercenários bárbaros e missão dos prisioneiros. Caminho mantém a grafia original Qual-Kehk. |
| [Rogue Mercenary.png](../sprites/Npcs/Rogue%20Mercenary.png) | 1616 × 2644 | PNG / RGBA | 1 | Mercenária arqueira do Ato I, contratada com Kashya; aliada móvel com combate, não vendedora. Referência para integrar corpo, arco e direção. |
| [The Dark Wanderer.png](../sprites/Npcs/The%20Dark%20Wanderer.png) | 3476 × 1010 | PNG / RGBA | 1 | Viajante Sombrio, aparição narrativa relacionada à chegada a Kurast; separar corpo e efeito visual. Não é uma classe jogável nem o sprite do chefe Diablo. |
| [Traders.png](../sprites/Npcs/Traders.png) | 982 × 347 | PNG / RGBA | 1 | Duas sequências rotuladas de comerciantes/bancas com atuação de cenário; identidade, ato e presença efetiva não confirmados. Não pressupor menu comercial funcional para cada figura. |
| [Valkyrie.png](../sprites/Npcs/Valkyrie.png) | 3401 × 1505 | PNG / RGBA | 1 | Invocação da Amazon, aliada de combate; não é NPC de cidade ou mercenária contratada. Corpo e efeitos de surgimento precisam de rótulos distintos. |
| [Warriv (Act 1).png](../sprites/Npcs/Warriv%20%28Act%201%29.png) | 1885 × 596 | PNG / RGBA | 1 | Ato I: líder da caravana; viagem para Lut Gholein quando a progressão permite. Variante explícita do Ato I. |
| [Warriv (Act 2).png](../sprites/Npcs/Warriv%20%28Act%202%29.png) | 1020 × 976 | PNG / RGBA | 1 | Ato II: versão em Lut Gholein, retorno ao acampamento; não tratar como novo personagem independente no split de treinamento. |

## Objects — 18 imagens

| Arquivo | Folha (px) | Formato / modo | Quadros de arquivo | Uso no jogo / estudo |
|---|---:|---|---:|---|
| [Altar (Secret Passage).png](../sprites/Objects/Altar%20%28Secret%20Passage%29.png) | 926 × 285 | PNG / RGBA | 1 | Altar de passagem secreta conforme rótulo da extração; estrutura animada. Localização e vínculo exatos de missão não confirmados. |
| [Altar.png](../sprites/Objects/Altar.png) | 1013 × 214 | PNG / RGBA | 1 | Altar com sequência e efeito separado na folha; não confundir com Inimigos/Altar nem assumir que seja shrine de um bônus específico. |
| [Arcane Sanctuary Teleporter 1.png](../sprites/Objects/Arcane%20Sanctuary%20Teleporter%201.png) | 1381 × 763 | PNG / RGBA | 1 | Teletransportador do Arcane Sanctuary, Ato II; portal visual e mecanismo de ligação entre plataformas são elementos diferentes. |
| [Banner.png](../sprites/Objects/Banner.png) | 591 × 302 | PNG / RGBA | 1 | Bandeira animada de cenário; loop de tecido, sem hitbox de combatente. |
| [Barrel.png](../sprites/Objects/Barrel.png) | 1321 × 494 | PNG / RGBA | 1 | Barril quebrável; estados íntegro/quebra e detritos/efeitos. Recompensa e dano de explosão dependem do tipo lógico do objeto. |
| [Blood Pool.png](../sprites/Objects/Blood%20Pool.png) | 683 × 85 | PNG / RGBA | 1 | Poça de sangue; efeito/decoração no chão. Não criar dano persistente somente pelo aspecto. |
| [Blood Vassel.png](../sprites/Objects/Blood%20Vassel.png) | 451 × 79 | PNG / RGBA | 1 | Recipiente de sangue (grafia Vassel preservada); pequena sequência de objeto, função interativa exata não confirmada. |
| [Desert Water Source.png](../sprites/Objects/Desert%20Water%20Source.png) | 1241 × 330 | PNG / RGBA | 1 | Fonte/poça de água de cenário desértico; superfície animada e pequenos efeitos. Não presumir cura de well sem identificação do objeto original. |
| [Escaping Spirit.png](../sprites/Objects/Escaping%20Spirit.png) | 11360 × 2457 | PNG / RGBA | 1 | Espírito escapando, efeito transitório; entidade de efeito, não personagem completo com locomoção. |
| [Fire (Large).png](../sprites/Objects/Fire%20%28Large%29.png) | 2381 × 416 | PNG / RGBA | 1 | Três ciclos de fogo de tamanhos diferentes, 20 quadros visuais cada; referência para volume e evolução de chamas. |
| [Fire (Small).png](../sprites/Objects/Fire%20%28Small%29.png) | 872 × 1234 | PNG / RGBA | 1 | Folha com múltiplos blocos de fogo pequeno e fases visuais; separar cada bloco, não concatenar toda a imagem em um loop. |
| [Fire Trap.png](../sprites/Objects/Fire%20Trap.png) | 6661 × 4042 | PNG / RGBA | 1 | Armadilha de fogo; máquina/estado e emissão devem ser anotados separadamente; dano ocorre por eventos da lógica. |
| [Fireplace 01.png](../sprites/Objects/Fireplace%2001.png) | 581 × 88 | PNG / RGBA | 1 | Braseiro/lareira com corpo e chama; estudo de composição de objeto e fogo. |
| [Fireplace 02.png](../sprites/Objects/Fireplace%2002.png) | 581 × 124 | PNG / RGBA | 1 | Objeto com estado idle e if on; corpo e chama em linhas separadas. Não concatenar as duas linhas como uma única trajetória temporal. |
| [Fireplace 03.png](../sprites/Objects/Fireplace%2003.png) | 861 × 259 | PNG / RGBA | 1 | Objeto com take off, turn on e on; transição de ativação e estado contínuo são clipes distintos. |
| [Floor Seal.png](../sprites/Objects/Floor%20Seal.png) | 4313 × 3269 | PNG / RGBA | 1 | Selo/mecanismo de chão com vários blocos; abertura/ativação visual, associação a selo específico do jogo não confirmada. |
| [Fog.png](../sprites/Objects/Fog.png) | 2421 × 474 | PNG / RGBA | 1 | Folha rotulada Fog que apresenta formas elípticas no chão; não assumir uma textura volumétrica de névoa ou modo aditivo sem verificar o recurso original. |
| [Teleporter 3.png](../sprites/Objects/Teleporter%203.png) | 2131 × 1414 | PNG / RGBA | 1 | Teletransportador com figuras e arcos/efeitos em múltiplos blocos; destino, ato e variante não confirmados pelo número 3. |

## Parts — 14 imagens

| Arquivo | Folha (px) | Formato / modo | Quadros de arquivo | Uso no jogo / estudo |
|---|---:|---|---:|---|
| [Rogue Parts - Rogue Body Light (Unused).png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Body%20Light%20%28Unused%29.png) | 6673 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Body Light (Unused). Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Unused é um rótulo do arquivo; não confirma uso na versão lançada. |
| [Rogue Parts - Rogue Body Light.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Body%20Light.png) | 6871 × 6132 | PNG / RGB | 1 | Componente modular Rogue: Body Light. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Body Medium (Unused).png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Body%20Medium%20%28Unused%29.png) | 6467 × 3680 | PNG / RGBA | 1 | Componente modular Rogue: Body Medium (Unused). Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Unused é um rótulo do arquivo; não confirma uso na versão lançada. |
| [Rogue Parts - Rogue Body Medium.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Body%20Medium.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Body Medium. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Bow (Large).png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Bow%20%28Large%29.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Bow (Large). Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Bow (Small).png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Bow%20%28Small%29.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Bow (Small). Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Head Light.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Head%20Light.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Head Light. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Head Medium.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Head%20Medium.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Head Medium. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Left Hand.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Left%20Hand.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Left Hand. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Left Pauldron Light.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Left%20Pauldron%20Light.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Left Pauldron Light. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Left Pauldron Medium.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Left%20Pauldron%20Medium.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Left Pauldron Medium. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Right Hand.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Right%20Hand.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Right Hand. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Right Pauldron Light.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Right%20Pauldron%20Light.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Right Pauldron Light. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |
| [Rogue Parts - Rogue Right Pauldron Medium.png](../sprites/Parts/Rogue%20Parts/Rogue%20Parts%20-%20Rogue%20Right%20Pauldron%20Medium.png) | 6871 × 4906 | PNG / RGBA | 1 | Componente modular Rogue: Right Pauldron Medium. Sincronizar ação, direção, frame, origem e ordem de desenho com corpo/arco/mãos. Não usar como personagem completo nem centralizar a peça isoladamente. |

## Tiles — 22 imagens

| Arquivo | Folha (px) | Formato / modo | Quadros de arquivo | Uso no jogo / estudo |
|---|---:|---|---:|---|
| [Barracks Floor.png](../sprites/Tiles/Act%201/Barracks%20Floor.png) | 800 × 652 | PNG / RGB | 1 | Piso do Ato I, conjunto Barracks Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Barracks.png](../sprites/Tiles/Act%201/Barracks.png) | 1672 × 1546 | PNG / RGBA | 1 | Arquitetura/objetos do Ato I, conjunto Barracks. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Catacomb.png](../sprites/Tiles/Act%201/Catacomb.png) | 4640 × 962 | PNG / RGBA | 1 | Arquitetura/objetos do Ato I, conjunto Catacomb. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Catacombs Floor.png](../sprites/Tiles/Act%201/Catacombs%20Floor.png) | 800 × 1220 | PNG / RGB | 1 | Piso do Ato I, conjunto Catacombs Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Cathedral Floor.png](../sprites/Tiles/Act%201/Cathedral%20Floor.png) | 800 × 893 | PNG / RGB | 1 | Piso do Ato I, conjunto Cathedral Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Cathedral.png](../sprites/Tiles/Act%201/Cathedral.png) | 3200 × 1440 | PNG / RGBA | 1 | Arquitetura/objetos do Ato I, conjunto Cathedral. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Cave Floor.png](../sprites/Tiles/Act%201/Cave%20Floor.png) | 800 × 3852 | PNG / RGBA | 1 | Piso do Ato I, conjunto Cave Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Caves.png](../sprites/Tiles/Act%201/Caves.png) | 640 × 771 | PNG / RGBA | 1 | Arquitetura/objetos do Ato I, conjunto Caves. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Court Floor.png](../sprites/Tiles/Act%201/Court%20Floor.png) | 800 × 1846 | PNG / RGB | 1 | Piso do Ato I, conjunto Court Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Court Wall.png](../sprites/Tiles/Act%201/Court%20Wall.png) | 4960 × 994 | PNG / RGB | 1 | Arquitetura/objetos do Ato I, conjunto Court Wall. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Crypt Floor.png](../sprites/Tiles/Act%201/Crypt%20Floor.png) | 800 × 479 | PNG / RGB | 1 | Piso do Ato I, conjunto Crypt Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Crypt Wall.png](../sprites/Tiles/Act%201/Crypt%20Wall.png) | 4160 × 288 | PNG / RGB | 1 | Arquitetura/objetos do Ato I, conjunto Crypt Wall. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Graveyard Ground.png](../sprites/Tiles/Act%201/Graveyard%20Ground.png) | 800 × 479 | PNG / RGB | 1 | Piso do Ato I, conjunto Graveyard Ground. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Graveyard.png](../sprites/Tiles/Act%201/Graveyard.png) | 5920 × 833 | PNG / RGBA | 1 | Arquitetura/objetos do Ato I, conjunto Graveyard. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Monastery Floor.png](../sprites/Tiles/Act%201/Monastery%20Floor.png) | 800 × 79 | PNG / RGB | 1 | Piso do Ato I, conjunto Monastery Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Monastery Walls.png](../sprites/Tiles/Act%201/Monastery%20Walls.png) | 8800 × 640 | PNG / RGB | 1 | Arquitetura/objetos do Ato I, conjunto Monastery Walls. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Outdoor Floor.png](../sprites/Tiles/Act%201/Outdoor%20Floor.png) | 1601 × 4768 | PNG / RGBA | 1 | Piso do Ato I, conjunto Outdoor Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Outdoor.png](../sprites/Tiles/Act%201/Outdoor.png) | 3200 × 5582 | PNG / RGBA | 1 | Arquitetura/objetos do Ato I, conjunto Outdoor. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Town Floor.png](../sprites/Tiles/Act%201/Town%20Floor.png) | 800 × 2959 | PNG / RGBA | 1 | Piso do Ato I, conjunto Town Floor. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Town Objects.png](../sprites/Tiles/Act%201/Town%20Objects.png) | 5760 × 2502 | PNG / RGBA | 1 | Arquitetura/objetos do Ato I, conjunto Town Objects. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |
| [Tristram Ground.png](../sprites/Tiles/Act%201/Tristram%20Ground.png) | 800 × 959 | PNG / RGB | 1 | Piso do Ato I, conjunto Tristram Ground. Peças espaciais/variantes para composição de mapa; colunas não significam tempo. Colisão, materiais e conexão não estão codificados no PNG. |
| [Tristram Walls.png](../sprites/Tiles/Act%201/Tristram%20Walls.png) | 5280 × 1346 | PNG / RGB | 1 | Arquitetura/objetos do Ato I, conjunto Tristram Walls. Paredes, fachadas ou props são peças espaciais com oclusão e ponto de chão próprios; não são animação por ordem de leitura. |

## Arquivo auxiliar fora do corpus visual

`sprites/Objects/chibi-isometric-rpg-development.zip` tem 49 entradas (35 arquivos e 14 diretórios) e contém um projeto TypeScript/Next.js: `package.json`, `src/game/`, `src/db/`, rotas de API e documentos de GDD/arquitetura/roadmap. Não contém uma coleção adicional de PNG/GIF. Foi inspecionado como ZIP, sem executar código ou instalar dependências. Não pertence à contagem de imagens ou de frames. Preservado no lugar original; não tratado como documentação autoritativa do Diablo II. Lista exata em [archive-contents.json](data/archive-contents.json).
