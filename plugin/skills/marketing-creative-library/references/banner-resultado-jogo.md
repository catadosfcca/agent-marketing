# Banner oficial Resultado do Jogo

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Use este modelo para publicar o resultado final mantendo a mesma linguagem visual do [banner oficial de anúncio](banner-oficial-jogo.md), de [padrao-visual-global.md](padrao-visual-global.md) e as duas faixas de [patrocinadores-oficiais.md](patrocinadores-oficiais.md).

## Trava anterior à geração

Antes de chamar a ferramenta de imagem:

- preencha [formulario-resultado-jogo.md](formulario-resultado-jogo.md);
- pergunte obrigatoriamente se o CATADOS F.C.C.A. é mandante ou visitante;
- aplique [regras-confronto.md](regras-confronto.md) para nomes, escudos, placares e autores dos gols;
- confirme o placar final com o usuário;
- calcule RESULTADO_CATADOS a partir do placar;
- confirme que TITULO_PRINCIPAL e PALAVRA_DESTAQUE correspondem ao resultado;
- confira se a contagem dos autores dos gols corresponde ao placar de cada time;
- confirme a imagem de referência, o escudo adversário e os assets oficiais.

Não gere enquanto houver PREENCHER, DEFINIR APÓS RESPOSTA, informação contraditória ou arquivo obrigatório ausente.

## Envio obrigatório dos arquivos à ferramenta

Antes da geração, executar [envio de assets](envio-de-assets.md) e anexar a prancha oficial com escudo e patrocinadores no campo real de entrada de imagens da ferramenta. Os caminhos nas variáveis deste prompt não substituem anexos. A prancha identifica as marcas; aplicar seis no topo, cinco na base e o escudo na área central prevista neste modelo. Se os arquivos não puderem ser enviados, informar a limitação em vez de entregar um banner sem as marcas.

## Prompt oficial

Substitua todos os campos {{...}} pelo formulário validado e envie somente o bloco abaixo à ferramenta de geração.

