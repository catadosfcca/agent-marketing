# Briefing e padrão de entrega

## Briefing mínimo

Colete ou infira, sem bloquear desnecessariamente:

| Campo | Exemplos |
| --- | --- |
| Objetivo | divulgar, convocar, celebrar, vender, informar |
| Público | torcida, jogadores, comunidade, clientes, equipe interna |
| Peça | banner, post, story, thumbnail, capa, telão |
| Canal | Instagram, LinkedIn, WhatsApp, YouTube, site, impressão |
| Mensagem | título, data, placar, CTA, nomes |
| Mando de campo | perguntar se o CATADOS é mandante ou visitante em todo confronto |
| Identidade | cores, logo, tipografia, uniforme, mascote |
| Patrocinadores | usar sempre os 11 assets de [patrocinadores-oficiais.md](patrocinadores-oficiais.md) |
| Clima | épico, divertido, premium, caloroso, competitivo |
| Materiais | fotos autorizadas, logos, mockups, referências |
| Uso de pessoa real | arquivo enviado, autorização e atributos que devem ser preservados |
| Restrições | itens obrigatórios, proibições, prazo e aprovações |

Use {{CAMPO}} para informação ausente que precisa ser substituída antes da publicação. Nunca transforme um campo não confirmado em fato.

Toda entrega deve usar [padrao-visual-global.md](padrao-visual-global.md). O padrão visual e a faixa de patrocinadores são requisitos do briefing, não opcionais, salvo pedido explícito do usuário.

O banner mestre é sempre 4:5 em 2160 × 2700. Registre outras dimensões apenas como adaptações derivadas.

Em peças de confronto, aplique [regras-confronto.md](regras-confronto.md) antes de montar o prompt. A resposta sobre mando de campo é obrigatória e define nomes e escudos à esquerda e à direita.

## Estrutura do prompt de imagem

Monte o prompt nesta sequência:

```text
Crie uma imagem publicitária para {{OBJETIVO}}, destinada a {{PÚBLICO}}.

Formato e composição: {{PROPORÇÃO/DIMENSÕES}}, {{ENQUADRAMENTO}}, com área limpa em {{POSIÇÃO}} para aplicação posterior de {{TEXTO/LOGO}}. Hierarquia visual: {{ELEMENTO 1}}, depois {{ELEMENTO 2}}, depois {{ELEMENTO 3}}.

Cena principal: {{SUJEITO, AÇÃO E AMBIENTE}}.
Direção de arte: {{ESTILO ORIGINAL}}, paleta {{CORES}}, iluminação {{LUZ}}, atmosfera {{CLIMA}}, acabamento {{TEXTURA/QUALIDADE}}.
Identidade: incorporar {{ELEMENTOS AUTORIZADOS}} de forma coerente, sem redesenhar o logo.

Padrão global: vermelho, preto e branco; alto contraste; geometria moderna; iluminação cinematográfica; grunge leve; acabamento premium; faixa branca de patrocinadores no rodapé ocupando aproximadamente 20% a 30% da altura, com as 11 logos oficiais em duas linhas balanceadas.

Não incluir texto legível, marcas inventadas, logos deformados, anatomia incorreta, elementos cortados de modo acidental, poluição visual ou informações não fornecidas.
```

Adapte o trecho não incluir texto legível apenas quando a ferramenta usada for confiável para texto e o usuário solicitar a peça final já diagramada.

## Copy e hierarquia

- Título: idealmente 2 a 7 palavras.
- Apoio: uma informação ou benefício por linha.
- CTA: curto e acionável.
- Datas, horários, placares e nomes: repetir exatamente como foram confirmados.
- Não coloque informação essencial apenas em legenda ou elemento decorativo.

## Tamanhos usuais

| Uso | Tamanho sugerido |
| --- | --- |
| Banner mestre obrigatório | 2160 × 2700 px, proporção 4:5 |

Não gere banners em outras dimensões. Quando o usuário pedir uma adaptação para outro canal, trate-a como exportação separada posterior ao banner mestre e recomponha o layout.
