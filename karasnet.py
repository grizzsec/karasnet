import tkinter as tk
import subprocess

def reconnaissance():
    # Etapa de reconocimiento
    target = entry_target.get()
    print(f"Realizando reconocimiento sobre {target}...")
    # Código para recopilar información sobre el objetivo

def weaponization():
    # Etapa de creación de armas
    weapon_type = weapon_var.get()
    
    if weapon_type == "exploit":
        exploit_name = entry_exploit_name.get()
        exploit_target = entry_exploit_target.get()
        if exploit_name and exploit_target:
            print(f"Creando exploit {exploit_name}...")
            # Código para desarrollar y construir el exploit
            
            print(f"Configurando el exploit para el objetivo {exploit_target}...")
            # Código para configurar el exploit para el objetivo específico
        else:
            print("Debe proporcionar un nombre de exploit y un objetivo del exploit.")
    
    elif weapon_type == "malware":
        malware_name = entry_malware_name.get()
        malware_functionality = entry_malware_functionality.get()
        if malware_name and malware_functionality:
            print(f"Creando malware {malware_name}...")
            # Código para desarrollar y construir el malware
            
            print(f"Configurando el malware con la funcionalidad {malware_functionality}...")
            # Código para configurar el malware con la funcionalidad deseada
        else:
            print("Debe proporcionar un nombre de malware y una funcionalidad del malware.")

def delivery():
    # Etapa de entrega
    delivery_method = delivery_var.get()
    
    if delivery_method == "phishing":
        phishing_payload = entry_phishing_payload.get()
        phishing_url = entry_phishing_url.get()
        if phishing_payload and phishing_url:
            print(f"Enviando correo de phishing con el payload {phishing_payload}...")
            # Código para enviar correo de phishing con el payload
            
            print(f"Configurando la URL de destino del phishing: {phishing_url}...")
            # Código para configurar la URL de destino del phishing
        else:
            print("Debe proporcionar un payload de phishing y una URL de destino.")
        
    elif delivery_method == "entrega directa":
        delivery_payload = entry_delivery_payload.get()
        delivery_location = entry_delivery_location.get()
        if delivery_payload and delivery_location:
            print(f"Realizando entrega directa del payload {delivery_payload}...")
            # Código para realizar la entrega directa del payload
            
            print(f"Configurando la ubicación de destino para la entrega directa: {delivery_location}...")
            # Código para configurar la ubicación de destino de la entrega directa
        else:
            print("Debe proporcionar un payload de entrega directa y una ubicación de destino.")

def exploitation():
    # Etapa de explotación
    vulnerability = entry_vulnerability.get()
    if vulnerability:
        print(f"Explotando la vulnerabilidad {vulnerability}...")
        # Código para aprovechar la vulnerabilidad
    else:
        print("Debe proporcionar una vulnerabilidad a explotar.")

def installation():
    # Etapa de instalación
    print("Instalando acceso persistente en el objetivo...")
    # Código para instalar el acceso persistente

def command_and_control():
    # Etapa de comando y control
    print("Estableciendo comando y control...")
    # Código para establecer la conexión y controlar el objetivo

def actions_on_objective():
    # Etapa de acciones en el objetivo
    action_type = action_var.get()
    
    if action_type == "recopilación de información":
        print("Realizando recopilación de información...")
        # Código para realizar la recopilación de información
        
    elif action_type == "robo de credenciales":
        print("Realizando robo de credenciales...")
        # Código para realizar el robo de credenciales
        
    elif action_type == "borrado de archivos":
        print("Realizando borrado de archivos...")
        # Código para realizar el borrado de archivos

def rate_incident():
    # Calificar incidente
    incident_rating = entry_rating.get()
    if incident_rating.isdigit():
        incident_rating = int(incident_rating)
        if 1 <= incident_rating <= 5:
            print(f"El incidente ha sido calificado con una criticidad de {incident_rating}/5.")
            # Código para registrar la calificación del incidente
        else:
            print("La calificación del incidente debe estar en el rango del 1 al 5.")
    else:
        print("La calificación del incidente debe ser un número entero.")

# Crear la ventana principal
window = tk.Tk()
window.title("Karasnet by Christian de López")

# Etapa de reconocimiento
frame_recon = tk.LabelFrame(window, text="Reconocimiento")
frame_recon.pack(padx=10, pady=10)

label_target = tk.Label(frame_recon, text="Objetivo:")
label_target.pack()
entry_target = tk.Entry(frame_recon)
entry_target.pack()

button_recon = tk.Button(frame_recon, text="Realizar reconocimiento", command=reconnaissance)
button_recon.pack()

# Etapa de creación de armas
frame_weapon = tk.LabelFrame(window, text="Creación de Armas")
frame_weapon.pack(padx=10, pady=10)

weapon_var = tk.StringVar()
weapon_var.set("exploit")

