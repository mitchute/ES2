from CoolProp.CoolProp import PropsSI


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def get_cp(temperature):
    return PropsSI("C", "T", temperature + 273.15, "P", 120000, "WATER")
