#!/usr/bin/env python3
"""Confere o frontmatter de todos os arquivos de assunto (assuntos/**/*.md): começa com ---, é YAML válido, é um mapa
e nenhum item de lista virou "chave: valor" por causa de um ": " sem aspas.

    python3 scripts/frontmatter.py      # o CI roda; sai com 1 e lista cada erro com arquivo e linha

Pega o erro de 26/11/2026: em fontes-conferidas, um texto com ": " (Journal of Experimental Psychology: Applied)
sem aspas quebrava o YAML do 0.1, e quem lê o frontmatter (Obsidian, o Professor do dev-setup) via outra coisa.
Regra: item de lista com ": " dentro vai entre aspas duplas.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]


def erros(texto: str) -> list[str]:
    """Erros do frontmatter de um arquivo (lista vazia = válido)."""
    if not texto.startswith("---\n"):
        return ["não começa com o frontmatter (---)"]
    partes = texto.split("---\n", 2)
    if len(partes) < 3:
        return ["frontmatter sem o --- de fechamento"]
    try:
        dados = yaml.safe_load(partes[1])
    except yaml.YAMLError as e:
        marca = getattr(e, "problem_mark", None)
        onde = f"linha {marca.line + 2}: " if marca else ""  # +2: a linha 1 do arquivo é o ---
        problema = getattr(e, "problem", None) or str(e).splitlines()[0]
        return [f"{onde}YAML inválido ({problema}); ponha entre aspas duplas o texto que tem ': '"]
    if not isinstance(dados, dict):
        return ["o frontmatter não é um mapa de campos (chave: valor)"]
    # Com um só ": " sem aspas o YAML continua válido, mas o item da lista vira um par chave: valor em silêncio.
    return [f"{campo}: o item '{_texto(item)}' virou chave: valor; ponha entre aspas duplas"
            for campo, valor in dados.items() if isinstance(valor, list)
            for item in valor if isinstance(item, dict)]


def _texto(item: dict) -> str:
    return "; ".join(f"{k}: {v}" for k, v in item.items())[:80]


def conferir(raiz: Path = RAIZ) -> list[str]:
    saida = []
    for p in sorted((raiz / "assuntos").rglob("*.md")):
        saida += [f"{p.relative_to(raiz)}: {e}" for e in erros(p.read_text(encoding="utf-8"))]
    return saida


def main() -> int:
    problemas = conferir()
    for p in problemas:
        print(p)
    if problemas:
        return 1
    print("Frontmatter de todos os assuntos: YAML válido.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
