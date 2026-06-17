"""
equations.py — Standalone Scientific Equations
================================================

A reusable module containing 22 scientific equation functions.
Each function is independent and can be imported and used on its own:

    from equations import pythagorean_theorem, mean
    print(pythagorean_theorem(3, 4))  # {'a': 3, 'b': 4, 'c': 5.0, ...}
    print(mean([10, 20, 30]))         # {'values': [...], 'mean': 20.0}

Every function accepts numeric inputs and returns a dict containing
all input values plus the computed result(s).

Categories:
    Mathematics  — pythagorean_theorem, quadratic_formula, area_of_circle,
                   volume_of_sphere, area_of_triangle
    Algebra      — linear_equation, factorial, combination, permutation
    Trigonometry — sine_rule, cosine_rule, sine_value, cosine_value,
                   tangent_value
    Physics      — newtons_second_law, kinetic_energy, potential_energy,
                   ohms_law
    Statistics   — mean, standard_deviation, median

Dependencies: Python standard library only (math).
"""

import math


# ─────────────────────────────────────────────
# MATHEMATICS
# ─────────────────────────────────────────────

def pythagorean_theorem(a: float, b: float) -> dict:
    """
    Pythagorean Theorem
    -------------------
    In a right-angled triangle:  c² = a² + b²
    where a and b are the two shorter sides and c is the hypotenuse.

    Parameters:
        a (float): Length of side a
        b (float): Length of side b

    Returns:
        dict: Contains hypotenuse (c), a², b², and c²
    """
    a_sq = a ** 2
    b_sq = b ** 2
    c = math.sqrt(a_sq + b_sq)
    return {
        "a": a,
        "b": b,
        "c": round(c, 6),
        "a_squared": a_sq,
        "b_squared": b_sq,
        "c_squared": round(a_sq + b_sq, 6),
    }


def quadratic_formula(a: float, b: float, c: float) -> dict:
    """
    Quadratic Formula
    -----------------
    Solves  ax² + bx + c = 0
    x = (-b ± √(b² - 4ac)) / 2a

    Parameters:
        a (float): Coefficient of x²
        b (float): Coefficient of x
        c (float): Constant term

    Returns:
        dict: Contains discriminant and real roots (if any)
    """
    discriminant = b ** 2 - 4 * a * c
    result = {
        "a": a, "b": b, "c": c,
        "discriminant": discriminant,
        "root_1": None,
        "root_2": None,
    }
    if discriminant > 0:
        result["root_1"] = round((-b + math.sqrt(discriminant)) / (2 * a), 6)
        result["root_2"] = round((-b - math.sqrt(discriminant)) / (2 * a), 6)
    elif discriminant == 0:
        result["root_1"] = round(-b / (2 * a), 6)
    return result


def area_of_circle(radius: float) -> dict:
    """
    Area of a Circle
    ----------------
    A = π × r²

    Parameters:
        radius (float): Radius of the circle

    Returns:
        dict: Contains radius and area
    """
    area = math.pi * radius ** 2
    return {"radius": radius, "area": round(area, 6)}


def volume_of_sphere(radius: float) -> dict:
    """
    Volume of a Sphere
    ------------------
    V = (4/3) × π × r³

    Parameters:
        radius (float): Radius of the sphere

    Returns:
        dict: Contains radius and volume
    """
    volume = (4 / 3) * math.pi * radius ** 3
    return {"radius": radius, "volume": round(volume, 6)}


def area_of_triangle(base: float, height: float) -> dict:
    """
    Area of a Triangle
    ------------------
    A = ½ × base × height

    Parameters:
        base (float): Base of the triangle
        height (float): Height of the triangle

    Returns:
        dict: Contains base, height, and area
    """
    area = 0.5 * base * height
    return {"base": base, "height": height, "area": round(area, 6)}


# ─────────────────────────────────────────────
# ALGEBRA
# ─────────────────────────────────────────────

