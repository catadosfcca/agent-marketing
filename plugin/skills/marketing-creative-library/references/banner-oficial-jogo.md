# Banner oficial de anúncio de jogo

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Este é o modelo da opção Divulgação de jogo — TEM CATADOS EM CAMPO do menu. Usar TEM CATADOS EM CAMPO como título padrão, salvo outro título explicitamente pedido. Este é o modelo prioritário para anunciar partidas. Ele gera uma arte final quadrada com texto incorporado.

Este modelo é uma aplicação integral de [padrao-visual-global.md](padrao-visual-global.md).

## Dados e anexos obrigatórios

Primeiro preencha [formulario-banner-jogo.md](formulario-banner-jogo.md). Cada campo do formulário corresponde diretamente a uma variável deste prompt.

Antes de preencher os lados, pergunte obrigatoriamente: **O CATADOS F.C.C.A. é mandante ou visitante nesta partida?** Aplique [regras-confronto.md](regras-confronto.md).

Não execute a geração se MANDO_DE_CAMPO_CATADOS não estiver confirmado, se algum lado ainda estiver como DEFINIR APÓS RESPOSTA, se houver divergência entre data e dia da semana, se algum campo obrigatório estiver vazio ou se a referência visual e os dois escudos não tiverem sido anexados. Não extraia escudos de pesquisa na internet e não os recrie.

## Transmissão da partida

Aplicar [transmissão Catados TV](transmissao-catados-tv.md). Perguntar **Vai ter transmissão?** junto com os dados faltantes, somente quando o usuário ainda não tiver informado. Validar VAI_TER_TRANSMISSAO como SIM ou NÃO antes de gerar. Com SIM, preparar TEXTO_TRANSMISSAO: AO VIVO NO YOUTUBE · CATADOS TV; com NÃO, deixá-lo vazio e omitir a chamada. Não exigir link.

## Envio obrigatório dos arquivos à ferramenta

Antes da geração, executar [envio de assets](envio-de-assets.md) e anexar a prancha oficial com escudo e patrocinadores no campo real de entrada de imagens da ferramenta. Os caminhos nas variáveis deste prompt não substituem anexos. A prancha identifica as marcas; aplicar seis no topo, cinco na base e o escudo na área central prevista neste modelo. Se os arquivos não puderem ser enviados, informar a limitação em vez de entregar um banner sem as marcas.

## Prompt oficial

Substitua todos os campos {{...}} pelos valores do formulário antes de enviar à ferramenta. Não altere a grafia preenchida pelo usuário. O bloco de copy aparece apenas uma vez para impedir informações conflitantes.

