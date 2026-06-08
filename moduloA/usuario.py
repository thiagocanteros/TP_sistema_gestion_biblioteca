# usuario.py
# Clase Usuario que hereda de Entidad

from moduloA.entidad import Entidad

class Usuario(Entidad):
    def __init__(self, id, nombre, dni):
        super().__init__(id)
        self.nombre = nombre
        self.dni = dni

    def mostrar_info(self):
        return f"Usuario: {self.nombre}, DNI: {self.dni}"

    def validar_datos(self):
        if not self.nombre:
            raise ValueError("El nombre es obligatorio")
        if not isinstance(self.dni, int):
            raise ValueError("El DNI debe ser un número entero")
