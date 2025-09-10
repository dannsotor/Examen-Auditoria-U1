# Informe de Auditoría de Sistemas - Examen de la Unidad I

**Nombres y apellidos:** Duanet Soto Rodríguez  
**Fecha:** 10/09/2025  
**URL GitHub:** [https://github.com/dannsotor/Examen-Auditoria-U1.git](https://github.com/dannsotor/Examen-Auditoria-U1.git)

---
<img width="596" height="386" alt="image" src="https://github.com/user-attachments/assets/d65952b6-7965-43b4-92e0-c31ac98bd5ad" />
Luego npm run deb y nos dará nuestra ip: en este caso seria http://localhost:5176/

<img width="556" height="363" alt="image" src="https://github.com/user-attachments/assets/655035c5-0bf4-4c12-8088-9d19f427ce31" />

## Instrucciones Generales

Como auditor externo contratado por un banco, debe evaluar los activos de información, utilizando modelos de lenguaje avanzados ejecutados localmente.  
Este proceso incluye la generación automática de perfiles de riesgo, análisis de impactos, recomendaciones de mitigación alineadas con ISO 27001 y una interfaz intuitiva para la gestión de casos identificados.

---

## 1. Proyecto de Auditoría de Riesgos

**Ip:** `http://localhost:5176`  

### Login  
**Evidencia:**  


Primero levantamos el servidor para poder visualizar el sistema.  
<img width="685" height="522" alt="image" src="https://github.com/user-attachments/assets/646500f0-6ad0-4f3d-8491-92d94c315d68" />


<img width="691" height="279" alt="image" src="https://github.com/user-attachments/assets/bd194230-9bed-4572-b42d-81903d9e50d2" />
Luego el frontend lo levantamos en Git Bash y nos dará nuestra ip.  
<img width="588" height="312" alt="image" src="https://github.com/user-attachments/assets/da2126ee-15df-4abb-8934-7e9a8166f781" />

Seguidamente podremos observar nuestro login corregido.  
<img width="558" height="773" alt="image" src="https://github.com/user-attachments/assets/2cfc3842-d69b-4641-92b6-6b1d83950ac5" />


**Descripción:**  

El inicio de sesión ficticio se implementó mediante un endpoint en el backend (`/api/login`) desarrollado con Flask.  
En lugar de conectarse a una base de datos, se definió una lista de usuarios preconfigurados en memoria (por ejemplo, `admin/123456` o `auditor/1234`).  
<img width="569" height="143" alt="image" src="https://github.com/user-attachments/assets/b98543fb-3d57-4636-be43-61128644402c" />

Cuando el usuario ingresa sus credenciales desde el formulario del frontend, estas se envían al endpoint en formato JSON, se validan contra esa lista y, si coinciden, el sistema devuelve un objeto de respuesta con estado **ok**, el rol asignado y un token simulado.  
Este enfoque permite demostrar la autenticación y el control de acceso sin necesidad de configurar una base de datos real.


---

## Motor de Inteligencia Artificial

**Evidencia:**  
<img width="652" height="220" alt="image" src="https://github.com/user-attachments/assets/3c08e9f5-2780-457a-8c56-95219ab7a309" />


Aquí se agregó la lógica para tomar un activo desde el frontend, enviarlo al modelo de IA y devolver riesgos + impactos de forma estructurada (listas separadas).  
<img width="704" height="393" alt="image" src="https://github.com/user-attachments/assets/d940881f-12f6-4546-90b1-d65a31943c40" />

- Uso de un prompt especializado (rol system) para guiar al modelo a responder con riesgos alineados a ISO 27000.  
- Uso de expresiones regulares (`re.findall`) para separar automáticamente los riesgos y los impactos en listas distintas.  
- Esto convierte la salida libre del modelo en datos estructurados, listos para mostrarse en la tabla del frontend.

---

## 2. Hallazgos

Estos serían mis **5 hallazgos**:
<img width="686" height="587" alt="image" src="https://github.com/user-attachments/assets/21f59589-2ede-4eb7-b98e-bed23bc57479" />

### Activo 1: Servidor de Correo
**Evidencia:**  

<img width="683" height="139" alt="image" src="https://github.com/user-attachments/assets/9a0ccef9-6558-4c31-a63e-6c8af8c8f5d3" />

- **Condición:** El servidor de correo presenta riesgo de pérdida de información por falta de medidas de protección avanzadas.  
- **Recomendación:** Implementación de firewall de nueva generación y configuración de reglas específicas para correo electrónico.  
- **Riesgo:** Probabilidad alta de ataque y alto impacto por exposición de datos sensibles.  

---

### Activo 2: VPN Corporativa
<img width="677" height="93" alt="image" src="https://github.com/user-attachments/assets/23a035a3-d67b-4285-bb20-a8a231e76875" />

- **Condición:** La VPN corporativa carece de mecanismos formales de concienciación del personal en seguridad.  
- **Recomendación:** Capacitación periódica del personal sobre seguridad en conexiones remotas y uso correcto de credenciales.  
- **Riesgo:** Media (la probabilidad depende del factor humano, con impacto considerable en caso de compromiso).  

---

### Activo 3: ERP Financiero
<img width="682" height="81" alt="image" src="https://github.com/user-attachments/assets/0c7fcc70-7aa4-4244-a154-6d7105120ccb" />


- **Condición:** El ERP financiero no cuenta con mecanismos de defensa suficientes contra accesos indebidos y fugas de datos críticos.  
- **Recomendación:** Implementación de firewall de nueva generación junto con monitoreo de accesos y segregación de funciones.  
- **Riesgo:** Alta (probabilidad alta de explotación y consecuencias críticas en la gestión financiera).  

---

### Activo 4: Entorno de Desarrollo
<img width="689" height="92" alt="image" src="https://github.com/user-attachments/assets/80c94c25-0a45-4d79-b874-e38a683b8565" />


- **Condición:** El entorno de desarrollo carece de medidas de respaldo adecuadas, lo que expone a pérdida de código fuente o configuraciones clave.  
- **Recomendación:** Establecer copias de seguridad periódicas y aislar el entorno de la red corporativa para evitar fugas.  
- **Riesgo:** Media (probabilidad media, con impacto moderado en continuidad de proyectos).  

---

### Activo 5: App Móvil para Clientes
![Uploading image.png…]()


- **Condición:** La aplicación móvil no tiene mecanismos robustos de respaldo, exponiendo información de clientes ante incidentes de pérdida o fallo de seguridad.  
- **Recomendación:** Establecer copias de seguridad periódicas, cifrado en reposo y en tránsito, y pruebas de penetración regulares.  
- **Riesgo:** Alta (probabilidad y consecuencias altas por afectar directamente a clientes y reputación institucional).  

---

## Conclusiones

- **Fortalecimiento de la seguridad perimetral y de acceso:** La evaluación evidenció que activos críticos como el Servidor de Correo y el ERP Financiero requieren medidas avanzadas de protección (firewalls de nueva generación, monitoreo de accesos) para garantizar la confidencialidad e integridad de la información sensible del banco.  

- **Importancia del factor humano y la continuidad operativa:** El análisis resaltó que la VPN Corporativa y el Entorno de Desarrollo dependen no solo de controles técnicos, sino también de la capacitación del personal y de la implementación de copias de seguridad periódicas.  

- **Protección de datos de clientes como prioridad estratégica:** La App Móvil para Clientes representa un activo de alto riesgo por su exposición directa al usuario final; por ello, la aplicación de medidas como cifrado, respaldos y pruebas de seguridad periódicas resulta fundamental para mantener la confianza de los clientes y cumplir con estándares como ISO/IEC 27001.  

---
