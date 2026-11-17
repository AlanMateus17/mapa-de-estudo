---
tags: [estudo, assunto, matematica, logica]
area: 01 · Matemática
etapa: 0.2
nivel-alvo: N3 (montar e simplificar qualquer expressão lógica sem consulta, e traduzir regras de negócio para lógica e para código)
quando: M1, semana 1 (sexta, 6h–11h)
professor: mat-linguagem
prereq: [0.1]
livro: VHSlins, Matemática Básica, Parte I, Cap. 1 (Linguagem Matemática)
status: a-estudar
verificado-em: 2026-11-17
versoes: [Node.js 22.23.4 (executa .ts direto), TypeScript 7.0.2 (tsc --strict sem erros em todos os exemplos)]
fontes-conferidas:
  - Stanford Encyclopedia of Philosophy, "The Emergence of First-Order Logic" (Boole 1847, Frege 1879, Peirce 1885)
  - Encyclopaedia Britannica, "History of logic: Gottlob Frege"
  - Shannon 1938, "A Symbolic Analysis of Relay and Switching Circuits", Transactions of the AIEE 57(12) (tese de mestrado no MIT, 1937)
  - MDN, operadores lógicos AND (&&) e de coalescência nula (??)
pendente:
  - Nenhum episódio do Akita sobre lógica proposicional foi conferido; nenhum é citado
  - A ordem de precedência entre → e ↔ varia entre livros; confira a convenção do VHSlins
atualizado: 2026-11-17
---

# Linguagem matemática e lógica

> **Em uma frase:** lógica é o conjunto de regras para dizer exatamente o que é verdade a partir de frases simples ligadas por **e, ou, não, se… então** e por **para todo** e **existe**, sem ambiguidade.
> **Nível-alvo:** N3. Você monta a tabela-verdade de qualquer expressão, simplifica com as leis de De Morgan, nega frases com "todo" e "algum" sem errar e traduz uma regra de negócio para lógica e para um `if`.
> **Os 20% que resolvem 80%:**
> 1. Os conectivos e a tabela-verdade de cada um.
> 2. **Se p então q** só é falso quando p é verdadeiro e q é falso.
> 3. As **leis de De Morgan**: ¬(p ∧ q) ≡ ¬p ∨ ¬q e ¬(p ∨ q) ≡ ¬p ∧ ¬q.
> 4. **Negar um quantificador:** "não é verdade que todos…" = "existe algum que não…".
> 5. **Contrapositiva** (¬q → ¬p) vale o mesmo que p → q; a **recíproca** (q → p) não.

---

## Roteiro (blocos de 25 minutos, sexta de manhã)

| Bloco | O que fazer | Seções |
|---|---|---|
| 1 | Diagnóstico. Depois leia o início do Cap. 1 do VHSlins (raciocínio, sentenças, conectivos) | 0 e livro |
| 2 | Por que existe e o que é; tabela-verdade de cor | 1 e 2 |
| 3 | Como funciona por baixo; checklist de conceitos | 3 e 4 |
| 4 | Livro: quantificadores, tautologia, argumento e equivalência | livro |
| 5 | Exemplo resolvido e exemplo com lacunas | 11 |
| 6 | Exemplo sozinho; exercícios N1 e N2 | 11 e 12 |
| 7 | Exercícios N3; confira no gabarito; `just erro` para cada erro | 12, 13 e 15 |
| 8 | Erros comuns, setup, mercado; livro: tipos de demonstração (só reconhecer) | 5 a 10 e livro |
| 9 | Exercício N4 (código) | 12 |
| 10 | Resumo de uma tela, cartões do Anki com as suas palavras e registros | 14 e 15 |

Cada bloco termina com o protocolo de fim de bloco (assunto 0.1): feche, reconstrua de cabeça, explique em 3 a 5 frases, anote o tempo.

## 0. Antes de começar: diagnóstico

Responda sem consulta, em 3 minutos:
1. Qual é a negação de "todos os pedidos foram entregues"?
2. Se p é falso e q é verdadeiro, qual é o valor de "se p então q"?
3. Simplifique `!(a || b)` sem o `!` do lado de fora.

