# Scientific Calculator

A full-featured scientific calculator built with **Flask**, **Tailwind CSS**, and **vanilla JavaScript**. Includes a sidebar of 22 reusable equations across Mathematics, Algebra, Trigonometry, Physics, and Statistics — each opening in its own tab with explanations and an interactive calculator.

---

## Features

- **Scientific calculator** — sin, cos, tan, log, ln, sqrt, cbrt, factorial, powers, constants (pi, e)
- **Keyboard support** — type expressions directly, press Enter to evaluate
- **22 equations** in a sidebar organized by category (Mathematics, Algebra, Trigonometry, Physics, Statistics)
- **Equation detail pages** — click any equation to open a new tab showing formula, explanation, interactive calculator, and Python source code
- **Equations module** (`equations.py`) — standalone, importable functions for use in other Python projects
- **Client-side evaluation** — all basic arithmetic is evaluated in JavaScript (no server round-trip)

---

## Project Structure

```
calculator/
  app.py              # Flask backend — routes and equation registry
  equations.py        # Standalone equation functions (reusable module)
  requirements.txt    # Python dependencies
  README.md
  templates/
    index.html        # Main calculator page with sidebar
    equation.html     # Equation detail page (opens in new tab)
```

---

## Prerequisites

- **Python 3.9 or higher** — [python.org/downloads](https://www.python.org/downloads/)
- **pip** — comes bundled with Python
- (Optional) **uv** — faster Python package manager — [docs.astral.sh/uv](https://docs.astral.sh/uv/)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/calculator.git
cd calculator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

| Platform | Command |
|----------|---------|
| **Windows (PowerShell)** | `.venv\Scripts\Activate.ps1` |
| **Windows (cmd)** | `.venv\Scripts\activate.bat` |
| **macOS / Linux** | `source .venv/bin/activate` |

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or if using **uv**:

```bash
uv venv .venv
uv pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

The server starts at **http://127.0.0.1:5000**. Open that URL in your browser.

Press `Ctrl+C` to stop the server.

---

## How to Use

### Calculator

| Action | How |
|--------|-----|
| Type numbers | Click the number buttons or use your keyboard |
| Operators | Click `+`, `−`, `×`, `÷` or type `+`, `-`, `*`, `/` |
| Scientific functions | Click `sin`, `cos`, `tan`, `log`, `√`, etc. |
| Exponent | Click `x²`, `x³`, or `^` for custom power |
| Evaluate | Click `=` or press `Enter` |
| Clear | Click `AC` or press `Escape` |
| Delete last character | Click `⌫` or press `Backspace` |

### Sidebar Equations

1. The sidebar on the left shows equations grouped by category
2. Click a category header to expand/collapse it
3. Click any equation name — it opens in a **new tab**
4. In the new tab you'll see:
   - The formula and what it does
   - An interactive calculator — fill in the fields and click **Calculate**
   - A plain-English explanation of how the equation works
   - The Python source code you can copy into your own project

---

## Using the Equations Module

The `equations.py` file is completely standalone. You can import it into any Python project:

```python
from equations import pythagorean_theorem, quadratic_formula, mean

# Pythagorean theorem: a=3, b=4 → c=5
result = pythagorean_theorem(3, 4)
print(result)  # {'a': 3, 'b': 4, 'c': 5.0, ...}

# Quadratic: x² - 5x + 6 = 0 → roots at 3 and 2
result = quadratic_formula(1, -5, 6)
print(result)  # {'discriminant': 1, 'root_1': 3.0, 'root_2': 2.0}

# Average of a list
result = mean([10, 20, 30, 40, 50])
print(result)  # {'mean': 30.0, ...}
```

### Available Functions

| Category | Function | Formula |
|----------|----------|---------|
| **Mathematics** | `pythagorean_theorem(a, b)` | c = sqrt(a² + b²) |
| | `quadratic_formula(a, b, c)` | x = (-b ± sqrt(b²-4ac)) / 2a |
| | `area_of_circle(radius)` | A = pi * r² |
| | `volume_of_sphere(radius)` | V = (4/3) * pi * r³ |
| | `area_of_triangle(base, height)` | A = 0.5 * b * h |
| **Algebra** | `linear_equation(slope, intercept, x)` | y = mx + c |
| | `factorial(n)` | n! |
| | `combination(n, r)` | C(n,r) = n! / (r! * (n-r)!) |
| | `permutation(n, r)` | P(n,r) = n! / (n-r)! |
| **Trigonometry** | `sine_rule(a, A, B)` | a/sin(A) = b/sin(B) |
| | `cosine_rule(a, b, C)` | c² = a² + b² - 2ab*cos(C) |
| | `sine_value(angle_deg)` | sin(theta) |
| | `cosine_value(angle_deg)` | cos(theta) |
| | `tangent_value(angle_deg)` | tan(theta) |
| **Physics** | `newtons_second_law(mass, accel)` | F = m * a |
| | `kinetic_energy(mass, velocity)` | KE = 0.5 * m * v² |
| | `potential_energy(mass, gravity, height)` | PE = m * g * h |
| | `ohms_law(voltage, current, resistance)` | V = I * R (provide any two) |
| **Statistics** | `mean(values)` | Sum / count |
| | `standard_deviation(values)` | Population std dev |
| | `median(values)` | Middle value |

Every function returns a `dict` with all input values and the computed result.

---

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, Tailwind CSS (via CDN), vanilla JavaScript
- **Evaluation:** Client-side JavaScript (no server round-trip for basic calculations)
- **Equations:** Standalone Python module (`equations.py`)

---

## License

MIT — use freely in personal or commercial projects.
