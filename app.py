"""
Scientific Calculator — Flask Backend
======================================
Routes:
  • GET  /                  → calculator page
  • GET  /equation/<slug>   → equation detail page (opens in new tab)
  • POST /calculate-equation → equation-specific calculator (used by detail pages)
"""

from flask import Flask, render_template, request, jsonify
import equations
import math

app = Flask(__name__)


# ─────────────────────────────────────────────
# Equation registry — maps URL slugs to metadata
# ─────────────────────────────────────────────

EQUATIONS = {
    # ── Mathematics ──
    "pythagorean-theorem": {
        "name": "Pythagorean Theorem",
        "category": "Mathematics",
        "formula": "c² = a² + b²",
        "description": "Relates the three sides of a right-angled triangle.",
        "params": [
            {"name": "a", "label": "Side a", "type": "number"},
            {"name": "b", "label": "Side b", "type": "number"},
        ],
        "fn": equations.pythagorean_theorem,
    },
    "quadratic-formula": {
        "name": "Quadratic Formula",
        "category": "Mathematics",
        "formula": "x = (-b ± √(b²-4ac)) / 2a",
        "description": "Finds the roots of any quadratic equation ax² + bx + c = 0.",
        "params": [
            {"name": "a", "label": "Coefficient a", "type": "number"},
            {"name": "b", "label": "Coefficient b", "type": "number"},
            {"name": "c", "label": "Constant c", "type": "number"},
        ],
        "fn": equations.quadratic_formula,
    },
    "area-of-circle": {
        "name": "Area of a Circle",
        "category": "Mathematics",
        "formula": "A = π × r²",
        "description": "Calculates the area enclosed by a circle.",
        "params": [
            {"name": "radius", "label": "Radius (r)", "type": "number"},
        ],
        "fn": equations.area_of_circle,
    },
    "volume-of-sphere": {
        "name": "Volume of a Sphere",
        "category": "Mathematics",
        "formula": "V = (4/3) × π × r³",
        "description": "Calculates the volume of a sphere.",
        "params": [
            {"name": "radius", "label": "Radius (r)", "type": "number"},
        ],
        "fn": equations.volume_of_sphere,
    },
    "area-of-triangle": {
        "name": "Area of a Triangle",
        "category": "Mathematics",
        "formula": "A = ½ × base × height",
        "description": "Calculates the area of a triangle from its base and height.",
        "params": [
            {"name": "base", "label": "Base", "type": "number"},
            {"name": "height", "label": "Height", "type": "number"},
        ],
        "fn": equations.area_of_triangle,
    },
    # ── Algebra ──
    "linear-equation": {
        "name": "Linear Equation",
        "category": "Algebra",
        "formula": "y = mx + c",
        "description": "Evaluates a straight-line equation at a given x.",
        "params": [
            {"name": "slope", "label": "Slope (m)", "type": "number"},
            {"name": "intercept", "label": "Intercept (c)", "type": "number"},
            {"name": "x", "label": "x value", "type": "number"},
        ],
        "fn": equations.linear_equation,
    },
    "factorial": {
        "name": "Factorial",
        "category": "Algebra",
        "formula": "n! = n × (n-1) × ... × 1",
        "description": "Computes the factorial of a non-negative integer.",
        "params": [
            {"name": "n", "label": "n", "type": "integer"},
        ],
        "fn": equations.factorial,
    },
    "combination": {
        "name": "Combination (nCr)",
        "category": "Algebra",
        "formula": "C(n,r) = n! / (r! × (n-r)!)",
        "description": "Number of ways to choose r items from n without regard to order.",
        "params": [
            {"name": "n", "label": "n (total)", "type": "integer"},
            {"name": "r", "label": "r (choose)", "type": "integer"},
        ],
        "fn": equations.combination,
    },
    "permutation": {
        "name": "Permutation (nPr)",
        "category": "Algebra",
        "formula": "P(n,r) = n! / (n-r)!",
        "description": "Number of ways to pick r items from n where order matters.",
        "params": [
            {"name": "n", "label": "n (total)", "type": "integer"},
            {"name": "r", "label": "r (pick)", "type": "integer"},
        ],
        "fn": equations.permutation,
    },
    # ── Trigonometry ──
    "sine-rule": {
        "name": "Sine Rule",
        "category": "Trigonometry",
        "formula": "a/sin(A) = b/sin(B)",
        "description": "Solves for an unknown side of a triangle using two angles and a known side.",
        "params": [
            {"name": "a", "label": "Side a", "type": "number"},
            {"name": "A", "label": "Angle A (degrees)", "type": "number"},
            {"name": "B", "label": "Angle B (degrees)", "type": "number"},
        ],
        "fn": equations.sine_rule,
    },
    "cosine-rule": {
        "name": "Cosine Rule",
        "category": "Trigonometry",
        "formula": "c² = a² + b² - 2ab·cos(C)",
        "description": "Finds the third side of a triangle given two sides and the included angle.",
        "params": [
            {"name": "a", "label": "Side a", "type": "number"},
            {"name": "b", "label": "Side b", "type": "number"},
            {"name": "C", "label": "Angle C (degrees)", "type": "number"},
        ],
        "fn": equations.cosine_rule,
    },
    "sine-value": {
        "name": "Sine (sin θ)",
        "category": "Trigonometry",
        "formula": "sin(θ)",
        "description": "Returns the sine of an angle given in degrees.",
        "params": [
            {"name": "angle_deg", "label": "Angle (degrees)", "type": "number"},
        ],
        "fn": equations.sine_value,
    },
    "cosine-value": {
        "name": "Cosine (cos θ)",
        "category": "Trigonometry",
        "formula": "cos(θ)",
        "description": "Returns the cosine of an angle given in degrees.",
        "params": [
            {"name": "angle_deg", "label": "Angle (degrees)", "type": "number"},
        ],
        "fn": equations.cosine_value,
    },
    "tangent-value": {
        "name": "Tangent (tan θ)",
        "category": "Trigonometry",
        "formula": "tan(θ)",
        "description": "Returns the tangent of an angle given in degrees.",
        "params": [
            {"name": "angle_deg", "label": "Angle (degrees)", "type": "number"},
        ],
        "fn": equations.tangent_value,
    },
    # ── Physics ──
    "newtons-second-law": {
        "name": "Newton's Second Law",
        "category": "Physics",
        "formula": "F = m × a",
        "description": "Force equals mass times acceleration.",
        "params": [
            {"name": "mass", "label": "Mass (kg)", "type": "number"},
            {"name": "acceleration", "label": "Acceleration (m/s²)", "type": "number"},
        ],
        "fn": equations.newtons_second_law,
    },
    "kinetic-energy": {
        "name": "Kinetic Energy",
        "category": "Physics",
        "formula": "KE = ½mv²",
        "description": "Energy possessed by an object due to its motion.",
        "params": [
            {"name": "mass", "label": "Mass (kg)", "type": "number"},
            {"name": "velocity", "label": "Velocity (m/s)", "type": "number"},
        ],
        "fn": equations.kinetic_energy,
    },
    "potential-energy": {
        "name": "Potential Energy",
        "category": "Physics",
        "formula": "PE = mgh",
        "description": "Gravitational potential energy relative to a reference height.",
        "params": [
            {"name": "mass", "label": "Mass (kg)", "type": "number"},
            {"name": "gravity", "label": "Gravity (m/s²)", "type": "number"},
            {"name": "height", "label": "Height (m)", "type": "number"},
        ],
        "fn": equations.potential_energy,
    },
    "ohms-law": {
        "name": "Ohm's Law",
        "category": "Physics",
        "formula": "V = I × R",
        "description": "Relates voltage, current, and resistance in an electrical circuit.",
        "params": [
            {"name": "voltage", "label": "Voltage (V)", "type": "number"},
            {"name": "current", "label": "Current (A)", "type": "number"},
            {"name": "resistance", "label": "Resistance (Ω)", "type": "number"},
        ],
        "fn": equations.ohms_law,
    },
    # ── Statistics ──
    "mean": {
        "name": "Arithmetic Mean",
        "category": "Statistics",
        "formula": "x̄ = Σxᵢ / n",
        "description": "The average of a set of numbers.",
        "params": [
            {"name": "values", "label": "Values (comma-separated)", "type": "csv"},
        ],
        "fn": equations.mean,
    },
    "standard-deviation": {
        "name": "Standard Deviation",
        "category": "Statistics",
        "formula": "σ = √(Σ(xᵢ-x̄)²/n)",
        "description": "Measures the spread of a dataset from its mean.",
        "params": [
            {"name": "values", "label": "Values (comma-separated)", "type": "csv"},
        ],
        "fn": equations.standard_deviation,
    },
    "median": {
        "name": "Median",
        "category": "Statistics",
        "formula": "middle value of sorted data",
        "description": "The middle value of a sorted dataset.",
        "params": [
            {"name": "values", "label": "Values (comma-separated)", "type": "csv"},
        ],
        "fn": equations.median,
    },
}


def _group_by_category():
    """Group equations by category for the sidebar."""
    groups = {}
    for slug, info in EQUATIONS.items():
        cat = info["category"]
        groups.setdefault(cat, []).append({"slug": slug, **info})
    return groups


# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", categories=_group_by_category())


@app.route("/equation/<slug>")
def equation_detail(slug):
    info = EQUATIONS.get(slug)
    if not info:
        return "Equation not found", 404
    return render_template("equation.html", slug=slug, eq=info)


@app.route("/calculate-equation", methods=["POST"])
def calculate_equation():
    data = request.get_json(force=True)
    slug = data.get("slug", "")
    params = data.get("params", {})

    info = EQUATIONS.get(slug)
    if not info:
        return jsonify({"error": "Unknown equation"}), 404

    try:
        fn = info["fn"]
        for p in info["params"]:
            if p["type"] == "csv" and p["name"] in params:
                params[p["name"]] = [float(v.strip()) for v in params[p["name"]].split(",")]
            elif p["type"] == "integer" and p["name"] in params:
                params[p["name"]] = int(params[p["name"]])
            elif p["type"] == "number" and p["name"] in params:
                params[p["name"]] = float(params[p["name"]])
        result = fn(**params)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
