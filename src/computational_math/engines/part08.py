"""Motor 08 — Cálculo multivariable, matricial y autodiferenciación.

Incluye un micro-motor de autodiferenciación en modo reverso (:class:`Var`) que
es, en miniatura, lo mismo que hacen PyTorch y JAX.
"""

from __future__ import annotations

import math
from typing import Callable, List, Sequence

from . import _linalg as la

PART = "08"
TITLE = "Cálculo multivariable, matricial y autodiferenciación"


class Var:
    """Escalar con gradiente: nodo de un grafo de cómputo en modo reverso."""

    __slots__ = ("value", "grad", "_backward", "_prev", "_op")

    def __init__(self, value: float, _prev: tuple = (), _op: str = ""):
        self.value = float(value)
        self.grad = 0.0
        self._backward: Callable[[], None] = lambda: None
        self._prev = _prev
        self._op = _op

    def __repr__(self) -> str:  # pragma: no cover - representación
        return f"Var(value={self.value:.6g}, grad={self.grad:.6g})"

    def __add__(self, other):
        other = other if isinstance(other, Var) else Var(other)
        out = Var(self.value + other.value, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Var) else Var(other)
        out = Var(self.value * other.value, (self, other), "*")

        def _backward():
            self.grad += other.value * out.grad
            other.grad += self.value * out.grad

        out._backward = _backward
        return out

    def __pow__(self, exponent: float):
        out = Var(self.value**exponent, (self,), f"**{exponent}")

        def _backward():
            self.grad += exponent * self.value ** (exponent - 1) * out.grad

        out._backward = _backward
        return out

    def exp(self):
        out = Var(math.exp(self.value), (self,), "exp")

        def _backward():
            self.grad += out.value * out.grad

        out._backward = _backward
        return out

    def log(self):
        out = Var(math.log(self.value), (self,), "log")

        def _backward():
            self.grad += out.grad / self.value

        out._backward = _backward
        return out

    def sin(self):
        out = Var(math.sin(self.value), (self,), "sin")

        def _backward():
            self.grad += math.cos(self.value) * out.grad

        out._backward = _backward
        return out

    def tanh(self):
        t = math.tanh(self.value)
        out = Var(t, (self,), "tanh")

        def _backward():
            self.grad += (1 - t * t) * out.grad

        out._backward = _backward
        return out

    def relu(self):
        out = Var(self.value if self.value > 0 else 0.0, (self,), "relu")

        def _backward():
            self.grad += (1.0 if self.value > 0 else 0.0) * out.grad

        out._backward = _backward
        return out

    __radd__ = __add__
    __rmul__ = __mul__

    def __neg__(self):
        return self * -1.0

    def __sub__(self, other):
        return self + (-(other if isinstance(other, Var) else Var(other)))

    def __rsub__(self, other):
        return (other if isinstance(other, Var) else Var(other)) + (-self)

    def __truediv__(self, other):
        other = other if isinstance(other, Var) else Var(other)
        return self * other**-1.0

    def backward(self) -> None:
        """Propaga el gradiente en orden topológico inverso."""
        orden: List[Var] = []
        visitados = set()

        def construir(nodo: "Var") -> None:
            if id(nodo) in visitados:
                return
            visitados.add(id(nodo))
            for hijo in nodo._prev:
                construir(hijo)
            orden.append(nodo)

        construir(self)
        self.grad = 1.0
        for nodo in reversed(orden):
            nodo._backward()


def _grad_num(f: Callable[[Sequence[float]], float], x: Sequence[float], h: float = 1e-6) -> List[float]:
    g = []
    for i in range(len(x)):
        up = list(x)
        down = list(x)
        up[i] += h
        down[i] -= h
        g.append((f(up) - f(down)) / (2 * h))
    return g


def _f(x: Sequence[float]) -> float:
    """Función de prueba: f(x,y) = x²y + 3xy² + 2."""
    return x[0] ** 2 * x[1] + 3 * x[0] * x[1] ** 2 + 2.0


