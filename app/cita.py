class Cita:
    def __init__(self, paciente, medico, fecha_hora, motivo):
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.estado = "Pendiente"

    def cancelar_cita(self, motivo_cancelacion):
        self.estado = "Cancelada"
        self.motivo_cancelacion = motivo_cancelacion

    def __repr__(self):
        return f"Cita de {self.paciente.nombre} con {self.medico.nombre} el {self.fecha_hora}"