Respostas na seção 13. **Acertou as 3?** Leia rápido as seções 2 e 4 e vá direto para os exercícios N3. **Errou alguma?** Siga o roteiro inteiro.

## 1. Por que isso existe (o problema e a história)

A linguagem do dia a dia é ambígua. "Você pode levar sorvete ou bolo" quer dizer um dos dois, ou os dois? "Todos os alunos não fizeram a prova" quer dizer que ninguém fez, ou que nem todos fizeram? Em matemática, num contrato e num programa, a ambiguidade custa caro. A lógica dá um sentido único a cada frase.

- **Aristóteles** sistematizou as regras do raciocínio válido na Grécia antiga.
- **George Boole** fez a virada no século XIX: em *The Mathematical Analysis of Logic* (1847) e em *An Investigation of the Laws of Thought* (1854), escreveu o raciocínio como **álgebra**, com símbolos e regras de cálculo. Daí vem o nome "booleano".
- **Gottlob Frege**, em *Begriffsschrift* (1879), introduziu de forma cuidadosa os **quantificadores** ("para todo", "existe") e as variáveis. Charles S. Peirce chegou a ideias parecidas de forma independente, em 1885.
- **Claude Shannon**, na tese de mestrado no MIT (1937, publicada em 1938), mostrou que a álgebra de Boole descreve circuitos de relés e interruptores. É por isso que o computador funciona com lógica: cada porta lógica de um processador é um conectivo de Boole feito com transistores (assunto 0.4).

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
| **Ou exclusivo** p ⊕ q (XOR) | V quando exatamente uma for V | "pagar com Pix ou com cartão, mas não com os dois" |
| **Condicional** p → q ("se p então q") | F só quando p é V e q é F | "Se a compra passa de R$ 200, então tem desconto" |
| **Bicondicional** p ↔ q ("se e somente se") | V quando p e q têm o mesmo valor | "o pedido está pago ↔ o saldo devedor é zero" |
| **Tautologia** | Sempre V, em toda linha da tabela | p ∨ ¬p |
| **Contradição** | Sempre F | p ∧ ¬p |
| **Contingência** | Às vezes V, às vezes F | p ∧ q |
| **Equivalência** (≡) | Duas fórmulas com a mesma tabela-verdade | p → q ≡ ¬p ∨ q |
| **Quantificador universal** ∀ | "Para todo" | ∀x (x é aluno → x fez a prova) |
| **Quantificador existencial** ∃ | "Existe pelo menos um" | ∃x (nota de x < 6) |
| **Argumento** | Premissas que levam a uma conclusão; é **válido** se, sempre que as premissas forem V, a conclusão também for | |

### Tabela-verdade dos conectivos

| p | q | ¬p | p ∧ q | p ∨ q | p ⊕ q | p → q | p ↔ q |
|---|---|---|---|---|---|---|---|
| V | V | F | V | V | F | V | V |
| V | F | F | F | V | V | **F** | F |
| F | V | V | F | V | V | V | F |
| F | F | V | F | F | F | V | V |

**Por que p → q é V quando p é F?** Pense numa promessa: "se você tirar 10, ganha um presente". Se você não tirou 10, a promessa não foi quebrada, ganhando ou não o presente. A promessa só é quebrada na linha p = V, q = F.

**XOR e bicondicional são opostos:** p ⊕ q ≡ ¬(p ↔ q). E p ⊕ q ≡ (p ∨ q) ∧ ¬(p ∧ q): "um ou outro, mas não os dois".

### Precedência (qual conectivo vem primeiro)

A convenção mais comum, do que liga mais forte para o que liga mais fraco: **¬**, depois **∧**, depois **∨**, depois **→**, depois **↔**. Então ¬p ∧ q ∨ r se lê ((¬p) ∧ q) ∨ r. Alguns livros tratam → e ↔ de outro jeito; **na dúvida, use parênteses**.

No TypeScript é igual nos três primeiros: `!` antes de `&&` antes de `||`. Por isso `true || false && false` dá `true` (o `&&` é feito primeiro), e `(true || false) && false` dá `false`.

### Ordem dos quantificadores

