import requests

# Reemplaza con tu clave API
api_key = '2c6a3d13f40145baa920727467794227'

# Configuración de headers
headers = {
    'X-Auth-Token': api_key
}

# Función para buscar equipos de una liga específica
def buscar_equipos(liga_id):
    url = f'https://api.football-data.org/v4/teams?competitions={liga_id}'
    
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

# ID para la Premier League en Football-Data.org
liga_id = 2021

# Buscar equipos y mostrar resultados
equipos = buscar_equipos(liga_id)

if equipos:
    for equipo in equipos:
        print(f"Nombre del equipo: {equipo['name']}")
else:
    print("No se encontraron equipos.")
