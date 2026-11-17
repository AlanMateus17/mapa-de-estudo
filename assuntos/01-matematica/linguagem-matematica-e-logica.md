---
tags: [estudo, assunto, matematica, logica]
area: 01 · Matemática
etapa: 0.2
nivel-alvo: N3 (montar e simplificar qualquer expressão lógica sem consulta, e traduzir regras de negócio para lógica e para código)
quando: M1, semana 1 (sexta)
professor: mat-linguagem
prereq: [0.1]
status: a-estudar
verificado-em: 2026-11-17
versoes: [Node.js 22.23.4 (executa .ts direto), TypeScript 7.0.2 (tsc --strict sem erros)]
fontes-conferidas:
  - Stanford Encyclopedia of Philosophy, "The Emergence of First-Order Logic" (Boole 1847, Frege 1879, Peirce 1885)
  - Encyclopaedia Britannica, "History of logic: Gottlob Frege"
  - Shannon 1938, "A Symbolic Analysis of Relay and Switching Circuits", Transactions of the AIEE 57(12) (tese de mestrado no MIT, 1937)
  - MDN, operador lógico AND (&&)
livro: VHSlins, Matemática Básica, Parte I, Cap. 1 (Linguagem Matemática)
pendente:
  - Nenhum episódio do Akita sobre lógica proposicional foi conferido; nenhum é citado
atualizado: 2026-11-17
---

# Linguagem matemática e lógica

> **Em uma frase:** lógica é o conjunto de regras para dizer exatamente o que é verdade a partir de frases simples ligadas por **e, ou, não, se… então** e por **para todo** e **existe**, sem ambiguidade.
> **Nível-alvo:** N3. Você monta a tabela-verdade de qualquer expressão, simplifica com as leis de De Morgan, nega frases com "todo" e "algum" sem errar e traduz uma regra de negócio para lógica e para um `if`.
> **Os 20% que resolvem 80%:**
> 1. Os 5 conectivos e a tabela-verdade de cada um.
> 2. **Se p então q** só é falso quando p é verdadeiro e q é falso.
> 3. As **leis de De Morgan**: ¬(p ∧ q) ≡ ¬p ∨ ¬q e ¬(p ∨ q) ≡ ¬p ∧ ¬q.
> 4. **Negar um quantificador:** "não é verdade que todos…" = "existe algum que não…".
> 5. **Contrapositiva** (¬q → ¬p) vale o mesmo que p → q; a **recíproca** (q → p) não.

---

## 1. Por que isso existe (o problema e a história)

A linguagem do dia a dia é ambígua. "Você pode levar sorvete ou bolo" quer dizer um dos dois, ou os dois? "Todos os alunos não fizeram a prova" quer dizer que ninguém fez, ou que nem todos fizeram? Em matemática, num contrato e num programa, a ambiguidade custa caro. A lógica dá um sentido único a cada frase.

- **Aristóteles** sistematizou as regras do raciocínio válido na Grécia antiga.
- **George Boole** fez a virada no século XIX: em *The Mathematical Analysis of Logic* (1847) e em *An Investigation of the Laws of Thought* (1854), escreveu o raciocínio como **álgebra**, com símbolos e regras de cálculo. Daí vem o nome "booleano".
- **Gottlob Frege**, em *Begriffsschrift* (1879), introduziu de forma cuidadosa os **quantificadores** ("para todo", "existe") e as variáveis. Charles S. Peirce chegou a ideias parecidas de forma independente, em 1885.
- **Claude Shannon**, na tese de mestrado no MIT (1937, publicada em 1938), mostrou que a álgebra de Boole descreve circuitos de relés e interruptores. É por isso que o computador funciona com lógica: cada porta lógica de um processador é um conectivo de Boole feito com transistores. Você vê isso no assunto 0.4.

A ponte que importa para você: o mesmo **e/ou/não** aparece na matemática, no circuito, no `if` do TypeScript, no `WHERE` do SQL e na regra de negócio do AM Gestão.

## 2. O que é

