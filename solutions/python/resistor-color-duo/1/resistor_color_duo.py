color_map = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
def value(colors):
    first_two = colors[:2]
    digits = [color_map[color.lower()] for color in first_two]
    return int(f"{digits[0]}{digits[1]}")

