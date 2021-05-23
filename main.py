"""
proyecto python Mysql:
-Abrir asistente
-Login o registro
-Si elegimos registro, crear un usuario en la bbdd
-Si elegimos login, identifica al usuario y nos preguntara
-Crear nota, mostrar notas, borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -registro
    -login
""")
hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()    

elif accion == "login":
    hazEl.login()
    

