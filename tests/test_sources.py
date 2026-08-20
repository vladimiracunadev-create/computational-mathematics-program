"""El registro de fuentes y su verificador offline."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from computational_math import curriculum, sources  # noqa: E402

import refresh_sources  # noqa: E402  isort:skip
import verify_sources  # noqa: E402  isort:skip


class TestComparacionDeTitulos(unittest.TestCase):
    """El comparador decide si un localizador describe la obra citada.

    Se prueba sin red: son las reglas, no las respuestas de las autoridades.
    """

    IGUALES = [
        ("Very Deep Convolutional Networks (VGG)",
         "Very Deep Convolutional Networks for Large-Scale Image Recognition"),
        ("Score-Based Generative Modeling through SDEs",
         "Score-Based Generative Modeling through Stochastic Differential Equations"),
        ("The ASA statement on p-values",
         "The ASA Statement on <i>p</i>-Values: Context, Process, and Purpose"),
        ("Precalculus", "Precalculus: Mathematics for Calculus"),
        ("Introduction to Linear Algebra", "Introduction to linear algebra"),
        ("All of Statistics", "All of Statistics: A Concise Course in Statistical Inference"),
    ]

    DISTINTAS = [
        ("Basic Mathematics", "Problems in Geometry"),
        ("Calculus", "Precalculus"),
        ("Algebra", "Linear Algebra Done Right"),
        ("Categorical Data Analysis", "Analysis of Ordinal Categorical Data"),
    ]

    def test_reconoce_la_misma_obra(self):
        for citado, resuelto in self.IGUALES:
            self.assertGreaterEqual(
                refresh_sources.parecido(citado, resuelto),
                refresh_sources.UMBRAL_TITULO,
                f"{citado!r} debería reconocer a {resuelto!r}",
            )

    def test_no_confunde_obras_distintas(self):
        for citado, resuelto in self.DISTINTAS:
            self.assertLess(
                refresh_sources.parecido(citado, resuelto),
                refresh_sources.UMBRAL_TITULO,
                f"{citado!r} no debería aceptar a {resuelto!r}",
            )


class TestIdentificadores(unittest.TestCase):
    def test_isbn13_valida_el_digito_de_control(self):
        self.assertTrue(sources.isbn13_valid("978-0-262-03561-3"))
        self.assertTrue(sources.isbn13_valid("9780387952840"))
        self.assertFalse(sources.isbn13_valid("9780262035614"))  # dígito cambiado
        self.assertFalse(sources.isbn13_valid("0262035618"))     # ISBN-10
        self.assertFalse(sources.isbn13_valid(""))

    def test_doi_se_normaliza(self):
        self.assertEqual(sources.normalise_doi("https://doi.org/10.1145/103162.103163"),
                         "10.1145/103162.103163")
        self.assertEqual(sources.normalise_doi("DOI:10.1137/1.9780898718027"),
                         "10.1137/1.9780898718027")

    def test_identificadores_se_extraen_de_la_url_citada(self):
        springer = sources.derive_identifiers("https://link.springer.com/book/10.1007/978-0-387-40065-5")
        self.assertEqual(springer["doi"], "10.1007/978-0-387-40065-5")
        self.assertEqual(springer["isbn13"], "9780387400655")

        arxiv = sources.derive_identifiers("https://arxiv.org/abs/1706.03762")
        self.assertEqual(arxiv["doi"], "10.48550/arxiv.1706.03762")

        suelta = sources.derive_identifiers("https://www.deeplearningbook.org/")
        self.assertIsNone(suelta["doi"])
        self.assertIsNone(suelta["isbn13"])

    def test_localizador_canonico_por_tipo(self):
        self.assertEqual(
            sources.canonical_locator({"type": "book", "isbn13": "9780262035613"}),
            "https://openlibrary.org/isbn/9780262035613",
        )
        self.assertEqual(
            sources.canonical_locator({"type": "paper", "doi": "10.1145/103162.103163"}),
            "https://doi.org/10.1145/103162.103163",
        )


class TestEtiquetas(unittest.TestCase):
    def test_se_separan_autores_titulo_y_año(self):
        datos = sources.parse_label("Strang, G. *Introduction to Linear Algebra*, 6ª ed., 2023, cap. 5")
        self.assertEqual(datos["authors"], ["Strang, G."])
        self.assertEqual(datos["title"], "Introduction to Linear Algebra")
        self.assertEqual(datos["published"], "2023")

    def test_las_iniciales_no_se_confunden_con_otro_autor(self):
        datos = sources.parse_label("Hastie, T.; Tibshirani, R.; Friedman, J. *The Elements*, 2009")
        self.assertEqual(datos["authors"], ["Hastie, T.", "Tibshirani, R.", "Friedman, J."])


class TestAreas(unittest.TestCase):
    """El vocabulario que cruza el tema de una obra con el de la clase."""

    def test_toda_parte_declara_lo_que_ensena(self):
        for parte in curriculum.parts():
            areas = sources.part_areas(parte["id"])
            self.assertTrue(areas["nucleo"], f"parte {parte['id']} sin núcleo")
            transversales = set(sources.transversal_areas())
            self.assertTrue(
                set(areas["nucleo"]) - transversales,
                f"la parte {parte['id']} solo declara áreas transversales",
            )

    def test_toda_clase_tiene_area_y_toda_obra_declara_la_suya(self):
        for clase in curriculum.classes():
            self.assertTrue(sources.class_areas(clase["id"]), f"clase {clase['id']}")
        registro = sources.load_registry()
        for entrada in registro["entries"]:
            self.assertTrue(entrada.get("covers"), f"{entrada['id']} no declara covers")

    def test_una_obra_fuera_de_tema_no_pasa_el_cruce(self):
        """La comprobación tiene filo: un libro de probabilidad no vale en IEEE 754."""
        registro = sources.load_registry()
        por_id = {e["id"]: e for e in registro["entries"]}
        fuera = sources.citation_fit(
            "028", por_id["blitzstein-introduction-to-probability"]["key"], registro
        )
        self.assertEqual(fuera.role, "fuera-de-tema")
        dentro = sources.citation_fit(
            "028", por_id["goldberg-what-every-computer-scientist-should-know-about"]["key"],
            registro,
        )
        self.assertEqual(dentro.role, "ancla")


class TestBibliografiaDeCadaClase(unittest.TestCase):
    def test_cada_clase_declara_por_que_cita_cada_obra(self):
        for clase in curriculum.classes():
            bloque = sources.class_block(clase["id"])
            self.assertTrue(bloque, f"clase {clase['id']} sin bibliografía")
            for linea in bloque:
                self.assertIn(" — ", linea, f"clase {clase['id']}")
                self.assertNotIn("fuera del tema", linea, f"clase {clase['id']}")

    def test_cada_clase_se_ancla_en_una_obra_de_su_tema(self):
        registro = sources.load_registry()
        for clase in curriculum.classes():
            papeles = {
                sources.citation_fit(uso.class_id, uso.key, registro).role
                for uso in sources.usages()
                if uso.class_id == clase["id"]
            }
            self.assertIn("ancla", papeles, f"clase {clase['id']} sin obra de su tema")


class TestRegistro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registro = sources.load_registry()

    def test_el_registro_existe_y_declara_su_esquema(self):
        self.assertEqual(self.registro["schema_version"], sources.SCHEMA_VERSION)
        self.assertTrue(self.registro["policy"])
        self.assertTrue(self.registro["entries"])

    def test_toda_obra_usada_esta_registrada(self):
        registradas = set(sources.entries_by_key(self.registro))
        usadas = set(sources.sources_used())
        self.assertEqual(usadas - registradas, set())
        self.assertEqual(registradas - usadas, set())

    def test_el_verificador_offline_pasa(self):
        errores = []
        verify_sources.comprueba(self.registro, errores)
        verify_sources.comprueba_areas(errores)
        verify_sources.comprueba_covers(self.registro, errores)
        verify_sources.comprueba_pertinencia(self.registro, errores)
        verify_sources.comprueba_readme(self.registro, errores)
        self.assertEqual(errores, [], "\n".join(errores))

    def test_el_bloque_de_bibliografia_del_readme_sale_del_registro(self):
        texto = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(verify_sources.bloque_readme(self.registro), texto)


if __name__ == "__main__":
    unittest.main()