def multivariable_functions() -> dict:
    """Una función de dos variables evaluada sobre una malla."""
    puntos = [(0.0, 0.0), (1.0, 1.0), (2.0, 1.0), (1.0, 2.0)]
    return {
        "funcion": "f(x,y) = x²y + 3xy² + 2",
        "dominio": "ℝ²",
        "codominio": "ℝ",
        "valores": {str(p): _f(p) for p in puntos},
        "no_conmuta_en_x_y": _f((2.0, 1.0)) != _f((1.0, 2.0)),
        "grafica_vive_en": "ℝ³",
    }


def level_curves() -> dict:
    """Curvas de nivel: dónde la función vale lo mismo."""
    def g(x, y):
        return x * x + y * y

    nivel = 4.0
    puntos = [(2.0, 0.0), (0.0, 2.0), (math.sqrt(2), math.sqrt(2)), (-2.0, 0.0)]
    return {
        "funcion": "g(x,y) = x² + y²",
        "nivel": nivel,
        "puntos_del_nivel": {str(p): round(g(*p), 10) for p in puntos},
        "forma_geometrica": "circunferencia de radio 2",
        "gradiente_en_(2,0)": [4.0, 0.0],
        "gradiente_perpendicular_a_la_curva": True,
        "curvas_mas_juntas": "mayor pendiente",
    }


def partial_derivatives() -> dict:
    """Derivadas parciales: mover una variable congelando el resto."""
    p = (2.0, 3.0)
    dfdx = 2 * p[0] * p[1] + 3 * p[1] ** 2
    dfdy = p[0] ** 2 + 6 * p[0] * p[1]
    num = _grad_num(_f, p)
    return {
        "punto": p,
        "∂f/∂x_analitica": dfdx,
        "∂f/∂x_numerica": round(num[0], 6),
        "∂f/∂y_analitica": dfdy,
        "∂f/∂y_numerica": round(num[1], 6),
        "coinciden": math.isclose(num[0], dfdx, rel_tol=1e-5) and math.isclose(num[1], dfdy, rel_tol=1e-5),
        "cruzadas_iguales_(Schwarz)": True,
    }


def gradient() -> dict:
    """El gradiente apunta al mayor ascenso."""
    p = [2.0, 3.0]
    g = _grad_num(_f, p)
    direccion = la.normalize(g)
    paso = 1e-3
    subida = _f(la.add(p, la.scale(direccion, paso)))
    bajada = _f(la.sub(p, la.scale(direccion, paso)))
    return {
        "punto": p,
        "gradiente": [round(v, 6) for v in g],
        "norma": round(la.norm(g), 6),
        "direccion_unitaria": [round(v, 6) for v in direccion],
        "f(p)": _f(p),
        "f(p + h·∇f)": round(subida, 8),
        "f(p - h·∇f)": round(bajada, 8),
        "el_gradiente_sube": subida > _f(p) > bajada,
        "descenso_usa_-∇f": True,
    }


def directional_derivative() -> dict:
    """Derivada direccional como proyección del gradiente."""
    p = [2.0, 3.0]
    g = _grad_num(_f, p)
    direcciones = {"e1": [1.0, 0.0], "e2": [0.0, 1.0], "45°": la.normalize([1.0, 1.0]),
                   "-∇f": la.normalize(la.scale(g, -1))}
    return {
        "punto": p,
        "gradiente": [round(v, 6) for v in g],
        "derivadas_direccionales": {k: round(la.dot(g, la.normalize(v)), 6) for k, v in direcciones.items()},
        "maxima_posible": round(la.norm(g), 6),
        "minima_posible": round(-la.norm(g), 6),
        "nula_en_direccion_perpendicular": round(la.dot(g, la.normalize([-g[1], g[0]])), 10),
    }


def tangent_plane() -> dict:
    """Plano tangente: la aproximación lineal en dos variables."""
    p = [2.0, 3.0]
    g = _grad_num(_f, p)
    f0 = _f(p)

    def plano(x, y):
        return f0 + g[0] * (x - p[0]) + g[1] * (y - p[1])

    cerca = (2.01, 3.01)
    lejos = (3.0, 4.0)
    return {
        "punto": p,
        "f(p)": f0,
        "gradiente": [round(v, 6) for v in g],
        "plano": f"z = {f0:.2f} + {g[0]:.2f}(x-2) + {g[1]:.2f}(y-3)",
        "error_cerca": round(abs(_f(cerca) - plano(*cerca)), 8),
        "error_lejos": round(abs(_f(lejos) - plano(*lejos)), 6),
        "el_error_crece_cuadraticamente": True,
    }


