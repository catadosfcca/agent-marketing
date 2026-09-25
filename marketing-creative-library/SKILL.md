---
name: marketing-creative-library
description: Planeja e cria prompts de imagens para campanhas do time, incluindo banners, jogos, resultados, aniversários, conquistas e outras peças comemorativas. Use quando o pedido envolver conceito visual, prompt para geração de imagem, variações de campanha ou revisão de uma peça; não use para textos longos sem componente visual.
---

# Biblioteca Criativa de Marketing

Transforme o pedido em uma direção visual pronta para produção e, quando solicitado, gere a imagem. Preserve informações fornecidas pelo usuário e não invente placares, datas, nomes, patrocinadores ou conquistas.

## Fluxo

1. Identifique objetivo, público, canal, formato, mensagem principal, identidade da marca e prazo. Se faltarem dados não críticos, faça suposições explícitas e use campos editáveis; pergunte apenas quando a ausência impedir um resultado correto.
   - Consulte [references/identidade-do-time.md](references/identidade-do-time.md) e aplique os campos já definidos. Não invente os campos ainda marcados como não definidos.
   - Para toda imagem, aplique obrigatoriamente [references/padrao-visual-global.md](references/padrao-visual-global.md) e use os assets de [references/patrocinadores-oficiais.md](references/patrocinadores-oficiais.md).
   - Em qualquer confronto com o CATADOS, aplique [references/regras-confronto.md](references/regras-confronto.md) e pergunte se o time é mandante ou visitante antes de definir os lados.
2. Escolha somente a referência relevante:
   - banners institucionais, promocionais ou de lançamento: [references/banners.md](references/banners.md)
   - banner Próxima Partida ou próximo jogo: preencha [references/formulario-proxima-partida.md](references/formulario-proxima-partida.md) e aplique [references/banner-proxima-partida.md](references/banner-proxima-partida.md)
   - anúncio oficial de partida: preencha [references/formulario-banner-jogo.md](references/formulario-banner-jogo.md) e aplique [references/banner-oficial-jogo.md](references/banner-oficial-jogo.md)
   - resultado final, placar ou autores dos gols: preencha [references/formulario-resultado-jogo.md](references/formulario-resultado-jogo.md) e aplique [references/banner-resultado-jogo.md](references/banner-resultado-jogo.md)
   - outras partidas, campeonatos, escalações, resultados ou conteúdo gamer: [references/jogos.md](references/jogos.md)
   - aniversários, boas-vindas, conquistas, premiações e agradecimentos: [references/celebracoes.md](references/celebracoes.md)
3. Para montar o pedido e entregar o resultado no padrão do time, leia [references/briefing-e-entrega.md](references/briefing-e-entrega.md).
4. Antes de aprovar ou gerar a peça, aplique [references/qualidade-e-seguranca.md](references/qualidade-e-seguranca.md).

## Regras essenciais

- Trabalhe em português do Brasil, salvo pedido em outro idioma.
- Preserve a assinatura vermelho, preto e branco, a geometria moderna, a iluminação cinematográfica, o grunge premium e a faixa de patrocinadores em todas as categorias. Adapte o cenário ao assunto sem perder essa identidade.
- Diferencie direção de arte, prompt de imagem e texto final da peça.
- Prefira gerar o fundo e os elementos visuais sem texto embutido. Reserve áreas limpas para título, data, placar, CTA e logos; recomende composição tipográfica posterior quando a ferramenta não garantir texto fiel.
- Exceção: nos banners Próxima Partida, anúncio oficial e Resultado do Jogo, siga as travas de texto e a saída de imagem final definidas nas referências correspondentes.
- Defina proporção ou dimensões antes da geração. Se o canal não for informado, use 1:1 em no mínimo 2048 × 2048 e indique adaptações para 1080 × 1350, 1080 × 1920 e 1920 × 1080.
- Não use nomes, logos, uniformes, personagens ou estilos protegidos como se houvesse licença. Quando a autorização não estiver clara, proponha uma direção original inspirada no gênero, não em um artista ou franquia específica.
- Não altere rostos, corpos, tons de pele, símbolos culturais ou atributos pessoais de modo ofensivo ou sem necessidade criativa.
- Para pessoas reais, mantenha semelhança apenas quando o usuário fornecer material autorizado e pedir isso explicitamente.
- Inclua sempre as 11 logos oficiais no rodapé branco, preservando os arquivos originais. Só é permitido aparar espaço branco externo durante a composição.
- Nunca infira o mando de campo. Sem resposta explícita de mandante ou visitante, não gere um banner de confronto.

## Saída padrão

Entregue, nesta ordem:

1. **Conceito:** uma frase com a ideia central.
2. **Direção de arte:** composição, paleta, luz, atmosfera e hierarquia.
3. **Copy na peça:** título, apoio e CTA, marcando qualquer campo ainda não confirmado.
4. **Prompt de geração:** um bloco autocontido, pronto para colar na ferramenta.
5. **Restrições:** o que deve ser evitado na imagem.
6. **Formatos:** tamanho principal e adaptações.

Quando o usuário pedir múltiplas opções, varie o conceito e a composição de forma significativa; não entregue apenas sinônimos.