```text
Crie uma IMAGEM finalizada, sem texto explicativo e sem produzir outro prompt: uma arte esportiva profissional no estilo de card oficial de convocação para jogo de futebol society, seguindo a referência {{IMAGEM_DE_REFERENCIA}}.

ESTRUTURA GERAL

- Layout vertical {{FORMATO}}, resolução exata {{RESOLUCAO}}.
- Aparência de altíssima resolução, extremamente nítida.
- Estilo moderno, impactante e dramático.
- Atmosfera de estádio lotado à noite.
- Iluminação forte com refletores laterais.
- Fundo em tons de vermelho e preto, com fumaça, partículas e faíscas.
- Rachadura ou corte de luz no centro, dividindo os times.
- Bola de futebol em destaque na parte inferior.
- Alto contraste, nitidez elevada e glow sutil.
- Resultado visual finalizado e pronto para postagem.

TÍTULO E HIERARQUIA

- Texto principal no alto da área central, abaixo da faixa superior de patrocinadores: {{TITULO_PRINCIPAL}}.
- Subtítulo logo abaixo: {{SUBTITULO}}.
- {{PALAVRA_DESTAQUE}} deve receber o maior destaque.
- As demais palavras do título devem ser secundárias.
- {{SUBTITULO}} deve ser terciário, porém destacado em faixa horizontal.
- Tipografia principal em caixa alta, extremamente robusta e condensada.
- Em {{PALAVRA_DESTAQUE}}, usar lettering com aparência de pincelada esportiva agressiva, textura desgastada e grunge nas letras, sem copiar uma fonte ou campanha protegida específica.
- Aplicar leve inclinação para sensação de movimento.
- Usar vermelho intenso, variações de brilho, sombras internas e contorno escuro sutil.
- Aplicar glow vermelho, arranhões, partículas e um sublinhado dinâmico em pincel sob {{PALAVRA_DESTAQUE}}.
- As palavras secundárias em fonte sans-serif forte e mais limpa, branca ou cinza-claro.
- {{SUBTITULO}} em caixa alta, com tracking alto, dentro de faixa ou destaque horizontal.
- Aplicar efeito 3D discreto e sombra projetada suave.

TRAVA ABSOLUTA DE TEXTO

- Todos os textos devem estar corretos em português brasileiro.
- Não trocar letras, omitir acentos, alterar pontuação, abreviar ou acrescentar informações.
- Reproduzir exatamente o bloco abaixo, mantendo a mesma grafia:

{{TITULO_PRINCIPAL}}
{{SUBTITULO}}
{{DATA_E_DIA}}
{{HORARIO}}
{{LOCAL}}
{{ENDERECO}}
{{TEXTO_TRANSMISSAO}}
{{TEXTO_AREA_PATROCINADORES}}

- Omitir TEXTO_TRANSMISSAO quando VAI_TER_TRANSMISSAO for NÃO; não imprimir uma linha vazia ou placeholder.
- Conferir visualmente cada linha antes de finalizar.
- Não repetir data, horário, local ou endereço em outra parte da arte.

ÁREA CENTRAL E ESCUDOS

- Inserir os dois escudos originais anexados no centro.
- À esquerda: {{TIME_ESQUERDA}}, usando {{ARQUIVO_ESCUDO_ESQUERDA}}.
- À direita: {{TIME_DIREITA}}, usando {{ARQUIVO_ESCUDO_DIREITA}}.
- Confirmar que o CATADOS está à esquerda quando mandante e à direita quando visitante.
- Inserir VS luminoso no centro.
- Adicionar energia ou raio dividindo os escudos.
- Manter proporção original e alta qualidade.
- Não redesenhar, recriar, reinterpretar, retocar ou completar os escudos.
- Não alterar cores, tipografia, contornos, proporções ou conteúdo interno.
- Não aplicar filtros que modifiquem o design.
- Usar exatamente os arquivos anexados.
- Somente efeitos externos de sombra e brilho são permitidos, sem alterar os pixels internos dos escudos.

INFORMAÇÕES DO JOGO

- Data e dia: {{DATA_E_DIA}}.
- Horário: {{HORARIO}}.
- Local: {{LOCAL}}.
- Endereço: {{ENDERECO}}.
- Mostrar ícone de calendário ao lado da data.
- Mostrar ícone de relógio ao lado do horário.
- Mostrar ícone de localização ao lado do campo.
- Usar tipografia esportiva, moderna, forte e legível.
- Destacar o horário em vermelho.
- Destacar o nome do campo em caixa ou faixa.
- Manter todas as informações dentro da área segura e separadas visualmente dos escudos.

TRANSMISSÃO — CHAMADA CONDICIONAL

- Status confirmado da transmissão: {{VAI_TER_TRANSMISSAO}}. Esse status é controle interno e não aparece na imagem.
- Se SIM, reproduzir exatamente {{TEXTO_TRANSMISSAO}} uma única vez em um selo compacto e legível, abaixo das informações do jogo e acima da faixa inferior de patrocinadores.
- Se NÃO, omitir completamente a chamada, inclusive selo ou ícone de live. Omitir TEXTO_TRANSMISSAO vazio sem mostrar placeholders.
- A chamada faz parte do texto autorizado da arte somente quando a transmissão estiver confirmada.
- Não inventar link, canal, @handle, horário da transmissão ou QR code; não inserir a pergunta do briefing na imagem.
- Preservar a hierarquia do confronto e não cobrir escudos, data, horário ou patrocinadores.

ÁREA DE PATROCINADORES

- Criar duas faixas horizontais separadas com fundo branco puro #FFFFFF: uma no topo e outra na base.
- Usar as 11 logos de {{LOGOS_PATROCINADORES}} diretamente dos assets oficiais.
- Usar uma única linha em cada faixa: itens 1 a 6 no topo e itens 7 a 11 na base, na ordem da biblioteca, sem duplicar marcas. Reservar inicialmente 8% a 10% da altura para cada faixa, ajustando pela legibilidade e área segura do formato.
- Centralizar cada logo em sua célula, com espaços e margens uniformes.
- Equalizar a altura visual e preservar a proporção de cada arquivo.
- Quando preenchido, inserir {{TEXTO_AREA_PATROCINADORES}} uma única vez, imediatamente acima da faixa inferior, sem sobrepor as marcas.
- Pode aparar somente áreas brancas externas e bordas vazias para centralizar e ampliar as logos.
- Não cortar conteúdo colorido, textos, símbolos, telefones ou elementos das marcas.
- Não redesenhar, recolorir, filtrar, estilizar ou aplicar efeitos nas logos.
- Manter título e informações do jogo entre as faixas, sem sobreposição.
- Manter alinhamento e proporções profissionais.

ESTILO VISUAL

- Paleta predominante: vermelho, preto e branco.
- Texturas metálicas e esportivas.
- Sensação de evento grande e decisivo.
- Visual profissional de mídia esportiva.
- Iluminação cinematográfica.
- Não inserir marcas d'água, patrocinadores fictícios, pessoas reconhecíveis não fornecidas, texto adicional ou elementos sem relação com o jogo.
- Aplicar também estas observações, quando houver: {{OBSERVACOES_ADICIONAIS}}.

SAÍDA

Gerar somente a imagem final da arte. Não descrever, não explicar, não criar outro prompt e não incluir conteúdo fora da imagem.
```

## Preenchimento inicial

O [formulário do banner](formulario-banner-jogo.md) já contém o exemplo CATADOS FCCA × DEMOCRATAS FC e pode ser duplicado para novas partidas. Use ANO_PARA_VALIDACAO para conferir o dia da semana, mas não imprima esse campo na arte.

## Controle de qualidade obrigatório

Depois da geração, rejeite e gere novamente apenas se ocorrer um destes problemas:

- qualquer caractere divergir do bloco de copy;
- a chamada de transmissão faltar com SIM, aparecer com NÃO, estiver duplicada ou indicar plataforma/canal incorretos;
- data e dia da semana forem incompatíveis;
- escudos trocados de lado, deformados ou reinterpretados;
- o CATADOS estiver à direita como mandante ou à esquerda como visitante;
- alguma das 11 logos estiver ausente, alterada, ilegível ou fora de ordem;
- uma das duas faixas não tiver fundo branco puro ou as marcas não estiverem distribuídas em 6 no topo e 5 na base;
- presença de logo fictícia na área de patrocinadores;
- conteúdo cortado, ilegível ou fora da área segura;
- texto adicional não solicitado.

Limite a três tentativas automáticas. Se a trava de texto ou a fidelidade dos escudos continuar falhando, informe a limitação e recomende gerar o fundo sem texto para finalização em ferramenta de design.