| Termo | O que é | Exemplo |
|---|---|---|
| **Proposição** | Frase que é **verdadeira (V)** ou **falsa (F)**, nunca as duas | "7 é primo" (V) |
| **Não é proposição** | Pergunta, ordem, frase com variável livre | "Feche a porta." · "x > 3" (depende de x) |
| **Sentença aberta** | Frase com variável; vira proposição quando você dá valor ou quantifica | "x > 3" |
| **Negação** ¬p | Inverte o valor | ¬(7 é primo) = F |
| **Conjunção** p ∧ q ("e") | V só se as duas forem V | `estoque > 0 && clienteAtivo` |
| **Disjunção** p ∨ q ("ou" inclusivo) | F só se as duas forem F | `pix || cartao` |
| **Condicional** p → q ("se p então q") | F só quando p é V e q é F | "Se a compra passa de R$ 200, então tem desconto" |
| **Bicondicional** p ↔ q ("se e somente se") | V quando p e q têm o mesmo valor | "o pedido está pago ↔ o saldo devedor é zero" |
| **Tautologia** | Sempre V, em toda linha da tabela | p ∨ ¬p |
| **Contradição** | Sempre F | p ∧ ¬p |
| **Equivalência** (≡) | Duas fórmulas com a mesma tabela-verdade | p → q ≡ ¬p ∨ q |
| **Quantificador universal** ∀ | "Para todo" | ∀x (x é aluno → x fez a prova) |
| **Quantificador existencial** ∃ | "Existe pelo menos um" | ∃x (nota de x < 6) |
| **Argumento** | Premissas que levam a uma conclusão; é **válido** se, sempre que as premissas forem V, a conclusão também for | |

### Tabela-verdade dos conectivos

| p | q | ¬p | p ∧ q | p ∨ q | p → q | p ↔ q |
|---|---|---|---|---|---|---|
| V | V | F | V | V | V | V |
| V | F | F | F | V | **F** | F |
| F | V | V | F | V | V | F |
| F | F | V | F | F | V | V |

**Por que p → q é V quando p é F?** Pense numa promessa: "se você tirar 10, ganha um presente". Se você não tirou 10, a promessa não foi quebrada, ganhando ou não o presente. A promessa só é quebrada na linha p = V, q = F.

## 3. Como funciona por baixo

- **Cada linha da tabela é um caso.** Com n proposições há 2ⁿ linhas. Duas fórmulas são equivalentes quando batem nas 2ⁿ linhas, e isso dá para conferir por força bruta (o código da seção 11 faz exatamente isso).
- **Quantificador é um "e" ou um "ou" sobre um conjunto.** Num conjunto finito, ∀x P(x) é P(x₁) ∧ P(x₂) ∧ … e ∃x P(x) é P(x₁) ∨ P(x₂) ∨ …. Por isso a negação troca um pelo outro, exatamente como De Morgan: ¬∀x P(x) ≡ ∃x ¬P(x) e ¬∃x P(x) ≡ ∀x ¬P(x).
- **Conjunto vazio:** "todo elemento do vazio satisfaz P" é **verdadeiro** (não há contraexemplo) e "existe elemento do vazio com P" é **falso**. No TypeScript, `[].every(...)` dá `true` e `[].some(...)` dá `false`, pela mesma razão.
- **Na máquina:** Shannon mostrou que interruptores em série fazem "e" e em paralelo fazem "ou". Hoje são transistores dentro das portas lógicas do processador (assunto 0.4).

## 4. Conceitos que você precisa dominar

- [ ] Reconhecer o que é e o que não é proposição.
- [ ] Os 5 conectivos e as tabelas-verdade de cor.
- [ ] Montar a tabela-verdade de uma fórmula composta, com 2ⁿ linhas.
- [ ] Identificar tautologia, contradição e contingência (às vezes V, às vezes F).
- [ ] Provar equivalências pela tabela: p → q ≡ ¬p ∨ q; p ↔ q ≡ (p → q) ∧ (q → p).
- [ ] **Leis de De Morgan** e dupla negação (¬¬p ≡ p).
- [ ] Distributiva: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r).
- [ ] Condicional, **recíproca** (q → p), **inversa** (¬p → ¬q) e **contrapositiva** (¬q → ¬p): só a contrapositiva é equivalente.
- [ ] Condição **suficiente** (p em p → q) e **necessária** (q em p → q).
- [ ] Quantificadores ∀ e ∃, e a **negação** de cada um.
- [ ] Argumento válido × conclusão verdadeira: um argumento pode ser válido com conclusão falsa (se uma premissa for falsa).
- [ ] *Modus ponens* (p → q, p, logo q) e *modus tollens* (p → q, ¬q, logo ¬p).
- [ ] As duas falácias mais comuns: **afirmar o consequente** (p → q, q, logo p) e **negar o antecedente** (p → q, ¬p, logo ¬q).
- [ ] **Tipos de demonstração** (só reconhecer, nível N1 aqui): direta, por contrapositiva, por absurdo e por contraexemplo.

## 5. Qualidades