def multivariable_chain_rule() -> dict:
    """Regla de la cadena con variables intermedias."""
    t = 1.5

    def x(t):
        return math.cos(t)

    def y(t):
        return math.sin(t)

    def h(t):
        return _f((x(t), y(t)))

    g = _grad_num(_f, (x(t), y(t)))
    dxdt, dydt = -math.sin(t), math.cos(t)
    cadena = g[0] * dxdt + g[1] * dydt
    numerica = (h(t + 1e-6) - h(t - 1e-6)) / 2e-6
    return {
        "composicion": "f(x(t), y(t)) con x=cos t, y=sin t",
        "t": t,
        "∂f/∂x·dx/dt + ∂f/∂y·dy/dt": round(cadena, 6),
        "dh/dt_numerica": round(numerica, 6),
        "coinciden": math.isclose(cadena, numerica, rel_tol=1e-4),
        "estructura": "producto punto entre gradiente y velocidad",
    }


def jacobian() -> dict:
    """Jacobiano de una función vectorial."""
    def F(v):
        x, y = v
        return [x * x + y, math.sin(x) * y, x - 3 * y]

    p = [1.0, 2.0]
    h = 1e-6
    J = []
    for i in range(3):
        fila = []
        for j in range(2):
            up, down = list(p), list(p)
            up[j] += h
            down[j] -= h
            fila.append((F(up)[i] - F(down)[i]) / (2 * h))
        J.append([round(v, 6) for v in fila])
    return {
        "F": "(x²+y, sin(x)·y, x-3y)",
        "punto": p,
        "shape_del_jacobiano": (3, 2),
        "jacobiano": J,
        "fila_i_es_el_gradiente_de_Fi": True,
        "analitico_fila_1": [2 * p[0], 1.0],
        "vjp": "modo reverso calcula vᵀJ sin construir J",
        "jvp": "modo directo calcula Jv",
    }


def hessian() -> dict:
    """Hessiano: curvatura y clasificación del punto crítico."""
    def q(v):
        return v[0] ** 2 + 3 * v[1] ** 2

    p = [0.0, 0.0]
    h = 1e-4
    H = []
    for i in range(2):
        fila = []
        for j in range(2):
            pp, pm, mp, mm = list(p), list(p), list(p), list(p)
            pp[i] += h
            pp[j] += h
            pm[i] += h
            pm[j] -= h
            mp[i] -= h
            mp[j] += h
            mm[i] -= h
            mm[j] -= h
            fila.append(round((q(pp) - q(pm) - q(mp) + q(mm)) / (4 * h * h), 4))
        H.append(fila)
    valores, _ = la.symmetric_eigen(H)
    return {
        "funcion": "x² + 3y²",
        "punto_critico": p,
        "gradiente": [round(v, 8) for v in _grad_num(q, p)],
        "hessiano": H,
        "autovalores": [round(v, 4) for v in valores],
        "definido_positivo": all(v > 0 for v in valores),
        "clasificacion": "mínimo local",
        "silla_si_hay_signos_mixtos": True,
    }


def multivariable_taylor() -> dict:
    """Taylor de segundo orden en dos variables."""
    p = [1.0, 1.0]
    g = _grad_num(_f, p)
    f0 = _f(p)
    d = [0.05, -0.03]
    lineal = f0 + la.dot(g, d)
    h = 1e-4
    H = []
    for i in range(2):
        fila = []
        for j in range(2):
            pp, pm, mp, mm = list(p), list(p), list(p), list(p)
            pp[i] += h
            pp[j] += h
            pm[i] += h
            pm[j] -= h
            mp[i] -= h
            mp[j] += h
            mm[i] -= h
            mm[j] -= h
            fila.append((_f(pp) - _f(pm) - _f(mp) + _f(mm)) / (4 * h * h))
        H.append(fila)
    cuadratico = lineal + 0.5 * la.dot(d, la.matvec(H, d))
    exacto = _f(la.add(p, d))
    return {
        "punto_base": p,
        "desplazamiento": d,
        "valor_exacto": round(exacto, 10),
        "orden_0": round(f0, 10),
        "orden_1": round(lineal, 10),
        "orden_2": round(cuadratico, 10),
        "error_orden_1": round(abs(exacto - lineal), 10),
        "error_orden_2": round(abs(exacto - cuadratico), 12),
    }


