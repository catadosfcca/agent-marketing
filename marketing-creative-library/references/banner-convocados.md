# Banner oficial Convocados

Use este modelo para anunciar exclusivamente a lista de jogadores convocados. A peça segue [padrao-visual-global.md](padrao-visual-global.md), utiliza o escudo oficial do CATADOS e inclui o rodapé de [patrocinadores-oficiais.md](patrocinadores-oficiais.md).

## Trava anterior à geração

Antes de chamar a ferramenta de imagem:

- preencha [formulario-convocados.md](formulario-convocados.md);
- solicite o upload da FOTO_JOGADOR_DESTAQUE;
- confirme AUTORIZACAO_USO_DA_FOTO;
- confirme a grafia de todos os nomes;
- conte as linhas e valide QUANTIDADE_CONVOCADOS;
- confirme a referência do uniforme quando houver troca de roupa;
- confirme o escudo oficial e os 11 assets de patrocinadores.

Não gere enquanto houver PREENCHER, ANEXAR, autorização pendente ou divergência entre lista e quantidade.

## Prompt oficial

Substitua todos os campos {{...}} pelos valores validados do formulário. Envie somente o bloco abaixo à ferramenta de geração.

```text
Crie diretamente uma IMAGEM FINAL de convocação do CATADOS FCCA, sem explicação e sem produzir outro prompt. A peça deve parecer uma publicação oficial de um departamento de mídia esportiva de elite, com linguagem editorial original, cinematográfica, premium e profissional, sem copiar a identidade de clube, liga, marca ou campanha específica.

OBJETIVO

- Criar um pôster CONVOCADOS poderoso, prestigioso, moderno e competitivo.
- Comunicar exclusivamente a convocação do elenco.
- Dar protagonismo à foto do jogador e manter a lista perfeitamente legível em celular.

FORMATO E COMPOSIÇÃO

- Proporção {{FORMATO}}, resolução {{RESOLUCAO}}.
- Reservar o rodapé para os patrocinadores.
- Usar {{POSICAO_JOGADOR_DESTAQUE}} para o jogador em destaque, ocupando {{OCUPACAO_VISUAL_JOGADOR}} da área útil acima do rodapé.
- Posicionar a lista no lado oposto ao jogador.
- Aplicar {{COLUNAS_DA_LISTA}} colunas, escolhendo automaticamente duas ou três quando necessário para leitura.
- Criar hierarquia clara entre título, escudo, jogador, subtítulo e lista.
- Manter margens seguras e não encostar textos, rosto, escudo ou nomes nas bordas.

JOGADOR EM DESTAQUE

- Usar exatamente {{FOTO_JOGADOR_DESTAQUE}} como referência de {{NOME_JOGADOR_DESTAQUE}}.
- Preservar com máxima fidelidade rosto, estrutura facial, cabelo, barba, tom de pele, idade aparente e características distintivas.
- Preservar proporções corporais naturais; não transformar o corpo da pessoa.
- Usar postura heroica e confiante somente quando compatível com a foto fornecida.
- Aplicar recorte profissional, integração realista com o cenário, luz de recorte e tratamento cinematográfico sem modificar a identidade.
- Tratamento da roupa: {{TRATAMENTO_DO_UNIFORME}}.
- Só aplicar uniforme oficial se {{ARQUIVO_REFERENCIA_UNIFORME}} contiver um arquivo autorizado; caso contrário, manter a roupa original.
- Não inventar escudo, patrocinador ou detalhes de uniforme.

IDENTIDADE E TÍTULO

- Usar {{ARQUIVO_ESCUDO_CATADOS}} como elemento oficial de identidade.
- Não redesenhar, recriar, recolorir, filtrar ou alterar o escudo.
- Exibir {{TITULO_PRINCIPAL}} em caixa alta, com tipografia robusta, condensada e de alto impacto.
- Exibir {{SUBTITULO}} imediatamente abaixo, com sans-serif forte e tracking controlado.
- Integrar vermelho, preto e branco, geometria diagonal, glow sutil, textura metálica e grunge leve.
- O título deve ser o texto de maior destaque, seguido do subtítulo e da lista.

LISTA DE CONVOCADOS

- Inserir exatamente {{QUANTIDADE_CONVOCADOS}} jogadores:

{{LISTA_CONVOCADOS}}

- Se {{EXIBIR_NUMEROS_CAMISA}} for NÃO, mostrar somente a numeração sequencial da lista e os nomes; omitir todos os valores NÚMERO: NÃO INFORMAR.
- Se {{EXIBIR_NUMEROS_CAMISA}} for SIM, mostrar o número de camisa confirmado ao lado de cada jogador.
- Preservar grafia, acentos, espaços, hífens e apelidos exatamente como fornecidos.
- Organizar em colunas balanceadas, com espaçamento editorial e leitura confortável em tela pequena.
- Não duplicar, remover, reordenar ou inventar jogadores.

AMBIENTE E DIREÇÃO DE ARTE

- Criar estádio profissional noturno ao fundo, sem informação de partida.
- Usar refletores, gramado premium, luzes da torcida, névoa, partículas, flares e iluminação volumétrica moderada.
- Aplicar realismo fotográfico, textura de pele natural, tecido detalhado, foco nítido, profundidade de campo e gradação de cor premium.
- Preservar acabamento editorial esportivo de elite com composição original.
- Evitar excesso de efeitos, poluição visual ou perda de legibilidade.

PROIBIÇÕES ABSOLUTAS

- Não incluir adversário, escudo adversário, data, horário, local, competição, placar, resultado, VS, fixture, tabela ou card de partida.
- Não inserir nomes além da lista confirmada.
- Não alterar a pessoa fotografada nem criar uma identidade facial diferente.
- Não usar marcas ou identidades visuais de competições e empresas como imitação.

TRAVA DE TEXTO

- Reproduzir exatamente:

{{TITULO_PRINCIPAL}}
{{SUBTITULO}}
{{LISTA_CONVOCADOS}}
{{TEXTO_AREA_PATROCINADORES}}

- Conferir cada nome antes de finalizar.
- Não corrigir apelidos ou nomes próprios sem confirmação do usuário.

ÁREA DE PATROCINADORES

- Criar faixa obrigatória no rodapé com fundo branco puro #FFFFFF.
- Usar diretamente as 11 logos de {{LOGOS_PATROCINADORES}}.
- Organizar em duas linhas balanceadas: seis logos na primeira e cinco na segunda.
- Centralizar cada marca em sua célula, preservar proporções e manter margens uniformes.
- Inserir {{TEXTO_AREA_PATROCINADORES}} acima da área.
- Pode aparar somente espaço branco externo.
- Não cortar, redesenhar, recolorir, filtrar ou aplicar efeitos nas logos.

SAÍDA

- Aplicar estas observações quando houver: {{OBSERVACOES_ADICIONAIS}}.
- Gerar somente a imagem final.
- Não descrever, explicar, reescrever o prompt ou incluir conteúdo fora da arte.
```

## Controle de qualidade obrigatório

Rejeite a imagem e tente novamente somente quando:

- rosto, cabelo, barba, tom de pele ou proporções não corresponderem à foto;
- houver troca de roupa sem referência de uniforme autorizada;
- título, subtítulo ou algum nome estiver incorreto;
- quantidade exibida diferir de QUANTIDADE_CONVOCADOS;
- jogador estiver duplicado, ausente ou inventado;
- lista estiver ilegível em celular;
- aparecer adversário ou qualquer informação de partida;
- escudo estiver deformado ou alterado;
- qualquer uma das 11 logos estiver ausente, alterada ou ilegível;
- rodapé não tiver fundo branco puro.

Limite a três tentativas automáticas. Persistindo erro em rosto, nomes, escudo ou logos, pare e recomende gerar o fundo sem textos e finalizar a composição em ferramenta de design.
