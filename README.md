# Sistema de Gestión de Citas Médicas

Este proyecto es un sistema de gestión de citas médicas que permite a los pacientes agendar, cancelar y gestionar sus citas con médicos. El sistema también permite a los médicos manejar su agenda y optimiza la disponibilidad para mejorar la atención al paciente.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Usadas](#tecnologías-usadas)
- [Requerimientos](#requerimientos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- Verificación de disponibilidad de médicos según la especialidad.
- Asignación de médico de preferencia para los pacientes.
- Visualización de citas disponibles con fecha y hora.
- Notificación a los pacientes dos días antes de la cita.
- Manejo de la agenda de los médicos.
- Opción para que los pacientes cancelen citas.
- Reorganización de citas en caso de cancelaciones.
- Almacenamiento seguro de datos de pacientes y médicos.
- Solicitud de citas por parte de los usuarios.
- Confirmaciones de citas vía correo electrónico o mensajes de texto.
- Generación de reportes sobre médicos y especialidades.
- Cálculo de porcentajes de ausentismo.
- Exportación de reportes a Excel.

## Tecnologías Usadas

- Python
- Rich (para la interfaz de línea de comandos)
- Excel (para la exportación de reportes)

## Requerimientos

- Python 3.x
- Biblioteca Rich: Se puede instalar utilizando pip.

```bash
pip install rich
