import streamlit as st
st.write("---")
st.header("⭐ Algunos trabajos realizados:")
col1,col2,col3 = st.columns([1,1,1], gap = "medium", vertical_alignment = "top")
with col1:
    st.image("views/foto1.jpg")
    st.write("Maria Claudia Rodríguez.")
    st.image("views/foto2.jpg")
    st.write("Nathalie Falcon García.")
    st.image("views/foto3.jpg")
    st.write("Lauren Ortega Cruz.")
with col2:
    st.image("views/foto4.jpg")
    st.write("Kamila Hernández López.")
    st.image("views/foto5.jpg")
    st.write("Mariam Vento Ragati.")
    st.image("views/foto6.jpg")
    st.write("Melissa del Valle Calvo.")
with col3:
    st.image("views/foto7.jpg")
    st.write("Adriana Pitón de la Caridad.")
    st.image("views/foto8.jpg")
    st.write("Aliadne Díaz Sotomayor.")
    st.image("views/foto9.jpg")
    st.write("Liannette Pieg Varona.")
st.write("---")
st.subheader("⭐ ¡Planifique su sesión!")
st.page_link("page/planificar_evento.py", label = ":rainbow[*Mila's Studio Photo*] 🌸")
    