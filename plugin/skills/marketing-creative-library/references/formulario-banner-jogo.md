# Formulário do banner oficial de jogo

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Duplique e edite este formulário para cada partida. Altere somente os valores depois dos dois-pontos. Não remova os nomes dos campos.

```text
TITULO_PRINCIPAL: TEM CATADOS EM CAMPO
SUBTITULO: AMISTOSO
PALAVRA_DESTAQUE: CATADOS
FORMATO: 4:5
RESOLUCAO: 2160 × 2700

MANDO_DE_CAMPO_CATADOS: PREENCHER
ADVERSARIO: PREENCHER
ARQUIVO_ESCUDO_CATADOS: ../assets/escudos/catados-fcca.jpeg
ARQUIVO_ESCUDO_ADVERSARIO: ANEXAR

TIME_ESQUERDA: DEFINIR APÓS RESPOSTA
ARQUIVO_ESCUDO_ESQUERDA: DEFINIR APÓS RESPOSTA

TIME_DIREITA: DEFINIR APÓS RESPOSTA
ARQUIVO_ESCUDO_DIREITA: DEFINIR APÓS RESPOSTA

DATA_E_DIA: PREENCHER
ANO_PARA_VALIDACAO: PREENCHER
VAI_TER_TRANSMISSAO: PREENCHER
TEXTO_TRANSMISSAO: DEFINIR APÓS RESPOSTA
LINK_TRANSMISSAO: OPCIONAL
HORARIO: PREENCHER
LOCAL: PREENCHER
ENDERECO: PREENCHER

IMAGEM_DE_REFERENCIA: OPCIONAL
TEXTO_AREA_PATROCINADORES: PATROCINADORES
LOGOS_PATROCINADORES: USAR BIBLIOTECA OFICIAL
OBSERVACOES_ADICIONAIS: NENHUMA
```

## Regras de preenchimento

- Use exatamente a grafia que deverá aparecer na arte.
- Pergunte **Vai ter transmissão?** se essa informação ainda não foi dada para a partida atual. Siga [transmissão Catados TV](transmissao-catados-tv.md).
- Com SIM, usar TEXTO_TRANSMISSAO: AO VIVO NO YOUTUBE · CATADOS TV. Com NÃO, deixar TEXTO_TRANSMISSAO vazio e omitir a chamada. LINK_TRANSMISSAO é opcional; não inventar URLs.
- Não gerar enquanto VAI_TER_TRANSMISSAO estiver pendente. Não imprimir os campos de controle SIM/NÃO, PREENCHER, DEFINIR APÓS RESPOSTA ou OPCIONAL na arte.
- FORMATO e RESOLUCAO devem permanecer em 4:5 e 2160 × 2700.
- Antes de preencher os lados, pergunte obrigatoriamente: O CATADOS F.C.C.A. é mandante ou visitante nesta partida?
- Aplique [regras-confronto.md](regras-confronto.md). Não infira o mando e não gere enquanto MANDO_DE_CAMPO_CATADOS estiver como PREENCHER.
- Se MANDANTE, CATADOS fica à esquerda. Se VISITANTE, CATADOS fica à direita.
- ANO_PARA_VALIDACAO serve apenas para conferir se o dia da semana está correto; ele não aparece na peça.
- ANEXAR significa que o arquivo original deve acompanhar o pedido.
- USAR BIBLIOTECA OFICIAL significa inserir as 11 logos de [patrocinadores-oficiais.md](patrocinadores-oficiais.md).
- Se um campo obrigatório estiver vazio, o agente deve pedir o dado antes de gerar a imagem.