def unconstrained_optimization() -> dict:
    """Descenso de gradiente sobre una cuadrática con historial."""
    def q(v):
        return (v[0] - 3.0) ** 2 + 5 * (v[1] + 1.0) ** 2

    x = [0.0, 0.0]
    lr = 0.08
    historial = []
    for paso in range(60):
        g = _grad_num(q, x)
        x = la.sub(x, la.scale(g, lr))
        if paso in (0, 4, 19, 59):
            historial.append({"paso": paso + 1, "x": [round(v, 6) for v in x], "f": round(q(x), 10)})
    return {
        "funcion": "(x-3)² + 5(y+1)²",
        "minimo_teorico": [3.0, -1.0],
        "learning_rate": lr,
        "historial": historial,
        "solucion_final": [round(v, 6) for v in x],
        "gradiente_final": [round(v, 8) for v in _grad_num(q, x)],
        "convergio": la.norm(_grad_num(q, x)) < 1e-4,
    }


def lagrange_multipliers() -> dict:
    """Maximizar xy sujeto a x+y=10 con multiplicadores de Lagrange."""
    # ∇f = λ∇g  ->  (y, x) = λ(1, 1)  ->  x = y = 5, λ = 5
    x = y = 5.0
    lam = 5.0
    alternativas = {f"x={a}": a * (10 - a) for a in (1.0, 3.0, 5.0, 7.0, 9.0)}
    return {
        "objetivo": "max xy",
        "restriccion": "x + y = 10",
        "solucion": (x, y),
        "valor_optimo": x * y,
        "multiplicador_lambda": lam,
        "interpretacion_de_lambda": "cuánto mejora el óptimo si la restricción sube en 1",
        "verificacion_alternativas": alternativas,
        "es_el_maximo": all(v <= x * y for v in alternativas.values()),
    }


def double_integrals() -> dict:
    """Integral doble sobre un rectángulo por suma de Riemann."""
    def f(x, y):
        return x * y

    n = 200
    hx, hy = 2.0 / n, 3.0 / n
    total = sum(f((i + 0.5) * hx, (j + 0.5) * hy) * hx * hy for i in range(n) for j in range(n))
    exacto = (2.0**2 / 2) * (3.0**2 / 2)
    return {
        "integrando": "xy",
        "region": "[0,2] × [0,3]",
        "aproximacion": round(total, 8),
        "valor_exacto": exacto,
        "error": round(abs(total - exacto), 10),
        "teorema_de_Fubini": "∫∫ = ∫(∫dx)dy cuando f es integrable",
        "subdivisiones": n * n,
    }


def triple_integrals() -> dict:
    """Volumen y masa de un cubo con densidad variable."""
    n = 60
    h = 1.0 / n
    volumen = sum(h**3 for _ in range(n) for _ in range(n) for _ in range(n))
    masa = sum((1 + (i + 0.5) * h) * h**3 for i in range(n) for _ in range(n) for _ in range(n))
    return {
        "region": "cubo unitario",
        "volumen_aproximado": round(volumen, 8),
        "volumen_exacto": 1.0,
        "densidad": "ρ(x,y,z) = 1 + x",
        "masa_aproximada": round(masa, 6),
        "masa_exacta_3/2": 1.5,
        "error_masa": round(abs(masa - 1.5), 6),
        "coste": f"{n**3} celdas",
    }


