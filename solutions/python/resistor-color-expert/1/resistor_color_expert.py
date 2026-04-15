def resistor_label(colors):
    digits = {
        "black":0,"brown":1,"red":2,"orange":3,"yellow":4,
        "green":5,"blue":6,"violet":7,"grey":8,"white":9
    }

    tolerance = {
        "grey":0.05,"violet":0.1,"blue":0.25,"green":0.5,
        "brown":1,"red":2,"gold":5,"silver":10
    }

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        value = (digits[colors[0]] * 10 + digits[colors[1]]) * (10 ** digits[colors[2]])
        tol = tolerance[colors[3]]
    else:
        value = (digits[colors[0]] * 100 +
                 digits[colors[1]] * 10 +
                 digits[colors[2]]) * (10 ** digits[colors[3]])
        tol = tolerance[colors[4]]

    # Unit conversion
    if value >= 1_000_000:
        value /= 1_000_000
        unit = "megaohms"
    elif value >= 1000:
        value /= 1000
        unit = "kiloohms"
    else:
        unit = "ohms"

    # Clean value (remove .0)
    if value == int(value):
        value = int(value)

    # ✅ FIXED tolerance formatting
    tol_str = str(tol).rstrip('0').rstrip('.')

    return f"{value} {unit} ±{tol_str}%"
