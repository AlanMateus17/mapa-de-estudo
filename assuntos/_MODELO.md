---
tags: [estudo, assunto, modelo]
tipo: modelo
versao: 2 (2026-11-17)
---

# Modelo de arquivo de assunto

> Todo arquivo segue o **protocolo de escrita** do [MAPA](../MAPA.md#como-cada-arquivo-é-escrito): fonte primária na versão atual, código executado, fatos conferidos, `verificado-em` preenchido.
>
> Copie este arquivo para `assuntos/<área>/<assunto>.md` e preencha. Um arquivo por assunto. Ele serve para quatro coisas ao mesmo tempo: **estudar**, **revisar** (Anki e provas), **dar aula** (base da ficha dupla e do livro *Lógica e Máquina*) e **alimentar o setup** (registros de leitura, erros e atritos).

## Como este modelo junta as fontes

- **O jeito do Akita de aprender:** começar pelo **porquê** e pela **história**, descer até **como funciona por baixo**, fazer na mão antes de usar a ferramenta pronta, ler a fonte primária, não tratar linguagem como religião.
- **A ciência do estudo (assunto 0.1):** diagnóstico antes, recuperação ativa, exemplos com retirada de apoio, intercalação, revisão espaçada, ensinar.
- **O método do Professor (dev-setup):** 20/80 em duas passadas, exercícios N1–N4, protocolo de fim de bloco, ficha dupla e registro de entrevista.
- **O mercado:** o que se cobra de júnior, pleno e sênior, e como o assunto aparece em entrevista.
- **TDAH:** um roteiro de blocos curtos no começo do arquivo, para nunca precisar decidir "por onde eu começo".

---

```markdown
---
tags: [estudo, assunto, <área>]
area: <número e nome da área no MAPA>
etapa: <número no MAPA, ex.: 0.4>
nivel-alvo: N1 | N2 | N3 | N4
quando: M1 | T2 | H ...
professor: <id do módulo no curriculo.json, se houver>
prereq: [<assuntos que precisam vir antes>]
livro: <livro e trecho, como em `just livros para ETAPA`>
status: a-estudar | estudando | dominado | ensinado
verificado-em: AAAA-MM-DD
versoes: [<ex.: Node 22, TypeScript 7>]
fontes-conferidas: [<fontes primárias usadas>]
pendente: [<o que não deu para confirmar>]
atualizado: AAAA-MM-DD
---

# <Assunto>

> **Em uma frase:** ...
> **Nível-alvo:** N? (o que isso quer dizer aqui)
> **Os 20% que resolvem 80%:** 3 a 5 itens.

## Roteiro (blocos de 25 minutos)
| Bloco | O que fazer (ação concreta, não "estudar X") | Seções | Ao terminar, registre (comando) |
Última linha: "Fim | Fechar o assunto: ficha e colheita | 15 | just ficha ETAPA e just colher ETAPA".
Depois da tabela: "Como fazer cada bloco (sempre igual)": antes, durante, fechar, registrar (copie do 0.1).

## 0. Antes de começar: diagnóstico
Os 7 passos do 0.1 (preparar, responder com porquê, dar a certeza 1 a 3, parar no timer, conferir, `just diag`, seguir a decisão), e então 3 perguntas sem consulta, com a resposta comentada na seção 13.

## 1. Por que isso existe (o problema e a história)
## 2. O que é
## 3. Como funciona por baixo
## 4. Conceitos que você precisa dominar (checklist; cada item vira cartão com as suas palavras)
## 5. Qualidades
## 6. Defeitos, limites e críticas
## 7. Quando usar e quando não usar
## 8. Erros comuns
## 9. No seu setup e no AM Gestão
## 10. O que o mercado cobra (júnior, pleno, sênior, perguntas de entrevista)

## 11. Exemplos com retirada de apoio
1. **Resolvido:** passo a passo, com o porquê de cada passo.
2. **Com lacunas:** o mesmo tipo de problema, com partes para você completar.
3. **Sozinho:** um problema parecido, sem ajuda.
Todo código aqui é executado antes de entrar no arquivo (versão anotada no cabeçalho).

## 12. Exercícios N1–N4
N1 reconhecer · N2 aplicar · N3 combinar e achar o erro · N4 mini-projeto real. Primeiro sem IA.

## 13. Gabarito comentado
A resposta de cada exercício e, principalmente, **por que** ela é a certa e qual é o erro mais provável. Só consulte depois de tentar.

## 14. Resumo de uma tela (para as revisões espaçadas)
O mínimo para revisar em 2 minutos sem reler o arquivo: as definições, as regras e as armadilhas.

## 15. Registros no setup
- Leitura: `just livros ler LIVRO --trecho ... --min ... --assunto ETAPA --nota "..."`
- Cada erro nos exercícios: `just erro ETAPA "o erro" --certo "o certo"`
- Algo do setup travou ou foi manual: `just atrito "..." --area ...`
- Diagnóstico: `just diag ETAPA c3 x2 c1 --min N` (certo/errado + certeza 1 a 3).
- Tempo de cada bloco: `just professor fechar ID MINUTOS`.
- Fechar o assunto: `just ficha ETAPA`, preencher sem abrir o arquivo, `just colher ETAPA --seco` e `just colher ETAPA`. Os componentes do `ensino-ti` ligados à etapa ficam em `data/aulas.json` do dev-setup (acrescente a etapa lá antes).

## 16. Fontes (na ordem de uso)
1. Documentação oficial ou fonte primária · 2. Akita (só o que foi conferido) · 3. Curso da Alura · 4. Livro
(conteúdo pago e página de livro nunca vão para a IA)

## 17. Como saber que dominou
- Explico em 3 a 5 frases sem jargão.
- Resolvo o N4 sem consulta.
- Registro de entrevista preenchido.
- (N4) Dei a aula de verdade: onde e quando.
```
