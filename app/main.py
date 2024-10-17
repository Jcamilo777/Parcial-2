from rich import print
from rich.console import Console
from rich.table import Table
from hospital import Hospital

console = Console()
hospital = Hospital()


def mostrar_menu():
    console.print("\n[bold cyan]--- Menú ---[/bold cyan]")
    console.print("1. Agregar persona")
    console.print("2. Pedir cita")
    console.print("3. Cancelar cita")
    console.print("4. Asignar médico de preferencia")
    console.print("5. Ver citas pendientes")
    console.print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tipo_persona = input("Ingrese el tipo de persona (médico o paciente): ")
        identificacion = input("Ingrese la identificación: ")
        nombre = input("Ingrese el nombre: ")
        celular = input("Ingrese el celular: ")
        correo = input("Ingrese el correo: ")

        if tipo_persona.lower() == "medico":
            especialidad = input("Ingrese la especialidad: ")
            hospital.agregar_medico(identificacion, nombre, celular, correo, especialidad)
        elif tipo_persona.lower() == "paciente":
            hospital.agregar_paciente(identificacion, nombre, celular, correo)
        else:
            console.print("[red]Tipo de persona inválido.[/red]")

    elif opcion == "2":
        id_paciente = input("Ingrese la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)
        if paciente:
            especialidad = input("Ingrese la especialidad requerida: ")
            medicos_disponibles = hospital.obtener_medicos_por_especialidad(especialidad)
            if medicos_disponibles:
                console.print("[bold]Médicos disponibles:[/bold]")
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("ID")
                table.add_column("Nombre")
                for medico in medicos_disponibles:
                    table.add_row(medico.identificacion, medico.nombre)
                console.print(table)
                id_medico = input("Seleccione el ID del médico: ")
                medico = hospital.buscar_medico(id_medico)
                fecha = input("Ingrese la fecha y hora de la cita (YYYY-MM-DD HH:MM): ")
                motivo = input("Ingrese el motivo de la cita: ")
                hospital.agendar_cita(paciente, medico, fecha, motivo)
            else:
                console.print(f"[red]No hay médicos disponibles para la especialidad {especialidad}.[/red]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    elif opcion == "3":
        id_paciente = input("Ingrese la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)
        if paciente:
            citas = hospital.obtener_citas_paciente(paciente)
            if citas:
                console.print("[bold]Citas pendientes:[/bold]")
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("No.")
                table.add_column("Fecha y Hora")
                table.add_column("Médico")
                for idx, cita in enumerate(citas):
                    table.add_row(str(idx + 1), cita.fecha_hora, cita.medico.nombre)
                opcion_cita = int(input("Seleccione la cita a cancelar: "))
                if 1 <= opcion_cita <= len(citas):
                    cita_a_cancelar = citas[opcion_cita - 1]
                    hospital.cancelar_cita(cita_a_cancelar)
                else:
                    console.print("[red]Opción inválida.[/red]")
            else:
                console.print("[yellow]No tiene citas pendientes.[/yellow]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    elif opcion == "4":
        id_paciente = input("Ingrese la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)
        if paciente:
            id_medico = input("Ingrese la identificación del médico de preferencia: ")
            medico = hospital.buscar_medico(id_medico)
            if medico:
                paciente.asignar_medico_preferencia(medico)
            else:
                console.print("[red]Médico no encontrado.[/red]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    elif opcion == "5":
        id_paciente = input("Ingrese la identificación del paciente: ")
        paciente = hospital.buscar_paciente(id_paciente)
        if paciente:
            citas = hospital.obtener_citas_paciente(paciente)
            if citas:
                console.print("[bold]Citas pendientes:[/bold]")
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("Fecha y Hora")
                table.add_column("Médico")
                for cita in citas:
                    table.add_row(cita.fecha_hora, cita.medico.nombre)
                console.print(table)
            else:
                console.print("[yellow]No tiene citas pendientes.[/yellow]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    elif opcion == "6":
        console.print("[green]Saliendo del programa...[/green]")
        break

    else:
        console.print("[red]Opción inválida.[/red]")

