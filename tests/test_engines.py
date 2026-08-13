"""Los 18 motores didácticos: cobertura, determinismo y corrección numérica."""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import curriculum, engines  # noqa: E402
from computational_math.engines import _linalg as la  # noqa: E402
from computational_math.engines.part08 import Var  # noqa: E402


class TestCobertura(unittest.TestCase):
    def test_hay_18_motores(self):
        self.assertEqual(len(engines.ENGINE_MODULES), 18)

    def test_todas_las_clases_tienen_demostracion(self):
        mapa = engines.all_class_demos()
        self.assertEqual(len(mapa), 360)
        for clase in curriculum.classes():
            with self.subTest(clase=clase["id"]):
                self.assertIn(clase["id"], mapa)

    def test_cada_demo_registrada_existe(self):
        for nombre in engines.ENGINE_MODULES:
            motor = engines.load_engine(nombre[-2:])
            for class_id, demo in motor.CLASS_DEMOS.items():
                with self.subTest(clase=class_id):
                    self.assertIn(demo, motor.DEMOS)

    def test_toda_demo_tiene_docstring(self):
        for nombre in engines.ENGINE_MODULES:
            motor = engines.load_engine(nombre[-2:])
            for demo, funcion in motor.DEMOS.items():
                with self.subTest(motor=nombre, demo=demo):
                    self.assertTrue((funcion.__doc__ or "").strip())

    def test_todas_las_demos_devuelven_dict_no_vacio(self):
        for clase in curriculum.classes():
            with self.subTest(clase=clase["id"]):
                resultado = engines.run_class(clase["id"])
                self.assertIsInstance(resultado, dict)
                self.assertTrue(resultado)

    def test_las_demos_son_deterministas(self):
        # Muestra representativa: una clase de cada parte, incluidas las estocásticas.
        for parte in curriculum.parts():
            class_id = parte["classes"][-1]["id"]
            with self.subTest(clase=class_id):
                self.assertEqual(engines.run_class(class_id), engines.run_class(class_id))

    def test_parte_desconocida(self):
        with self.assertRaises(KeyError):
            engines.load_engine("99")