Com dois quantificadores diferentes, **a ordem muda o sentido**:
- ∀ cliente ∃ pedido (o pedido é do cliente): "todo cliente tem pelo menos um pedido". Cada cliente pode ter o seu.
- ∃ pedido ∀ cliente (o pedido é do cliente): "existe um único pedido que é de todos os clientes ao mesmo tempo". Bem mais forte, e quase sempre falso.

Com dois quantificadores **iguais**, a ordem não importa: ∀x ∀y ≡ ∀y ∀x.

## 3. Como funciona por baixo

- **Cada linha da tabela é um caso.** Com n proposições há 2ⁿ linhas. Duas fórmulas são equivalentes quando batem nas 2ⁿ linhas, e isso dá para conferir por força bruta (o exemplo resolvido da seção 11 faz exatamente isso).
- **Quantificador é um "e" ou um "ou" sobre um conjunto.** Num conjunto finito, ∀x P(x) é P(x₁) ∧ P(x₂) ∧ … e ∃x P(x) é P(x₁) ∨ P(x₂) ∨ …. Por isso a negação troca um pelo outro, como em De Morgan: ¬∀x P(x) ≡ ∃x ¬P(x) e ¬∃x P(x) ≡ ∀x ¬P(x).
- **Conjunto vazio:** "todo elemento do vazio satisfaz P" é **verdadeiro** (não há contraexemplo) e "existe elemento do vazio com P" é **falso**. No TypeScript, `[].every(...)` dá `true` e `[].some(...)` dá `false`, pela mesma razão.
- **Na máquina:** Shannon mostrou que interruptores em série fazem "e" e em paralelo fazem "ou". Hoje são transistores dentro das portas lógicas do processador. O XOR é a porta que soma dois bits sem o "vai um" (assunto 0.4).

## 4. Conceitos que você precisa dominar

- [ ] Reconhecer o que é e o que não é proposição.
- [ ] Os conectivos (¬, ∧, ∨, ⊕, →, ↔) e as tabelas-verdade de cor.
- [ ] Precedência e uso de parênteses.
- [ ] Montar a tabela-verdade de uma fórmula composta, com 2ⁿ linhas.
- [ ] Identificar tautologia, contradição e contingência.
- [ ] Provar equivalências pela tabela: p → q ≡ ¬p ∨ q; p ↔ q ≡ (p → q) ∧ (q → p); p ⊕ q ≡ ¬(p ↔ q).
- [ ] **Leis de De Morgan** e dupla negação (¬¬p ≡ p).
- [ ] Distributiva: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r).
- [ ] Condicional, **recíproca** (q → p), **inversa** (¬p → ¬q) e **contrapositiva** (¬q → ¬p): só a contrapositiva é equivalente.
- [ ] Condição **suficiente** (p em p → q) e **necessária** (q em p → q).
- [ ] Quantificadores ∀ e ∃, a **negação** de cada um e a **ordem** quando estão juntos.
- [ ] Argumento válido × conclusão verdadeira.
- [ ] *Modus ponens* (p → q, p, logo q) e *modus tollens* (p → q, ¬q, logo ¬p).
- [ ] As duas falácias mais comuns: **afirmar o consequente** (p → q, q, logo p) e **negar o antecedente** (p → q, ¬p, logo ¬q).
- [ ] **Tipos de demonstração** (só reconhecer, nível N1 aqui): direta, por contrapositiva, por absurdo e por contraexemplo.

## 5. Qualidades

- **Elimina ambiguidade:** uma frase lógica tem um sentido só.
- **É verificável mecanicamente:** a tabela-verdade decide qualquer equivalência proposicional.
- **Serve para tudo o que vem depois:** conjuntos (0.3), circuitos (0.4), `if` e testes (0.6, 2.4), SQL (4.2), requisitos e critérios de aceite (4.5).
- **Ensina a negar direito,** o que é metade do trabalho de achar bug: "o que precisa ser verdade para isso dar errado?"

## 6. Defeitos, limites e críticas