```text
Crie diretamente uma IMAGEM FINAL de resultado de jogo, sem explicação e sem produzir outro prompt. Preserve exatamente a composição, linguagem visual, hierarquia, cores e acabamento do banner oficial usado como referência em {{IMAGEM_DE_REFERENCIA}}.

ESTRUTURA GERAL

- Layout vertical {{FORMATO}}, resolução exata {{RESOLUCAO}}.
- Arte esportiva profissional, moderna, impactante e dramática.
- Atmosfera de estádio lotado à noite.
- Paleta vermelho, preto e branco.
- Fundo abstrato geométrico com linhas, blocos, cortes diagonais e overlays.
- Luzes focais, refletores laterais, névoa cinematográfica, fumaça, partículas e faíscas moderadas.
- Textura metálica, grunge leve, alto contraste, glow sutil e nitidez elevada.
- Manter a mesma identidade do banner de anúncio, substituindo o confronto futuro pelo resultado final.

TÍTULO

- Texto principal: {{TITULO_PRINCIPAL}}.
- Subtítulo: {{SUBTITULO}}.
- Palavra de maior destaque: {{PALAVRA_DESTAQUE}}.
- Usar a mesma tipografia robusta, condensada, inclinada e esportiva do banner oficial.
- Aplicar textura desgastada, contorno escuro, brilho vermelho, sombra suave e sublinhado dinâmico.
- O título deve dominar a primeira leitura e refletir corretamente {{RESULTADO_CATADOS}}.

ÁREA CENTRAL, ESCUDOS E PLACAR

- Inserir os dois escudos originais na mesma área central do banner oficial.
- À esquerda: {{TIME_ESQUERDA}}, usando {{ARQUIVO_ESCUDO_ESQUERDA}}.
- À direita: {{TIME_DIREITA}}, usando {{ARQUIVO_ESCUDO_DIREITA}}.
- Confirmar que o CATADOS está à esquerda quando mandante e à direita quando visitante.
- Exibir o placar central em grande destaque: {{PLACAR_ESQUERDA}} × {{PLACAR_DIREITA}}.
- Usar números grandes, robustos, muito legíveis e com acabamento metálico esportivo.
- Manter o símbolo × centralizado entre os números.
- Usar corte de luz, energia ou raio separando os lados sem prejudicar a leitura.
- Preservar integralmente cores, tipografia, contornos e proporções dos escudos.
- Não redesenhar, recriar, retocar, filtrar ou alterar os arquivos.

AUTORES DOS GOLS

- Abaixo do time esquerdo, exibir GOLS: {{AUTORES_GOLS_ESQUERDA}}.
- Abaixo do time direito, exibir GOLS: {{AUTORES_GOLS_DIREITA}}.
- Usar blocos simétricos, legíveis e alinhados com o respectivo escudo.
- Manter cada autor associado ao lado correto.
- Quando o valor for NÃO INFORMAR, omitir somente o bloco daquele time.
- Quando o valor for NENHUM, usar um traço discreto no lugar dos nomes.
- Preservar grafia, acentos e multiplicadores como Nome (2).
- Não inventar atletas nem redistribuir gols.

TRAVA ABSOLUTA DE TEXTO

- Reproduzir exatamente os dados validados:

{{TITULO_PRINCIPAL}}
{{SUBTITULO}}
{{TIME_ESQUERDA}}
{{PLACAR_ESQUERDA}} × {{PLACAR_DIREITA}}
{{TIME_DIREITA}}
GOLS: {{AUTORES_GOLS_ESQUERDA}}
GOLS: {{AUTORES_GOLS_DIREITA}}
{{DATA_E_DIA}}
{{HORARIO}}
{{LOCAL}}
{{ENDERECO}}
{{COMPETICAO}}
{{TEXTO_AREA_PATROCINADORES}}

- Omitir apenas os blocos autorizados como NÃO INFORMAR.
- Não trocar letras, números, lados, acentos, pontuação ou nomes.
- Não repetir o placar com valores diferentes.

INFORMAÇÕES DO JOGO

- Exibir {{DATA_E_DIA}}, {{HORARIO}}, {{LOCAL}}, {{ENDERECO}} e {{COMPETICAO}} em uma faixa organizada no conteúdo central, acima da faixa inferior de patrocinadores.
- Usar ícones discretos de calendário, relógio e localização.
- Manter leitura clara sem competir com título, placar ou autores dos gols.
- Aplicar esta observação de resultado quando houver: {{OBSERVACAO_RESULTADO}}.

ÁREA DE PATROCINADORES

- Criar duas faixas horizontais separadas com fundo branco puro #FFFFFF: uma no topo e outra na base.
- Usar diretamente as 11 logos de {{LOGOS_PATROCINADORES}}.
- Usar uma única linha em cada faixa: itens 1 a 6 no topo e itens 7 a 11 na base, na ordem da biblioteca, sem duplicar marcas. Reservar inicialmente 8% a 10% da altura para cada faixa, ajustando pela legibilidade e área segura do formato.
- Centralizar cada marca em sua célula, com margens uniformes.
- Equalizar altura visual sem distorcer proporções.
- Quando preenchido, inserir {{TEXTO_AREA_PATROCINADORES}} uma única vez, imediatamente acima da faixa inferior, sem sobrepor as marcas.
- Pode aparar somente espaço branco externo e bordas vazias.
- Não cortar, redesenhar, recolorir, filtrar, estilizar ou aplicar efeitos nas logos.

SAÍDA

- Aplicar estas observações adicionais quando houver: {{OBSERVACOES_ADICIONAIS}}.
- Gerar somente a imagem final.
- Não descrever, explicar, reescrever o prompt ou incluir conteúdo fora da arte.
```

## Validação do resultado

- Se PLACAR_CATADOS > PLACAR_ADVERSARIO, RESULTADO_CATADOS deve ser VITÓRIA.
- Se PLACAR_CATADOS = PLACAR_ADVERSARIO, RESULTADO_CATADOS deve ser EMPATE.
- Se PLACAR_CATADOS < PLACAR_ADVERSARIO, RESULTADO_CATADOS deve ser DERROTA.
- Título e palavra de destaque devem respeitar esse cálculo.
- A soma dos autores deve corresponder ao placar, considerando Nome (2) como dois gols.
- Se houver disputa por pênaltis, prorrogação ou gol contra, descreva em OBSERVACAO_RESULTADO e confirme com o usuário antes de gerar.

## Controle de qualidade obrigatório

Rejeite a imagem e tente novamente apenas quando:

- título ou destaque contradizer o placar;
- algum número do placar estiver incorreto ou associado ao time errado;
- autor de gol estiver ausente, inventado, duplicado ou do lado errado;
- contagem dos autores não corresponder ao placar;
- CATADOS estiver à direita como mandante ou à esquerda como visitante;
- escudo estiver deformado, alterado, trocado ou cortado;
- qualquer uma das 11 logos estiver ausente, alterada ou ilegível;
- uma das duas faixas não tiver fundo branco puro ou as marcas não estiverem distribuídas em 6 no topo e 5 na base;
- texto estiver incorreto, ilegível ou fora da área segura.

Limite a três tentativas automáticas. Persistindo erro em texto, placar, escudos ou logos, pare e recomende gerar somente o fundo para finalização em ferramenta de design.
