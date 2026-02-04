import streamlit as st
import re
import datetime as datetime
from time import sleep
from core import load_projects, load_inventory, save_events

def validate_name(name, field_name):

    if not re.match(r'^[A-Za-z\\s-]+$', name):
        return False, f"{field_name} debe contener solo letras, espacios o guiones."
    if len(name) < 2:
        return False, f"{field_name} debe tener al menos dos caracteres de longitud."
    return True, ""

def reset():
    st.session_state.sesión = {
        "Nombre": None,
        "Apellido": None,
        "Fecha": None,
        "Espacio": None,
        "Iluminación": None,
        "Cámara": None,
        "Fotógrafo": None,
        "Auxiliar": None,
        "Vestuario": 0}
    
    st.session_state.inventario = {
        "Local": "",
        "Cámara": [],
        "Fotógrafo": "",
        "Vestuario": None,
        "Auxiliar": [],
        "Espacio": []
    }
    st.session_state.eventos_programados = load_projects()

if "inventario" not in st.session_state:
    st.session_state.inventario = {
        "Local": "",
        "Cámara": [],
        "Fotógrafo": "",
        "Vestuario": None,
        "Auxiliar": [],
        "Espacio": []
    }

if "sesión" not in st.session_state:
    st.session_state.sesión = {
        "Nombre": None,
        "Apellido": None,
        "Fecha": None,
        "Espacio": None,
        "Iluminación": None,
        "Cámara": None,
        "Fotógrafo": None,
        "Auxiliar": None,
        "Vestuario": 0
    }

if "eventos_programados" not in st.session_state:
    st.session_state.eventos_programados = load_projects()

st.header("Planificar proyecto:", text_alignment="center", anchor=False)

st.divider()

st.subheader("Fecha", text_alignment="center", anchor=False)
fecha = st.date_input(
    "**Introduzca una fecha para la sección:**",
    min_value = datetime.datetime.today().date() + datetime.timedelta(days=1),
    format = "DD/MM/YYYY",
    value = None
)

if fecha:
    if len(st.session_state.eventos_programados) == 0:
        st.session_state.sesión["Fecha"] = str(fecha)
        st.success("Fecha Válida.")
        st.session_state.inventario = load_inventory()
    else:
        fecha_valida = True
        for sesion in st.session_state.eventos_programados.keys():
            if str(fecha) == sesion:
                st.error(f'La fecha: {sesion} está ocupada, por favor elija otra fecha.')
                fecha_valida = False
                st.session_state.sesión["Fecha"] = None
                st.session_state.inventario = {
                        "Local": "",
                        "Cámara": [],
                        "Fotógrafo": "",
                        "Vestuario": None,
                        "Auxiliar": [],
                        "Espacio": []
                    }
                break
        
        if fecha_valida:
            st.success("Fecha Válida.")
            st.session_state.sesión["Fecha"] = str(fecha)
            st.session_state.inventario = load_inventory()

elif st.session_state.sesión["Fecha"] == None:                    
    dia_valido = datetime.datetime.today().date() + datetime.timedelta(days=1)
    disponible = False
    if len(st.session_state.eventos_programados.keys()) != 0:
        while True:
            
            for sesion in st.session_state.eventos_programados.values():
                if sesion["Fecha"] == str(dia_valido):
                    dia_valido = dia_valido + datetime.timedelta(days=1)
                    disponible = False
                    break
                disponible = True    
            if disponible:
                disponible = False
                break   
    st.info(f"Espacio para tu sesión: {str(dia_valido)}")

st.write("\n")
st.divider()

st.subheader("Nombre y Apellido", text_alignment="center", anchor=False)

st.write("\n")

col1,col2 = st.columns(2,
                       gap="small",
                       vertical_alignment="center"
                       )
with col1:
    if st.session_state.sesión["Fecha"] != None:
        nombre = st.text_input(
            "**Introduzca el nombre de la persona:**",
            value = st.session_state.sesión["Nombre"],
            max_chars = 15,
            autocomplete=None,
            placeholder = "Nombre" 
        )
    else:
        nombre = st.text_input(
            "**Introduzca el nombre de la persona:**",
            value = None,
            max_chars = 15,
            autocomplete=None,
            placeholder = "Escoja una Fecha Válida",
            disabled=True 
        )

    if nombre:
        nombre_val, nombre_error = validate_name(nombre, "Nombre")
        if not nombre_val:
            st.error(nombre_error)
            st.session_state.sesión["Nombre"] = None
        else:
            st.success("Nombre Válido.")
            st.session_state.sesión["Nombre"] = nombre
    else:
        st.session_state.sesión["Nombre"] = None
