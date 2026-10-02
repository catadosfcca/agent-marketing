# Formulário do banner Convocados

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Preencha este formulário e anexe a foto do jogador em destaque antes da geração. Altere somente os valores depois dos dois-pontos e as linhas da lista.

```text
TITULO_PRINCIPAL: CONVOCADOS
SUBTITULO: CATADOS FCCA

NOME_JOGADOR_DESTAQUE: PREENCHER
FOTO_JOGADOR_DESTAQUE: ANEXAR
AUTORIZACAO_USO_DA_FOTO: USO SOLICITADO PELO USUÁRIO
POSICAO_JOGADOR_DESTAQUE: DIREITA
OCUPACAO_VISUAL_JOGADOR: 40% A 50%

TRATAMENTO_DO_UNIFORME: MANTER ROUPA ORIGINAL
ARQUIVO_REFERENCIA_UNIFORME: NÃO INFORMAR
ARQUIVO_ESCUDO_CATADOS: ../assets/escudos/catados-fcca.jpeg

EXIBIR_NUMEROS_CAMISA: NÃO
QUANTIDADE_CONVOCADOS: CALCULAR A PARTIR DA LISTA
COLUNAS_DA_LISTA: AUTOMÁTICO
LISTA_CONVOCADOS:
PREENCHER COM A LISTA ATUAL DO USUÁRIO

FORMATO: 4:5
RESOLUCAO: 2160 × 2700
LOGOS_PATROCINADORES: USAR BIBLIOTECA OFICIAL
TEXTO_AREA_PATROCINADORES: PATROCINADORES
OBSERVACOES_ADICIONAIS: NENHUMA
```

## Regras de preenchimento

- FORMATO e RESOLUCAO devem permanecer em 4:5 e 2160 × 2700.
- FOTO_JOGADOR_DESTAQUE é obrigatória e deve ser anexada pelo usuário.
- AUTORIZACAO_USO_DA_FOTO deve estar como CONFIRMADA antes da geração.
- Não altere fisionomia, cabelo, barba, tom de pele, idade aparente ou proporções corporais.
- Só troque a roupa pelo uniforme oficial quando ARQUIVO_REFERENCIA_UNIFORME for anexado e autorizado. Caso contrário, mantenha a roupa original.
- Use exatamente os nomes fornecidos, incluindo acentos e apelidos.
- Se EXIBIR_NUMEROS_CAMISA for NÃO, remova os trechos NÚMERO da arte.
- QUANTIDADE_CONVOCADOS deve ser igual à quantidade de linhas da lista.
- COLUNAS_DA_LISTA pode ser 1, 2, 3 ou AUTOMÁTICO; priorize leitura em celular.
- Não inclua adversário, data, horário, local, competição, placar, VS ou qualquer informação de partida.
- Use o escudo oficial do CATADOS sem alterações.
- Inclua as 11 logos de [patrocinadores-oficiais.md](patrocinadores-oficiais.md) no rodapé branco.
- Não gere enquanto houver PREENCHER, ANEXAR ou autorização pendente.
