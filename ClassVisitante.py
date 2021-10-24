from Clase bloque import*


class Visitante:
    def __init__(self):
        # Indica el nivel actual de tabulación.
        self.tabulacion = 0
    def tabular(self, mensaje):
        # Mostrar un mensaje, precedido del número actual
        # de tabulaciones requeridas.
        print("{}{}".format('\t' * self.tabulacion, mensaje))
    def escribirBloque(self, bloque):
        # Se incrementa el nivel de tabulación.
        self.tabulacion += 1
        # Se visita el bloque.
        bloque.acepta(self)
        # Se decrementa el nivel de tabulación.
        self.tabulacion -= 1
    def visitaSi(self, si):
        # Mostrar la instrucción 'if' seguida de su condición.
        self.tabular("if {}:".format(si.condicion))
        # Se escribe el primer bloque.
        self.escribirBloque(si.entonces)
        # Se escribe la palabra clave 'else'
        self.tabular("else:")
        # Se escribe el bloque 'else'.
        self.escribirBloque(si.si_no)
    def visitaMientrasQue(self, mientrasque):
        # Se escribe la instrucción 'while'.
        self.tabular("while {}:".format(mientrasque.condicion))
        # Después se escribe el bloque.
        self.escribirBloque(mientrasque.bloque)
    def visitaMostrar(self, mostrar):
        self.tabular("print({})".format(mostrar.mensaje))
        def visitaBloque(self, bloque):
        # Se visita cada instrucción del bloque.
        for instruccion in bloque.instrucciones:
        instruccion.acepta(self)