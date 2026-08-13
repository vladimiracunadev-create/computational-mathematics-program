"""Motor 11 — Métodos numéricos y computación científica.

Raíces, interpolación, splines, diferenciación y cuadratura numérica, sistemas
lineales iterativos, mínimos cuadrados y ecuaciones diferenciales.
"""

from __future__ import annotations

import math

from . import _linalg as la

PART = "11"
TITLE = "Métodos numéricos y computación científica"

TOL = 1e-12
MAX_ITER = 200


def _f(x: float) -> float:
    """Función de prueba con raíz en x = 2: x³ - 2x - 4."""
    return x**3 - 2 * x - 4


def _df(x: float) -> float:
    return 3 * x**2 - 2


def numerical_errors() -> dict:
    """Error de truncamiento frente a error de redondeo."""
    def f(x):
        return math.sin(x)

    x = 1.0
    informe = []
    for h in (1e-1, 1e-3, 1e-5, 1e-8, 1e-12):
        adelante = (f(x + h) - f(x)) / h
        central = (f(x + h) - f(x - h)) / (2 * h)
        informe.append({
            "h": h,
            "error_adelante": abs(adelante - math.cos(x)),
            "error_central": abs(central - math.cos(x)),
        })
    return {
        "derivada_exacta": math.cos(x),
        "informe": informe,
        "h_optimo_aprox": math.sqrt(2.2e-16),
        "por_que_hay_un_optimo": "truncamiento baja con h, redondeo sube con 1/h",
        "orden_adelante": "O(h)",
        "orden_central": "O(h²)",
    }


def bisection() -> dict:
    """Bisección: lenta pero garantizada si hay cambio de signo."""
    a, b = 1.0, 3.0
    iteraciones = []
    for i in range(MAX_ITER):
        c = (a + b) / 2
        if _f(a) * _f(c) <= 0:
            b = c
        else:
            a = c
        if i in (0, 4, 19, 49):
            iteraciones.append({"iter": i + 1, "x": round(c, 12), "f(x)": round(_f(c), 12),
                                "amplitud": round(b - a, 15)})
        if b - a < TOL:
            break
    raiz = (a + b) / 2
    return {
        "funcion": "x³ - 2x - 4",
        "intervalo_inicial": (1.0, 3.0),
        "cambio_de_signo": _f(1.0) * _f(3.0) < 0,
        "iteraciones_registradas": iteraciones,
        "raiz": round(raiz, 12),
        "residuo": round(_f(raiz), 14),
        "iteraciones_totales": i + 1,
        "convergencia": "lineal: gana 1 bit por iteración",
    }


def newton_raphson() -> dict:
    """Newton: convergencia cuadrática cerca de la raíz."""
    x = 3.0
    historial = []
    for i in range(MAX_ITER):
        fx = _f(x)
        if abs(fx) < TOL:
            break
        x_nuevo = x - fx / _df(x)
        historial.append({"iter": i + 1, "x": round(x_nuevo, 14), "error": abs(x_nuevo - 2.0)})
        x = x_nuevo
    return {
        "funcion": "x³ - 2x - 4",
        "punto_inicial": 3.0,
        "historial": historial,
        "raiz": round(x, 14),
        "iteraciones": len(historial),
        "residuo": round(_f(x), 16),
        "duplica_digitos_por_iteracion": True,
        "riesgo": "f'(x) ≈ 0 o punto inicial lejano hacen que diverja",
    }


def secant() -> dict:
    """Secante: casi tan rápida como Newton sin necesitar la derivada."""
    x0, x1 = 1.0, 3.0
    historial = []
    for i in range(MAX_ITER):
        f0, f1 = _f(x0), _f(x1)
        if abs(f1) < TOL or abs(f1 - f0) < 1e-300:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        historial.append({"iter": i + 1, "x": round(x2, 14), "error": abs(x2 - 2.0)})
        x0, x1 = x1, x2
    return {
        "puntos_iniciales": (1.0, 3.0),
        "historial": historial,
        "raiz": round(x1, 14),
        "iteraciones": len(historial),
        "orden_de_convergencia": round((1 + math.sqrt(5)) / 2, 6),
        "no_requiere_derivada": True,
        "coste_por_iteracion": "1 evaluación de f",
    }


