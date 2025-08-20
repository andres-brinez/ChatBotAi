# Chatbot con IA usando Flask y Gemini 🤖

Este es un proyecto de chatbot web simple, pero funcional, que demuestra la integración de una interfaz de usuario básica con una API de inteligencia artificial. El backend está desarrollado con Flask (Python) y el frontend con HTML, CSS y JavaScript. La comunicación con la IA se realiza a través de la API de Google Gemini.

## Características Principales

- **Interfaz de Usuario**: Interfaz de chat intuitiva y moderna.
- **Conectividad**: Backend en Flask para manejar las peticiones HTTP.
- **Inteligencia Artificial**: Utiliza la API de Google Gemini para generar respuestas conversacionales.
- **Seguridad**: La clave de la API se gestiona de forma segura a través de un archivo `.env`.

## Requisitos Previos 🛠️
Para ejecutar este proyecto, necesitas tener instalado lo siguiente:
- **Python 3.8 o superior**: Puedes descargarlo desde el [sitio oficial de Python](https://www.python.org/downloads/).
- **Clave de la API de Google Gemini**: Obtén una clave de API gratuita en el [sitio de Google AI Studio](https://ai.google/studio/).

## Estructura del Proyecto 📂
La estructura de carpetas y archivos es simple y organizada para facilitar la navegación:

```
/chatbot_flask
├── /static
│   ├── style.css
│   └── script.js
├── /templates
│   └── index.html
├── .env
└── app.py
```


## Configuración y Ejecución del Proyecto 🚀
Sigue estos pasos para poner en marcha el proyecto:
1. **Configurar el entorno virtual**  
   Abre una terminal en la carpeta principal del proyecto y crea un entorno virtual para aislar las dependencias.

```
bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

3. **Instalar las dependencias**  
   Con el entorno virtual activado, instala todas las librerías necesarias.
```
bash
   pip install Flask python-dotenv google-generativeai
```

4. **Configurar la clave de la API**  
   En la carpeta raíz del proyecto, crea un archivo llamado `.env` y añade tu clave de API de Gemini, sustituyendo `tu_clave_de_api_aqui`.

```
env
   GOOGLE_API_KEY=tu_clave_de_api_aqui
```


**Importante**: No subas el archivo `.env` a repositorios públicos como GitHub para proteger tu clave.
4. **Ejecutar la aplicación**  
   Ahora, simplemente ejecuta el archivo principal de la aplicación.
```
bash
   python app.py
```

La aplicación se ejecutará en un servidor local. Abre tu navegador y ve a [http://127.0.0.1:5000](http://127.0.0.1:5000) para ver el chatbot en acción.
## Tecnologías Utilizadas 💻
- **Python**: Lenguaje de programación del backend.
- **Flask**: Microframework web para el servidor.
- **HTML5, CSS3, JavaScript**: Tecnologías de desarrollo web para el frontend.
- **Google Gemini API**: Servicio de inteligencia artificial para las respuestas del chatbot.
- **python-dotenv**: Librería para gestionar variables de entorno.

- 
## Imagenes 

<img width="846" height="405" alt="image" src="https://github.com/user-attachments/assets/83e1a272-ea18-4570-9bb6-7841587c2919" />
<img width="796" height="812" alt="image" src="https://github.com/user-attachments/assets/827a4a30-7e02-4eb4-9cd0-b3316efd239d" />
<img width="588" height="799" alt="image" src="https://github.com/user-attachments/assets/5112201a-883a-41b9-8a13-5e3dc52718b8" />


