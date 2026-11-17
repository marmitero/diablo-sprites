# Fontes, evidência e proveniência

Consultas em 17/11/2026. Links externos descrevem o jogo e sua tecnologia; não comprovam que a pessoa que montou cada folha exportou exatamente aquele recurso/versão. A evidência primária deste acervo é o conjunto de imagens do snapshot e seus hashes.

## Fontes para a produção e a tecnologia

| Fonte | Autor/origem | Uso nesta documentação | Limite |
|---|---|---|---|
| [Postmortem: Blizzard’s Diablo II](https://www.cs.hmc.edu/~markk/SWE_copies/postmortem__diablo_ii.html) | Erich Schaefer, desenvolvedor original; cópia do texto publicado em 2000 | Produção em 3D Studio Max/Photoshop e sistema de componentes | Não contém os fontes 3D deste acervo |
| [Game Developer, outubro de 2000](https://media.gdcvault.com/GD_Mag_Archives/GDM_October_2000.pdf) | Edição com o postmortem original | Fonte editorial do relato de produção | Relato histórico, não especificação destas folhas |
| [Resurrecting a Classic, GDC 2022](https://www.gdcvault.com/play/1028028/Resurrecting-a-Classic-Bringing-Diablo) e [slides](https://media.gdcvault.com/GDC%2B2022/Speaker%2BSlides/Resurrecting%2Ba%2BClassic_Todisco_Kevin.pdf) | Kevin Todisco, equipe de remasterização | Explica o mundo original baseado em sprites pré-renderizados e composição | Não confundir a engine 3D do remaster com o jogo clássico |
| [Extracting Diablo II Animations](https://tristram-archives.github.io/diablo2_infodump/2013/just%20hosting%20these%2C%20Downloaded%20from%20Internet/documentation/extracting_diablo_2_animations.pdf) | Paul Siramy, autor das ferramentas/tutoriais de extração | Papel de DCC, COF, colormaps, offsets e animação | Engenharia comunitária de formatos; não atribuir a ele a extração destas folhas sem prova |
| [OpenDiablo2: decodificação DCC](https://github.com/OpenDiablo2/OpenDiablo2/blob/master/d2core/d2asset/dcc_animation.go) | Implementação aberta de engine | Comparação de estrutura: direções e frames por direção | Reimplementação, não código-fonte da Blizzard; não é decodificador destas folhas PNG/GIF |

Não foi deduzido o timing nativo de nenhuma imagem a partir dessas fontes. Não foi atribuída ordem de bússola às linhas por analogia com DCC.

## Fontes oficiais de função no jogo

- [Arreat Summit — NPCs](https://classic.battle.net/diablo2exp/npcs/): índice oficial de personagens e atos.
- [Ato I](https://classic.battle.net/diablo2exp/npcs/act1.shtml): Akara, Charsi, Gheed, Kashya, Warriv e serviços.
- [Ato II](https://classic.battle.net/diablo2exp/npcs/act2.shtml): moradores, comércio, cura, contratação e transporte de Lut Gholein.
- [Ato III](https://classic.battle.net/diablo2exp/npcs/act3.shtml): Alkor, Asheara, Hratli, Meshif e Ormus.
- [Ato IV](https://classic.battle.net/diablo2exp/npcs/act4.shtml): Hadriel, Halbu, Jamella e contexto de Izual.
- [Ato V](https://classic.battle.net/diablo2exp/npcs/act5.shtml): moradores e serviços de Harrogath.
- [Hirelings](https://classic.battle.net/diablo2exp/basics/hirelings.shtml): Rogue Scouts do Ato I, Greiz, Asheara e Qual-Kehk; distinção entre contratante e unidade contratada.
- [Amazon Passive and Magic](https://classic.battle.net/diablo2exp/skills/amazon-passive.shtml): Valkyrie como habilidade/invocação da Amazon.
- [Monsters](https://classic.battle.net/diablo2exp/monsters/): índice oficial de bestiários e chefes. Nomes de extração não equivalem automaticamente aos nomes de cada variante de monstro.

O escopo é o jogo clássico/expansão, sem presumir mudanças do Resurrected ou de mods. Não foram transcritas estatísticas de balanceamento, regras de dano ou dados atuais de patches.

## Cadeia de proveniência do repositório

| Campo | Estado observado |
|---|---|
| Repositório | `marmitero/diablo-sprites`, público |
| Commit-base | `da3fd762ee2f5463e652d820e69ab1e12662aae6` |
| Natureza declarada pelo organizador | Acervo parcial associado a Diablo II, para estudo e futuro treinamento de sprites |
| Licença no snapshot | Nenhum arquivo de licença encontrado; metadado de licença do GitHub vazio |
| Créditos nas folhas | Exemplos visíveis: SUTINOER; “ripped by napalm” em folhas de classes |
| Site/extrator original por folha | Não fornecido de maneira verificável |
| Versão exata do jogo por folha | Não fornecida |
| Arquivo nativo / token por folha | Não fornecido |
| Fontes 3D / rig / luz | Não presentes |
| Base de uso para treinamento | Não documentada neste snapshot |

Registrar crédito incorporado não comprova a autoria do sprite original ou concede licença. A ausência de licença no repositório não deve ser substituída por uma licença permissiva inventada. Não há neste documento uma conclusão jurídica sobre um treinamento específico; há a descrição dos dados de proveniência disponíveis e ausentes.

Para cada derivado, conservar `source_path`, SHA-256, retângulo, método de máscara, modificações e vínculo ao original. Não apagar créditos dos originais; excluir legendas/créditos da região de treinamento apenas nas cópias de trabalho, com rastreabilidade. O ZIP auxiliar tem origem própria não documentada e não deve ser fundido silenciosamente ao corpus.

## Como resolver uma identidade ambígua

Comparar o recurso nativo obtido por uma base de uso apropriada, registrar token/caminho e versão, confrontar as poses e rótulos e só então atualizar a função no catálogo. `Carniflower`, `Cameos`, `Traders`, alguns altares e variantes genéricas permanecem sem associação exata validada. Um nome plausível não é evidência suficiente para treinar o rótulo.