- **O "ou" da lógica é inclusivo;** no português do dia a dia, muitas vezes é exclusivo. Traduzir regra de negócio exige perguntar qual dos dois o cliente quis dizer (∨ ou ⊕).
- **O "se… então" lógico não é causa.** "Se 2 + 2 = 5, então a Lua é de queijo" é verdadeiro na lógica (antecedente falso). Isso estranha no começo e não descreve causalidade.
- **A tabela-verdade explode:** com 20 proposições são mais de um milhão de linhas. Para fórmulas grandes, usa-se álgebra (as leis) e, em computação, algoritmos especializados (SAT).
- **Lógica proposicional não fala de "todos" e "alguns";** para isso é preciso a lógica de predicados, que é bem mais rica e mais difícil.
- **No JavaScript, `&&` e `||` não devolvem só `true` ou `false`:** devolvem um dos operandos (exemplo executado na seção 9). É uma fonte clássica de bug.

## 7. Quando usar e quando não usar

- **Use** sempre que escrever uma condição (`if`, filtro, `WHERE`), um critério de aceite, um teste ou uma regra de permissão.
- **Use a contrapositiva** quando a frase direta for difícil de verificar: "se o pedido foi pago, então tem comprovante" equivale a "se não tem comprovante, não foi pago".
- **Simplifique com De Morgan** antes de escrever um `if` com muitos `!`.
- **Não use** a tabela-verdade para fórmulas enormes; passe para as leis algébricas.

## 8. Erros comuns

- Tratar a recíproca como equivalente: "todo pagamento por Pix é instantâneo" não quer dizer "todo pagamento instantâneo é por Pix".
- Negar "todos são" como "todos não são". A negação certa de "todos os pedidos foram entregues" é "**algum** pedido não foi entregue".
- Negar "p e q" como "não p e não q" (o certo é "não p **ou** não q").
- Usar "ou" inclusivo quando a regra era exclusiva, e vice-versa.
- Trocar a ordem de dois quantificadores diferentes.
- Confiar na precedência em vez de usar parênteses numa expressão longa.
- Esquecer a fronteira ao traduzir: "a partir de 30 dias" é `dias >= 30`, não `dias > 30`.
- Achar que `x > 3` é uma proposição.
- No TypeScript: usar `||` para valor padrão e perder o zero (`quantidade || 1` troca 0 por 1). Use `??` quando zero ou string vazia forem valores válidos.

## 9. No seu setup e no AM Gestão

- **Regras de negócio são lógica:** "o pedido só fecha se estiver pago **e** tiver item **e não** estiver cancelado" vira `pago && itens.length > 0 && !cancelado`. Negando com De Morgan, você acha todos os jeitos de ele **não** fechar, que são exatamente os casos de teste.
- **Escada de inadimplência (exercício do Mês 1):** cada faixa é uma conjunção de fronteiras (`dias >= 30 && dias < 60`); as faixas precisam ser exaustivas e não se sobrepor, o que é uma pergunta de lógica.
- **Quantificadores no código:** ∀ é `every`, ∃ é `some`. "Todos os itens têm estoque" = `itens.every(i => i.estoque > 0)`.
- **Curto-circuito como proteção:** `cliente && cliente.nome` só lê o nome se o cliente existir, porque o `&&` para no primeiro valor falso.
- **O que `&&`, `||` e `??` devolvem** (executado com Node 22.23.4 e conferido com `tsc --strict`, TypeScript 7.0.2; os valores vêm de funções para o compilador não acusar condição sempre verdadeira ou sempre falsa):

```ts
function mostrar(rotulo: string, valor: unknown): void {
  console.log(rotulo, JSON.stringify(valor));
}
const quantidade: number = Number("0");
const nome: string = String("");
mostrar("0 || 1     ->", quantidade || 1);      // 1   (o || troca o zero)
mostrar("0 ?? 1     ->", quantidade ?? 1);      // 0   (o ?? só troca null e undefined)
mostrar('"" || "?"  ->', nome || "?");          // "?"
mostrar('"" && "x"  ->', nome && "x");          // ""  (para no primeiro falso e devolve ele)
mostrar('"a" && "x" ->', String("a") && "x");   // "x" (tudo verdadeiro: devolve o último)
```

  Regra: `&&` devolve o primeiro valor falso, ou o último se todos forem verdadeiros; `||` devolve o primeiro verdadeiro, ou o último; `??` devolve o da esquerda, a não ser que ele seja `null` ou `undefined`.