def linear_equation(slope: float, intercept: float, x: float) -> dict:
    """
    Linear Equation (Slope-Intercept Form)
    ---------------------------------------
    y = mx + c
    where m is the slope and c is the y-intercept.

    Parameters:
        slope (float): Slope (m) of the line
        intercept (float): Y-intercept (c)
        x (float): x value to evaluate

    Returns:
        dict: Contains slope, intercept, x, and y
    """
    y = slope * x + intercept
    return {"slope": slope, "intercept": intercept, "x": x, "y": round(y, 6)}


def factorial(n: int) -> dict:
    """
    Factorial
    ---------
    n! = n × (n-1) × (n-2) × ... × 2 × 1

    Parameters:
        n (int): Non-negative integer

    Returns:
        dict: Contains n and n!
    """
    result = math.factorial(n)
    return {"n": n, "factorial": result}


def combination(n: int, r: int) -> dict:
    """
    Combination (n choose r)
    ------------------------
    C(n, r) = n! / (r! × (n-r)!)

    Parameters:
        n (int): Total items
        r (int): Items to choose

    Returns:
        dict: Contains n, r, and C(n, r)
    """
    result = math.comb(n, r)
    return {"n": n, "r": r, "combination": result}


def permutation(n: int, r: int) -> dict:
    """
    Permutation (n pick r)
    ----------------------
    P(n, r) = n! / (n-r)!

    Parameters:
        n (int): Total items
        r (int): Items to pick

    Returns:
        dict: Contains n, r, and P(n, r)
    """
    result = math.perm(n, r)
    return {"n": n, "r": r, "permutation": result}


# ─────────────────────────────────────────────
# TRIGONOMETRY
# ─────────────────────────────────────────────

def sine_rule(a: float, A: float, B: float) -> dict:
    """
    Sine Rule
    ---------
    a / sin(A) = b / sin(B)
    Solves for side b given side a and angles A and B (in degrees).

    Parameters:
        a (float): Known side length
        A (float): Angle opposite side a (in degrees)
        B (float): Angle opposite side b (in degrees)

    Returns:
        dict: Contains a, A, B, and computed side b
    """
    A_rad = math.radians(A)
    B_rad = math.radians(B)
    b = a * math.sin(B_rad) / math.sin(A_rad)
    return {"a": a, "A_deg": A, "B_deg": B, "b": round(b, 6)}


def cosine_rule(a: float, b: float, C: float) -> dict:
    """
    Cosine Rule
    -----------
    c² = a² + b² - 2ab × cos(C)
    Finds side c given sides a, b and included angle C (in degrees).

    Parameters:
        a (float): Side a
        b (float): Side b
        C (float): Included angle (in degrees)

    Returns:
        dict: Contains a, b, C, and computed side c
    """
    C_rad = math.radians(C)
    c_sq = a ** 2 + b ** 2 - 2 * a * b * math.cos(C_rad)
    c = math.sqrt(c_sq)
    return {"a": a, "b": b, "C_deg": C, "c": round(c, 6)}


def sine_value(angle_deg: float) -> dict:
    """
    Sine of an Angle
    -----------------
    sin(θ)  where θ is in degrees.

    Parameters:
        angle_deg (float): Angle in degrees

    Returns:
        dict: Contains angle in degrees and its sine value
    """
    return {"angle_deg": angle_deg, "sine": round(math.sin(math.radians(angle_deg)), 6)}


def cosine_value(angle_deg: float) -> dict:
    """
    Cosine of an Angle
    -------------------
    cos(θ)  where θ is in degrees.

    Parameters:
        angle_deg (float): Angle in degrees

    Returns:
        dict: Contains angle in degrees and its cosine value
    """
    return {"angle_deg": angle_deg, "cosine": round(math.cos(math.radians(angle_deg)), 6)}


