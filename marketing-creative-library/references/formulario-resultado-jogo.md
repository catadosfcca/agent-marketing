# Formulário do banner Resultado do Jogo

Duplique e edite este formulário após cada partida. Altere somente os valores depois dos dois-pontos.

```text
TITULO_PRINCIPAL: DEU VITÓRIA DOS CATADOS!
SUBTITULO: RESULTADO FINAL
PALAVRA_DESTAQUE: VITÓRIA
RESULTADO_CATADOS: PREENCHER AUTOMATICAMENTE

MANDO_DE_CAMPO_CATADOS: PREENCHER
ADVERSARIO: PREENCHER
ARQUIVO_ESCUDO_CATADOS: ../assets/escudos/catados-fcca.jpeg
ARQUIVO_ESCUDO_ADVERSARIO: ANEXAR

TIME_ESQUERDA: DEFINIR APÓS RESPOSTA
ARQUIVO_ESCUDO_ESQUERDA: DEFINIR APÓS RESPOSTA
PLACAR_ESQUERDA: DEFINIR APÓS RESPOSTA
AUTORES_GOLS_ESQUERDA: DEFINIR APÓS RESPOSTA

TIME_DIREITA: DEFINIR APÓS RESPOSTA
ARQUIVO_ESCUDO_DIREITA: DEFINIR APÓS RESPOSTA
PLACAR_DIREITA: DEFINIR APÓS RESPOSTA
AUTORES_GOLS_DIREITA: DEFINIR APÓS RESPOSTA

PLACAR_CATADOS: PREENCHER
PLACAR_ADVERSARIO: PREENCHER
AUTORES_GOLS_CATADOS: PREENCHER OU NÃO INFORMAR
AUTORES_GOLS_ADVERSARIO: PREENCHER OU NÃO INFORMAR

DATA_E_DIA: PREENCHER
ANO_PARA_VALIDACAO: PREENCHER
HORARIO: PREENCHER
LOCAL: PREENCHER
ENDERECO: PREENCHER
COMPETICAO: AMISTOSO

IMAGEM_DE_REFERENCIA: ANEXAR BANNER OFICIAL
TEXTO_AREA_PATROCINADORES: PATROCINADORES
LOGOS_PATROCINADORES: USAR BIBLIOTECA OFICIAL
OBSERVACAO_RESULTADO: NENHUMA
OBSERVACOES_ADICIONAIS: NENHUMA
```

## Regras de preenchimento

- Pergunte obrigatoriamente: O CATADOS F.C.C.A. é mandante ou visitante nesta partida?
- Aplique [regras-confronto.md](regras-confronto.md) antes de preencher qualquer campo esquerdo ou direito.
- Use somente números inteiros iguais ou maiores que zero nos placares.
- Calcule RESULTADO_CATADOS: VITÓRIA quando PLACAR_CATADOS for maior; EMPATE quando for igual; DERROTA quando for menor.
- O título é editável, mas deve ser compatível com RESULTADO_CATADOS. Não use VITÓRIA em empate ou derrota.
- Para autores dos gols, use nomes confirmados separados por vírgula. Quando alguém marcar mais de uma vez, use Nome (2), Nome (3) e assim por diante.
- Se os autores não forem conhecidos ou não devam aparecer, use NÃO INFORMAR.
- Quando um time fizer zero gols, use NENHUM no campo de autores.
- A soma dos gols atribuídos aos autores deve corresponder ao placar do respectivo time.
- Se MANDANTE, CATADOS e seus dados ficam à esquerda. Se VISITANTE, ficam à direita.
- ANO_PARA_VALIDACAO não aparece na arte; serve apenas para conferir a data.
- Use as 11 logos de [patrocinadores-oficiais.md](patrocinadores-oficiais.md).
- Não gere enquanto houver PREENCHER ou DEFINIR APÓS RESPOSTA.
