import json
import os

FILEPATH_1 = "data/proyectos.json"
FILEPATH_2 = "data/inventario.json"

def load_projects():           
    
    if not os.path.exists(FILEPATH_1):
        return
    try:
        with open(FILEPATH_1, "r") as f:
            data = json.load(f)  
            data = data.get("sesiones")
            return data
    except Exception as e:
        print(f'Error al cargar datos: {e}')
     
def load_inventory():       
    if not os.path.exists(FILEPATH_2):
        return
    try:
        with open(FILEPATH_2, "r") as f:
            data = json.load(f)
            data = data.get("inventory", {})  
            return data
    except Exception as e:
        print(f'Error al cargar datos: {e}')

def save_events(data):       
    sesiones = {
        "sesiones": data
    }
    with open(FILEPATH_1, "w") as f:
        json.dump(sesiones, f, indent=4)
