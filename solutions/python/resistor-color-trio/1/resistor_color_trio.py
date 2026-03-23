COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
UNITS = ["ohms", "kiloohms", "megaohms", "gigaohms"]
def label(colors):
    val1 = COLORS.index(colors[0])
    val2 = COLORS.index(colors[1])
    exponent = COLORS.index(colors[2])
    total_ohms = (val1 * 10 + val2) * (10 ** exponent)
    unit_index = 0
    while total_ohms >= 1000 and total_ohms % 1000 == 0 and unit_index < len(UNITS) - 1:
        total_ohms //= 1000
        unit_index += 1
    return f"{total_ohms} {UNITS[unit_index]}"