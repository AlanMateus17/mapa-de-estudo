# Changelog

## 2026-11-26

### Corrigido
- 0.1: o frontmatter não era YAML válido. A fonte de Richland, Kornell e Kao 2009 e Butterfield e Metcalfe 2001 tinha ": " duas vezes sem aspas (Journal of Experimental Psychology: Applied; JEP: Learning); agora está entre aspas duplas.
- 0.2: a fonte da Britannica ("History of logic: Gottlob Frege") virava um par chave: valor sem dar erro; agora está entre aspas simples.

### Adicionado
- `scripts/frontmatter.py` e o CI `Frontmatter`: todo assunto começa com frontmatter, o YAML é válido, é um mapa de campos e nenhum item de lista virou "chave: valor". Testes em `tests/test_frontmatter.py`. Regra: item com ": " vai entre aspas.

## 2026-11-21

### Alterado
- 0.1 e 0.2: passo "Registrar a nota" no fechamento do assunto (`just professor nota`, sem IA, ou `prova` e `corrigir`, com IA). No dev-setup v2.40 o Professor só libera um assunto depois que os assuntos de que ele depende passam na prova; sem esse passo, o 0.2 ficava bloqueado. Conteúdo do assunto não mudou.

## 2026-11-17 (6)

### Alterado
- 0.1 e 0.2: diagnóstico em 7 passos (responder com porquê, dar a certeza de 1 a 3 antes de conferir, `just diag`, seguir a decisão), com as fontes do pré-teste (Richland, Kornell e Kao 2009) e da hipercorreção (Butterfield e Metcalfe 2001).
- 0.1 e 0.2: roteiro com a coluna "Ao terminar, registre" (o comando do setup de cada bloco) e "Como fazer cada bloco" (antes, durante, fechar, registrar).
- 0.1 e 0.2: "Fechar o assunto" com `just ficha` e `just colher`, que levam o estudo para os planos de aula do `ensino-ti`, o pipeline de conteúdo, o banco de exercícios e o Anki.
- Modelo atualizado com as mesmas regras.

## 2026-11-17 (5)

### Alterado
- 0.2: exemplo executado do que `&&`, `||` e `??` devolvem (seção 9); antes o arquivo citava o comportamento sem mostrar.
- 0.1 *Aprender a aprender* no modelo v2: roteiro em 7 blocos, diagnóstico, checklist de conceitos, exemplos com retirada de apoio (montar um bloco de estudo, cartão ruim e cartão bom), exercícios N1–N4 com gabarito comentado, resumo de uma tela e registros no setup.
- Akita #76 e #65 conferidos pelas transcrições publicadas no site dele; nova seção sobre onde a pesquisa concorda e onde discorda dele.
- Entram as fontes primárias de exemplos resolvidos e retirada de apoio (Sweller e Cooper 1985; Renkl et al. 2002; Kalyuga et al. 2003).
- Saem as referências aos episódios #63 e #119, que não foram conferidos.

## 2026-11-17 (4)

### Alterado
- Modelo de assunto v2: roteiro em blocos de 25 minutos, diagnóstico antes de começar, exemplos com retirada de apoio (resolvido, com lacunas, sozinho), gabarito comentado, resumo de uma tela e registros no setup (`just livros ler`, `just erro`, `just atrito`, `just professor fechar`).
- 0.2 no modelo v2: entram ou exclusivo (XOR), precedência dos conectivos, ordem dos quantificadores, contingência e gabarito de todos os exercícios; todos os blocos de código executados com Node 22.23.4 e conferidos com `tsc --strict` (TypeScript 7.0.2).

## 2026-11-17 (3)

### Adicionado
- Assunto 0.2 *Linguagem matemática e lógica*, verificado pelo protocolo; exemplo resolvido executado com Node 22.23.4 e conferido com `tsc --strict` (TypeScript 7.0.2).

## 2026-11-17 (2)

### Alterado
- Licença: o resumo em `LICENSE.md` foi trocado pelo texto legal completo da CC BY-NC-SA 4.0 em `LICENSE`, copiado do repositório oficial da Creative Commons; aviso de copyright e resumo no README.

### Removido
- Os rascunhos de 0.6, 1.3, 1.5, 2.1 e 4.4: só ficam no repositório arquivos que passaram pelo protocolo. Eles voltam quando forem reescritos.

## 2026-11-17

### Adicionado
- Repositório criado a partir do vault de estudo do autor.
- `MAPA.md`: todas as áreas e assuntos em etapas por pré-requisito (Etapas 0 a 8 e horizonte), com nível-alvo e dependências.
- `assuntos/_MODELO.md`: modelo de arquivo de assunto e protocolo de escrita.
- Assunto 0.1 *Aprender a aprender*, verificado pelo protocolo.
- Rascunhos de 0.6 Lógica, 1.3 Terminal, 1.5 Git, 2.1 TypeScript e 4.4 POO, marcados como pendentes de verificação.
- Verificação automática de links internos no CI.
