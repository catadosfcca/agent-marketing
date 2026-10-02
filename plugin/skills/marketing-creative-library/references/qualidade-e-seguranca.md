# Qualidade, consistência e segurança

## Aplicação no plugin

As regras operacionais de [operacao-do-agente.md](operacao-do-agente.md) prevalecem sobre exigências genéricas deste modelo. Respeite formato e exceções pedidos pelo usuário; reaproveite dados já informados; use os assets incluídos sem pedir novo upload; trate exemplos como exemplos, nunca como fatos da partida atual. Não exija reconfirmação de uso de fotos enviadas para a criação solicitada. Gere a imagem quando o usuário pedir a arte.

Avalie toda peça também contra [padrao-visual-global.md](padrao-visual-global.md).

## Checklist antes de gerar

- Objetivo, público e canal estão claros?
- Em confronto com o CATADOS, o usuário confirmou explicitamente se o time é mandante ou visitante?
- O CATADOS está à esquerda quando mandante e à direita quando visitante?
- Em banner de resultado, o placar final foi confirmado e o título corresponde a vitória, empate ou derrota?
- A contagem dos autores dos gols corresponde ao placar de cada time?
- Em banner de convocados, a foto em destaque foi anexada e seu uso foi autorizado?
- A quantidade informada corresponde à lista e todos os nomes foram confirmados?
- Dimensão ou proporção foi definida?
- O banner mestre está exatamente em 4:5 e 2160 × 2700?
- O elemento principal continua reconhecível em miniatura?
- Existe espaço seguro para título, CTA, data, placar e logos?
- A composição usa vermelho, preto e branco, geometria moderna, iluminação cinematográfica, grunge leve e acabamento premium?
- A faixa de patrocinadores tem fundo branco puro e ocupa aproximadamente 20% a 30% do rodapé sem sobrepor conteúdo?
- As 11 logos oficiais estão presentes em duas linhas balanceadas, seis na primeira e cinco na segunda?
- Todos os fatos foram confirmados ou marcados como {{CAMPO}}?
- Fotos, marcas, uniformes e personagens têm autorização ou foram substituídos por alternativas originais?
- O prompt evita depender de texto gerado dentro da imagem?
- A direção é original e não pede imitação de artista vivo, campanha, franquia ou estúdio específico?

## Checklist da imagem gerada

- Rostos, mãos, membros, objetos e perspectivas estão coerentes.
- A pessoa retratada preserva características e tom de pele.
- O logo, se usado como referência autorizada, não foi redesenhado ou deformado.
- Não há letras, números, marcas d'água ou símbolos acidentais.
- A área reservada comporta a copy sem cobrir o foco.
- Contraste e hierarquia funcionam no tamanho real do canal.
- Não surgiram patrocinadores, troféus, uniformes, estatísticas ou informações não solicitadas.
- Placar e autores dos gols aparecem associados ao escudo correto?
- Em convocados, a pessoa preserva fisionomia e a lista não contém nomes ausentes, duplicados ou inventados?
- A faixa contém exatamente os assets de [patrocinadores-oficiais.md](patrocinadores-oficiais.md)?
- Todas as logos preservam proporção, desenho e cores, com recorte limitado ao espaço branco externo?
- A peça não ridiculariza adversários nem reforça estereótipos.

## Restrições reutilizáveis

Acrescente ao prompt apenas as restrições relevantes:

```text
Evitar: texto ou números incorretos, logos inventados ou deformados, marcas d'água, patrocinadores fictícios, anatomia incorreta, mãos extras, rostos duplicados, olhos assimétricos, objetos flutuantes, perspectiva quebrada, recortes acidentais, fundo poluído, excesso de efeitos, contraste insuficiente, baixa resolução, aparência genérica de banco de imagens e informações não fornecidas.
```

## Critérios de variação

Ao criar alternativas, mude pelo menos três dimensões:

- metáfora ou ideia central;
- enquadramento e distribuição dos elementos;
- atmosfera e iluminação;
- paleta ou contraste;
- nível de realismo;
- uso de fotografia, 3D, colagem ou ilustração original.

Não trate simples troca de cor ou pequenas mudanças de adjetivo como novo conceito.

## Entrega para produção

Quando a peça for aprovada, registre junto dela:

- versão e data;
- formato e canal;
- prompt final utilizado;
- assets autorizados;
- confirmação de presença e integridade das 11 logos oficiais;
- copy confirmada;
- observações de acessibilidade, incluindo contraste e texto alternativo sugerido.
