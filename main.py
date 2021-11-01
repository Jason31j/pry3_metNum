import clases as cls
import numpy as np

#un bucle que pregunte si se desea seguir introduciendo datos
#que en cada iteracion se reciba un valor de x y uno de y y al final se haga .append()

valoresX = []
valoresY = []
decision = 1

decision = int(input("Desea ingresar datos\n 1.Si\n 2.No\n"))
while (decision == 1):
    
    valX = float(input("Ingrese el valor de X: "))
    valY = float(input("Ingrese el valor de Y: "))
    valoresX.append(valX)
    valoresY.append(valY)
    decision = int(input("Desea ingresar más datos\n 1.Si\n 2.No\n"))


if(len(valoresY) < 3):
    print("No se ingresaron valores suficientes para ejecutar la regreseión")
else:
    
    lineal = cls.RegresionLineal(valoresX, valoresY)
    print("El modelo lineal es: "+ lineal.armarFuncion())
    print(lineal.coeDet)
    print("===========================")

    polinomial = cls.RegresionPolinomial(valoresX, valoresY)
    print("El modelo polinomial de 2do grado es: " + polinomial.armarFuncion())
    print(polinomial.coeDet)
    print("===========================")

    exponencial = cls.RegresionExponencial(valoresX, valoresY)
    print("El modelo exponencial es: "+ exponencial.armarFuncion())
    print(exponencial.coeDet)
    print("===========================")
    

if(lineal.coeDet > polinomial.coeDet and lineal.coeDet > exponencial.coeDet):
    print("El mejor ajuste fue con regresión lineal con un coeficiente de determinación {} y un coeficiente de correlación {}".format(lineal.coeDet, lineal.coeDet**0.5))    
elif(polinomial.coeDet > lineal.coeDet and polinomial.coeDet > exponencial.coeDet):
    print("El mejor ajuste fue con regresión polinomial de segundo grado con un coeficiente de determinación de {} y un coeficiente de correlación {}".format(polinomial.coeDet, polinomial.coeDet**0.5))    
else:
    print("El mejor ajuste fue con regresión exponencial con un coeficiente de determinación {} y un coeficiente de correlación {}".format(exponencial.coeDet, exponencial.coeDet**0.5))        