- **Revisão de código de IA (Trilha R):** confira toda condição que a IA escrever: fronteira (`>` ou `>=`), negação, "ou" inclusivo ou exclusivo e parênteses.
- **Professor:** módulo `mat-linguagem`.

## 10. O que o mercado cobra

Ninguém pede "lógica proposicional" na vaga, mas ela aparece em todo lugar:
- **Júnior:** escrever e ler condições compostas sem errar; entender curto-circuito, `&&`, `||`, `??`; montar casos de teste para uma regra.
- **Pleno e sênior:** simplificar regras de permissão e de negócio, escrever critérios de aceite sem ambiguidade, revisar condições geradas por IA.
- **Perguntas de entrevista comuns:** simplificar `!(a && !b)`; dizer o que `0 || "padrão"` devolve; escrever a negação de uma regra; explicar a diferença entre `||` e `??`; explicar o XOR.

## 11. Exemplos com retirada de apoio

### 11.1 Resolvido: provar as leis de De Morgan por força bruta

**O problema:** mostrar que ¬(p ∧ q) e ¬p ∨ ¬q têm sempre o mesmo valor.

**O raciocínio:** duas fórmulas são equivalentes se baterem em todas as 2ⁿ linhas. Com 2 proposições são 4 linhas: dá para testar todas.

```ts
type Formula = (p: boolean, q: boolean) => boolean;

const implica = (p: boolean, q: boolean): boolean => !p || q;

// Testa as 4 combinações; se alguma linha diferir, não são equivalentes.
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

**Por que cada passo:** `p → q` é escrito como `!p || q` porque as duas têm a mesma tabela (essa equivalência é o coração do exemplo). O laço duplo gera as 4 linhas. Um único `return false` basta para provar que **não** são equivalentes: um contraexemplo derruba uma regra geral.

### 11.2 Com lacunas: XOR

Complete os `___` antes de olhar o gabarito. A função deve dar V quando exatamente uma das duas for V.

```text
const xor = (p: boolean, q: boolean): boolean => p ___ q;

