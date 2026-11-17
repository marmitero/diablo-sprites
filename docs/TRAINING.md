# Guia de preparação e treinamento de IA

## Objetivo e limite do corpus

Objetivo: gerar **sprites originais com clipes coerentes**, anatomia estável, ações legíveis, vistas consistentes, equipamento e efeitos sincronizados. O objetivo não é memorizar folhas e seus créditos. O acervo pode apoiar estudo, anotação e avaliação; 153 folhas não equivalem a 153 personagens independentes nem a milhares de clipes automaticamente rotulados.

A coleção é desigual: sete classes com variantes correlacionadas, 39 folhas na categoria Npcs, fauna de escala muito pequena, peças minúsculas em canvases grandes e cenários de outro tipo. Um único treinamento indiferenciado de folha inteira aprenderia fundos, grades, textos e mistura de escalas. Preparar a base de uso/proveniência e curadoria antes de decidir um treinamento efetivo; nenhum modelo foi treinado nesta etapa.

## Unidade de dados

Um exemplo temporal deve representar uma entidade, variante, ação e vista, com frames em ordem. Manter variantes e vistas como relações do mesmo asset, não como identidades independentes. Efeitos, tiles e camadas devem ter tarefas e manifests próprios.

Campos mínimos por clipe:

| Campo | Conteúdo |
|---|---|
| Identidade | family_id, entity_id, variant_id, component_id opcional |
| Origem | source_path, source_sha256, origem/autor/extrator conhecidos, base de uso |
| Semântica | action, rótulo original, descrição, loop/one-shot, flags de incerteza |
| Espaço | view_id, ângulo confirmado ou null, canvas lógico, pivô/offsets |
| Tempo | Lista ordenada de frames, durations confirmadas ou null; eventos confirmados ou vazios |
| Qualidade | revisão visual, fundo residual, recorte, oclusão, score e observações |
| Split | grupo de família e conjunto train/val/test, atribuído após deduplicação |

O `source_asset_id` nativo permanece null se desconhecido. Não converter nome amigável em token de DCC por adivinhação. `duration_ms: null` não pode ser substituído pelo tempo artificial do preview no dataset.

## Preparação

1. Congelar snapshot, hashes e metadados; ferramentas de auditoria neste repositório ajudam a reproduzir a medição.
2. Registrar proveniência e o estado de permissão/uso por item ou grupo.
3. Separar personagens compostos, componentes, fauna, VFX, objetos e tiles.
4. Anotar retângulos e relações temporais; validar clipes, não só contagem de células.
5. Remover fundo/grade/créditos apenas nas cópias derivadas e manter mapeamento à origem. As origens permanecem intactas.
6. Definir canvas/pivô comuns por unidade e escala controlada por família; não ampliar Rat e Duriel para o mesmo corpo aparente sem declarar normalização.
7. Criar captions específicas; exemplos abaixo. Não transformar suposições em verdade de treino.
8. Detectar duplicatas exatas, poses repetidas, variantes próximas e versões do mesmo personagem.
9. Separar grupos de identidade/família antes de escolher frames para train/val/test.
10. Inspeção humana de amostras de todas as ações, vistas e componentes antes de liberar um lote.

PNG RGB pode ser convertido a RGBA como derivado, mas alpha não é conhecido por simples conversão. Para fundos exatos, uma máscara por cor pode servir em exemplos limpos; pixels contaminados/antialias demandam revisão. Preservar halos intencionais do efeito. Não usar blur para esconder máscara ruim.

## Captions úteis

- Bird: “ave pequena em voo, vista view_03, fase 2 de 8; rótulo da folha walk; direção absoluta não confirmada”.
- Rat die: “rato morto, vista view_05, pose única; não é fase 5 de uma animação de morte”.
- Charsi smith: “ferreira martelando, sequência contínua de ofício, quadro 27 de 129, vista fixa da sequência exportada”.
- Rogue Head: “componente cabeça da mesma unidade, ação/vista/fase associadas ao corpo; origem comum; não personagem inteiro”.
- Fire Large: “ciclo fire_2, fase 7 de 20, chama média desta folha, fundo removido em derivado”.

