# Auditoria e estado do projeto

## Base e método

Base auditada: commit `da3fd762ee2f5463e652d820e69ab1e12662aae6`, mensagem `sprites`, branch `main`. Data: 17/11/2026. A documentação e as ferramentas adicionadas depois dessa base não fazem parte da contagem de 154 arquivos originais.

Foi lida a árvore recursiva do GitHub e obtida uma cópia local. As 153 imagens foram abertas e medidas com Pillow; foram geradas pranchas de inspeção cobrindo todas as folhas. Exemplos selecionados foram examinados em resolução nativa e tiveram células medidas. O ZIP foi listado sem executar seu conteúdo. Referências oficiais e relatos/implementações primárias foram consultados para separar função no jogo de estrutura de exportação.

Não foi feita uma inspeção manual de cada pose de cada folha. Não foi recuperado o material nativo do jogo nem inferido timing de pixels. A inspeção visual global não equivale à aprovação de cada frame para treinamento.

## Resultados confirmados

- 154 arquivos: 153 imagens e um ZIP.
- 129 PNG e 24 GIF; **todos os GIFs têm um único quadro codificado**.
- 16 animais, 20 folhas de classes, 24 inimigos, 39 folhas em Npcs, 18 objetos/efeitos, 14 peças Rogue e 22 tilesets do Ato I.
- Sete classes presentes; Amazon e Sorceress não têm Medium; Paladin Heavy tem dois escudos.
- Modos RGB/RGBA/P e fundos distintos; alpha não é uniforme.
- Folhas com legendas, créditos, grades e espaços sem poses; não são atlas finais prontos.
- Layout temporal não uniforme: vistas por linha, sequências quebradas, blocos de efeitos e organização espacial de tiles.
- `Valkyrie` é invocação e `Rogue Mercenary` é aliada contratada, apesar de ambas estarem em Npcs.
- ZIP auxiliar: **49 entradas, 35 arquivos e 14 diretórios**, de projeto TypeScript/Next.js; não é pacote adicional de sprites.
- Não há recursos nativos DCC/COF/DT1/DS1 ou metadados de animação no snapshot.

Os hashes e medidas estão em [data/inventory.json](data/inventory.json), o relatório reexecutável em [data/technical-audit.json](data/technical-audit.json) e os exemplos em [../examples/layouts.json](../examples/layouts.json).

## O que foi entregue

README de entrada; catálogo de todas as imagens com uso/limites; guia de funcionamento no jogo; anatomia de frames; direção artística; pipeline de pacote original; plano de treinamento/avaliação; fontes/proveniência; auditoria reproduzível; exemplos de recorte e previews de estudo gerados por ferramenta. Os sprites originais permanecem preservados, sem alterações.

## Verificação desta entrega

As duas ferramentas foram executadas. Auditoria: 153 imagens lidas e contagens por formato/pasta conferidas. Extração: 349 células em 9 blocos e 44 grupos de vista/clipe, sem retângulos fora da origem ou células inesperadamente vazias. Recortes amostrados foram inspecionados visualmente, incluindo a diferença de tamanho do idle de Bird. Links Markdown locais foram resolvidos e os hashes de todas as imagens comparados aos originais. O timing dos previews é artificial.

## Lacunas que não devem virar suposições

| Dado | Situação | Como resolver |
|---|---|---|
| Total de poses do acervo | Não anotado integralmente | Delimitar todos os blocos e revisar células |
| Ação/vista/frame de toda folha | Parcial, exemplos executáveis | Anotação por entidade e revisão dos clipes |
| Orientação absoluta das linhas | Não confirmada | Turnaround e revisão visual; mapear ângulo explicitamente |
| Timing original por célula | Não fornecido | Recursos/tabelas da versão correspondente; não usar 100 ms de preview como verdade |
| Eventos de ataque/disparo | Não fornecidos | Evidência de lógica e reprodução específica |
| Origem e offsets nativos | Não fornecidos | Dados de exportação/nativos; ou definir contrato próprio declarado |
| Ordem de camadas Rogue | COFs não presentes | Anotar por frame/vista e validar composição |
| Conteúdo unused/cut | Nomes sugerem casos; não prova | Fonte/versionamento e confirmação de presença no jogo |
| Permissão/proveniência | Incompleta | Registrar origem e base de uso por grupo |
| Identidades genéricas | Algumas não confirmadas | Comparar com recurso nativo e fonte de função |

## Roadmap recomendado

| Marco | Entrega | Condição de conclusão |
|---|---|---|
| D0 — esta etapa | Inventário e guia de estudo | Arquivos reais cobertos, limites explícitos, ferramentas executáveis |
| D1 — anotação piloto | Bird, Rat, Charsi, uma classe, uma família inimiga, um VFX e um tileset | Todos os blocos dessas folhas com retângulos, vista, ordem e revisão |
| D2 — corpus anotado | Demais folhas e relações de variantes | Nenhuma célula de treino sem rótulo, origem e estado de qualidade |
| D3 — produção própria | Personagem original e ação piloto | Identidade e movimento aprovados com clipes e registro |
| D4 — expansão própria | Vistas, equipamento, combate e efeitos | Contratos comuns e integração funcionando |
| D5 — experiência de IA | Baselines, splits e avaliação | Melhoria demonstrada em identidades não vistas, com taxa de descarte reportada |

D0 entrega documentação e evidências, não declara D1/D2 completos ou o corpus liberado para treino. A conclusão do usuário sobre arte ou resultado futuro deve ser registrada separadamente, sem aprovações presumidas.
