from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import re

app = Flask(__name__)
CORS(app)

# ===== LOGIN FICTICIO SIN BASE DE DATOS =====
USERS = [
    {"user": "admin", "pass": "123456", "role": "admin"},
    {"user": "auditor", "pass": "1234", "role": "auditor"},
]

@app.post("/api/login")
def login():
    data = request.get_json(force=True)
    u = data.get("user", "")
    p = data.get("pass", "")
    match = next((x for x in USERS if x["user"] == u and x["pass"] == p), None)
    if not match:
        return jsonify({"ok": False, "msg": "Credenciales inválidas"}), 401

    # Token ficticio (no real JWT, solo string simulado)
    token = f"TOKEN::{match['user']}::{match['role']}"
    return jsonify({
        "ok": True,
        "token": token,
        "user": match["user"],
        "role": match["role"]
    })


# ===== TU FRONTEND (dist) =====
@app.route('/', methods=["GET", "POST"])
def serve_index():
    return send_from_directory('dist', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('dist', path)


# ===== CLIENTE LOCAL OLLAMA =====
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # requerido por la librería, aunque no se use
)


# ===== ENDPOINT: ANALIZAR RIESGOS =====
@app.route('/analizar-riesgos', methods=['POST'])
def analizar_riesgos():
    data = request.get_json()
    activo = data.get('activo')
    if not activo:
        return jsonify({"error": "El campo 'activo' es necesario"}), 400

    riesgos, impactos = obtener_riesgos(activo)
    return jsonify({"activo": activo, "riesgos": riesgos, "impactos": impactos})


# ===== ENDPOINT: SUGERIR TRATAMIENTO =====
@app.route('/sugerir-tratamiento', methods=['POST'])
def sugerir_tratamiento():
    data = request.get_json()
    activo = data.get('activo')
    riesgo = data.get('riesgo')
    impacto = data.get('impacto')

    if not activo or not riesgo or not impacto:
        return jsonify({"error": "Los campos 'activo', 'riesgo' e 'impacto' son necesarios"}), 400

    entrada_tratamiento = f"{activo};{riesgo};{impacto}"
    tratamiento = obtener_tratamiento(entrada_tratamiento)

    return jsonify({
        "activo": activo,
        "riesgo": riesgo,
        "impacto": impacto,
        "tratamiento": tratamiento
    })


# ===== FUNCIONES AUXILIARES (IA) =====
def obtener_tratamiento(riesgo):
    response = client.chat.completions.create(
        model="ramiro:instruct",
        messages=[
            {"role": "system", "content": "Responde en español, eres una herramienta para gestión de riesgos de la ISO 27000. El usuario te dará un asset, riesgo e impacto, responde con un tratamiento en <200 caracteres."},
            {"role": "user", "content": "mi telefono movil;Acceso no autorizado;un atacante puede acceder a la información personal y confidencial almacenada en el teléfono"},
            {"role": "assistant", "content": "Habilitar bloqueo de pantalla con contraseña o huella digital."},
            {"role": "user", "content": riesgo}
        ]
    )
    return response.choices[0].message.content


def obtener_riesgos(activo):
    response = client.chat.completions.create(
        model="ramiro:instruct",
        messages=[
            {"role": "system", "content": "Responde en español. Eres una herramienta ISO 27000. El usuario te dará un activo tecnológico y debes devolver 5 riesgos con sus impactos, en formato bullets."},
            {"role": "user", "content": "mi raspberry pi"},
            {"role": "assistant", "content": """• **Acceso no autorizado**: terceros pueden acceder a la información almacenada.
• **Pérdida de datos**: errores de hardware o malware provocan pérdida de información.
• **Vulnerabilidades de software**: exploits no parchados comprometen el sistema.
• **Inseguridad de la red**: conexión expuesta permite interceptar tráfico o inyectar malware.
• **Fallos físicos**: sobrecalentamiento o cortocircuito afectan la disponibilidad."""},
            {"role": "user", "content": activo}
        ]
    )
    answer = response.choices[0].message.content

    patron = r'\*\*\s*(.+?)\*\*:\s*(.+?)(?:\.|\n|$)'
    resultados = re.findall(patron, answer)

    riesgos = [resultado[0] for resultado in resultados]
    impactos = [resultado[1] for resultado in resultados]

    return riesgos, impactos


# ===== MAIN =====
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
