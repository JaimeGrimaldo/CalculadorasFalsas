def biseccion(f, a, b, tol):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return None
    i = 0
    while abs(b - a) > tol:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        i += 1
        print(f"Iteración {i}: a={a}, b={b}, c={c}, f(c)={fc}")
    return (a + b) / 2

f = lambda x: -x**3 + x**2 + 1.5
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tol = float(input("Ingrese la tolerancia deseada: "))

raiz = biseccion(f, a, b, tol)
if raiz is None:
    print("No se encontró una raíz en el intervalo dado.")
else:
    print(f"La raíz aproximada es {raiz}")