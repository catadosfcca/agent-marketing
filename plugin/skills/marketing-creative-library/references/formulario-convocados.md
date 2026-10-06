# Formulário do banner Convocados

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Antes da geração, o usuário deve enviar a lista atual completa de convocados e anexar a foto do jogador em destaque. Aceitar a lista como texto na conversa ou arquivo legível. Reutilizar materiais já enviados para esta convocação e pedir juntos somente os que faltarem. Não gerar enquanto a lista ou a foto estiver ausente ou inacessível. Preencha este formulário com esses materiais. Altere somente os valores depois dos dois-pontos e as linhas da lista.

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
- LISTA_CONVOCADOS é obrigatória, deve conter a lista atual completa enviada pelo usuário e estar legível; não usar exemplos ou lista de outra convocação.
- FOTO_JOGADOR_DESTAQUE é obrigatória e deve ser anexada pelo usuário e efetivamente enviada como referência visual à ferramenta. Não aceitar somente o nome do jogador ou um caminho inacessível como foto.
- O envio da foto para esta criação registra AUTORIZACAO_USO_DA_FOTO como USO SOLICITADO PELO USUÁRIO; não pedir reconfirmação de uso.
- Não altere fisionomia, cabelo, barba, tom de pele, idade aparente ou proporções corporais.
- Só troque a roupa pelo uniforme oficial quando ARQUIVO_REFERENCIA_UNIFORME for anexado e autorizado. Caso contrário, mantenha a roupa original.
- Use exatamente os nomes fornecidos, incluindo acentos e apelidos.
- Se EXIBIR_NUMEROS_CAMISA for NÃO, remova os trechos NÚMERO da arte.
- QUANTIDADE_CONVOCADOS deve ser igual à quantidade de linhas da lista.
- COLUNAS_DA_LISTA pode ser 1, 2, 3 ou AUTOMÁTICO; priorize leitura em celular.
- Não inclua adversário, data, horário, local, competição, placar, VS ou qualquer informação de partida.
- Use o escudo oficial do CATADOS sem alterações.
- Inclua as 11 logos de [patrocinadores-oficiais.md](patrocinadores-oficiais.md) em duas faixas brancas, seis no topo e cinco na base.
- Não gere enquanto a lista ou a foto estiver ausente, vazia ou ilegível/inacessível, ou enquanto houver PREENCHER ou ANEXAR em campo obrigatório. Não gerar uma versão sem foto nem inventar nomes para completar a lista.