radio_exploit = tk.Radiobutton(frame_weapon, text="Exploit", variable=weapon_var, value="exploit")
radio_exploit.pack()
label_exploit_name = tk.Label(frame_weapon, text="Nombre del exploit:")
label_exploit_name.pack()
entry_exploit_name = tk.Entry(frame_weapon)
entry_exploit_name.pack()
label_exploit_target = tk.Label(frame_weapon, text="Objetivo del exploit:")
label_exploit_target.pack()
entry_exploit_target = tk.Entry(frame_weapon)
entry_exploit_target.pack()

radio_malware = tk.Radiobutton(frame_weapon, text="Malware", variable=weapon_var, value="malware")
radio_malware.pack()
label_malware_name = tk.Label(frame_weapon, text="Nombre del malware:")
label_malware_name.pack()
entry_malware_name = tk.Entry(frame_weapon)
entry_malware_name.pack()
label_malware_functionality = tk.Label(frame_weapon, text="Funcionalidad del malware:")
label_malware_functionality.pack()
entry_malware_functionality = tk.Entry(frame_weapon)
entry_malware_functionality.pack()

button_weapon = tk.Button(frame_weapon, text="Crear armas", command=weaponization)
button_weapon.pack()

# Etapa de entrega
frame_delivery = tk.LabelFrame(window, text="Entrega")
frame_delivery.pack(padx=10, pady=10)

delivery_var = tk.StringVar()
delivery_var.set("phishing")

radio_phishing = tk.Radiobutton(frame_delivery, text="Phishing", variable=delivery_var, value="phishing")
radio_phishing.pack()
label_phishing_payload = tk.Label(frame_delivery, text="Payload de phishing:")
label_phishing_payload.pack()
entry_phishing_payload = tk.Entry(frame_delivery)
entry_phishing_payload.pack()
label_phishing_url = tk.Label(frame_delivery, text="URL de destino:")
label_phishing_url.pack()
entry_phishing_url = tk.Entry(frame_delivery)
entry_phishing_url.pack()

radio_delivery = tk.Radiobutton(frame_delivery, text="Entrega directa", variable=delivery_var, value="entrega directa")
radio_delivery.pack()
label_delivery_payload = tk.Label(frame_delivery, text="Payload de entrega directa:")
label_delivery_payload.pack()
entry_delivery_payload = tk.Entry(frame_delivery)
entry_delivery_payload.pack()
label_delivery_location = tk.Label(frame_delivery, text="Ubicación de destino:")
label_delivery_location.pack()
entry_delivery_location = tk.Entry(frame_delivery)
entry_delivery_location.pack()

button_delivery = tk.Button(frame_delivery, text="Realizar entrega", command=delivery)
button_delivery.pack()

# Etapa de explotación
frame_exploit = tk.LabelFrame(window, text="Explotación")
frame_exploit.pack(padx=10, pady=10)

label_vulnerability = tk.Label(frame_exploit, text="Vulnerabilidad a explotar:")
label_vulnerability.pack()
entry_vulnerability = tk.Entry(frame_exploit)
entry_vulnerability.pack()

button_exploit = tk.Button(frame_exploit, text="Explotar vulnerabilidad", command=exploitation)
button_exploit.pack()

# Etapa de instalación
frame_installation = tk.LabelFrame(window, text="Instalación")
frame_installation.pack(padx=10, pady=10)

button_installation = tk.Button(frame_installation, text="Instalar acceso persistente", command=installation)
button_installation.pack()

# Etapa de comando y control
frame_c2 = tk.LabelFrame(window, text="Comando y Control")
frame_c2.pack(padx=10, pady=10)

button_c2 = tk.Button(frame_c2, text="Establecer comando y control", command=command_and_control)
button_c2.pack()

# Etapa de acciones en el objetivo
frame_actions = tk.LabelFrame(window, text="Acciones en el Objetivo")
frame_actions.pack(padx=10, pady=10)

action_var = tk.StringVar()
action_var.set("recopilación de información")

radio_info_collection = tk.Radiobutton(frame_actions, text="Recopilación de Información", variable=action_var, value="recopilación de información")
radio_info_collection.pack()

radio_credentials_theft = tk.Radiobutton(frame_actions, text="Robo de Credenciales", variable=action_var, value="robo de credenciales")
radio_credentials_theft.pack()

radio_file_deletion = tk.Radiobutton(frame_actions, text="Borrado de Archivos", variable=action_var, value="borrado de archivos")
radio_file_deletion.pack()

button_actions = tk.Button(frame_actions, text="Realizar acciones en el objetivo", command=actions_on_objective)
button_actions.pack()

# Etapa de calificación de incidente
frame_rating = tk.LabelFrame(window, text="Calificación de Incidente")
frame_rating.pack(padx=10, pady=10)

label_rating = tk.Label(frame_rating, text="Calificación del incidente (1-5):")
label_rating.pack()
entry_rating = tk.Entry(frame_rating)
entry_rating.pack()

button_rating = tk.Button(frame_rating, text="Calificar Incidente", command=rate_incident)
button_rating.pack()

# Mensaje de derechos reservados
frame_footer = tk.Frame(window)
frame_footer.pack(pady=20)

label_footer = tk.Label(frame_footer, text="Todos los derechos reservados bajo la marca Karasnet")
label_footer.pack()

window.mainloop()
