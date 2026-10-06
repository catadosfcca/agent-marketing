# Banner oficial Próxima Partida

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Use este modelo para anunciar o próximo jogo em estilo matchday. Primeiro preencha [formulario-proxima-partida.md](formulario-proxima-partida.md).

Este modelo é uma aplicação integral de [padrao-visual-global.md](padrao-visual-global.md).

## Trava anterior à geração

Antes de chamar a ferramenta de imagem:

- pergunte obrigatoriamente: O CATADOS F.C.C.A. é mandante ou visitante nesta partida?;
- aplique [regras-confronto.md](regras-confronto.md) e só depois preencha TIME_1 e TIME_2;
- confirme que MANDO_DE_CAMPO_CATADOS não está como PREENCHER e nenhum lado está como DEFINIR APÓS RESPOSTA;
- confirme que todos os campos obrigatórios foram preenchidos;
- valide DATA_E_DIA usando ANO_PARA_VALIDACAO;
- confirme que a data completa é futura;
- confirme o anexo da imagem-modelo e dos dois escudos;
- confirme a disponibilidade dos 11 assets de [patrocinadores-oficiais.md](patrocinadores-oficiais.md).

Não gere se qualquer validação falhar. Peça somente os dados ou anexos faltantes.

## Transmissão da partida

Aplicar [transmissão Catados TV](transmissao-catados-tv.md). Perguntar **Vai ter transmissão?** junto com os dados faltantes, somente quando o usuário ainda não tiver informado. Validar VAI_TER_TRANSMISSAO como SIM ou NÃO antes de gerar. Com SIM, preparar TEXTO_TRANSMISSAO: AO VIVO NO YOUTUBE · CATADOS TV; com NÃO, deixá-lo vazio e omitir a chamada. Não exigir link.

## Envio obrigatório dos arquivos à ferramenta

Antes da geração, executar [envio de assets](envio-de-assets.md) e anexar a prancha oficial com escudo e patrocinadores no campo real de entrada de imagens da ferramenta. Os caminhos nas variáveis deste prompt não substituem anexos. A prancha identifica as marcas; aplicar seis no topo, cinco na base e o escudo na área central prevista neste modelo. Se os arquivos não puderem ser enviados, informar a limitação em vez de entregar um banner sem as marcas.

## Prompt oficial

Substitua cada campo {{...}} pelo valor correspondente do formulário. Depois envie somente o conteúdo do bloco à ferramenta de geração.