def tangent_value(angle_deg: float) -> dict:
    """
    Tangent of an Angle
    -------------------
    tan(θ)  where θ is in degrees.

    Parameters:
        angle_deg (float): Angle in degrees

    Returns:
        dict: Contains angle in degrees and its tangent value
    """
    return {"angle_deg": angle_deg, "tangent": round(math.tan(math.radians(angle_deg)), 6)}


# ─────────────────────────────────────────────
# PHYSICS
# ─────────────────────────────────────────────

def newtons_second_law(mass: float, acceleration: float) -> dict:
    """
    Newton's Second Law
    -------------------
    F = m × a
    where F is force (N), m is mass (kg), a is acceleration (m/s²).

    Parameters:
        mass (float): Mass in kg
        acceleration (float): Acceleration in m/s²

    Returns:
        dict: Contains mass, acceleration, and force
    """
    force = mass * acceleration
    return {"mass": mass, "acceleration": acceleration, "force": round(force, 6)}


def kinetic_energy(mass: float, velocity: float) -> dict:
    """
    Kinetic Energy
    ---------------
    KE = ½ × m × v²

    Parameters:
        mass (float): Mass in kg
        velocity (float): Velocity in m/s

    Returns:
        dict: Contains mass, velocity, and kinetic energy
    """
    ke = 0.5 * mass * velocity ** 2
    return {"mass": mass, "velocity": velocity, "kinetic_energy": round(ke, 6)}


def potential_energy(mass: float, gravity: float, height: float) -> dict:
    """
    Gravitational Potential Energy
    ------------------------------
    PE = m × g × h

    Parameters:
        mass (float): Mass in kg
        gravity (float): Gravitational field strength (m/s²), use 9.81 for Earth
        height (float): Height in metres

    Returns:
        dict: Contains mass, gravity, height, and potential energy
    """
    pe = mass * gravity * height
    return {"mass": mass, "gravity": gravity, "height": height, "potential_energy": round(pe, 6)}


def ohms_law(voltage: float = None, current: float = None, resistance: float = None) -> dict:
    """
    Ohm's Law
    ---------
    V = I × R
    Provide any two values to calculate the third.

    Parameters:
        voltage (float): Voltage in volts (optional)
        current (float): Current in amps (optional)
        resistance (float): Resistance in ohms (optional)

    Returns:
        dict: Contains all three electrical quantities
    """
    provided = sum(x is not None for x in [voltage, current, resistance])
    if provided < 2:
        return {"error": "Provide at least two of voltage, current, resistance"}
    if voltage is None:
        voltage = current * resistance
    elif current is None:
        current = voltage / resistance
    elif resistance is None:
        resistance = voltage / current
    return {
        "voltage": round(voltage, 6),
        "current": round(current, 6),
        "resistance": round(resistance, 6),
    }


# ─────────────────────────────────────────────
# STATISTICS
# ─────────────────────────────────────────────

def mean(values: list) -> dict:
    """
    Arithmetic Mean
    ---------------
    x̄ = (Σ xᵢ) / n

    Parameters:
        values (list): List of numbers

    Returns:
        dict: Contains the list and its mean
    """
    m = sum(values) / len(values)
    return {"values": values, "mean": round(m, 6)}


def standard_deviation(values: list) -> dict:
    """
    Standard Deviation (Population)
    ------------------------------
    σ = √( Σ(xᵢ - x̄)² / n )

    Parameters:
        values (list): List of numbers

    Returns:
        dict: Contains the list, mean, variance, and standard deviation
    """
    m = sum(values) / len(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    return {
        "values": values,
        "mean": round(m, 6),
        "variance": round(variance, 6),
        "standard_deviation": round(std_dev, 6),
    }


def median(values: list) -> dict:
    """
    Median
    ------
    The middle value when the list is sorted.

    Parameters:
        values (list): List of numbers

    Returns:
        dict: Contains the list and its median
    """
    s = sorted(values)
    n = len(s)
    if n % 2 == 1:
        med = s[n // 2]
    else:
        med = (s[n // 2 - 1] + s[n // 2]) / 2
    return {"values": values, "median": round(med, 6)}
