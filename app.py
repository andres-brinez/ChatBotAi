import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# Carga las variables de entorno del archivo .env
load_dotenv()

# Configura un logging básico
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configura la API de Google Gemini
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    logging.critical("La variable de entorno GOOGLE_API_KEY no está configurada.")
    raise ValueError("No se encontró GOOGLE_API_KEY en las variables de entorno.")

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    logging.critical(f"Fallo al configurar la IA Generativa: {e}")
    raise

app = Flask(__name__)

# Ruta para servir la página HTML principal
@app.route('/')
def home():
    print("Home")
    return render_template('index.html')

# Ruta para manejar las peticiones del chatbot
@app.route('/api/chat', methods=['POST'])
def chat():
    print("Chat")
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Falta el campo "message" en el cuerpo de la petición'}), 400

        user_message = data['message']
        if not isinstance(user_message, str) or not user_message.strip():
            return jsonify({'error': 'El mensaje debe ser una cadena de texto no vacía'}), 400
        
        # Envía el mensaje a la API de Gemini
        response = model.generate_content(user_message)
        
        # Obtiene el texto de la respuesta
        gemini_response = response.text

        return jsonify({'response': gemini_response})
    except Exception as e:
        logging.error(f"Ocurrió un error en el endpoint de chat: {e}", exc_info=True)
        return jsonify({'response': 'Lo siento, ha ocurrido un error. Intenta de nuevo más tarde.'}), 500

if __name__ == '__main__':
    # Para entornos de producción, se recomienda usar un servidor WSGI
    # como Gunicorn o Waitress en lugar del servidor de desarrollo.
    app.run(debug=True)