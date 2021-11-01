import numpy as np
import math as mt

class Regresion:

    cantObser = None
    valoresX = []
    valoresY = []

    valX2 = []
    
    coeDet = None
    sr = None

    consts = []
    
    #es la media del valor que se usa para calcular la varianza con cada valor
    valProme = None
    
    sumVarianza = None

    matA = None
    matB = None

    def __init__(self, valX, valY):
        self.valoresX = valX
        self.valoresY = valY
        self.cantObser = len(self.valoresY)
        self.calcularDatos()

    def calcularDatos(self):

        if len(self.valX2) == 0:
            for i in range(len(self.valoresX)):
                self.valX2.append(self.valoresX[i] * self.valoresX[i]) 
        self.sumVarianza = sum(self.varianza)

    def calcularVarianza(self, vals):
        for i in range(len(vals)):   
            self.varianza.append((vals[i] - self.valProme)**2)

    def calcularConsts(self):
        self.crearMatrices()
        self.consts = np.dot(np.linalg.inv(self.matA), self.matB)

    def calcularCoeDet(self, sumVarianza, sr):
        self.coeDet = (sumVarianza - sr)/sumVarianza


class RegresionLineal(Regresion):

    valXY = []
    varianza = []
    evalFun = []

    def calcularDatos(self):
        self.valProme = sum(self.valoresY)/self.cantObser
        self.calcularVarianza(self.valoresY)
        super().calcularDatos()
        for i in range(len(self.valoresX)):
            self.valXY.append(self.valoresX[i] * self.valoresY[i])
        self.calcularConsts()
        self.calcularEvalFun()
        self.calcularCoeDet(self.sumVarianza, self.sr)
        

    def crearMatrices(self):
        self.matA = np.array([[self.cantObser, sum(self.valoresX)],[sum(self.valoresX), sum(self.valX2)]])
        self.matB = np.array([[sum(self.valoresY)],[sum(self.valXY)]])

    def calcularEvalFun(self):
        for i in range(self.cantObser):
            self.evalFun.append((self.valoresY[i] - float(self.consts[0]) - float(self.consts[1]*self.valoresX[i]))**2)
        self.sr = sum(self.evalFun)

    def armarFuncion(self):
        return ("y = {:.2f} + {:.2f} x".format(float(self.consts[0]), float(self.consts[1])))

    def mostrarTodo(self):
        print(self.valoresX)
        print(self.valoresY)
        print(self.valXY)
        print(self.valX2)
        print(self.valProme)
        print(self.varianza)
        print(self.evalFun)
        print(self.consts)
        print(self.sr)
        print(self.coeDet)


class RegresionPolinomial(Regresion):

    valX3 = []
    valX4 = []
    valXY = []
    valX2Y = []
    varianza = []
    evalFun = []

    def calcularDatos(self):
        self.valProme = sum(self.valoresY)/self.cantObser
        self.calcularVarianza(self.valoresY)
        super().calcularDatos()

        for i in range(self.cantObser):
            self.valX3.append(self.valoresX[i]**3)
            self.valX4.append(self.valoresX[i]**4)
            self.valXY.append(self.valoresX[i] * self.valoresY[i])
            self.valX2Y.append(self.valX2[i] * self.valoresY[i])

        self.calcularConsts()
        self.calcularEvalFun()
        self.calcularCoeDet(self.sumVarianza, self.sr)
        

    def calcularEvalFun(self):
        for i in range(self.cantObser):
            self.evalFun.append((self.valoresY[i] - float(self.consts[0]) - float(self.consts[1]*self.valoresX[i]) - float(self.consts[2]*self.valX2[i]))**2)
        self.sr = sum(self.evalFun)
    
    def crearMatrices(self):
        self.matA = np.array([[self.cantObser, sum(self.valoresX), sum(self.valX2)], [sum(self.valoresX), sum(self.valX2), sum(self.valX3)], [sum(self.valX2), sum(self.valX3), sum(self.valX4)]])
        self.matB = np.array([[sum(self.valoresY)], [sum(self.valXY)], [sum(self.valX2Y)]])

    def armarFuncion(self):
        return ("y = {:.2f} + {:.2f} x + {:.2f} x^2".format(float(self.consts[0]), float(self.consts[1]), float(self.consts[2])))

    def mostrarTodo(self):
        print(self.valoresX)
        print(self.valoresY)
        print(self.valX2)
        print(self.valX3)
        print(self.valX4)
        print(self.valXY)
        print(self.valX2Y)
        print(self.valProme)
        print(self.varianza)
        print(self.evalFun)
        print(self.consts)
        print(self.sr)
        print(self.coeDet)

class RegresionExponencial(Regresion):

    valLny = []
    valXLny = []
    varianza = []
    evalFun = []

    def calcularDatos(self):
        for i in range(self.cantObser):
            self.valLny.append(mt.log(self.valoresY[i]))
            self.valXLny.append(self.valoresX[i] * mt.log(self.valoresY[i]))
        self.valProme = sum(self.valLny)/self.cantObser
        self.calcularVarianza(self.valLny)
        super().calcularDatos()
        self.calcularConsts()
        self.calcularEvalFun()
        self.calcularCoeDet(self.sumVarianza, self.sr)

    def crearMatrices(self):
        self.matA = np.array([[self.cantObser, sum(self.valoresX)],[sum(self.valoresX), sum(self.valX2)]])
        self.matB = np.array([[sum(self.valLny)],[sum(self.valXLny)]])

    def calcularEvalFun(self):
        for i in range(self.cantObser):
            self.evalFun.append(float((self.valLny[i] - mt.log(mt.exp(self.consts[0])) - self.consts[1]*self.valoresX[i])**2))
        self.sr = sum(self.evalFun)

    def armarFuncion(self):
        return ("y = {:.2f} e^{:.2f} x".format(float(mt.exp(self.consts[0])), float(self.consts[1])))

    def mostrarTodo(self):
        print(self.valoresX)
        print(self.valoresY)
        print(self.valX2)
        print(self.valLny)
        print(self.valXLny)
        print(self.valProme)
        print(self.varianza)
        print(self.evalFun)
        print(self.consts)
        print(self.sr)
        print(self.coeDet)