def lagrange_interpolation() -> dict:
    """Interpolación de Lagrange y el fenómeno de Runge."""
    def interpola(nodos, valores, x):
        total = 0.0
        for i, (xi, yi) in enumerate(zip(nodos, valores)):
            base = 1.0
            for j, xj in enumerate(nodos):
                if i != j:
                    base *= (x - xj) / (xi - xj)
            total += yi * base
        return total

    def runge(x):
        return 1 / (1 + 25 * x * x)

    resultados = {}
    for n in (5, 9, 13):
        nodos = [-1 + 2 * k / (n - 1) for k in range(n)]
        valores = [runge(x) for x in nodos]
        error = max(abs(interpola(nodos, valores, -1 + 2 * k / 200) - runge(-1 + 2 * k / 200))
                    for k in range(201))
        resultados[f"n={n}"] = round(error, 6)
    nodos = [0.0, 1.0, 2.0]
    return {
        "polinomio_por_3_puntos": [interpola(nodos, [1.0, 3.0, 7.0], x) for x in (0.5, 1.5)],
        "pasa_por_los_nodos": [interpola(nodos, [1.0, 3.0, 7.0], x) for x in nodos],
        "error_maximo_de_Runge_por_grado": resultados,
        "el_error_crece_con_el_grado": resultados["n=13"] > resultados["n=5"],
        "solucion": "nodos de Chebyshev o splines por tramos",
    }


def splines() -> dict:
    """Spline lineal por tramos frente a un polinomio único."""
    nodos = [0.0, 1.0, 2.0, 3.0, 4.0]
    valores = [0.0, 1.0, 0.0, 1.0, 0.0]

    def spline(x):
        for i in range(len(nodos) - 1):
            if nodos[i] <= x <= nodos[i + 1]:
                t = (x - nodos[i]) / (nodos[i + 1] - nodos[i])
                return valores[i] * (1 - t) + valores[i + 1] * t
        return valores[-1]

    return {
        "nodos": nodos,
        "valores": valores,
        "spline_en_0.5": spline(0.5),
        "spline_en_1.5": spline(1.5),
        "spline_en_2.25": spline(2.25),
        "pasa_por_todos_los_nodos": all(math.isclose(spline(x), y) for x, y in zip(nodos, valores)),
        "acotado_entre_min_y_max": all(0.0 <= spline(x / 10) <= 1.0 for x in range(41)),
        "ventaja_sobre_polinomio_global": "sin oscilaciones y con soporte local",
        "spline_cubico": "añade continuidad de la primera y segunda derivada",
    }


def numerical_differentiation() -> dict:
    """Fórmulas de diferencias y su orden de error."""
    def f(x):
        return math.exp(x)

    x, h = 0.5, 1e-4
    adelante = (f(x + h) - f(x)) / h
    atras = (f(x) - f(x - h)) / h
    central = (f(x + h) - f(x - h)) / (2 * h)
    segunda = (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)
    return {
        "funcion": "e^x", "x": x, "h": h,
        "exacta": f(x),
        "adelante": round(adelante, 10),
        "atras": round(atras, 10),
        "central": round(central, 10),
        "error_adelante": abs(adelante - f(x)),
        "error_central": abs(central - f(x)),
        "segunda_derivada": round(segunda, 8),
        "central_es_2_ordenes_mejor": abs(central - f(x)) < abs(adelante - f(x)),
    }


def quadrature() -> dict:
    """Cuadratura gaussiana: máxima exactitud con mínimos nodos."""
    def f(x):
        return math.exp(-x * x)

    # Gauss-Legendre de 3 puntos en [-1,1] trasladado a [0,1]
    nodos = [-math.sqrt(3 / 5), 0.0, math.sqrt(3 / 5)]
    pesos = [5 / 9, 8 / 9, 5 / 9]
    a, b = 0.0, 1.0
    gauss = (b - a) / 2 * sum(w * f((b - a) / 2 * t + (a + b) / 2) for t, w in zip(nodos, pesos))
    referencia = math.sqrt(math.pi) / 2 * math.erf(1.0)
    n = 3
    h = (b - a) / n
    trap = h * (f(a) / 2 + sum(f(a + i * h) for i in range(1, n)) + f(b) / 2)
    return {
        "integrando": "e^(-x²) en [0,1]",
        "referencia": round(referencia, 12),
        "gauss_3_nodos": round(gauss, 12),
        "error_gauss": round(abs(gauss - referencia), 12),
        "trapecio_3_subintervalos": round(trap, 12),
        "error_trapecio": round(abs(trap - referencia), 10),
        "gauss_n_puntos_es_exacta_hasta_grado": 2 * 3 - 1,
        "evaluaciones_usadas": 3,
    }