def vector_fields() -> dict:
    """Campo vectorial, líneas de flujo y campo conservativo."""
    def campo(x, y):
        return (-y, x)

    def gradiente_de_potencial(x, y):
        return (2 * x, 2 * y)

    puntos = [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0)]
    return {
        "campo_rotacional": "F(x,y) = (-y, x)",
        "valores": {str(p): campo(*p) for p in puntos},
        "campo_conservativo": "G = ∇(x²+y²) = (2x, 2y)",
        "valores_G": {str(p): gradiente_de_potencial(*p) for p in puntos},
        "F_es_perpendicular_al_radio": all(abs(p[0] * campo(*p)[0] + p[1] * campo(*p)[1]) < 1e-12 for p in puntos),
        "G_deriva_de_un_potencial": True,
    }


def divergence_curl() -> dict:
    """Divergencia y rotacional calculados numéricamente."""
    def F(x, y):
        return (x * x, x * y)

    x0, y0, h = 1.0, 2.0, 1e-5
    div = ((F(x0 + h, y0)[0] - F(x0 - h, y0)[0]) / (2 * h)
           + (F(x0, y0 + h)[1] - F(x0, y0 - h)[1]) / (2 * h))
    rot = ((F(x0 + h, y0)[1] - F(x0 - h, y0)[1]) / (2 * h)
           - (F(x0, y0 + h)[0] - F(x0, y0 - h)[0]) / (2 * h))
    return {
        "campo": "F(x,y) = (x², xy)",
        "punto": (x0, y0),
        "divergencia_numerica": round(div, 6),
        "divergencia_analitica_2x+x": 3 * x0,
        "rotacional_numerico": round(rot, 6),
        "rotacional_analitico_y": y0,
        "divergencia_mide": "fuente o sumidero",
        "rotacional_mide": "circulación local",
    }


def matrix_calculus() -> dict:
    """Identidades básicas de cálculo matricial."""
    a = [[2.0, 1.0], [1.0, 3.0]]
    x = [1.0, 2.0]

    def cuadratica(v):
        return la.dot(v, la.matvec(a, v))

    def lineal(v):
        return la.dot([4.0, -1.0], v)

    return {
        "d(aᵀx)/dx": [4.0, -1.0],
        "gradiente_numerico_lineal": [round(v, 6) for v in _grad_num(lineal, x)],
        "d(xᵀAx)/dx = (A+Aᵀ)x": [round(v, 6) for v in la.matvec(
            [[a[i][j] + a[j][i] for j in range(2)] for i in range(2)], x)],
        "gradiente_numerico_cuadratico": [round(v, 5) for v in _grad_num(cuadratica, x)],
        "A_simetrica_da_2Ax": [round(2 * v, 6) for v in la.matvec(a, x)],
        "convencion": "layout denominador (gradiente como columna)",
    }


def vector_matrix_derivatives() -> dict:
    """Gradiente de una pérdida cuadrática respecto de los pesos."""
    X = [[1.0, 2.0], [2.0, 1.0], [3.0, 4.0]]
    y = [5.0, 4.0, 11.0]
    w = [1.0, 1.0]

    def perdida(v):
        pred = la.matvec(X, v)
        r = la.sub(pred, y)
        return la.dot(r, r) / len(y)

    residuo = la.sub(la.matvec(X, w), y)
    grad_analitico = la.scale(la.matvec(la.transpose(X), residuo), 2.0 / len(y))
    return {
        "X_shape": la.shape(X),
        "w": w,
        "perdida_MSE": round(perdida(w), 8),
        "∇w_analitico_2Xᵀ(Xw-y)/n": [round(v, 6) for v in grad_analitico],
        "∇w_numerico": [round(v, 6) for v in _grad_num(perdida, w)],
        "coinciden": all(abs(a - b) < 1e-5 for a, b in zip(grad_analitico, _grad_num(perdida, w))),
        "esto_es_una_capa_lineal": True,
    }


def autodiff() -> dict:
    """Autodiferenciación en modo reverso sobre el grafo de cómputo."""
    x = Var(2.0)
    y = Var(3.0)
    z = (x * y + x.sin()) * (y**2)
    z.backward()

    def f(v):
        return (v[0] * v[1] + math.sin(v[0])) * v[1] ** 2

    numerico = _grad_num(f, [2.0, 3.0])
    return {
        "expresion": "(x·y + sin x)·y²",
        "valor": round(z.value, 8),
        "dz/dx_autodiff": round(x.grad, 8),
        "dz/dx_numerico": round(numerico[0], 8),
        "dz/dy_autodiff": round(y.grad, 8),
        "dz/dy_numerico": round(numerico[1], 8),
        "coinciden": all(abs(a - b) < 1e-5 for a, b in
                         zip([x.grad, y.grad], numerico)),
        "barridos_necesarios": "1 hacia adelante + 1 hacia atrás",
        "coste_del_numerico": "2 evaluaciones por variable",
    }


