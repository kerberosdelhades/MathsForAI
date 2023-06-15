def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplificar_fraccion(fraccion):
    numerador, denominador = fraccion.split('/')
    numerador = int(numerador)
    denominador = int(denominador)
    
    mcd = gcd(numerador, denominador)
    
    numerador_reducido = numerador // mcd
    denominador_reducido = denominador // mcd
    
    return f"{numerador_reducido}/{denominador_reducido}"

fraccion_input = input("Ingrese la fracción (en el formato 'numerador/denominador'): ")

fraccion_simplificada = simplificar_fraccion(fraccion_input)

print("Fracción simplificada:", fraccion_simplificada)
