import streamlit as st

st.title(body=":rainbow[*Mila's Studio Photo*] 🌸", text_alignment = "center", anchor=False)
sobre_nosotros_page = st.Page(
    page = "page/sobre_nosotros.py",
    title = "Sobre nosotros",
    icon = ":material/info:",
    default = True
)
otros_trabajos = st.Page(
    page = "page/otros_trabajos.py",
    title = "Otros trabajos",
    icon = ":material/person:"
)
planificar_eventos = st.Page(
    page = "page/planificar_evento.py",
    title = "Planificar sesión",
    icon = ":material/star:"
)
sesiones_programadas = st.Page(
    page = "page/sesiones_programadas.py",
    title = "Sesiones programadas",
    icon = ":material/home:"
)
pg = st.navigation(
    {
    "Info":[sobre_nosotros_page],
    "Eventos":[planificar_eventos, sesiones_programadas, otros_trabajos ]
    }
)
pg.run()

