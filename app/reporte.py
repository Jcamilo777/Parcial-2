import csv
import json
from paciente import Paciente
from medico import Medico
from cita import Cita
from datetime import datetime

def cargar_pacientes(archivo_csv, hospital):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hospital.agregar_paciente(
                row['identificación'],
                row['nombre_completo'],
                row['celular'],
                row['correo']
            )

def cargar_medicos(archivo_json, hospital):
    with open(archivo_json, encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        for item in data:
            hospital.agregar_medico(
                item['id'],
                item['nombre'],
                item['correo'],
                item['correo'],
                item['especialidad']
            )

def cargar_citas(archivo_csv, hospital):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            paciente = hospital.buscar_paciente(row['paciente'])
            medico = hospital.buscar_medico(row['medicos'])
            if paciente and medico:
                fecha_hora = datetime.strptime(row['fecha_hora'], '%Y-%m-%d %H:%M:%S')
                hospital.agendar_cita(paciente, medico, fecha_hora.strftime('%Y-%m-%d %H:%M'), "Cita cargada")