class TestLinalg(unittest.TestCase):
    def test_resuelve_sistema_lineal(self):
        a = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]
        b = [8.0, -11.0, -3.0]
        x, _, _ = la.gaussian_elimination(a, b)
        for esperado, obtenido in zip([2.0, 3.0, -1.0], x):
            self.assertAlmostEqual(esperado, obtenido, places=10)

    def test_inversa_por_producto(self):
        a = [[4.0, 7.0], [2.0, 6.0]]
        producto = la.matmul(a, la.inverse(a))
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(producto[i][j], 1.0 if i == j else 0.0, places=10)

    def test_determinante_y_rango(self):
        self.assertAlmostEqual(la.determinant([[1.0, 2.0], [3.0, 4.0]]), -2.0, places=10)
        self.assertEqual(la.rank([[1.0, 2.0], [2.0, 4.0]]), 1)
        self.assertEqual(la.rank(la.identity(4)), 4)

    def test_qr_produce_columnas_ortonormales(self):
        a = [[1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
        q, r = la.qr(a)
        qtq = la.matmul(la.transpose(q), q)
        for i in range(len(qtq)):
            for j in range(len(qtq)):
                self.assertAlmostEqual(qtq[i][j], 1.0 if i == j else 0.0, places=9)
        producto = la.matmul(q, r)
        for i in range(3):
            for j in range(2):
                self.assertAlmostEqual(producto[i][j], a[i][j], places=9)

    def test_autovalores_de_matriz_simetrica(self):
        a = [[4.0, 1.0], [1.0, 3.0]]
        valores, _ = la.symmetric_eigen(a)
        self.assertAlmostEqual(sum(valores), 7.0, places=9)          # traza
        self.assertAlmostEqual(valores[0] * valores[1], 11.0, places=9)  # determinante

    def test_svd_reconstruye_la_matriz(self):
        a = [[3.0, 0.0], [4.0, 5.0]]
        u, s, v = la.svd(a)
        for i in range(2):
            for j in range(2):
                reconstruido = sum(u[i][k] * s[k] * v[j][k] for k in range(2))
                self.assertAlmostEqual(reconstruido, a[i][j], places=8)

    def test_lu_reconstruye_la_matriz(self):
        a = [[4.0, 3.0], [6.0, 3.0]]
        lower, upper = la.lu(a)
        producto = la.matmul(lower, upper)
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(producto[i][j], a[i][j], places=10)

    def test_matriz_singular_lanza_error(self):
        with self.assertRaises(ValueError):
            la.inverse([[1.0, 2.0], [2.0, 4.0]])


class TestAutodiff(unittest.TestCase):
    def test_gradiente_de_un_polinomio(self):
        x = Var(3.0)
        y = x * x + 2.0 * x + 1.0
        y.backward()
        self.assertAlmostEqual(y.value, 16.0, places=12)
        self.assertAlmostEqual(x.grad, 8.0, places=12)   # 2x + 2

    def test_acumula_gradientes_en_nodos_reutilizados(self):
        x = Var(2.0)
        y = x * x + x
        y.backward()
        self.assertAlmostEqual(x.grad, 5.0, places=12)

    def test_coincide_con_diferencias_finitas(self):
        def f(v):
            return math.exp(v) * math.sin(v)

        punto = 0.7
        x = Var(punto)
        z = x.exp() * x.sin()
        z.backward()
        numerico = (f(punto + 1e-6) - f(punto - 1e-6)) / 2e-6
        self.assertAlmostEqual(x.grad, numerico, places=5)

    def test_operaciones_derivadas(self):
        a, b = Var(4.0), Var(2.0)
        c = (a - b) / b
        c.backward()
        self.assertAlmostEqual(c.value, 1.0, places=12)
        self.assertAlmostEqual(a.grad, 0.5, places=12)


class TestResultadosNumericos(unittest.TestCase):
    """Comprueba afirmaciones concretas que las demostraciones deben cumplir."""

    def test_suma_de_gauss(self):
        r = engines.run_class("001")
        self.assertTrue(r["coinciden"])
        self.assertEqual(r["suma_formula_cerrada"], 5050)

    def test_punto_flotante_no_es_exacto(self):
        r = engines.run_class("029")
        self.assertFalse(r["iguales"])
        self.assertTrue(r["comparacion_correcta"])

    def test_rotacion_preserva_la_norma(self):
        r = engines.run_class("074")
        self.assertTrue(r["preserva_la_norma"])
        self.assertAlmostEqual(r["determinante"], 1.0, places=10)

    def test_orden_topologico_detecta_dag(self):
        r = engines.run_class("096")
        self.assertTrue(r["es_DAG"])
        self.assertEqual(r["nodos_ordenados"], 6)

    def test_pca_explica_casi_toda_la_varianza(self):
        r = engines.run_class("135")
        self.assertGreater(r["varianza_explicada_PC1_%"], 90)

    def test_regla_de_la_cadena(self):
        r = engines.run_class("147")
        self.assertTrue(r["coinciden"])

    def test_backpropagation_manual_igual_a_automatica(self):
        r = engines.run_class("180")
        self.assertTrue(r["coinciden"])

    def test_bayes_con_baja_prevalencia(self):
        r = engines.run_class("186")
        self.assertLess(r["P(enfermo|+)"], 0.1)

    def test_intervalo_de_confianza_cubre_lo_esperado(self):
        r = engines.run_class("205")
        self.assertGreater(r["cobertura_simulada_%"], 92.0)
        self.assertLess(r["cobertura_simulada_%"], 98.0)

    def test_newton_converge_mas_rapido_que_biseccion(self):
        newton = engines.run_class("223")
        biseccion = engines.run_class("222")
        self.assertLess(newton["iteraciones"], biseccion["iteraciones_totales"])
        self.assertAlmostEqual(newton["raiz"], 2.0, places=8)

    def test_adam_converge(self):
        r = engines.run_class("250")
        self.assertLess(r["resultado"]["f_final"], 1e-4)

    def test_entropia_maxima_en_la_uniforme(self):
        r = engines.run_class("262")
        self.assertAlmostEqual(r["entropias_bits"]["uniforme_4"], 2.0, places=9)
        self.assertEqual(r["entropias_bits"]["determinista"], 0.0)

    def test_kl_no_es_simetrica(self):
        r = engines.run_class("264")
        self.assertFalse(r["simetrica"])
        self.assertEqual(r["KL(p||p)"], 0.0)

    def test_regresion_lineal_recupera_los_parametros(self):
        r = engines.run_class("282")
        self.assertTrue(r["coinciden"])

    def test_red_neuronal_resuelve_las_espirales(self):
        r = engines.run_class("320")
        self.assertGreater(r["accuracy_test"], 0.85)

    def test_atencion_causal_no_mira_el_futuro(self):
        r = engines.run_class("326")
        self.assertTrue(r["el_token_0_solo_se_ve_a_si_mismo"])
        for i, fila in enumerate(r["matriz_causal"]):
            for j in range(i + 1, len(fila)):
                self.assertEqual(fila[j], 0.0)

    def test_mini_transformer_aprende_la_tarea(self):
        r = engines.run_class("340")
        self.assertGreater(r["accuracy_test"], 0.9)
        self.assertTrue(r["la_atencion_aprende_a_mirar_i-1"])

    def test_clustering_espectral_encuentra_el_corte_minimo(self):
        r = engines.run_class("354")
        self.assertTrue(r["particion_correcta"])
        self.assertEqual(r["aristas_cortadas"], 1)

    def test_capstone_final_reproduce_el_resultado(self):
        r = engines.run_class("360")
        self.assertTrue(r["el_error_decrece_monotonamente"])
        self.assertTrue(r["es_simetrica"])


if __name__ == "__main__":
    unittest.main()