// confira contra a definição "um ou outro, mas não os dois":
// xor(p, q) === ((p ___ q) && !(p ___ q))
```

### 11.3 Sozinho: a ordem dos quantificadores

Com `clientes = ["Ana", "Bia"]` e um pedido de cada uma, escreva em TypeScript, com `every` e `some`:
1. "todo cliente tem pelo menos um pedido";
2. "existe um pedido que é de todos os clientes".

Diga o valor de cada um **antes** de rodar. Resposta na seção 13.

## 12. Exercícios

Primeiro no papel, sem IA. Depois confira no gabarito. Cada erro: `just erro 0.2 "o erro" --certo "o certo"`.

- **N1 (reconhecer):**
  1. Quais são proposições? "Barbacena fica em Minas." · "x + 1 = 5" · "Estude hoje." · "Todo número par é divisível por 2."
  2. Diga o valor de p → q quando p = F e q = F, e explique com a ideia de promessa.
  3. Calcule `true || false && false` e explique a precedência.
- **N2 (aplicar):**
  1. Monte a tabela-verdade de (p → q) ∧ (q → p) e compare com p ↔ q.
  2. Negue em português, sem usar "não é verdade que": "Todo aluno entregou o trabalho." · "Algum pedido está atrasado." · "O pedido está pago e foi entregue."
  3. A regra "o cliente paga com Pix ou com cartão" é ∨ ou ⊕ num caixa que não aceita pagamento dividido? Justifique.
- **N3 (combinar e achar o erro):**
  1. Simplifique `!(pago && !cancelado)` com De Morgan e explique cada passo.
  2. Ache o erro: "Se o cliente paga com Pix, o pagamento é instantâneo. O pagamento foi instantâneo. Logo, foi Pix." Dê o nome da falácia.
  3. Escreva uma escada de inadimplência com 4 faixas (ativo, atraso, restrito, suspenso) e prove que cada número de dias cai em exatamente uma faixa. Use os limites da sua regra; os do gabarito são de exemplo.
- **N4 (mini-projeto real):**
  1. No repositório `logica-ts`, escreva um gerador de tabela-verdade e um verificador de equivalências (como o 11.1) e use-o para provar De Morgan, a contrapositiva e p ⊕ q ≡ ¬(p ↔ q).
  2. Escreva a verificação automática da escada de inadimplência para todos os dias de 0 a 400.
  3. Dê aos seus alunos uma aula de 15 minutos sobre "por que se p então q é verdadeiro quando p é falso".

## 13. Gabarito comentado

**Diagnóstico**
1. "**Algum** pedido não foi entregue." O erro típico é "todos os pedidos não foram entregues", que diz outra coisa: que nenhum foi entregue.
2. **V.** Com p falso, a promessa não foi testada, então não foi quebrada.
3. `!a && !b` (De Morgan: o `!` entra e o `||` vira `&&`).

**N1**
1. São proposições: "Barbacena fica em Minas" (V) e "Todo número par é divisível por 2" (V). "x + 1 = 5" é sentença aberta (depende de x). "Estude hoje" é ordem, não tem valor V ou F.
2. **V.** Mesmo argumento do diagnóstico.
3. **`true`.** O `&&` é feito antes: `false && false` dá `false`, e `true || false` dá `true`. Com parênteses `(true || false) && false`, o resultado vira `false`.

**N2**
1. A tabela dá V, F, F, V nas linhas VV, VF, FV, FF, igual a p ↔ q. Por isso se diz "se e somente se" = "se" nos dois sentidos.
2. "**Algum** aluno não entregou o trabalho." · "**Nenhum** pedido está atrasado" (= todo pedido não está atrasado). · "O pedido **não** está pago **ou não** foi entregue."
3. **⊕ (exclusivo).** Se o caixa não aceita dividir, pagar com os dois ao mesmo tempo é impossível ou proibido. Num caixa que aceita dividir, vira ∨. A lógica obriga a fazer essa pergunta ao cliente.

**N3**
1. `!(pago && !cancelado)` → De Morgan: `!pago || !!cancelado` → dupla negação: `!pago || cancelado`. Lendo em português: "o pedido não está liberado quando não foi pago ou foi cancelado". A versão simplificada também já lista os dois casos de teste.
2. **Afirmar o consequente.** "Se Pix, então instantâneo" não diz nada sobre o que acontece quando o pagamento é instantâneo: outro meio também pode ser instantâneo. Só a contrapositiva vale: "não foi instantâneo, logo não foi Pix".
3. Com limites de exemplo (ativo < 1 dia; atraso de 1 a 29; restrito de 30 a 59; suspenso a partir de 60): as fronteiras a testar são 0, 1, 29, 30, 59 e 60. As faixas usam `>=` no início e `<` no fim, e o fim de uma é o início da seguinte; por isso não sobra buraco nem sobreposição. O código abaixo confere todos os dias de 0 a 400.

```ts
type Status = "ativo" | "atraso" | "restrito" | "suspenso";
const faixas: Array<[Status, (d: number) => boolean]> = [
  ["ativo", (d) => d < 1],
  ["atraso", (d) => d >= 1 && d < 30],
  ["restrito", (d) => d >= 30 && d < 60],
  ["suspenso", (d) => d >= 60],
];
let ok = true;
for (let d = 0; d <= 400; d++) {
  const quantas = faixas.filter(([, f]) => f(d)).length;
  if (quantas !== 1) ok = false;
}
console.log("cada dia em exatamente uma faixa:", ok); // true
```

**11.2 (XOR com lacunas)**

```ts
const xor = (p: boolean, q: boolean): boolean => p !== q;
console.log([true, false].every((p) => [true, false].every((q) => xor(p, q) === ((p || q) && !(p && q))))); // true
```

As lacunas são `!==`, `||` e `&&`. Comparar dois booleanos com `!==` é exatamente o XOR: dá V quando são diferentes.

**11.3 (ordem dos quantificadores)**

```ts
const clientes = ["Ana", "Bia"];
const pedidos = [{ id: 1, cliente: "Ana" }, { id: 2, cliente: "Bia" }];
console.log(clientes.every((cl) => pedidos.some((pd) => pd.cliente === cl))); // true
console.log(pedidos.some((pd) => clientes.every((cl) => pd.cliente === cl))); // false
```

O primeiro é V: cada cliente tem o seu pedido. O segundo é F: nenhum pedido é de Ana e de Bia ao mesmo tempo. Trocar a ordem trocou o sentido.

**Um detalhe que o compilador ensina:** ao testar `"" && "foo"` com os valores escritos direto no código, o `tsc --strict` acusa erro ("This kind of expression is always falsy"), porque percebe que a condição nunca muda e trata isso como provável bug. Para demonstrar o `&&`, os valores precisam vir de variáveis.

## 14. Resumo de uma tela

- **Proposição:** V ou F, nunca os dois. "x > 3" não é (é sentença aberta).
- **p → q** só é F em V → F. **p ↔ q:** mesmo valor. **p ⊕ q:** valores diferentes.
- **Precedência:** ¬, ∧, ∨, →, ↔. Na dúvida, parênteses. No código: `!`, `&&`, `||`.
- **De Morgan:** ¬(p ∧ q) ≡ ¬p ∨ ¬q · ¬(p ∨ q) ≡ ¬p ∧ ¬q.
- **Quantificadores:** ¬∀ ≡ ∃¬ · ¬∃ ≡ ∀¬. Ordem de ∀ e ∃ juntos muda o sentido. Vazio: ∀ dá V, ∃ dá F.
- **Só a contrapositiva** (¬q → ¬p) equivale a p → q. Recíproca e inversa não.
- **Falácias:** afirmar o consequente, negar o antecedente.
- **Código:** ∀ = `every`, ∃ = `some`; `&&`/`||` devolvem um operando; `??` preserva 0 e "".

## 15. Registros no setup

- **Leitura:** `just livros ler vhslins-matematica-basica --trecho "Cap. 1" --min 50 --assunto 0.2 --nota "o que entendi, com as minhas palavras"`
- **Cada erro nos exercícios:** `just erro 0.2 "neguei 'todos' como 'todos não'" --certo "algum não"`
- **Algo do setup travou ou foi manual** (por exemplo, rodar o TypeScript): `just atrito "..." --area estudo`
- **Fim do assunto:** `just professor fechar mat-linguagem MINUTOS` e preencha a ficha dupla (a aula da promessa é uma boa ficha) e o registro de entrevista.
- **Anki:** um cartão por item da seção 14, com as suas palavras, pedindo para **usar** ("negue: …", "simplifique: …"), não para reconhecer.

## 16. Fontes (na ordem de uso)

1. **Livro:** VHSlins, *Matemática Básica*, Parte I, **Cap. 1, Linguagem Matemática**: raciocínio, sentenças, conectivos, quantificadores, tabela-verdade, tautologia e contradição, argumento, equivalência e tipos de demonstração. (Página do livro nunca vai para a IA.)
2. **História, fontes de referência:**
   - [Stanford Encyclopedia of Philosophy: The Emergence of First-Order Logic](https://plato.stanford.edu/entries/logic-firstorder-emergence/)
   - [Britannica: History of logic, Gottlob Frege](https://www.britannica.com/topic/history-of-logic/Gottlob-Frege)
   - Shannon, C. E. (1938). *A Symbolic Analysis of Relay and Switching Circuits.* Transactions of the AIEE, 57(12), 713–723.
3. **Documentação:** [MDN: operador lógico AND (&&)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Logical_AND) · [MDN: operador de coalescência nula (??)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
4. **Akita:** nenhum episódio conferido trata de lógica proposicional; os episódios de computação entram no 0.4.

## 17. Como saber que dominou

- [ ] Acerto o diagnóstico da seção 0 sem pensar.
- [ ] Monto, sem consulta, a tabela-verdade de uma fórmula com 3 proposições.
- [ ] Nego corretamente 10 frases com "todo", "algum", "e" e "ou".
- [ ] Explico em 3 a 5 frases, sem jargão, por que p → q é verdadeiro quando p é falso.
- [ ] Traduzo a regra de fechamento de pedido para lógica, para TypeScript e para a lista de casos de teste.
- [ ] **Registro de entrevista:** contexto (regra de inadimplência com faixas), decisão (fronteiras escritas como conjunções e verificadas para todos os dias), alternativa descartada (condições soltas sem prova de exaustividade), resultado (número de casos-limite cobertos).
- [ ] **N4:** dei a aula da promessa (p → q) para os meus alunos. Onde e quando: ______
