import requests

# Reemplaza con tu clave API
api_key = '2c6a3d13f40145baa920727467794227'

# Configuración de headers
headers = {
    'X-Auth-Token': api_key
}

# Función para buscar equipos de una liga específica
def buscar_equipos(liga_id):
    url = f'https://api.football-data.org/v4/competitions/{liga_id}/teams'
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data['teams']  # Devuelve la lista de equipos
        else:
            print(f'Error en la solicitud: {response.status_code}')
            print(response.json())  # Mostrar detalles del error
            return []
    except Exception as e:
        print(f'Error al buscar equipos: {e}')
        return []

# Función para buscar un equipo por nombre
def buscar_equipo_por_nombre(equipos, nombre_equipo):
    for equipo in equipos:
        if nombre_equipo.lower() in equipo['name'].lower():
            return equipo
    return None

# ID para la Premier League en Football-Data.org
liga_id = 2021  # Cambia este ID según la liga que deseas consultar

# Buscar equipos y mostrar resultados
equipos = buscar_equipos(liga_id)

if equipos:
    nombre_equipo_buscado = 'Manchester United'  # Cambia el nombre del equipo que deseas buscar
    equipo_encontrado = buscar_equipo_por_nombre(equipos, nombre_equipo_buscado)
    
    if equipo_encontrado:
        print(f"Equipo encontrado: {equipo_encontrado['name']}")
    else:
        print("Equipo no encontrado.")
else:
    print("No se encontraron equipos.")
