# karasnet
Karasnet es una herramienta de un ciclo de ataque cibernético. (Versión en Desarrollo-Pruebas)

# ¿Qué hace? 

Esta herramienta es una representación simplificada de un ciclo de ataque cibernético. Está dividida en diferentes etapas que componen un ataque típico:

1. Reconocimiento: En esta etapa, se recopila información sobre el objetivo del ataque. Se ingresa el objetivo en la interfaz gráfica y se realiza una función llamada "reconnaissance()" que imprimirá un mensaje indicando que se está realizando el reconocimiento.

2. Creación de Armas: En esta etapa, se crean las "armas" que se utilizarán en el ataque. Puedes elegir entre un "exploit" o un "malware" en la interfaz gráfica. Dependiendo de la elección, se ingresarán detalles como el nombre del exploit o malware, y se ejecutará la función "weaponization()" que imprimirá mensajes indicando la creación y configuración de las armas.

3. Entrega: En esta etapa, se selecciona el método de entrega del ataque. Puedes elegir entre "phishing" (correo electrónico de phishing) o "entrega directa" en la interfaz gráfica. Se ingresan detalles como el payload de phishing o la ubicación de entrega directa, y se ejecuta la función "delivery()" que imprimirá mensajes indicando el envío o la entrega directa.

4. Explotación: En esta etapa, se aprovecha una vulnerabilidad en el objetivo del ataque. Se ingresa la vulnerabilidad en la interfaz gráfica y se ejecuta la función "exploitation()" que imprimirá un mensaje indicando que se está explotando la vulnerabilidad.

5. Instalación: En esta etapa, se instala un acceso persistente en el objetivo. Se ejecuta la función "installation()" que imprimirá un mensaje indicando que se está instalando el acceso persistente.

6. Comando y Control: En esta etapa, se establece una conexión para controlar el objetivo. Se ejecuta la función "command_and_control()" que imprimirá un mensaje indicando que se está estableciendo el comando y control.

7. Acciones en el Objetivo: En esta etapa, se realizan acciones específicas en el objetivo del ataque. Puedes elegir entre "recopilación de información", "robo de credenciales" o "borrado de archivos" en la interfaz gráfica. Dependiendo de la elección, se ejecutará la función correspondiente ("actions_on_objective()") que imprimirá mensajes indicando la acción realizada.

8. Calificación de Incidente: En esta etapa, se califica el incidente en términos de su criticidad. Se ingresa la calificación en la interfaz gráfica y se ejecuta la función "rate_incident()" que imprimirá mensajes indicando la calificación del incidente.

# ¿Cómo se ejecuta?

git clone del repositorio
chmod +x al archivo .py
ejecutar el archivo .py

Recuerda que para ejecutar esta herramienta, debes tener Python instalado en tu sistema y también la biblioteca `tkinter`. Puedes interactuar con la herramienta ingresando los datos correspondientes en cada etapa y haciendo clic en los botones para ejecutar las funciones asociadas a cada etapa. Los mensajes impresos en la consola indicarán las acciones que se están llevando a cabo en cada etapa del ciclo de ataque.
