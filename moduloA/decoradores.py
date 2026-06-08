# decoradores.py
# Decoradores útiles para el Módulo A

from datetime import datetime

# Decorador para registrar cambios en métodos
def registrar_cambio(func):
    def wrapper(self, *args, **kwargs):
        resultado = func(self, *args, **kwargs)
        print(f"[Decorador] Método {func.__name__} ejecutado en {datetime.now()}")
        return resultado
    return wrapper

# Decorador para validar datos antes de ejecutar un método
def validar_datos(func):
    def wrapper(self, *args, **kwargs):
        self.validar_datos()  # Llama al método de validación de la clase
        return func(self, *args, **kwargs)
    return wrapper
