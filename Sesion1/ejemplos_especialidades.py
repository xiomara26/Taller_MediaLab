# ejemplos_especialidades.py
# Un diccionario por especialidad: cambian las claves, no la lógica.

periodismo = {"medio": "RPP", "fecha": "2026-09-16", "enlace": "https://ejemplo.pe/nota"}
publicidad = {"canal": "Instagram", "formato": "reel", "fecha": "2026-10-01"}
audiovisual = {"escena": 3, "duracion_seg": 45, "locacion": "Mercado central"}
desarrollo = {"comunidad": "Comunidad de ejemplo", "indicador": "Acceso a agua", "fuente": "INEI"}

casos = [periodismo, publicidad, audiovisual, desarrollo]
print("Casos cargados:", len(casos))
print("Claves de publicidad:", list(publicidad.keys()))
print("Locación de la escena:", audiovisual["locacion"])
