class Agenda:
    def __init__(self):
        self.citas_pendientes = []
        self.citas_realizadas = []
        self.citas_canceladas = []

    def agregar_cita(self, cita):
        self.citas_pendientes.append(cita)

    def cancelar_cita(self, cita):
        if cita in self.citas_pendientes:
            self.citas_pendientes.remove(cita)
            self.citas_canceladas.append(cita)

    def verificar_disponibilidad(self, fecha_hora):
        for cita in self.citas_pendientes:
            if cita.fecha_hora == fecha_hora:
                return False
        return True