- **Elimina ambiguidade:** uma frase lógica tem um sentido só.
- **É verificável mecanicamente:** a tabela-verdade decide qualquer equivalência proposicional.
- **Serve para tudo o que vem depois:** conjuntos (0.3), circuitos (0.4), `if` e testes (0.6, 2.4), SQL (4.2), requisitos e critérios de aceite (4.5).
- **Ensina a negar direito,** o que é metade do trabalho de achar bug: "o que precisa ser verdade para isso dar errado?"

## 6. Defeitos, limites e críticas

- **O "ou" da lógica é inclusivo;** no português do dia a dia, muitas vezes é exclusivo. Traduzir regra de negócio exige perguntar qual dos dois o cliente quis dizer.
- **O "se… então" lógico não é causa.** "Se 2 + 2 = 5, então a Lua é de queijo" é verdadeiro na lógica (antecedente falso). Isso estranha no começo e não descreve causalidade.
- **A tabela-verdade explode:** com 20 proposições são mais de um milhão de linhas. Para fórmulas grandes, usa-se álgebra (as leis) e, em computação, algoritmos especializados (SAT).
- **Lógica proposicional não fala de "todos" e "alguns";** para isso é preciso a lógica de predicados (quantificadores), que é bem mais rica e mais difícil.
- **No JavaScript, `&&` e `||` não devolvem só `true` ou `false`:** devolvem um dos operandos (seção 9). É uma fonte clássica de bug.

## 7. Quando usar e quando não usar

- **Use** sempre que escrever uma condição (`if`, filtro, `WHERE`), um critério de aceite, um teste ou uma regra de permissão.
- **Use a contrapositiva** quando a frase direta for difícil de verificar: "se o pedido foi pago, então tem comprovante" equivale a "se não tem comprovante, não foi pago".
- **Simplifique com De Morgan** antes de escrever um `if` com muitos `!`.
- **Não use** a tabela-verdade para fórmulas enormes; passe para as leis algébricas.

## 8. Erros comuns

- Tratar a recíproca como equivalente: "todo pagamento por Pix é instantâneo" não quer dizer "todo pagamento instantâneo é por Pix".
- Negar "todos são" como "todos não são". A negação certa de "todos os pedidos foram entregues" é "**algum** pedido não foi entregue".
- Negar "p e q" como "não p e não q" (o certo é "não p **ou** não q").
- Esquecer a fronteira ao traduzir: "a partir de 30 dias" é `dias >= 30`, não `dias > 30`.
- Achar que `x > 3` é uma proposição.
- No TypeScript: usar `||` para valor padrão e perder o zero (`quantidade || 1` troca 0 por 1). Use `??` quando zero ou string vazia forem valores válidos.

## 9. No seu setup e no AM Gestão

- **Regras de negócio são lógica:** "o pedido só fecha se estiver pago **e** tiver item **e não** estiver cancelado" vira `pago && itens.length > 0 && !cancelado`. Negando com De Morgan, você acha todos os jeitos de ele **não** fechar, que são exatamente os casos de teste.
- **Escada de inadimplência (exercício do Mês 1):** cada faixa é uma conjunção de fronteiras (`dias >= 30 && dias < 60`); as faixas precisam ser exaustivas e não se sobrepor, o que é uma pergunta de lógica.
- **Quantificadores no código:** ∀ é `every`, ∃ é `some`. "Todos os itens têm estoque" = `itens.every(i => i.estoque > 0)`.
- **Curto-circuito como proteção:** `cliente && cliente.nome` só lê o nome se o cliente existir, porque o `&&` para no primeiro valor falso.
- **Professor:** módulo `mat-linguagem`. **Registro de leitura:** `just livros ler vhslins-matematica-basica --trecho "Cap. 1" --min ... --assunto 0.2 --nota "..."`.

## 10. O que o mercado cobra

Ninguém pede "lógica proposicional" na vaga, mas ela aparece em todo lugar:
- **Júnior:** escrever e ler condições compostas sem errar; entender curto-circuito, `&&`, `||`, `??`; montar casos de teste para uma regra.
- **Pleno e sênior:** simplificar regras de permissão e de negócio, escrever critérios de aceite sem ambiguidade, revisar condições geradas por IA (é comum a IA trocar `>` por `>=` ou negar errado).
- **Perguntas de entrevista comuns:** simplificar `!(a && !b)`; dizer o que `0 || "padrão"` devolve; escrever a negação de uma regra; explicar a diferença entre `||` e `??`.

## 11. Exercícios

Primeiro no papel, sem IA. Depois confira no código.

- **N1 (reconhecer):**
  - Quais são proposições? "Barbacena fica em Minas." · "x + 1 = 5" · "Estude hoje." · "Todo número par é divisível por 2."
  - Diga o valor de p → q quando p = F e q = F, e explique com a ideia de promessa.
