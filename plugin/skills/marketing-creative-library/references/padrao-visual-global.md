# Padrão visual global

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Esta referência é obrigatória para toda imagem gerada pela biblioteca. Ela consolida a linguagem dos dois banners oficiais e deve ser combinada com o prompt específico da peça.

## Assinatura visual obrigatória

- Paleta predominante: vermelho intenso, preto e branco.
- Alto contraste, leitura imediata e aparência profissional para redes sociais.
- Composição moderna com linhas, blocos, cortes diagonais, overlays e formas geométricas.
- Iluminação cinematográfica com luzes focais, refletores laterais, brilhos controlados e glow sutil.
- Profundidade por fumaça, névoa, partículas ou faíscas usadas com moderação.
- Texturas esportivas ou metálicas com grunge leve e acabamento premium.
- Sensação de evento relevante, energia, movimento e grande produção.
- Nitidez alta, sem borrões, pixelização ou excesso de efeitos.

Em conteúdos esportivos, integrar atmosfera de estádio ou arena. Em aniversários, boas-vindas, conquistas e peças institucionais, adaptar o ambiente ao contexto, mas preservar paleta, geometria, contraste, luz dramática e acabamento premium. Não inserir um estádio literal quando ele prejudicar a mensagem.

## Composição

- Título ou elemento principal deve dominar a primeira leitura.
- Usar diagonais, cortes de luz ou separação energética para organizar lados, etapas ou personagens.
- Manter hierarquia clara entre título, informação secundária e detalhes.
- Reservar áreas seguras para textos, escudos, pessoas e logos.
- Evitar elementos importantes próximos das bordas.
- Preservar legibilidade em miniatura.
- Em confrontos com o CATADOS, aplicar obrigatoriamente [regras-confronto.md](regras-confronto.md): mandante à esquerda, visitante à direita e VS central.

## Tipografia

- Títulos em caixa alta, robustos, condensados e de alto impacto.
- Palavra principal pode usar lettering esportivo com pincelada, textura desgastada, grunge leve, inclinação e sublinhado dinâmico.
- Textos secundários devem usar sans-serif forte, limpa e legível.
- Subtítulos podem usar tracking alto dentro de faixa ou highlight horizontal.
- Aplicar sombra, contorno ou glow somente na intensidade necessária para contraste.
- Todo texto deve ser validado em português brasileiro antes da geração e conferido caractere por caractere depois.
- Nunca inventar nomes, datas, horários, locais, resultados ou informações.

## Escudos, marcas e pessoas

- Usar somente arquivos fornecidos ou explicitamente autorizados.
- Não redesenhar, recriar, reinterpretar, retocar, distorcer, cortar ou alterar cores e proporções.
- Permitir apenas sombra ou brilho externos que não modifiquem o conteúdo original.
- Não inventar escudos, patrocinadores, uniformes ou marcas.
- Preservar fisionomia, tom de pele e características de pessoas reais quando houver referência autorizada.

## Área de patrocinadores: duas faixas horizontais

Exceção fixa: a imagem de Busca de times visitantes não contém patrocinadores nem faixas reservadas a marcas. Usar somente o escudo original como referência de identidade e aproveitar o espaço para a mensagem. Não aplicar o bloco reutilizável de patrocinadores abaixo nessa categoria.

Aplicar as 11 logos de [patrocinadores-oficiais.md](patrocinadores-oficiais.md) em duas faixas separadas: itens 1 a 6 no topo e itens 7 a 11 na base, com uma única linha por faixa. Respeitar as exceções operacionais e mudanças solicitadas pelo usuário.

- Usar fundo branco puro #FFFFFF nas duas faixas.
- Reservar inicialmente 8% a 10% da altura para cada faixa, ajustando pela legibilidade no tamanho final.
- Posicionar o conteúdo principal entre as faixas; o título fica abaixo da faixa superior e as informações finais acima da inferior.
- Separar as faixas do conteúdo com linha ou transição discreta que não invada o fundo branco.
- Centralizar cada marca em sua célula; usar margens e espaçamento uniformes.
- Manter peso visual equivalente nas duas faixas e preservar a proporção de cada logo; centralizar o grupo de cinco sem ampliar sua escala para preencher a largura.
- Usar somente os 11 assets oficiais, exatamente uma vez cada, sem redesenhar, recolorir, filtrar ou estilizar.
- Aparar apenas espaço branco externo e bordas vazias; nunca cortar conteúdo da marca.
- Respeitar áreas seguras do canal e não sobrepor faixas a título, escudos, informações ou pessoas.
- Seguir a divisão e o dimensionamento detalhados em [patrocinadores-oficiais.md](patrocinadores-oficiais.md); não voltar a concentrar as 11 marcas no rodapé por padrão.

## Formato e qualidade

- Todo banner mestre deve usar formato 4:5 e resolução exata de 2160 × 2700.
- Não gere banner quadrado como arquivo mestre.
- Para adaptações posteriores, recompor a hierarquia; não apenas cortar ou esticar.
- Uma adaptação nunca substitui nem altera o mestre 2160 × 2700.
- Manter alta resolução, nitidez e contraste adequados ao canal.
- Gerar arte pronta para publicação quando o prompt exigir imagem final.

## Bloco reutilizável para prompts

Inclua este resumo em toda solicitação de imagem:

```text
Criar o banner mestre em formato 4:5, resolução exata 2160 × 2700. Aplicar o padrão visual global da marca: paleta vermelho, preto e branco; alto contraste; geometria moderna com diagonais, blocos e overlays; iluminação cinematográfica; glow sutil; profundidade por névoa, fumaça ou partículas moderadas; grunge leve e acabamento premium. Manter hierarquia forte, nitidez alta e leitura em miniatura. Incluir duas faixas horizontais separadas de fundo branco puro, com uma linha por faixa: itens 1 a 6 no topo e itens 7 a 11 na base, exatamente uma vez cada. Reservar inicialmente 8% a 10% da altura por faixa, ajustando pela legibilidade e pelas áreas seguras do canal. Manter título, escudos, fotos e informações entre as faixas; centralizar o grupo de cinco com escala visual equivalente ao grupo de seis. Centralizar e alinhar as marcas, preservar proporções e aparar somente espaço branco externo. Não redesenhar, recolorir, filtrar ou alterar logos, escudos ou pessoas de referência.
```