def trapezoid_rule() -> dict:
    """Regla del trapecio y su convergencia O(h²)."""
    def f(x):
        return 1 / (1 + x * x)

    a, b = 0.0, 1.0
    exacto = math.pi / 4
    informe = []
    anterior = None
    for n in (2, 4, 8, 16, 32):
        h = (b - a) / n
        s = h * (f(a) / 2 + sum(f(a + i * h) for i in range(1, n)) + f(b) / 2)
        err = abs(s - exacto)
        informe.append({"n": n, "valor": round(s, 12), "error": err,
                        "razon_de_error": round(anterior / err, 4) if anterior else None})
        anterior = err
    return {
        "integrando": "1/(1+x²) en [0,1]",
        "valor_exacto_pi/4": exacto,
        "informe": informe,
        "duplicar_n_divide_el_error_por_4": True,
        "orden": "O(h²)",
    }


def simpson_rule() -> dict:
    """Simpson y su convergencia O(h⁴)."""
    def f(x):
        return 1 / (1 + x * x)

    a, b = 0.0, 1.0
    exacto = math.pi / 4
    informe = []
    anterior = None
    for n in (2, 4, 8, 16):
        h = (b - a) / n
        s = h / 3 * (f(a) + f(b)
                     + 4 * sum(f(a + i * h) for i in range(1, n, 2))
                     + 2 * sum(f(a + i * h) for i in range(2, n, 2)))
        err = abs(s - exacto)
        informe.append({"n": n, "valor": round(s, 14), "error": err,
                        "razon_de_error": round(anterior / err, 3) if anterior and err else None})
        anterior = err
    return {
        "integrando": "1/(1+x²) en [0,1]",
        "valor_exacto": exacto,
        "informe": informe,
        "requiere_n_par": True,
        "duplicar_n_divide_el_error_por_16": True,
        "exacta_para_polinomios_de_grado_3": True,
    }


def direct_linear_solvers() -> dict:
    """Solvers directos: LU y sustitución, con conteo de operaciones."""
    a = [[4.0, -2.0, 1.0], [-2.0, 4.0, -2.0], [1.0, -2.0, 4.0]]
    b = [11.0, -16.0, 17.0]
    x, _, swaps = la.gaussian_elimination(a, b)
    lower, upper = la.lu(a)
    return {
        "A": a,
        "b": b,
        "solucion": [round(v, 10) for v in x],
        "residuo": [round(v, 12) for v in la.sub(la.matvec(a, x), b)],
        "intercambios": swaps,
        "L": [[round(v, 6) for v in row] for row in lower],
        "U": [[round(v, 6) for v in row] for row in upper],
        "determinante": round(la.determinant(a), 8),
        "coste_LU": "O(n³/3)",
        "coste_de_cada_sistema_adicional": "O(n²)",
    }


