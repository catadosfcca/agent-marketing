# Envio do escudo e dos patrocinadores

Os assets incluídos no plugin são a fonte oficial. Ferramentas generativas podem não anexá-los automaticamente; isso **não** significa que os arquivos estejam ausentes. O agente deve tentar as rotas abaixo antes de pedir qualquer reenvio ao usuário.

## Ordem obrigatória de recuperação

1. Identificar quais assets a peça exige.
2. Tentar usar diretamente os arquivos internos da skill:
   - `../assets/escudos/catados-fcca.jpeg`
   - `../assets/referencias/referencias-oficiais.png`
   - `../assets/referencias/patrocinadores-topo.png`
   - `../assets/referencias/patrocinadores-base.png`
3. Se a ferramenta de imagem não aceitar asset interno como referência, procurar a mesma identidade já disponível na conversa ou em arquivos acessíveis da conta antes de pedir upload. Priorizar arquivos com nomes oficiais e artes anteriores do próprio Catados; não usar emblemas de terceiros nem versões claramente divergentes.
4. Quando houver ferramenta de composição gráfica/edição exata disponível, **preferir este fluxo** para marcas:
   - gerar apenas a base/fundo/layout esportivo, reservando as áreas de escudo e patrocinadores;
   - aplicar depois o escudo original e as faixas oficiais como imagens intactas, sem redesenho;
   - aplicar o escudo do adversário fornecido pelo usuário como arquivo intacto;
   - inserir textos por composição para evitar erros de grafia quando possível.
5. Só pedir ao usuário um anexo se o asset obrigatório não puder ser obtido de nenhuma das fontes acima.

## Regra de fidelidade

- Nunca substituir o escudo do Catados por um emblema inventado.
- Nunca substituir patrocinadores por nomes digitados, caixas vazias ou logos sintetizados.
- Nunca afirmar que o plugin “não contém” os arquivos quando a listagem da skill indicar que eles existem.
- Não pedir novamente um arquivo que já tenha sido fornecido na conversa atual.

## Peças com 11 patrocinadores

A referência oficial é `../assets/referencias/referencias-oficiais.png`. Para resultado final fiel, preferir compor diretamente as faixas `patrocinadores-topo.png` e `patrocinadores-base.png` sobre a arte, pois isso preserva as marcas melhor que a reconstrução generativa.

Layout obrigatório em cards esportivos:
- faixa branca superior: seis logos oficiais;
- conteúdo principal no centro;
- faixa branca inferior: cinco logos oficiais.

A prancha completa serve para conferência e identidade; as faixas prontas servem para composição exata.

## Peças apenas com escudo

Usar `../assets/escudos/catados-fcca.jpeg` como arquivo oficial. Em Busca de times visitantes, não usar patrocinadores nem suas faixas.

## Escudo do adversário

Se o usuário fornecer o escudo do adversário, reaproveitar o arquivo já anexado. Não pedir novamente e não redesenhá-lo.

## Validação final

Antes de declarar a arte pronta, conferir quando a ferramenta permitir:
- escudo oficial do Catados presente e reconhecível;
- escudo do adversário correto;
- patrocinadores obrigatórios presentes nas duas faixas, quando aplicável;
- nenhuma marca convertida em texto ou redesenhada;
- textos, horário, data e local corretos.

Se houver erro concreto, corrigir em até três tentativas. Se a composição exata estiver disponível, use-a em vez de regenerar logos repetidamente.
