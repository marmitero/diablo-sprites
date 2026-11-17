# Lycan — identidade e função

Classe original solicitada em 17/11/2026. Um lobisomem bípede atlético, de combate próximo, desenvolvido por síntese visual orientada por contrato. Não é uma extração da forma de lobisomem do Druid, não é um sprite oficial e não reutiliza o corpo de um inimigo do acervo.

## Identidade visual v1

- Pelagem castanho-carvão, abdômen castanho e juba cinza-prateada sobre pescoço/ombros.
- Focinho lupino comprido, olhos âmbar discretos e orelhas pontudas.
- Tórax forte, braços compridos e mãos articuladas com garras, sem transformar o corpo em gorila.
- Pernas digitígradas: joelho e jarrete distintos, apoio nas patas e dedos; não encurtar a perna distante.
- Uma cauda curta e espessa, ocluída pelo corpo quando apropriado.
- Tanga de couro rasgada e cinto simples; sem armadura, joias ou arma empunhada.
- Acabamento de fantasia sombria com material e volume inspirados no estudo de sprites pré-renderizados.

Essa identidade é uma proposta visual v1, sem aprovação do usuário presumida. A folha de identidade é mais detalhada e maior que um sprite nativo do acervo; as folhas de movimento são estudos raster do mesmo personagem. O método utilizado não recriou o pipeline original de 3D Studio Max nem contém rig 3D.

## Função jogável proposta

| Elemento | Comportamento a implementar em um jogo futuro | Representação |
|---|---|---|
| Garras | Ataque principal de alcance curto | Antecipação de ombro, giro de tronco, arco da mão e recuperação |
| Mordida | Ataque mais comprometido, com avanço curto | Recuo de cabeça, avanço do focinho e retorno; evitar esticar pescoço |
| Uivo | Habilidade de área/fortalecimento, regra a definir | Peito expande, cabeça sobe, mandíbula abre, gesto termina |
| Corrida | Locomoção mais agressiva que walk | Inclinação do corpo e passada mais ampla |
| Hit | Reação breve a dano | Recuo de tórax preservando a anatomia |
| Death | Derrota e corpo final | Perda de apoio, queda e pose final sem reinício automático |

Não foram inventados valores de dano, custo, cooldown ou balanceamento como se viessem do Diablo II. A classe não está integrada a uma engine: são assets e especificação de comportamento. Um futuro recurso de ferocidade pode controlar ataques e uivo, mas fica fora da arte/contrato já desenhados.

## Adaptação, não reskin

O Lycan usa as próprias garras como arma; não deve manter o balanço de espada de um Barbarian nem a anatomia plantígrada de um humano. A marcha exige relação correta entre quadril, joelho, jarrete e pata. O tronco inclina levemente, a cabeça equilibra o corpo, e mãos/cauda acompanham a passada. A juba é movimento secundário, não uma massa que muda de tamanho a cada quadro.

Nas costas, não desenhar focinho/peitoral atravessando o corpo. O braço distante pode desaparecer por oclusão sem perder comprimento. A cauda não deve duplicar ao girar. Marcas de pelo, cinto, tanga e massa de ombros devem permanecer reconhecíveis entre vistas.