def jacobi_gauss_seidel() -> dict:
    """Métodos iterativos sobre una matriz diagonalmente dominante."""
    a = [[10.0, -1.0, 2.0], [-1.0, 11.0, -1.0], [2.0, -1.0, 10.0]]
    b = [6.0, 25.0, -11.0]
    n = 3
    dominante = all(abs(a[i][i]) > sum(abs(a[i][j]) for j in range(n) if j != i) for i in range(n))

    x_j = [0.0] * n
    iter_j = 0
    for iter_j in range(1, MAX_ITER + 1):
        nuevo = [(b[i] - sum(a[i][j] * x_j[j] for j in range(n) if j != i)) / a[i][i] for i in range(n)]
        if max(abs(p - q) for p, q in zip(nuevo, x_j)) < 1e-12:
            x_j = nuevo
            break
        x_j = nuevo

    x_gs = [0.0] * n
    iter_gs = 0
    for iter_gs in range(1, MAX_ITER + 1):
        anterior = list(x_gs)
        for i in range(n):
            x_gs[i] = (b[i] - sum(a[i][j] * x_gs[j] for j in range(n) if j != i)) / a[i][i]
        if max(abs(p - q) for p, q in zip(anterior, x_gs)) < 1e-12:
            break

    return {
        "A": a,
        "diagonalmente_dominante": dominante,
        "jacobi_solucion": [round(v, 10) for v in x_j],
        "jacobi_iteraciones": iter_j,
        "gauss_seidel_solucion": [round(v, 10) for v in x_gs],
        "gauss_seidel_iteraciones": iter_gs,
        "gauss_seidel_es_mas_rapido": iter_gs < iter_j,
        "jacobi_es_paralelizable": True,
    }


def iterative_tolerances() -> dict:
    """Criterio de parada: absoluto, relativo y residuo."""
    a = [[10.0, -1.0], [-1.0, 10.0]]
    b = [9.0, 9.0]
    x = [0.0, 0.0]
    informe = []
    for i in range(1, 31):
        anterior = list(x)
        for k in range(2):
            x[k] = (b[k] - sum(a[k][j] * x[j] for j in range(2) if j != k)) / a[k][k]
        cambio = max(abs(p - q) for p, q in zip(x, anterior))
        residuo = la.norm(la.sub(la.matvec(a, x), b))
        if i in (1, 3, 6, 12):
            informe.append({"iter": i, "cambio_absoluto": cambio,
                            "cambio_relativo": cambio / max(abs(v) for v in x),
                            "norma_del_residuo": residuo})
        if cambio < 1e-14:
            break
    return {
        "informe": informe,
        "iteraciones_hasta_1e-14": i,
        "solucion": [round(v, 12) for v in x],
        "criterio_recomendado": "combinar cambio relativo y residuo, con tope de iteraciones",
        "peligro_de_solo_absoluto": "falla si la escala del problema es muy grande o muy pequeña",
        "siempre_declarar_max_iter": True,
    }


def numerical_least_squares() -> dict:
    """Mínimos cuadrados: ecuaciones normales frente a QR."""
    xs = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    ys = [1.1, 2.0, 2.9, 4.2, 4.8, 6.1]
    A = [[1.0, x] for x in xs]
    At = la.transpose(A)
    normal = la.matmul(At, A)
    coef_normal, _, _ = la.gaussian_elimination(normal, la.matvec(At, ys))
    q, r = la.qr(A)
    coef_qr, _, _ = la.gaussian_elimination(r, la.matvec(la.transpose(q), ys))
    val_normal, _ = la.symmetric_eigen(normal)
    return {
        "datos": len(xs),
        "coeficientes_ecuaciones_normales": [round(v, 8) for v in coef_normal],
        "coeficientes_QR": [round(v, 8) for v in coef_qr],
        "coinciden": all(abs(a - b) < 1e-8 for a, b in zip(coef_normal, coef_qr)),
        "condicion_de_AᵀA": round(max(val_normal) / min(val_normal), 4),
        "las_normales_elevan_al_cuadrado_la_condicion": True,
        "recomendacion": "usar QR o SVD cuando A esté mal condicionada",
        "SSE": round(sum((y - (coef_qr[0] + coef_qr[1] * x)) ** 2 for x, y in zip(xs, ys)), 8),
    }


def odes() -> dict:
    """EDO con solución analítica para medir el error de cada método."""
    def f(t, y):
        return -2 * y + t

    def exacta(t):
        return 0.25 * (2 * t - 1) + 1.25 * math.exp(-2 * t)

    y0, t_final = 1.0, 1.0
    return {
        "edo": "y' = -2y + t, y(0) = 1",
        "solucion_analitica": "0.25(2t-1) + 1.25e^(-2t)",
        "y(0)": exacta(0.0),
        "y(1)_exacta": round(exacta(t_final), 12),
        "condicion_inicial": y0,
        "f(0,1)": f(0.0, 1.0),
        "es_lineal_de_primer_orden": True,
        "estable": True,
    }


