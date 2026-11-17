# Direção artística e qualidade de animação

## O alvo visual real

Diablo II clássico combina volume de formas pré-renderizadas, materiais e textura em pequena resolução, câmera elevada oblíqua e leitura de combate. A referência não é chibi por definição e não é evidência de desenho manual pixel a pixel. O postmortem da produção e a palestra técnica de remasterização confirmam a origem 3D pré-renderizada; links em [SOURCES.md](SOURCES.md).

As folhas preservam silhuetas assimétricas, equipamento, roupas, asas, membros e gestos. A qualidade a perseguir inclui coerência entre quadros, não apenas detalhamento de uma pose. Legendas, magenta, fundo cinza e créditos pertencem à montagem da folha, não à direção artística do personagem.

## O que estudar nos arquivos concretos

| Referência | Exercício de observação | Critério de reprodução original |
|---|---|---|
| Amazon Light / Heavy | Silhueta humana e leitura do arco, town/combat | Reconhecer a mesma personagem sem copiar equipamento/desenho |
| Paladin Heavy, dois escudos | Oclusão e mudança de área do escudo | Braço, escudo e corpo permanecem coerentes em cada vista |
| Cinco Balrogs | Corpo consistente sob troca de arma | Pivô e fase corporal comparáveis, arma com volume e empunhadura |
| Rogue Parts | Dependência entre peças mínimas | Composição sem frestas, duplicação de mãos ou cabeça flutuante |
| Charsi | Atuação de profissão e gesto longo | Martelo, mão e bigorna mantêm relação causal, sem reiniciar no meio |
| Duriel / Blunderbore | Peso, centro de massa e extensão de membros | Deslocamento/impacto legíveis sem alongamento arbitrário |
| Bird / Parrot | Arco das asas e vistas | Envergadura e espessura consistentes no tempo |
| Fire Large / Small | Crescimento e ruptura das chamas | Núcleo estável, periferia dinâmica, continuidade no loop |
| Fireplace 03 | Diferença entre transição e regime contínuo | Ignição não se repete no estado aceso |
| Barracks / Cathedral | Forma modular, material e quinas | Emendas e oclusão corretas em um mapa, não só em uma folha |

## Volume, câmera e iluminação

Congele câmera e projeção por família. Não alternar câmera elevada e vista lateral dentro de uma rotação. A distância da câmera não deve mudar para encaixar uma arma mais larga: aumente o canvas comum. Se o projeto for de plataforma lateral, defina outro contrato e use estas folhas como referência de movimento/material, sem fingir que todas as vistas já servem para plataforma.

Uma fonte de luz coerente deve produzir highlights compatíveis com o giro. Diferencie metal, couro, pele, pelo, tecido e osso por contraste, forma do brilho e textura. Microdetalhe que cintila em cada frame piora leitura temporal. Na redução, compare em tamanho nativo e em zoom inteiro; uma imagem bonita a 4× pode se tornar ruído no jogo.

Não há câmera, rig, luz ou material 3D original neste repositório. Qualquer valor numérico de câmera/luz sugerido para a nova produção é uma escolha do novo projeto, não uma medição histórica.

## Movimento

Descreva cada ação por fases: repouso → antecipação → execução → recuperação. Locomoção precisa de apoio alternado dos pés, trajetória de quadril e continuidade de mãos/arma/roupa. Ataques precisam de leitura de preparação, ponto de ação e recuperação; a fase de impacto não precisa ocupar tantos frames quanto a preparação.

Não confundir quantidade com fluidez: aumentar quadros por interpolação não corrige pose impossível nem ritmo errado. Preservar contato de pé, comprimento de membros, volume do tronco e trajetória da arma tem prioridade. Em walk, medir deslocamento do pé apoiado relativo ao chão; em idle, conferir se a base oscila sem intenção.

O braço distante pode ficar ocluído e reaparecer, mas não deve trocar de identidade com o próximo. Costas não precisam mostrar o objeto carregado à frente do corpo. Simetria por espelhamento é apenas uma decisão de produção: trocar o lado da arma/escudo pode alterar a identidade.

## Fogo e outros efeitos

Nos três blocos de `Fire (Large)` são observáveis silhuetas com núcleo claro, regiões alaranjadas/escuras e pontas que se desprendem. Construa um ciclo com evolução, não uma figura laranja rígida transladada. Faça o corpo do objeto ficar fixo enquanto a chama muda; conserve a origem no chão.

Para um efeito novo, separar: emissão, núcleo, chama/energia, partículas, rastro, impacto e dissipação. O impacto pode disparar detritos do chão e luz temporária; essas são decisões do pacote futuro. Declarar explicitamente se o efeito é pintado nos frames, renderizado de simulação ou executado pela engine. Bloom/blur devem preservar silhueta e contraste; mantenha versão sem pós-processamento para diagnosticar halos.

Efeitos aditivos e sprites opacos não compartilham necessariamente o mesmo tratamento de alpha. Não eliminar preto indiscriminadamente: pode ser contorno legítimo, fundo de exportação ou parte do efeito. Criar previews sobre fundo claro, escuro e xadrez revela bordas contaminadas.

## Critérios de aprovação

Aprovar identidade estática antes de multiplicar ações. Depois aprovar um ciclo em uma vista; revisar frame a frame e em movimento; só então expandir direções e equipamento. A avaliação deve combinar:

- silhueta reconhecível e proporções estáveis;
- pivô e escala sem oscilação involuntária;
- contatos e oclusão convincentes;
- início/fim do loop sem salto;
- arma/equipamento sem desaparecimentos arbitrários;
- ação legível em tamanho nativo;
- evento de gameplay sincronizado;
- efeitos sem recorte e sem fundo residual.

Esses são critérios propostos ao projeto futuro. Não representam uma certificação de todos os quadros deste acervo.
