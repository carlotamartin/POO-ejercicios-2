import ClassVisitable import*
import ClassVisitante import*
import ClassMostrar import*


class Principal:
    mostrar_ok = Mostrar('"OK"')
    mostrar_ko = Mostrar('"KO"')
    alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko)
    bloque_alternativa = Bloque()
    bloque_alternativa.agregarInstruccion(alternativa)
    bucle = MientrasQue(True, bloque_alternativa) 
