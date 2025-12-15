# 🛡️ Sistema de Vigilancia de Logs (Dockerized)

![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![Nginx](https://img.shields.io/badge/Nginx-Reverse_Proxy-green?logo=nginx)
![Python](https://img.shields.io/badge/Python-Scripting-yellow?logo=python)
![CI](https://img.shields.io/badge/GitHub_Actions-CI-black?logo=github)

Este proyecto implementa una infraestructura completa de monitoreo de logs. Evolucionó de un simple script en Python a una *arquitectura de microservicios orquestada con Docker Compose*.

El sistema genera registros simulados, los almacena de forma persistente y los sirve a través de un dashboard web con actualización automática.

## 🏗️ Arquitectura del Sistema

El proyecto consta de dos servicios contenerizados que se comunican mediante Volúmenes Compartidos:

1.  *Servicio Vigilante (Backend):* Contenedor Python que genera y escribe logs simulando actividad del sistema. Sincronizado con la zona horaria del host.
2.  *Servicio Webserver (Frontend/Proxy):* Contenedor Nginx configurado para leer los logs y servirlos vía HTTP con auto-refresh.

## 📋 Características Clave

* *🐳 Containerización:* Entorno totalmente aislado y reproducible usando Docker.
* *💾 Persistencia de Datos:* Uso de *Docker Volumes* para evitar pérdida de datos si los contenedores se reinician.
* *⚙️ Orquestación:* Gestión de servicios múltiples y redes mediante docker-compose.
* *👀 Observabilidad Web:* Dashboard accesible vía navegador mediante Nginx como Proxy Inverso.
* *🤖 CI/CD:* Integración con *GitHub Actions* para testing automático del build en cada push.
* *⏰ Sincronización:* Mapeo de /etc/localtime para garantizar timestamps correctos en los logs.

## 🚀 Instalación y Despliegue (Recomendado)

Requisitos: Tener instalado *Docker* y *Docker Compose*.

1.  *Clonar el repositorio:*
    bash
    git clone [https://github.com/TU_USUARIO/sistema-vigilancia-logs.git](https://github.com/TU_USUARIO/sistema-vigilancia-logs.git)
    cd sistema-vigilancia-logs
    

2.  *Levantar la infraestructura:*
    bash
    docker compose up -d
    

3.  *Ver el resultado:*
    Abre tu navegador y visita: http://localhost/logs
    (La página se actualizará automáticamente cada 3 segundos).

4.  *Detener el sistema:*
    bash
    docker compose down
    

---

## 🛠️ Instalación Legacy (Modo Nativo Systemd)

Si prefieres ejecutarlo directamente en el Host (Linux) sin Docker:

1.  Copiar el archivo de servicio: sudo cp vigilante.service /etc/systemd/system/
2.  Habilitar el servicio: sudo systemctl enable vigilante
3.  Iniciar: sudo systemctl start vigilante
4.  (Requiere configuración manual de Nginx en el Host para la vista web).

## 📂 Estructura del Proyecto

```text
.
├── docker-compose.yml    # Orquestación de servicios
├── Dockerfile            # Definición de la imagen Python
├── vigilante.py          # Lógica del script
├── nginx_conf/           # Configuración inyectada a Nginx
├── logs/                 # Volumen persistente (Ignorado por Git)
└── .github/workflows/    # Pipeline de CI (GitHub Actions)