Índices ilustrativos devem apontar a coordenadas reais quando usados no dataset. Nomes do jogo servem à rastreabilidade do acervo; nos alvos de criação, preferir descrições estruturais e identidades originais.

## Evitar vazamento

Manter todas as variantes Balrog na mesma partição. Agrupar Rogue Mercenary e suas peças quando a associação for confirmada; por precaução não colocá-las em treino/teste separados como se fossem identidades independentes. Agrupar Paladin e escudos, as variantes da mesma classe, e Warriv dos dois atos. Folhas coletivas precisam ser separadas em entidades antes do split.

Separar aleatoriamente frames vizinhos faz o teste medir memorização de quase duplicatas. Dividir vistas de um mesmo personagem entre treino e teste não mede generalização para novos personagens; pode servir a uma tarefa específica de vista nova, desde que declarada e reportada separadamente. Percentuais dependem do corpus final: não prescrever 80/10/10 para um conjunto pequeno sem avaliar cobertura.

## Currículo proposto

| Marco | Tarefa | Evidência de progresso |
|---|---|---|
| T0 | Corpus anotado, auditável e com proveniência | Manifestos, amostras e exclusões justificadas |
| T1 | Identidade e vistas estáticas de personagem original | Proporção, equipamento e perspectiva estáveis |
| T2 | Idle e walk em uma vista | Contato de pés, loop e ausência de flicker |
| T3 | Mesmas ações em múltiplas vistas | Geometria/oclusão consistentes entre vistas |
| T4 | Attack, hurt, death e cast | Fases claras e eventos sincronizados |
| T5 | Troca de equipamento / peças | Corpo e pivô preservados, ordem de desenho correta |
| T6 | Efeitos e objetos com transições | Spawn/loop/dissipação coerentes e sem recorte |
| T7 | Integração de unidade e cenário | Teste em engine e avaliação cega em escala nativa |

Começar com baseline controlável: produção própria com rig/câmera e sequência de referência, ou pipeline de geração condicionado por pose, vista e identidade. Comparar geração independente com geração temporal condicionada no mesmo conjunto. A escolha de arquitetura, checkpoint e hardware depende de requisitos ainda não definidos; não há justificativa aqui para prescrever um modelo como solução comprovada.

## Avaliação

Usar personagens/famílias de teste que não estejam no treino. Avaliar cada vista e ação, além da média. Comparar com um baseline e registrar taxa de descarte, correções manuais e custo por clipe aprovado.

- Identidade: rosto/silhueta/roupa/arma estáveis durante a sequência e entre vistas.
- Anatomia: comprimentos, volume e articulações sem variações inexplicáveis.
- Temporal: flicker, duplicação, salto no loop, contato de pé e trajetória de arma.
- Modularidade: emendas, oclusão correta e alinhamento de peças.
- Efeito: continuidade, expansão/dissipação, alpha e vínculo ao ponto de emissão.
- Uso no jogo: pivô, eventos, colisão definida separadamente e comportamento de estados.
- Generalização: personagem novo, combinação nova de equipamento e ação nova, reportados como tarefas distintas.

Métricas de diferença entre pixels/fluxo podem ajudar a detectar outliers, mas não devem penalizar movimento legítimo nem substituir revisão perceptiva. Distância visual a uma imagem de referência não mede sozinha qualidade de animação. Não declarar sucesso porque o modelo reproduziu um frame conhecido.

## O que não ensinar como regra

Número universal de frames; oito direções em toda entidade; morte sempre animada; arma sempre visível; loop em todo efeito; cinza/magenta como estilo; as mesmas dimensões para todos os corpos; nome de pasta como classe de gameplay; todo animal como inimigo; todos os sprites como conteúdo efetivamente usado no lançamento.

Próximo passo verificável: completar a anotação de um pequeno conjunto de famílias com funções diferentes, publicar clipes e revisar rótulos antes de aumentar o volume. O contrato deve ser o mesmo para dados próprios e referências, permitindo substituir gradualmente o corpus por produção original controlada.
