from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)


def calcular(operacion, a, b=None):
    """Realiza una operación matemática sin ejecutar código arbitrario."""
    if operacion == "suma":
        return a + b
    if operacion == "resta":
        return a - b
    if operacion == "multiplicacion":
        return a * b
    if operacion == "division":
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
    if operacion == "potencia":
        resultado = a ** b
        if isinstance(resultado, complex) or not math.isfinite(float(resultado)):
            raise ValueError("El resultado no es un número real finito.")
        return resultado
    if operacion == "raiz_cuadrada":
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada real de un número negativo.")
        return math.sqrt(a)
    if operacion == "raiz_cubica":
        return math.copysign(abs(a) ** (1 / 3), a)
    if operacion == "factorial":
        if a < 0 or not a.is_integer():
            raise ValueError("El factorial requiere un entero no negativo.")
        if a > 170:
            raise ValueError("Para mantener un resultado manejable, usa un entero de hasta 170.")
        return math.factorial(int(a))
    if operacion == "media":
        if b is None:
            raise ValueError("Introduce dos números para calcular la media.")
        return (a + b) / 2
    raise ValueError("Selecciona una operación válida.")


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/calcular")
def api_calcular():
    data = request.get_json(silent=True) or {}
    try:
        operacion = str(data.get("operacion", ""))
        a = float(data.get("a", ""))
        b_raw = data.get("b")
        b = float(b_raw) if b_raw not in (None, "") else None

        if not math.isfinite(a) or (b is not None and not math.isfinite(b)):
            raise ValueError("Introduce números finitos.")

        resultado = calcular(operacion, a, b)
        if isinstance(resultado, float) and not math.isfinite(resultado):
            raise ValueError("El resultado no es finito.")
        if isinstance(resultado, float):
            resultado = round(resultado, 10)
        return jsonify({"ok": True, "resultado": resultado})
    except (ValueError, OverflowError) as exc:
        return jsonify({"ok": False, "error": str(exc) or "No se pudo realizar la operación."}), 400


if __name__ == "__main__":
    app.run(debug=True)
