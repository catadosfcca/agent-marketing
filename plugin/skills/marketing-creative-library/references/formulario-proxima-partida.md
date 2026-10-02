# Formulário do banner Próxima Partida

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Duplique e edite este formulário para cada novo jogo. Altere somente os valores depois dos dois-pontos.

```text
TITULO_PRINCIPAL: PRÓXIMA PARTIDA

MANDO_DE_CAMPO_CATADOS: PREENCHER
ADVERSARIO: PREENCHER
ARQUIVO_ESCUDO_CATADOS: ../assets/escudos/catados-fcca.jpeg
ARQUIVO_ESCUDO_ADVERSARIO: ANEXAR

TIME_1: DEFINIR APÓS RESPOSTA
ARQUIVO_ESCUDO_TIME_1: DEFINIR APÓS RESPOSTA

TIME_2: DEFINIR APÓS RESPOSTA
ARQUIVO_ESCUDO_TIME_2: DEFINIR APÓS RESPOSTA

DATA_E_DIA: PREENCHER
ANO_PARA_VALIDACAO: PREENCHER
HORARIO: PREENCHER
LOCAL: PREENCHER
COMPETICAO: AMISTOSO

ARQUIVOS_LOGOS_PATROCINADORES: USAR BIBLIOTECA OFICIAL
IMAGEM_MODELO: OPCIONAL

CORES_PRINCIPAIS: vermelho, preto e branco
FORMATO: 4:5
RESOLUCAO: 2160 × 2700
OBSERVACOES_ADICIONAIS: NENHUMA
```

## Regras do formulário

- Use exatamente a grafia que deverá aparecer na arte.
- FORMATO e RESOLUCAO devem permanecer em 4:5 e 2160 × 2700.
- Antes de preencher TIME_1 e TIME_2, pergunte obrigatoriamente: O CATADOS F.C.C.A. é mandante ou visitante nesta partida?
- Aplique [regras-confronto.md](regras-confronto.md). Não infira o mando e não gere enquanto MANDO_DE_CAMPO_CATADOS estiver como PREENCHER.
- Se MANDANTE, CATADOS ocupa TIME_1 à esquerda. Se VISITANTE, CATADOS ocupa TIME_2 à direita.
- Antes da geração, corrija ortografia e formatação em português e salve o valor corrigido no formulário. Não altere nomes próprios ou fatos sem confirmação.
- ANO_PARA_VALIDACAO não aparece na imagem; ele confirma o dia da semana e se a data ainda é futura.
- ANEXAR exige o arquivo original junto ao pedido.
- USAR BIBLIOTECA OFICIAL significa inserir as 11 logos de [patrocinadores-oficiais.md](patrocinadores-oficiais.md).
- Se COMPETICAO estiver vazia, omita essa linha da arte.
- Não gere enquanto houver PREENCHER, campo obrigatório vazio ou arquivo obrigatório sem anexo.
