import sys
# La vista se encarga de recuperar la acción del usuario
# que consiste en escribir una línea de texto en la entrada estándar.

class Vista:
    def entrada(self):
        return sys.stdin.readline()
# El controlador hace el enlace entre la vista y el modelo,
# realizando el procesamiento de datos.