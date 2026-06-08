# libro.py
# Clase Libro que hereda de Entidad

from moduloA.entidad import Entidad

class Libro(Entidad):
    def __init__(self, id, titulo, autor, anio):
        super().__init__(id)
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        return f"Libro: {self.titulo} ({self.anio}), Autor: {self.autor}"

    def validar_datos(self):
        if not self.titulo or not self.autor:
            raise ValueError("El título y el autor son obligatorios")
        if not isinstance(self.anio, int):
            raise ValueError("El año debe ser un número entero")
