# entidad.py
# Módulo A — Núcleo del dominio y arquitectura base

from abc import ABC, abstractmethod
from datetime import datetime

# --- Metaclase para control de creación de clases ---
class EntidadMeta(type):
    def __new__(mcls, name, bases, namespace):
        if 'id' not in namespace:
            namespace['id'] = None
        print(f"[Metaclase] Creando clase: {name}")
        return super().__new__(mcls, name, bases, namespace)

# --- Decorador para registrar modificaciones ---
def registrar_cambio(func):
    def wrapper(self, *args, **kwargs):
        resultado = func(self, *args, **kwargs)
        print(f"[Decorador] {func.__name__} ejecutado en {datetime.now()}")
        return resultado
    return wrapper

# --- Clase base abstracta ---
class Entidad(ABC, metaclass=EntidadMeta):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def mostrar_info(self):
        pass

    @registrar_cambio
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)
