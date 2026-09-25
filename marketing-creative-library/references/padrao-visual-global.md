# Padrão visual global

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

## Área obrigatória de patrocinadores

Toda peça deve conter uma faixa horizontal exclusiva no rodapé com as 11 logos de [patrocinadores-oficiais.md](patrocinadores-oficiais.md).

- Usar fundo sempre branco puro #FFFFFF.
- Reservar aproximadamente 20% a 30% da altura, ampliando quando necessário para manter todas as marcas legíveis.
- Em peças quadradas ou verticais, organizar em duas linhas balanceadas: seis logos na primeira e cinco na segunda.
- Separar a faixa do conteúdo principal com linha ou transição discreta que não invada o fundo branco.
- Centralizar cada marca em sua célula, com margens e espaçamento uniformes.
- Equalizar altura visual e preservar a proporção de cada logo.
- Usar somente os 11 assets oficiais, sem redesenhar, recolorir, filtrar ou estilizar.
- Pode aparar apenas espaço branco externo e bordas vazias durante a composição; nunca cortar conteúdo da marca.
- Nunca sobrepor a faixa ao título, informações principais, escudos ou pessoas.

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
Criar o banner mestre em formato 4:5, resolução exata 2160 × 2700. Aplicar o padrão visual global da marca: paleta vermelho, preto e branco; alto contraste; geometria moderna com diagonais, blocos e overlays; iluminação cinematográfica; glow sutil; profundidade por névoa, fumaça ou partículas moderadas; grunge leve e acabamento premium. Manter hierarquia forte, nitidez alta e leitura em miniatura. Incluir no rodapé uma faixa de fundo branco puro, ocupando aproximadamente 20% a 30% da altura, com as 11 logos oficiais em duas linhas balanceadas, seis na primeira e cinco na segunda. Centralizar e alinhar as marcas, preservar proporções e aparar somente espaço branco externo. Não redesenhar, recolorir, filtrar ou alterar logos, escudos ou pessoas de referência.
```
