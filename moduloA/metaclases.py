# metaclases.py
# Ejemplo de metaclase para controlar la creación de clases

class EntidadMeta(type):
    def __new__(mcls, name, bases, namespace):
        # Validación: todas las clases deben tener atributo 'id'
        if 'id' not in namespace:
            namespace['id'] = None
        
        print(f"[Metaclase] Creando clase: {name}")
        return super().__new__(mcls, name, bases, namespace)
