# Sistema de Vigilancia de Logs (Linux Daemon)

Este proyecto implementa un servicio de monitoreo en segundo plano (daemon) para sistemas Linux, desarrollado en Python y gestionado mediante Systemd.

##  Características
* *Persistencia:* Se ejecuta automáticamente al inicio del sistema usando systemd.
* *Logging:* Escritura de registros en ruta protegida /var/log/ mediante gestión de permisos.
* *Resiliencia:* Reinicio automático ante fallos (Crash recovery).

## Tecnologías
* *Python 3:* Lógica del script.
* *Bash/Linux:* Gestión de permisos y usuarios.
* *Systemd:* Creación del servicio (.service).

##  Instalación
1. Clonar el repositorio.
2. Copiar el archivo de servicio: sudo cp vigilante.service /etc/systemd/system/
3. Habilitar el servicio: sudo systemctl enable vigilante
4. Iniciar: sudo systemctl start vigilante