with col2:
    if st.session_state.sesión["Fecha"] != None:
        apellido = st.text_input(
            "**Introduzca el appelido de la persona:**",
            value = st.session_state.sesión["Apellido"],
            max_chars = 15,
            autocomplete=None,
            placeholder = "Apellido" 
        )
    else:
        apellido = st.text_input(
            "**Introduzca el apellido de la persona:**",
            value = None,
            max_chars = 15,
            autocomplete=None,
            placeholder = "Escoja una Fecha Válida",
            disabled=True 
        )
    
    if apellido:
        apellido_val, apellido_error = validate_name(apellido, "Apellido")
        if not apellido_val:
            st.error(apellido_error)
            st.session_state.sesión["Apellido"] = None
        else:
            st.success("Apellido Válido.")
            st.session_state.sesión["Apellido"] = apellido
    else:
        st.session_state.sesión["Apellido"] = None

st.divider()

st.subheader("Espacio e Iluminación", text_alignment="center", anchor=False)

st.write("\n")

st.session_state.sesión["Espacio"] = st.selectbox(
    label="**Seleccione el espacio en el que se va a desarrollar la sesión:**",
    options=st.session_state.inventario["Espacio"],
    index=None
)
if st.session_state.sesión["Espacio"] == "Interior":
    st.info("Sesiones en Espacios Interiores requieren Focos para la iluminación. Se le asignaran automáticamente.")
    st.session_state.sesión["Iluminación"] = "Focos"
elif st.session_state.sesión["Espacio"] == "Exterior":
    st.info("Sesiones en Espacios Interiores no pueden usar Focos para la iluminación. Se aprovecha la iluminación Natural")
    st.session_state.sesión["Iluminación"] = "Natural"
else:
    st.warning("Seleccionar un espacio para la sesión es obligatorio.")
    st.session_state.sesión["Espacio"] = None
    st.session_state.sesión["Iluminación"] = None

st.divider()
st.subheader("Equipo principal", text_alignment="center", anchor=False)

st.write("\n")

st.session_state.sesión["Cámara"] = st.selectbox(
    label="**Seleccione un modelo de Cámara:**",
    options=st.session_state.inventario["Cámara"],
    index=None
    )
if st.session_state.sesión["Cámara"] != None:
    st.info("La cámara depende de un fotógrafo, se le asignará a Mila como fotógrafa")
    st.session_state.sesión["Fotógrafo"] = st.session_state.inventario["Fotógrafo"]
if st.session_state.sesión["Cámara"] == None:
    st.warning("Se requiere obligadamente de una Cámara para la sesión")
    st.session_state.sesión["Fotógrafo"] = None

st.session_state.sesión["Auxiliar"] = st.selectbox(   
    label="**Seleccione una especialidad Auxiliar:**",
    options=st.session_state.inventario["Auxiliar"],
    index=None
    )

if st.session_state.sesión["Auxiliar"] != None:
    
    if st.session_state.sesión["Auxiliar"] == "Maquillista":
        st.info("El maquillista destaca en combinar técnicas, creatividad y conocimiento de la piel para comunicar una idea o resaltar la belleza del modelo.")
    if st.session_state.sesión["Auxiliar"] == "Estilista":
        st.info("El estilista es una persona especializada en crear estilos que combinan técnica, moda y creatividad para proyectar la mejor versión del modelo.")
    if st.session_state.sesión["Auxiliar"] == "Escenógrafo":
        st.info("El escenógrafo para fotografía es el arquitecto del espacio visual, quien convierte una idea en un escenario tangible que da identidad y fuerza a la imagen.")
    
if st.session_state.sesión["Auxiliar"] == None:
    st.warning("Para la calidad de la sesión se requiere un especialista Auxiliar.")
    st.session_state.sesión["Auxiliar"] = None

if st.session_state.inventario["Vestuario"] != None:
    st.session_state.sesión["Vestuario"] = st.slider(
        label="**Seleccione una cantidad de vestuarios para la Sesión:**",
        min_value=0,
        max_value=st.session_state.inventario["Vestuario"]
    )
else:
    st.session_state.sesión["Vestuario"] = st.slider(
        label="**Seleccione una cantidad de vestuarios para la Sesión:**",
        min_value=0,
        max_value=st.session_state.inventario["Vestuario"],
        disabled=True
    )
st.divider()

col1, col2, col3 = st.columns(3,
                           gap="small",
                           vertical_alignment="center")
with col2:
    
    st.subheader("Finalizar", text_alignment="center", anchor=False)
    
    with st.container(
    key="botones",
    horizontal_alignment="center",
    border=True
    ):
        agregar = st.button("Confirmar evento")

if agregar:
    campos_vacios = []
    for keys, values in st.session_state.sesión.items():
        if values == None:
            campos_vacios.append(keys)
    if len(campos_vacios) > 0:
        for i in campos_vacios:
            st.warning(f"Falta por llenar el campo de: {i}.")
        sleep(2)
        st.rerun()    
    else:
        st.session_state.eventos_programados[st.session_state.sesión["Fecha"]] = st.session_state.sesión
        save_events(st.session_state.eventos_programados)
        st.success(f"Se ha registrado una nueva sesión para la fecha : {st.session_state.sesión["Fecha"]}")
        reset()
        sleep(2)
        st.rerun()