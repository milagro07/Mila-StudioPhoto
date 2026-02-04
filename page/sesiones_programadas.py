import streamlit as st
import pandas as pd
from time import sleep
from core import load_projects, save_events

if "eventos_programados" not in st.session_state:
    st.session_state.eventos_programados = load_projects()

st.header("⭐ Listado de Sesiónes Planificadas", text_alignment="center", anchor=False)
st.divider()
if len(st.session_state.eventos_programados) != 0:
    sesiones_tabla = pd.DataFrame.from_dict(
        data=st.session_state.eventos_programados,
        orient="index"
    )
    st.dataframe(
        data=sesiones_tabla,
        width="stretch",
        height="auto",
        hide_index=True,
        column_order=["Fecha", "Nombre", "Apellido", "Espacio", "Iluminación", "Fotógrafo", "Cámara", "Auxiliar", "Vestuario"]
    )
    st.divider()
    st.subheader("⭐ Eliminar sesión planificada:", text_alignment="center", anchor=False)
    borrar = st.selectbox("Selecciones un evento para cancelar:",
                options=[f"{fecha} / {val["Nombre"]}" for fecha, val in load_projects().items()],
                index = None,
                placeholder = "Sesión a cancelar."
                )
    boton = st.button("Borrar")
    if boton:    
        if borrar:
            sesion = borrar.split()
            st.session_state.eventos_programados.pop(sesion[0])
            st.success(f"Ha eliminado la sesión del día {sesion[0]}")
            save_events(st.session_state.get("eventos_programados"))
            sleep(1.5)
            st.rerun()
        else:
            st.warning("No ha seleccionado ninguna sesión.") 
            sleep(1.5)
            st.rerun()
else:
    st.warning("En estos momentos no tenemos ninguna sesión programada. Si estás interesado o interesada en planificar una, no dudes en organizar una en el link de abajo. ¡Esperamos tu evento!")
    st.page_link("page/planificar_evento.py", label = ":rainbow[*Mila's Studio Photo*] 🌸")