def euler_method() -> dict:
    """Euler explícito: orden 1 y coste mínimo."""
    def f(t, y):
        return -2 * y + t

    def exacta(t):
        return 0.25 * (2 * t - 1) + 1.25 * math.exp(-2 * t)

    informe = []
    anterior = None
    for n in (5, 10, 20, 40, 80):
        h = 1.0 / n
        y, t = 1.0, 0.0
        for _ in range(n):
            y += h * f(t, y)
            t += h
        err = abs(y - exacta(1.0))
        informe.append({"pasos": n, "h": round(h, 6), "y(1)": round(y, 8), "error": err,
                        "razon": round(anterior / err, 4) if anterior else None})
        anterior = err
    return {
        "metodo": "Euler explícito",
        "informe": informe,
        "orden": 1,
        "duplicar_pasos_divide_el_error_por_2": True,
        "coste_por_paso": "1 evaluación de f",
        "limite_de_estabilidad": "h < 2/|λ| para y' = λy",
    }


def runge_kutta() -> dict:
    """RK4: cuatro evaluaciones por paso, error O(h⁴)."""
    def f(t, y):
        return -2 * y + t

    def exacta(t):
        return 0.25 * (2 * t - 1) + 1.25 * math.exp(-2 * t)

    informe = []
    anterior = None
    for n in (5, 10, 20, 40):
        h = 1.0 / n
        y, t = 1.0, 0.0
        for _ in range(n):
            k1 = f(t, y)
            k2 = f(t + h / 2, y + h * k1 / 2)
            k3 = f(t + h / 2, y + h * k2 / 2)
            k4 = f(t + h, y + h * k3)
            y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t += h
        err = abs(y - exacta(1.0))
        informe.append({"pasos": n, "y(1)": round(y, 12), "error": err,
                        "razon": round(anterior / err, 3) if anterior and err else None})
        anterior = err
    return {
        "metodo": "Runge-Kutta 4",
        "informe": informe,
        "orden": 4,
        "duplicar_pasos_divide_el_error_por_16": True,
        "coste_por_paso": "4 evaluaciones de f",
        "comparacion": "RK4 con 5 pasos supera a Euler con 80",
    }


def pde_discretization() -> dict:
    """Discretización de la ecuación del calor en 1D (esquema explícito)."""
    nx, alpha = 21, 0.4
    dx = 1.0 / (nx - 1)
    dt = alpha * dx * dx
    u = [math.sin(math.pi * i * dx) for i in range(nx)]
    inicial = list(u)
    pasos = 200
    for _ in range(pasos):
        nuevo = list(u)
        for i in range(1, nx - 1):
            nuevo[i] = u[i] + alpha * (u[i + 1] - 2 * u[i] + u[i - 1])
        nuevo[0] = nuevo[-1] = 0.0
        u = nuevo
    t_final = pasos * dt
    exacta = [math.exp(-math.pi**2 * t_final) * math.sin(math.pi * i * dx) for i in range(nx)]
    return {
        "ecuacion": "u_t = u_xx con u(0,t)=u(1,t)=0",
        "nodos": nx,
        "dx": round(dx, 6),
        "dt": round(dt, 8),
        "numero_de_courant_alpha": alpha,
        "estable_si_alpha<=0.5": alpha <= 0.5,
        "pico_inicial": round(max(inicial), 6),
        "pico_final_numerico": round(max(u), 8),
        "pico_final_analitico": round(max(exacta), 8),
        "error_maximo": round(max(abs(a - b) for a, b in zip(u, exacta)), 8),
    }


def scientific_computing() -> dict:
    """Qué aporta SciPy sobre una implementación propia."""
    try:  # pragma: no cover - depende del entorno
        import scipy  # noqa: F401
        disponible = True
        version = scipy.__version__
    except ImportError:
        disponible = False
        version = None
    return {
        "scipy_instalado": disponible,
        "version": version,
        "equivalencias": {
            "bisection": "scipy.optimize.brentq",
            "newton_raphson": "scipy.optimize.newton",
            "quadrature": "scipy.integrate.quad",
            "runge_kutta": "scipy.integrate.solve_ivp",
            "least_squares": "scipy.linalg.lstsq",
            "splines": "scipy.interpolate.CubicSpline",
        },
        "por_que_implementar_a_mano": "para saber cuándo la biblioteca miente o falla",
        "por_que_usar_la_biblioteca": "estabilidad, control de error y rendimiento probados",
        "este_motor_no_requiere_scipy": True,
    }


