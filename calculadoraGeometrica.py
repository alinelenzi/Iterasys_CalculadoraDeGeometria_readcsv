def calculaAreaQuadrado (lado):
    if lado > 0:
        return lado**2
    else:
        return "O lado do quadrado deve ser maior que zero"

def calculaAreaRetangulo (base, altura):
    if base > 0 and altura > 0:
        return base*altura
    else:
        return "A base e altura do retangulo devem ser maiores que zero"

def calculaAreaTriangulo (base, altura):
    if base > 0 and altura > 0:
        return base*altura/2;
    else:
        return "A base e altura do triangulo devem ser maiores que zero"


