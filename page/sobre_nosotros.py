import streamlit as st 

st.markdown("**Mila's Studio Photo** es un espacio creativo especializado en capturar momentos únicos con un estilo moderno y elegante. El estudio ofrece sesiones fotográficas profesionales para retratos, eventos y proyectos artísticos, combinando técnica, sensibilidad y atención al detalle. Su ambiente acogedor y su equipo apasionado buscan que cada cliente viva una experiencia personalizada, logrando imágenes que transmiten emociones auténticas y recuerdos inolvidables. Pulse aquí para más información: [📷](https://www.instagram.com/fotos.monii?igsh=Y3N6Nnp1ZjZlaXN1&utm_source=qr)", text_alignment="justify")
st.image("views/estudio.jpg")
st.subheader('⭐ ¿Por qué nosotros?')
st.markdown('''
1. :yellow-badge[Atención personalizada y profesional.]  
Desde el primer contacto, el equipo demuestra un trato cálido y atento, asegurándose de entender las necesidades específicas de cada cliente.

2. :yellow-badge[Equipamiento de alta gama.]  
El estudio cuenta con cámaras profesionales, iluminación avanzada y fondos variados que garantizan resultados de calidad superior.

3. :yellow-badge[Ambiente cómodo y acogedor.]  
El espacio está diseñado para que los clientes se sientan relajados y seguros, lo que se refleja en fotografías naturales y auténticas.

4. :yellow-badge[Creatividad y estilo único.] 
Cada sesión fotográfica se adapta al estilo del cliente, con propuestas creativas que hacen que cada imagen tenga personalidad propia.

5. :yellow-badge[Entrega puntual y edición impecable.]  
Los tiempos de entrega son rápidos y las fotos editadas mantienen un balance perfecto entre naturalidad y retoque profesional.               
''',
text_alignment="justify")
st.subheader("⭐ ¡Planifique su sesión!")
st.page_link("page/planificar_evento.py", label = ":rainbow[*Mila's Studio Photo*] 🌸")

