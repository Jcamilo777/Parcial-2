from .persona import Persona
from .agenda import Agenda

class Medico(Persona):
    def __init__(self, identificacion, nombre, celular, correo, especialidad):
        super().__init__(identificacion, nombre, celular, correo)
        self.especialidad = especialidad
        self.agenda = Agenda()

    def verificar_disponibilidad(self, fecha_hora):
        return self.agenda.verificar_disponibilidad(fecha_hora)