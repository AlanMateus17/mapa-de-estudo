import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import frontmatter as fm  # noqa: E402


class TestFrontmatter(unittest.TestCase):
    def test_dois_pontos_duas_vezes_quebra_o_yaml(self):
        # O caso do 0.1 em 26/11/2026: "...Psychology: Applied 15(3); ... JEP: Learning..." na mesma linha
        texto = ("---\netapa: 0.1\nfontes:\n  - Richland 2009, Journal of Experimental Psychology: Applied 15(3);"
                 " Butterfield 2001, JEP: Learning 27(6)\n---\n# x\n")
        e = fm.erros(texto)
        self.assertEqual(len(e), 1)
        self.assertIn("YAML inválido", e[0])

    def test_dois_pontos_uma_vez_vira_chave_em_silencio(self):
        texto = "---\netapa: 0.1\nfontes:\n  - Richland 2009, Journal of Experimental Psychology: Applied 15(3)\n---\n# x\n"
        e = fm.erros(texto)
        self.assertEqual(len(e), 1)
        self.assertIn("virou chave: valor", e[0])

    def test_com_aspas_vale(self):
        texto = '---\netapa: 0.1\nfontes:\n  - "Richland 2009, Journal of Experimental Psychology: Applied 15(3)"\n---\n# x\n'
        self.assertEqual(fm.erros(texto), [])

    def test_sem_frontmatter_ou_sem_fechar_ou_nao_mapa(self):
        self.assertIn("não começa", fm.erros("# título\n")[0])
        self.assertIn("fechamento", fm.erros("---\netapa: 1\n")[0])
        self.assertIn("mapa", fm.erros("---\n- a\n- b\n---\n")[0])

    def test_todos_os_assuntos_do_repositorio(self):
        self.assertEqual(fm.conferir(), [])


if __name__ == "__main__":
    unittest.main()
