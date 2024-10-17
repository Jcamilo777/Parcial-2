from .medico import Medico
from .paciente import Paciente
from .cita import Cita
from .agenda import Agenda
from datetime import datetime

class Hospital:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.agenda = Agenda()

    def agregar_paciente(self, identificacion, nombre, celular, correo):
        paciente = Paciente(identificacion, nombre, celular, correo)
        self.pacientes.append(paciente)
        print(f"Paciente {nombre} agregado al hospital.")

    def agregar_medico(self, identificacion, nombre, celular, correo, especialidad):
        medico = Medico(identificacion, nombre, celular, correo, especialidad)
        self.medicos.append(medico)
        print(f"Médico {nombre} agregado al hospital.")

    def buscar_paciente(self, identificacion):
        for paciente in self.pacientes:
            if paciente.identificacion == identificacion:
                return paciente
        return None

    def buscar_medico(self, identificacion):
        for medico in self.medicos:
            if medico.identificacion == identificacion:
                return medico
        return None

    def obtener_medicos_por_especialidad(self, especialidad):
        return [medico for medico in self.medicos if medico.especialidad.lower() == especialidad.lower()]

    def agendar_cita(self, paciente, medico, fecha_hora_str, motivo):
        fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
        if medico.verificar_disponibilidad(fecha_hora):
            nueva_cita = Cita(paciente, medico, fecha_hora, motivo)
            medico.agenda.agregar_cita(nueva_cita)
            self.agenda.agregar_cita(nueva_cita)
            print(f"Cita agendada para el paciente {paciente.nombre} con el Dr. {medico.nombre} el {fecha_hora}")
            # Enviar notificaciones
            paciente.recibir_notificacion(f"Tiene una cita agendada el {fecha_hora} con el Dr. {medico.nombre}")
        else:
            print(f"No hay disponibilidad con el Dr. {medico.nombre} en la fecha y hora {fecha_hora}")

    def cancelar_cita(self, cita):
        cita.cancelar_cita("Cancelada por el paciente")
        cita.medico.agenda.cancelar_cita(cita)
        self.agenda.cancelar_cita(cita)
        print(f"Cita cancelada: {cita}")

    def obtener_citas_paciente(self, paciente):
        return [cita for cita in self.agenda.citas_pendientes if cita.paciente == paciente]