```text
TRAVA DE EXECUÇÃO OBRIGATÓRIA

- Gerar diretamente a IMAGEM FINAL.
- Não explicar nem reescrever este prompt.
- Não gerar instruções adicionais.
- Não alterar a estrutura solicitada.
- Saída final: apenas a imagem.

OBJETIVO

Criar uma arte esportiva profissional no estilo pôster de divulgação de partida, matchday, baseada em {{IMAGEM_MODELO}}, com visual moderno, impactante e atmosfera de estádio.

CONTEÚDO PERSONALIZADO

- Título: {{TITULO_PRINCIPAL}}.
- Time 1: {{TIME_1}}.
- Escudo do Time 1: usar exatamente {{ARQUIVO_ESCUDO_TIME_1}}.
- Time 2: {{TIME_2}}.
- Escudo do Time 2: usar exatamente {{ARQUIVO_ESCUDO_TIME_2}}.
- Dia da partida: {{DATA_E_DIA}}.
- Horário: {{HORARIO}}.
- Local: {{LOCAL}}.
- Competição: {{COMPETICAO}}.
- Patrocinadores: usar somente {{ARQUIVOS_LOGOS_PATROCINADORES}}.

DIREÇÃO DE ARTE

- Estilo esportivo profissional de futebol, com atmosfera de estádio.
- Fundo abstrato com formas geométricas modernas: linhas, blocos, cortes diagonais e overlays.
- Paleta principal: {{CORES_PRINCIPAIS}}, com alto contraste.
- Integrar discretamente luzes e atmosfera de estádio ao fundo, preservando o estilo abstrato.
- Iluminação de alto contraste, luzes focais, brilhos intensos e névoa cinematográfica leve.
- Textura grunge sutil com acabamento premium moderno.
- Clima épico de final de uma grande competição, sem copiar a identidade visual de liga, clube ou campanha específica.

TÍTULO E DEMAIS TEXTOS

- {{TITULO_PRINCIPAL}} deve ser o elemento de maior destaque visual.
- Usar fonte impactante, forte, moderna, grande e legível.
- Aplicar estilo cinematográfico, épico e imponente, com glow sutil e alto contraste.
- Posicionar {{TIME_1}} abaixo ou próximo do escudo esquerdo.
- Posicionar {{TIME_2}} abaixo ou próximo do escudo direito.
- Inserir VS centralizado e destacado entre os escudos.
- Exibir {{HORARIO}} e {{LOCAL}} com leitura imediata.
- Exibir {{COMPETICAO}} quando o campo estiver preenchido.
- Manter padrão tipográfico cinematográfico e premium em todas as informações.

TRAVA DE TEXTO

- Reproduzir exatamente os valores já validados do formulário.
- Não trocar letras, remover acentos, inventar palavras ou acrescentar informações.
- O conteúdo textual da arte deve ser:

{{TITULO_PRINCIPAL}}
{{TIME_1}}
VS
{{TIME_2}}
{{DATA_E_DIA}}
{{HORARIO}} | {{LOCAL}}
{{COMPETICAO}}
{{TEXTO_TRANSMISSAO}}

- Omitir COMPETICAO quando o campo estiver vazio e TEXTO_TRANSMISSAO quando VAI_TER_TRANSMISSAO for NÃO. A chamada de transmissão é texto autorizado somente com SIM.
- Conferir caractere por caractere antes de finalizar.

TRANSMISSÃO — CHAMADA CONDICIONAL

- Status confirmado da transmissão: {{VAI_TER_TRANSMISSAO}}. Esse status é controle interno e não aparece na imagem.
- Se SIM, reproduzir exatamente {{TEXTO_TRANSMISSAO}} uma única vez em um selo compacto e legível, abaixo das informações do jogo e acima da faixa inferior de patrocinadores.
- Se NÃO, omitir completamente a chamada, inclusive selo ou ícone de live. Omitir TEXTO_TRANSMISSAO vazio sem mostrar placeholders.
- A chamada faz parte do texto autorizado da arte somente quando a transmissão estiver confirmada.
- Não inventar link, canal, @handle, horário da transmissão ou QR code; não inserir a pergunta do briefing na imagem.
- Preservar a hierarquia do confronto e não cobrir escudos, data, horário ou patrocinadores.

ÁREA DE PATROCINADORES

- Criar duas faixas horizontais separadas com fundo branco puro #FFFFFF: uma no topo e outra na base.
- Usar diretamente as 11 logos de {{ARQUIVOS_LOGOS_PATROCINADORES}}.
- Usar uma única linha em cada faixa: itens 1 a 6 no topo e itens 7 a 11 na base, na ordem da biblioteca, sem duplicar marcas. Reservar inicialmente 8% a 10% da altura para cada faixa, ajustando pela legibilidade e área segura do formato.
- Centralizar cada logo em sua célula, com margens e espaços uniformes.
- Equalizar a altura visual sem distorcer proporções.
- Dar boa visibilidade sem competir com o título.
- Pode aparar somente espaço branco externo e bordas vazias.
- Não cortar qualquer parte da marca.
- Não distorcer, redesenhar, recolorir, filtrar ou estilizar logos.

TRAVAS DOS ESCUDOS E LOGOS

- Não redesenhar, alterar, recriar ou estilizar os escudos.
- Não aplicar filtros, distorções ou efeitos que modifiquem os escudos.
- Usar exatamente os arquivos anexados.
- Não cortar partes importantes dos escudos ou logos.
- Permitir somente sombra ou brilho externos que não alterem o conteúdo dos arquivos.
- Não inventar patrocinadores, emblemas, nomes ou informações.

FORMATO E QUALIDADE

- Proporção: {{FORMATO}}.
- Resolução exata: {{RESOLUCAO}}.
- Alta nitidez, sem borrões, pixelização ou artefatos.
- Composição pronta para publicação em redes sociais.
- Respeitar áreas seguras e não encostar textos, escudos ou logos nas bordas.
- Aplicar estas observações quando houver: {{OBSERVACOES_ADICIONAIS}}.

RESULTADO FINAL

Entregar uma arte esportiva moderna, cinematográfica e épica, com fundo abstrato geométrico na paleta indicada, atmosfera de grande decisão, escudos e logos originais intactos, tipografia premium em português e duas faixas profissionais de patrocinadores, seis no topo e cinco na base.

Gerar somente a imagem final. Não descrever, não explicar, não criar outro prompt e não incluir conteúdo fora da arte.
```

## Controle de qualidade

Rejeite a imagem e tente novamente somente quando:

- qualquer texto divergir do formulário validado;
- a chamada de transmissão faltar com SIM, aparecer com NÃO, estiver duplicada ou indicar plataforma/canal incorretos;
- a data for passada ou não corresponder ao dia da semana;
- os times ou escudos estiverem trocados;
- escudo ou logo tiver sido deformado, reinterpretado ou cortado;
- o CATADOS estiver à direita como mandante ou à esquerda como visitante;
- alguma das 11 logos estiver ausente, alterada, ilegível ou fora de ordem;
- uma das duas faixas não tiver fundo branco puro ou as marcas não estiverem distribuídas em 6 no topo e 5 na base;
- aparecer patrocinador não fornecido;
- houver texto extra, ilegível ou fora da área segura;
- a resolução ou a proporção estiver incorreta.

Limite a três tentativas automáticas. Se texto, escudos ou logos continuarem incorretos, pare e recomende gerar apenas o fundo para finalização em ferramenta de design.
