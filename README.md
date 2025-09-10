# Informe de Auditoría de Sistemas - Examen de la Unidad I

**Nombres y apellidos:** Duanet Soto Rodríguez  
**Fecha:** 10/09/2025  
**URL GitHub:** [https://github.com/dannsotor/Examen-Auditoria-U1.git](https://github.com/dannsotor/Examen-Auditoria-U1.git)

---

## Instrucciones Generales

Como auditor externo contratado por un banco, debe evaluar los activos de información, utilizando modelos de lenguaje avanzados ejecutados localmente.  
Este proceso incluye la generación automática de perfiles de riesgo, análisis de impactos, recomendaciones de mitigación alineadas con ISO 27001 y una interfaz intuitiva para la gestión de casos identificados.

---

## 1. Proyecto de Auditoría de Riesgos

**Ip:** `http://localhost:5176`  

### Login  
**Evidencia:**  
![Evidencia Login](img/login.png)

Primero levantamos el servidor para poder visualizar el sistema.  
Luego el frontend lo levantamos en Git Bash y nos dará nuestra ip.  

Seguidamente podremos observar nuestro login corregido.  

**Descripción:**  
El inicio de sesión ficticio se implementó mediante un endpoint en el backend (`/api/login`) desarrollado con Flask.  
En lugar de conectarse a una base de datos, se definió una lista de usuarios preconfigurados en memoria (por ejemplo, `admin/123456` o `auditor/1234`).  

Cuando el usuario ingresa sus credenciales desde el formulario del frontend, estas se envían al endpoint en formato JSON, se validan contra esa lista y, si coinciden, el sistema devuelve un objeto de respuesta con estado **ok**, el rol asignado y un token simulado.  
Este enfoque permite demostrar la autenticación y el control de acceso sin necesidad de configurar una base de datos real.

---

## Motor de Inteligencia Artificial

**Evidencia:**  
![Evidencia IA](img/ia.png)

Aquí se agregó la lógica para tomar un activo desde el frontend, enviarlo al modelo de IA y devolver riesgos + impactos de forma estructurada (listas separadas).  

- Uso de un prompt especializado (rol system) para guiar al modelo a responder con riesgos alineados a ISO 27000.  
- Uso de expresiones regulares (`re.findall`) para separar automáticamente los riesgos y los impactos en listas distintas.  
- Esto convierte la salida libre del modelo en datos estructurados, listos para mostrarse en la tabla del frontend.

---

## 2. Hallazgos

Estos serían mis **5 hallazgos**:

### Activo 1: Servidor de Correo
**Evidencia:**  
![Servidor de Correo](img/activo1.png)

- **Condición:** El servidor de correo presenta riesgo de pérdida de información por falta de medidas de protección avanzadas.  
- **Recomendación:** Implementación de firewall de nueva generación y configuración de reglas específicas para correo electrónico.  
- **Riesgo:** Probabilidad alta de ataque y alto impacto por exposición de datos sensibles.  

---

### Activo 2: VPN Corporativa
![VPN Corporativa](img/activo2.png)

- **Condición:** La VPN corporativa carece de mecanismos formales de concienciación del personal en seguridad.  
- **Recomendación:** Capacitación periódica del personal sobre seguridad en conexiones remotas y uso correcto de credenciales.  
- **Riesgo:** Media (la probabilidad depende del factor humano, con impacto considerable en caso de compromiso).  

---

### Activo 3: ERP Financiero
![ERP Financiero](img/activo3.png)

- **Condición:** El ERP financiero no cuenta con mecanismos de defensa suficientes contra accesos indebidos y fugas de datos críticos.  
- **Recomendación:** Implementación de firewall de nueva generación junto con monitoreo de accesos y segregación de funciones.  
- **Riesgo:** Alta (probabilidad alta de explotación y consecuencias críticas en la gestión financiera).  

---

### Activo 4: Entorno de Desarrollo
![Entorno de Desarrollo](img/activo4.png)

- **Condición:** El entorno de desarrollo carece de medidas de respaldo adecuadas, lo que expone a pérdida de código fuente o configuraciones clave.  
- **Recomendación:** Establecer copias de seguridad periódicas y aislar el entorno de la red corporativa para evitar fugas.  
- **Riesgo:** Media (probabilidad media, con impacto moderado en continuidad de proyectos).  

---

### Activo 5: App Móvil para Clientes
![App Móvil](img/activo5.png)

- **Condición:** La aplicación móvil no tiene mecanismos robustos de respaldo, exponiendo información de clientes ante incidentes de pérdida o fallo de seguridad.  
- **Recomendación:** Establecer copias de seguridad periódicas, cifrado en reposo y en tránsito, y pruebas de penetración regulares.  
- **Riesgo:** Alta (probabilidad y consecuencias altas por afectar directamente a clientes y reputación institucional).  

---

## Conclusiones

- **Fortalecimiento de la seguridad perimetral y de acceso:** La evaluación evidenció que activos críticos como el Servidor de Correo y el ERP Financiero requieren medidas avanzadas de protección (firewalls de nueva generación, monitoreo de accesos) para garantizar la confidencialidad e integridad de la información sensible del banco.  

- **Importancia del factor humano y la continuidad operativa:** El análisis resaltó que la VPN Corporativa y el Entorno de Desarrollo dependen no solo de controles técnicos, sino también de la capacitación del personal y de la implementación de copias de seguridad periódicas.  

- **Protección de datos de clientes como prioridad estratégica:** La App Móvil para Clientes representa un activo de alto riesgo por su exposición directa al usuario final; por ello, la aplicación de medidas como cifrado, respaldos y pruebas de seguridad periódicas resulta fundamental para mantener la confianza de los clientes y cumplir con estándares como ISO/IEC 27001.  

---