def capstone_numerical_solver() -> dict:
    """Capstone: solver con informe de error y criterio de parada declarado."""
    def f(t, y):
        return -2 * y + t

    def exacta(t):
        return 0.25 * (2 * t - 1) + 1.25 * math.exp(-2 * t)

    informe = []
    for nombre, paso in (("euler", "1 evaluación"), ("rk4", "4 evaluaciones")):
        for n in (10, 40):
            h = 1.0 / n
            y, t = 1.0, 0.0
            for _ in range(n):
                if nombre == "euler":
                    y += h * f(t, y)
                else:
                    k1 = f(t, y)
                    k2 = f(t + h / 2, y + h * k1 / 2)
                    k3 = f(t + h / 2, y + h * k2 / 2)
                    k4 = f(t + h, y + h * k3)
                    y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
                t += h
            evaluaciones = n * (1 if nombre == "euler" else 4)
            informe.append({
                "metodo": nombre, "pasos": n, "evaluaciones": evaluaciones,
                "y(1)": round(y, 12), "error": abs(y - exacta(1.0)),
                "coste_por_paso": paso,
            })

    raiz_biseccion = 1.0
    a, b = 1.0, 3.0
    it_bis = 0
    while b - a > 1e-12 and it_bis < MAX_ITER:
        c = (a + b) / 2
        if _f(a) * _f(c) <= 0:
            b = c
        else:
            a = c
        it_bis += 1
        raiz_biseccion = c

    x, it_newton = 3.0, 0
    while abs(_f(x)) > 1e-14 and it_newton < MAX_ITER:
        x -= _f(x) / _df(x)
        it_newton += 1

    return {
        "problema_1": "EDO y' = -2y + t",
        "informe_edo": informe,
        "mejor_relacion_error_por_evaluacion": "rk4",
        "problema_2": "raíz de x³ - 2x - 4",
        "biseccion": {"raiz": round(raiz_biseccion, 12), "iteraciones": it_bis},
        "newton": {"raiz": round(x, 14), "iteraciones": it_newton},
        "tolerancia_declarada": 1e-12,
        "max_iteraciones_declarado": MAX_ITER,
        "regla": "ningún resultado numérico se publica sin tolerancia, iteraciones y error estimado",
    }


DEMOS = {
    "numerical_errors": numerical_errors,
    "bisection": bisection,
    "newton_raphson": newton_raphson,
    "secant": secant,
    "lagrange_interpolation": lagrange_interpolation,
    "splines": splines,
    "numerical_differentiation": numerical_differentiation,
    "quadrature": quadrature,
    "trapezoid_rule": trapezoid_rule,
    "simpson_rule": simpson_rule,
    "direct_linear_solvers": direct_linear_solvers,
    "jacobi_gauss_seidel": jacobi_gauss_seidel,
    "iterative_tolerances": iterative_tolerances,
    "numerical_least_squares": numerical_least_squares,
    "odes": odes,
    "euler_method": euler_method,
    "runge_kutta": runge_kutta,
    "pde_discretization": pde_discretization,
    "scientific_computing": scientific_computing,
    "capstone_numerical_solver": capstone_numerical_solver,
}

CLASS_DEMOS = {
    "221": "numerical_errors",
    "222": "bisection",
    "223": "newton_raphson",
    "224": "secant",
    "225": "lagrange_interpolation",
    "226": "splines",
    "227": "numerical_differentiation",
    "228": "quadrature",
    "229": "trapezoid_rule",
    "230": "simpson_rule",
    "231": "direct_linear_solvers",
    "232": "jacobi_gauss_seidel",
    "233": "iterative_tolerances",
    "234": "numerical_least_squares",
    "235": "odes",
    "236": "euler_method",
    "237": "runge_kutta",
    "238": "pde_discretization",
    "239": "scientific_computing",
    "240": "capstone_numerical_solver",
}