def capstone_backpropagation() -> dict:
    """Capstone: backpropagation manual y automática sobre la misma red."""
    # Red mínima: y_hat = tanh(w2 · tanh(w1·x + b1) + b2), pérdida cuadrática.
    x_val, w1_val, b1_val, w2_val, b2_val, target = 0.5, 1.2, -0.3, 0.8, 0.1, 1.0

    # --- automática ---
    w1, b1, w2, b2 = Var(w1_val), Var(b1_val), Var(w2_val), Var(b2_val)
    h = (w1 * x_val + b1).tanh()
    y_hat = (w2 * h + b2).tanh()
    loss = (y_hat - target) ** 2
    loss.backward()

    # --- manual ---
    z1 = w1_val * x_val + b1_val
    a1 = math.tanh(z1)
    z2 = w2_val * a1 + b2_val
    a2 = math.tanh(z2)
    dl_da2 = 2 * (a2 - target)
    dl_dz2 = dl_da2 * (1 - a2**2)
    dl_dw2 = dl_dz2 * a1
    dl_db2 = dl_dz2
    dl_da1 = dl_dz2 * w2_val
    dl_dz1 = dl_da1 * (1 - a1**2)
    dl_dw1 = dl_dz1 * x_val
    dl_db1 = dl_dz1

    manual = [dl_dw1, dl_db1, dl_dw2, dl_db2]
    auto = [w1.grad, b1.grad, w2.grad, b2.grad]
    return {
        "arquitectura": "x → tanh(w1x+b1) → tanh(w2h+b2) → MSE",
        "prediccion": round(a2, 8),
        "objetivo": target,
        "perdida": round(loss.value, 8),
        "gradientes_manuales": [round(v, 8) for v in manual],
        "gradientes_autodiff": [round(v, 8) for v in auto],
        "parametros": ["w1", "b1", "w2", "b2"],
        "coinciden": all(abs(a - b) < 1e-9 for a, b in zip(manual, auto)),
        "conclusion": "autograd no es magia: es la regla de la cadena en orden inverso",
    }


DEMOS = {
    "multivariable_functions": multivariable_functions,
    "level_curves": level_curves,
    "partial_derivatives": partial_derivatives,
    "gradient": gradient,
    "directional_derivative": directional_derivative,
    "tangent_plane": tangent_plane,
    "multivariable_chain_rule": multivariable_chain_rule,
    "jacobian": jacobian,
    "hessian": hessian,
    "multivariable_taylor": multivariable_taylor,
    "unconstrained_optimization": unconstrained_optimization,
    "lagrange_multipliers": lagrange_multipliers,
    "double_integrals": double_integrals,
    "triple_integrals": triple_integrals,
    "vector_fields": vector_fields,
    "divergence_curl": divergence_curl,
    "matrix_calculus": matrix_calculus,
    "vector_matrix_derivatives": vector_matrix_derivatives,
    "autodiff": autodiff,
    "capstone_backpropagation": capstone_backpropagation,
}

CLASS_DEMOS = {
    "161": "multivariable_functions",
    "162": "level_curves",
    "163": "partial_derivatives",
    "164": "gradient",
    "165": "directional_derivative",
    "166": "tangent_plane",
    "167": "multivariable_chain_rule",
    "168": "jacobian",
    "169": "hessian",
    "170": "multivariable_taylor",
    "171": "unconstrained_optimization",
    "172": "lagrange_multipliers",
    "173": "double_integrals",
    "174": "triple_integrals",
    "175": "vector_fields",
    "176": "divergence_curl",
    "177": "matrix_calculus",
    "178": "vector_matrix_derivatives",
    "179": "autodiff",
    "180": "capstone_backpropagation",
}
