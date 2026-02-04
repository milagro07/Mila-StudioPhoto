# 🌸 Mila's Studio Photo

## Dominio Seleccionado
**Sesiones de fotos en el estudio fotográfico Mila's Studio Photo**

## 📖 Descripción del Proyecto
:rainbow[**Mila's Studio Photo**] es un local dedicado a organizar sesiones de fotos de 15 para todo tipo de personas interesadas en este recuerdo. El proyecto presentado a continuación hace posible ese sueño de muchos de poder lucir una gama de fotos únicas y envidiables por muchos, pues gracias a Mila, fotógrafa profesional y muy famosa en el ámbito del arte de la fotografía, se obtienen las mejores vistas del ser humano; su belleza tanto interior como exterior.

## ⭐ Características Principales

Esta app te permite planificar una sesión de fotos a tu gusto:

*   **🌸 Ver Información sobre Mila's Studio Photo**: Conoce acerca de qué es Mila'Studio Photo y qué ofresemos en nuestro local.
*   **📷 Planificar Sesión de Fotos**: Organiza una sesión de fotos con las opciones de tú preferencia, eligiendo recursos de nuestro local para la realización de la misma: Espacio, Iluminación, Cámara, Fotógrafo, Auxiliar, Vestuario; así como otros datos como: Fecha, Nombre y Apellido de la persona que solucite nuestro servicio.
*   **📋 Listar Sesiones Programadas**: Revisa todos las sesiones que están programadas para las fechas siguientes y motívate a planificar tu propia sesión.
*   **🗑️ Borrar Sesiones Planificadas**: En caso de que no quieras mantener tu sesión planificada, siempre puedes cancelarla y planificarla para otro día si es de tu agrado.
*   **👤 Ver Otras Sesiones ya Realizadas**: Indaga entre algunos de nuestros mejores trabajos.

## ⚖️ Reglas del Proyecto (Restricciones del Proyecto)

### Restricción de Co-requisito
*   **Regla**: **Espacio interior requiere de Focos para la Iluminación**.
*   **Explicación**: Se necesita de de Iluminación por Focos cuando la sesió se realiza en Espacios Interiores para que la calidad de la imagen sea clara y precisa.
*   **Regla**: **Cámara depende de Fotógrafo**.
*   **Explicación**: Sin la presencia de un fotógrafo, no se puede trabajar con una cámara.

### Restricción de Exclusión Mutua
*   **Regla**: **Solo se puede seleccionar un Auxiliar entre maquillista, estilista y escenógrafo**.
*   **Explicación**: La selección de un solo Auxiliar se debe a que estos son profesionales y tienen muchas ideas contradictorias entre sí. Para evitar un disgusto por parte del cliente se tomó esta decisión.
*   **Regla**: **Espacio Exterior no puede usar Focos para la iluminación**.
*   **Explicación**: Por parte del equipo y por la situación energética de los últimos tiempos, se tomó la decisión de no emplear Focos para la iluminación es Espacios Exteriores, sino que aprovechar la Luz Natural para la realización de la Sesión.

### Otras Restricciones
*   **Regla**: **Todos los campos son obligatorios, excepto vestuario**.
*   **Explicación**: Para una mejor organización y calidad de la sesión, es obligatorio llenar todos los campos, excepto el de vestuario. El cliente puede elegir trabajar con una cantidad de vestuarios de nuestro salón o simplemente llevar los suyos propios.

## 🚀 Inicia el Proyecto

Sigue estos pasos para clonar y ejecutar el proyecto:

### Prerrequisitos

Asegúrate de tener instalado en tu sistema:
*   **Python 3.7 o superior**
*   **Git**
*   **pip** (generalmente viene con Python)

### Instalación y Ejecución

1.  **Clonar el Repositorio**
    ```bash
    git clone https://github.com/milagro07/Mila-StudioPhoto.git
    cd Mila-StudioPhoto
    ```

2.  **Crear y Activar un Entorno Virtual (Recomendado)**
    Es buena práctica aislar las dependencias del proyecto.
    *   **En Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   **En macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instalar las Dependencias**
    Con el entorno virtual activado, instala las librerías necesarias:
    ```bash
    pip install streamlit pandas
    ```
    *(Opcional)* Si existe un archivo `requirements.txt`, puedes usarlo:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la Aplicación**
    ¡Lanza la aplicación web de Streamlit!
    ```bash
    streamlit run home.py
    ```
    Automáticamente se abrirá una pestaña en tu navegador predeterminado (generalmente en `http://localhost:8501`) mostrando la aplicación.

## 📁 Estructura del Proyecto

```
Mila-StudioPhoto/
├── home.py                     # Archivo principal del proyecto
├── core.py                     # Algunas funciones del proyecto
├── requirements.txt            # Lista de dependencias para instalación fácil
├── data/                       # Posible carpeta para archivos de datos (CSV, JSON)
│   ├── inventario.json         # Registro de los recursos disponibles
│   └── proyectos.json          # Registro de sesiones planificadas
├── views/                      # Imágenes del proyecto
├── page/                       # Páginas del proyecto
└── README.md                   # Este archivo
```

## 🛠️ Tecnologías Utilizadas    

*   **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web interactivas en Python de manera rápida.
*   **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulación y análisis de datos, ideal para gestionar listas de sesiones de fotos.                                               
*   **Python**: Lenguaje de programación principal.

---

### Hecho con ❤️ por :@[milagro07](https://github.com/milagro07)