- **N2 (aplicar):**
  - Monte a tabela-verdade de (p → q) ∧ (q → p) e compare com p ↔ q.
  - Negue em português, sem usar "não é verdade que": "Todo aluno entregou o trabalho." · "Algum pedido está atrasado." · "O pedido está pago e foi entregue."
- **N3 (combinar e achar o erro):**
  - Simplifique `!(pago && !cancelado)` com De Morgan e explique cada passo.
  - Ache o erro: "Se o cliente paga com Pix, o pagamento é instantâneo. O pagamento foi instantâneo. Logo, foi Pix." Dê o nome da falácia.
  - Escreva a regra da escada de inadimplência como 4 condições e prove, com a tabela das fronteiras, que nenhum número de dias cai em duas faixas.
- **N4 (mini-projeto real):** escreva em TypeScript um gerador de tabela-verdade e um verificador de equivalências por força bruta, como o exemplo abaixo, e use-o para provar as duas leis de De Morgan e a equivalência da contrapositiva. Depois, dê aos seus alunos uma aula de 15 minutos sobre "por que se p então q é verdadeiro quando p é falso".

### Exemplo resolvido (executado com Node 22.23.4; `tsc --strict` sem erros com TypeScript 7.0.2)

```ts
type Formula = (p: boolean, q: boolean) => boolean;

const implica = (p: boolean, q: boolean): boolean => !p || q;

function equivalentes(f: Formula, g: Formula): boolean {
  for (const p of [true, false]) for (const q of [true, false]) if (f(p, q) !== g(p, q)) return false;
  return true;
}

console.log(equivalentes((p, q) => !(p && q), (p, q) => !p || !q)); // true  (De Morgan 1)
console.log(equivalentes((p, q) => !(p || q), (p, q) => !p && !q)); // true  (De Morgan 2)
console.log(equivalentes(implica, (p, q) => implica(!q, !p)));        // true  (contrapositiva)
console.log(equivalentes(implica, (p, q) => implica(q, p)));          // false (recíproca não vale)

const notas = [7, 8, 5, 9];
console.log(notas.every((x) => x >= 6));                               // false (∀)
console.log(notas.some((x) => x < 6));                                 // true  (∃)
console.log([].every((x: number) => x > 100), [].some((x: number) => x > 100)); // true false (vazio)
```

**Um detalhe que o compilador ensina:** ao testar `"" && "foo"` com valores escritos direto no código, o `tsc --strict` acusa erro ("This kind of expression is always falsy"). O TypeScript percebe que a condição nunca muda e trata isso como provável bug. Para demonstrar o comportamento do `&&`, os valores precisam vir de variáveis.

## 12. Fontes (na ordem de uso)

1. **Livro:** VHSlins, *Matemática Básica*, Parte I, **Cap. 1, Linguagem Matemática**: raciocínio, sentenças, conectivos, quantificadores, tabela-verdade, tautologia e contradição, argumento, equivalência e tipos de demonstração. (Página do livro nunca vai para a IA.)
2. **História, fontes de referência:**
   - [Stanford Encyclopedia of Philosophy: The Emergence of First-Order Logic](https://plato.stanford.edu/entries/logic-firstorder-emergence/)
   - [Britannica: History of logic, Gottlob Frege](https://www.britannica.com/topic/history-of-logic/Gottlob-Frege)
   - Shannon, C. E. (1938). *A Symbolic Analysis of Relay and Switching Circuits.* Transactions of the AIEE, 57(12), 713–723.
3. **Documentação:** [MDN: operador lógico AND (&&)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Logical_AND) · [MDN: operador de coalescência nula (??)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
4. **Akita:** nenhum episódio conferido trata de lógica proposicional; os episódios de computação entram no 0.4.

## 13. Como saber que dominou

- [ ] Monto, sem consulta, a tabela-verdade de uma fórmula com 3 proposições.
- [ ] Nego corretamente 10 frases com "todo", "algum", "e" e "ou".
- [ ] Explico em 3 a 5 frases, sem jargão, por que p → q é verdadeiro quando p é falso.
- [ ] Traduzo a regra de fechamento de pedido para lógica, para TypeScript e para a lista de casos de teste.
- [ ] **Registro de entrevista:** contexto (regra de inadimplência com faixas), decisão (fronteiras escritas como conjunções e testadas uma a uma), alternativa descartada (condições soltas sem prova de exaustividade), resultado (número de casos-limite cobertos).
- [ ] **N4:** dei a aula da promessa (p → q) para os meus alunos. Onde e quando: ______
