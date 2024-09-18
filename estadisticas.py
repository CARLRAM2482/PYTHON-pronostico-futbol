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

# Función para obtener los últimos partidos del equipo
def obtener_resultados_equipo(equipo_id):
    url = f'https://api.football-data.org/v4/teams/{equipo_id}/matches'
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data['matches']  # Devuelve la lista de partidos
        else:
            print(f'Error en la solicitud: {response.status_code}')
            print(response.json())  # Mostrar detalles del error
            return []
    except Exception as e:
        print(f'Error al obtener resultados: {e}')
        return []

# Función para obtener estadísticas de un partido
def obtener_estadisticas_partido(partido_id):
    url = f'https://api.football-data.org/v4/matches/{partido_id}'
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data['match']  # Devuelve los detalles del partido
        else:
            print(f'Error en la solicitud: {response.status_code}')
            print(response.json())  # Mostrar detalles del error
            return {}
    except Exception as e:
        print(f'Error al obtener estadísticas: {e}')
        return {}

# ID para la Premier League en Football-Data.org
liga_id = 2021  # Cambia este ID según la liga que deseas consultar

# Buscar equipos y mostrar resultados
equipos = buscar_equipos(liga_id)

if equipos:
    nombre_equipo_buscado = 'Manchester United'  # Cambia el nombre del equipo que deseas buscar
    equipo_encontrado = buscar_equipo_por_nombre(equipos, nombre_equipo_buscado)
    
    if equipo_encontrado:
        equipo_id = equipo_encontrado['id']
        print(f"Equipo encontrado: {equipo_encontrado['name']}")

        # Obtener los resultados de los partidos del equipo
        resultados = obtener_resultados_equipo(equipo_id)
        
        if resultados:
            for partido in resultados:
                fecha = partido['utcDate']
                local = partido['homeTeam']['name']
                visitante = partido['awayTeam']['name']
                goles_local = partido['score']['fullTime']['home']
                goles_visitante = partido['score']['fullTime']['away']
                
                print(f"Fecha: {fecha}")
                print(f"{local} {goles_local} - {goles_visitante} {visitante}")

                # Obtener estadísticas del partido
                partido_id = partido['id']
                estadisticas = obtener_estadisticas_partido(partido_id)
                
                if estadisticas:
                    print(f"Tiros al arco local: {estadisticas['homeTeam']['statistics']['shotsOnGoal']}")
                    print(f"Tiros al arco visitante: {estadisticas['awayTeam']['statistics']['shotsOnGoal']}")
                    print(f"Faltas local: {estadisticas['homeTeam']['statistics']['fouls']}")
                    print(f"Faltas visitante: {estadisticas['awayTeam']['statistics']['fouls']}")
                    print(f"Tiros de esquina local: {estadisticas['homeTeam']['statistics']['corners']}")
                    print(f"Tiros de esquina visitante: {estadisticas['awayTeam']['statistics']['corners']}")
                    print()
                else:
                    print("No se encontraron estadísticas para el partido.")
        else:
            print("No se encontraron resultados.")
    else:
        print("Equipo no encontrado.")
else:
    print("No se encontraron equipos.")
