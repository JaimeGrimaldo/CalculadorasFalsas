def secant(f, x0, x1, tol):
    cont = 0
    while abs(f(x1)) > tol:
        x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        cont = cont + 1
    return x1, cont


def f(x):
    return x**3 - 2*x - 5


x0 = float(input("Ingrese el valor de x0: "))
x1 = float(input("Ingrese el valor de x1: "))
tol = float(input("Ingrese el valor de tolerancia: "))

raiz, cont = secant(f, x0, x1, tol)
print("La raíz es:", raiz)
print("La encontro en la vuelta:",cont)
