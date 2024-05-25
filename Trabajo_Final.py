import mysql.connector

mydb = mysql.connector.connect(
    user='root',
    host='localhost',
    database='beta_final', 
    auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

# CRUD para Clientes
def crearCliente(id, nombre, apellido, contacto):
    query = "INSERT INTO Clientes (ID, Nombre, Apellido, Contacto) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, nombre, apellido, contacto))
    mydb.commit()
    print("Cliente creado exitosamente.")

def consultarCliente(id):
    query = "SELECT * FROM Clientes WHERE ID = %s"
    cursor.execute(query, (id,))
    cliente = cursor.fetchone()
    if cliente:
        print("Cliente encontrado:")
        print(cliente)
    else:
        print("Cliente no encontrado.")

def modificarCliente(id, nombre, apellido, contacto):
    query = "UPDATE Clientes SET Nombre = %s, Apellido = %s, Contacto = %s WHERE ID = %s"
    cursor.execute(query, (nombre, apellido, contacto, id))
    mydb.commit()
    print("Cliente modificado exitosamente.")

def eliminarCliente(id):
    query = "DELETE FROM Clientes WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Cliente eliminado exitosamente.")

# CRUD para VehiculosCarga
def crearVehiculoCarga(id, marca, capacidad_carga, disponible):
    query = "INSERT INTO VehiculosCarga (ID, Marca, CapacidadCarga, Disponible) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, marca, capacidad_carga, disponible))
    mydb.commit()
    print("Vehículo creado exitosamente.")

def consultarVehiculoCarga(id):
    query = "SELECT * FROM VehiculosCarga WHERE ID = %s"
    cursor.execute(query, (id,))
    vehiculo = cursor.fetchone()
    if vehiculo:
        print("Vehículo encontrado:")
        print(vehiculo)
    else:
        print("Vehículo no encontrado.")

def modificarVehiculoCarga(id, marca, capacidad_carga, disponible):
    query = "UPDATE VehiculosCarga SET Marca = %s, CapacidadCarga = %s, Disponible = %s WHERE ID = %s"
    cursor.execute(query, (marca, capacidad_carga, disponible, id))
    mydb.commit()
    print("Vehículo modificado exitosamente.")

def eliminarVehiculoCarga(id):
    query = "DELETE FROM VehiculosCarga WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Vehículo eliminado exitosamente.")

# CRUD para Alquileres
def crearAlquiler(id, id_cliente, id_vehiculo, ubicacion, fecha_inicio, fecha_fin, monto, estado):
    query = "INSERT INTO Alquileres (ID, IDCliente, IDVehiculo, Ubicacion, FechaInicio, FechaFin, Monto, Estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, id_cliente, id_vehiculo, ubicacion, fecha_inicio, fecha_fin, monto, estado))
    mydb.commit()
    print("Alquiler creado exitosamente.")

def consultarAlquiler(id):
    query = "SELECT * FROM Alquileres WHERE ID = %s"
    cursor.execute(query, (id,))
    alquiler = cursor.fetchone()
    if alquiler:
        print("Alquiler encontrado:")
        print(alquiler)
    else:
        print("Alquiler no encontrado.")

def modificarAlquiler(id, id_cliente, id_vehiculo, ubicacion, fecha_inicio, fecha_fin, monto, estado):
    query = "UPDATE Alquileres SET IDCliente = %s, IDVehiculo = %s, Ubicacion = %s, FechaInicio = %s, FechaFin = %s, Monto = %s, Estado = %s WHERE ID = %s"
    cursor.execute(query, (id_cliente, id_vehiculo, ubicacion, fecha_inicio, fecha_fin, monto, estado, id))
    mydb.commit()
    print("Alquiler modificado exitosamente.")

def eliminarAlquiler(id):
    query = "DELETE FROM Alquileres WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Alquiler eliminado exitosamente.")

# CRUD para Mantenimiento
def crearMantenimiento(id, id_vehiculo, descripcion, fecha, costo):
    query = "INSERT INTO Mantenimiento (ID, IDVehiculo, Descripcion, Fecha, Costo) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id, id_vehiculo, descripcion, fecha, costo))
    mydb.commit()
    print("Mantenimiento creado exitosamente.")

def consultarMantenimiento(id):
    query = "SELECT * FROM Mantenimiento WHERE ID = %s"
    cursor.execute(query, (id,))
    mantenimiento = cursor.fetchone()
    if mantenimiento:
        print("Mantenimiento encontrado:")
        print(mantenimiento)
    else:
        print("Mantenimiento no encontrado.")

def modificarMantenimiento(id, id_vehiculo, descripcion, fecha, costo):
    query = "UPDATE Mantenimiento SET IDVehiculo = %s, Descripcion = %s, Fecha = %s, Costo = %s WHERE ID = %s"
    cursor.execute(query, (id_vehiculo, descripcion, fecha, costo, id))
    mydb.commit()
    print("Mantenimiento modificado exitosamente.")

def eliminarMantenimiento(id):
    query = "DELETE FROM Mantenimiento WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Mantenimiento eliminado exitosamente.")

# CRUD para Empleados
def crearEmpleado(id, nombre, apellido, contacto, cargo):
    query = "INSERT INTO Empleados (ID, Nombre, Apellido, Contacto, Cargo) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id, nombre, apellido, contacto, cargo))
    mydb.commit()
    print("Empleado creado exitosamente.")

def consultarEmpleado(id):
    query = "SELECT * FROM Empleados WHERE ID = %s"
    cursor.execute(query, (id,))
    empleado = cursor.fetchone()
    if empleado:
        print("Empleado encontrado:")
        print(empleado)
    else:
        print("Empleado no encontrado.")

def modificarEmpleado(id, nombre, apellido, contacto, cargo):
    query = "UPDATE Empleados SET Nombre = %s, Apellido = %s, Contacto = %s, Cargo = %s WHERE ID = %s"
    cursor.execute(query, (nombre, apellido, contacto, cargo, id))
    mydb.commit()
    print("Empleado modificado exitosamente.")

def eliminarEmpleado(id):
    query = "DELETE FROM Empleados WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Empleado eliminado exitosamente.")

# CRUD para Reservas
def crearReserva(id, id_cliente, id_vehiculo, fecha_reserva, fecha_inicio, fecha_fin):
    query = "INSERT INTO Reservas (ID, IDCliente, IDVehiculo, FechaReserva, FechaInicio, FechaFin) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, id_cliente, id_vehiculo, fecha_reserva, fecha_inicio, fecha_fin))
    mydb.commit()
    print("Reserva creada exitosamente.")

def consultarReserva(id):
    query = "SELECT * FROM Reservas WHERE ID = %s"
    cursor.execute(query, (id,))
    reserva = cursor.fetchone()
    if reserva:
        print("Reserva encontrada:")
        print(reserva)
    else:
        print("Reserva no encontrada.")

def modificarReserva(id, id_cliente, id_vehiculo, fecha_reserva, fecha_inicio, fecha_fin):
    query = "UPDATE Reservas SET IDCliente = %s, IDVehiculo = %s, FechaReserva = %s, FechaInicio = %s, FechaFin = %s WHERE ID = %s"
    cursor.execute(query, (id_cliente, id_vehiculo, fecha_reserva, fecha_inicio, fecha_fin, id))
    mydb.commit()
    print("Reserva modificada exitosamente.")

def eliminarReserva(id):
    query = "DELETE FROM Reservas WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Reserva eliminada exitosamente.")

# CRUD para Devoluciones
def crearDevolucion(id, id_alquiler, fecha_devolucion, monto_a_pagar, dano):
    query = "INSERT INTO Devoluciones (ID, IDAlquiler, FechaDevolucion, MontoAPagar, Daño) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id, id_alquiler, fecha_devolucion, monto_a_pagar, dano))
    mydb.commit()
    print("Devolución creada exitosamente.")

def consultarDevolucion(id):
    query = "SELECT * FROM Devoluciones WHERE ID = %s"
    cursor.execute(query, (id,))
    devolucion = cursor.fetchone()
    if devolucion:
        print("Devolución encontrada:")
        print(devolucion)
    else:
        print("Devolución no encontrada.")

def modificarDevolucion(id, id_alquiler, fecha_devolucion, monto_a_pagar, dano):
    query = "UPDATE Devoluciones SET IDAlquiler = %s, FechaDevolucion = %s, MontoAPagar = %s, Daño = %s WHERE ID = %s"
    cursor.execute(query, (id_alquiler, fecha_devolucion, monto_a_pagar, dano, id))
    mydb.commit()
    print("Devolución modificada exitosamente.")

def eliminarDevolucion(id):
    query = "DELETE FROM Devoluciones WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Devolución eliminada exitosamente.")

# CRUD para Ingresos
def crearIngreso(id, fecha, monto, descripcion, id_alquiler):
    query = "INSERT INTO Ingresos (ID, Fecha, Monto, Descripcion, IDAlquiler) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id, fecha, monto, descripcion, id_alquiler))
    mydb.commit()
    print("Ingreso creado exitosamente.")

def consultarIngreso(id):
    query = "SELECT * FROM Ingresos WHERE ID = %s"
    cursor.execute(query, (id,))
    ingreso = cursor.fetchone()
    if ingreso:
        print("Ingreso encontrado:")
        print(ingreso)
    else:
        print("Ingreso no encontrado.")

def modificarIngreso(id, fecha, monto, descripcion, id_alquiler):
    query = "UPDATE Ingresos SET Fecha = %s, Monto = %s, Descripcion = %s, IDAlquiler = %s WHERE ID = %s"
    cursor.execute(query, (fecha, monto, descripcion, id_alquiler, id))
    mydb.commit()
    print("Ingreso modificado exitosamente.")

def eliminarIngreso(id):
    query = "DELETE FROM Ingresos WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Ingreso eliminado exitosamente.")

# CRUD para Egresos
def crearEgreso(id, fecha, monto, descripcion, id_mantenimiento, id_empleado):
    query = "INSERT INTO Egresos (ID, Fecha, Monto, Descripcion, IDMantenimiento, IDEmpleado) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, fecha, monto, descripcion, id_mantenimiento, id_empleado))
    mydb.commit()
    print("Egreso creado exitosamente.")

def consultarEgreso(id):
    query = "SELECT * FROM Egresos WHERE ID = %s"
    cursor.execute(query, (id,))
    egreso = cursor.fetchone()
    if egreso:
        print("Egreso encontrado:")
        print(egreso)
    else:
        print("Egreso no encontrado.")

def modificarEgreso(id, fecha, monto, descripcion, id_mantenimiento, id_empleado):
    query = "UPDATE Egresos SET Fecha = %s, Monto = %s, Descripcion = %s, IDMantenimiento = %s, IDEmpleado = %s WHERE ID = %s"
    cursor.execute(query, (fecha, monto, descripcion, id_mantenimiento, id_empleado, id))
    mydb.commit()
    print("Egreso modificado exitosamente.")

def eliminarEgreso(id):
    query = "DELETE FROM Egresos WHERE ID = %s"
    cursor.execute(query, (id,))
    mydb.commit()
    print("Egreso eliminado exitosamente.")

# Consultas adicionales
def vehiculosMasAlquilados():
    query = """
    SELECT V.ID, V.Marca, COUNT(A.IDVehiculo) AS TotalAlquileres
    FROM Alquileres A
    JOIN VehiculosCarga V ON A.IDVehiculo = V.ID
    GROUP BY V.ID, V.Marca
    ORDER BY TotalAlquileres DESC
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    print("Vehículos más alquilados:")
    for row in resultados:
        print(row)

def ingresosPorVehiculoPorRangoFechas(fecha_inicio, fecha_fin):
    query = """
    SELECT V.ID, V.Marca, SUM(A.Monto) AS Ingresos
    FROM Alquileres A
    JOIN VehiculosCarga V ON A.IDVehiculo = V.ID
    WHERE A.FechaInicio >= %s AND A.FechaFin <= %s
    GROUP BY V.ID, V.Marca
    """
    cursor.execute(query, (fecha_inicio, fecha_fin))
    resultados = cursor.fetchall()
    print(f"Ingresos por vehículo del {fecha_inicio} al {fecha_fin}:")
    for row in resultados:
        print(row)

def vehiculosDisponibles():
    query = "SELECT * FROM VehiculosCarga WHERE Disponible = 1"
    cursor.execute(query)
    resultados = cursor.fetchall()
    print("Vehículos disponibles:")
    for row in resultados:
        print(row)

def vehiculosReservadosPorEntregar():
    query = """
    SELECT V.ID, V.Marca, R.FechaInicio, R.FechaFin
    FROM Reservas R
    JOIN VehiculosCarga V ON R.IDVehiculo = V.ID
    WHERE R.FechaInicio > CURDATE()
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    print("Vehículos reservados por entregar:")
    for row in resultados:
        print(row)

def clientesConMayorFacturacionPorFechas(fecha_inicio, fecha_fin):
    query = """
    SELECT C.ID, C.Nombre, C.Apellido, SUM(A.Monto) AS TotalFacturado
    FROM Clientes C
    JOIN Alquileres A ON C.ID = A.IDCliente
    WHERE A.FechaInicio >= %s AND A.FechaFin <= %s
    GROUP BY C.ID, C.Nombre, C.Apellido
    ORDER BY TotalFacturado DESC
    """
    cursor.execute(query, (fecha_inicio, fecha_fin))
    resultados = cursor.fetchall()
    print(f"Clientes con mayor facturación del {fecha_inicio} al {fecha_fin}:")
    for row in resultados:
        print(row)

def equiposPendientesPorMantenimiento():
    query = """
    SELECT V.ID, V.Marca, M.Descripcion, M.Fecha
    FROM Mantenimiento M
    JOIN VehiculosCarga V ON M.IDVehiculo = V.ID
    WHERE M.Fecha > CURDATE()
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    print("Equipos pendientes por mantenimiento:")
    for row in resultados:
        print(row)

# Frontend
def menu_principal():
    while True:
        print("Seleccione una opción:")
        print("1. Operaciones CRUD")
        print("2. Consultas")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            menu_tablas()
        elif opcion == "2":
            menu_consultas()
        elif opcion == "3":
            break
        else:
            print("Opción no válida, intente de nuevo.")

def menu_tablas():
    while True:
        print("Seleccione la tabla para la cual desea realizar operaciones:")
        print("1. Clientes")
        print("2. Vehículos de Carga")
        print("3. Alquileres")
        print("4. Mantenimiento")
        print("5. Empleados")
        print("6. Reservas")
        print("7. Devoluciones")
        print("8. Ingresos")
        print("9. Egresos")
        print("10. Volver al menú anterior")

        opcion_tabla = input("Opción: ")

        if opcion_tabla == "1":
            menu_crud("Cliente")
        elif opcion_tabla == "2":
            menu_crud("VehiculoCarga")
        elif opcion_tabla == "3":
            menu_crud("Alquiler")
        elif opcion_tabla == "4":
            menu_crud("Mantenimiento")
        elif opcion_tabla == "5":
            menu_crud("Empleado")
        elif opcion_tabla == "6":
            menu_crud("Reserva")
        elif opcion_tabla == "7":
            menu_crud("Devolucion")
        elif opcion_tabla == "8":
            menu_crud("Ingreso")
        elif opcion_tabla == "9":
            menu_crud("Egreso")
        elif opcion_tabla == "10":
            break
        else:
            print("Opción no válida, intente de nuevo.")

def menu_crud(tabla):
    while True:
        print(f"\nOperaciones CRUD para la tabla '{tabla}':")
        print("1. Crear")
        print("2. Consultar")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Volver al menú anterior")

        opcion_crud = input("Opción: ")

        if opcion_crud == "1":
            crear_funcion = globals().get(f"crear{tabla}")
            if crear_funcion:
                crear_funcion(*obtener_datos(tabla))
            else:
                print("Función de creación no encontrada.")
        elif opcion_crud == "2":
            consultar_funcion = globals().get(f"consultar{tabla}")
            if consultar_funcion:
                id = input(f"Ingrese el ID del registro de la tabla '{tabla}': ")
                consultar_funcion(id)
            else:
                print("Función de consulta no encontrada.")
        elif opcion_crud == "3":
            modificar_funcion = globals().get(f"modificar{tabla}")
            if modificar_funcion:
                id = input(f"Ingrese el ID del registro de la tabla '{tabla}': ")
                datos = obtener_datos(tabla)
                modificar_funcion(id, *datos[1:])
            else:
                print("Función de modificación no encontrada.")
        elif opcion_crud == "4":
            eliminar_funcion = globals().get(f"eliminar{tabla}")
            if eliminar_funcion:
                id = input(f"Ingrese el ID del registro de la tabla '{tabla}': ")
                eliminar_funcion(id)
            else:
                print("Función de eliminación no encontrada.")
        elif opcion_crud == "5":
            break
        else:
            print("Opción no válida, intente de nuevo.")

def obtener_datos(tabla):
    datos = []
    if tabla == "Cliente":
        datos.append(input("Ingrese ID cliente: "))
        datos.append(input("Ingrese nombre: "))
        datos.append(input("Ingrese apellido: "))
        datos.append(input("Ingrese contacto: "))
    elif tabla == "VehiculoCarga":
        datos.append(input("Ingrese ID vehículo: "))
        datos.append(input("Ingrese marca: "))
        datos.append(input("Ingrese capacidad de carga: "))
        datos.append(input("Ingrese disponibilidad (1 para disponible, 0 para no disponible): "))
    elif tabla == "Alquiler":
        datos.append(input("Ingrese ID alquiler: "))
        datos.append(input("Ingrese ID cliente: "))
        datos.append(input("Ingrese ID vehículo: "))
        datos.append(input("Ingrese ubicación: "))
        datos.append(input("Ingrese fecha de inicio (YYYY-MM-DD): "))
        datos.append(input("Ingrese fecha de fin (YYYY-MM-DD): "))
        datos.append(input("Ingrese monto: "))
        datos.append(input("Ingrese estado: "))
    elif tabla == "Mantenimiento":
        datos.append(input("Ingrese ID mantenimiento: "))
        datos.append(input("Ingrese ID vehículo: "))
        datos.append(input("Ingrese descripción: "))
        datos.append(input("Ingrese fecha (YYYY-MM-DD): "))
        datos.append(input("Ingrese costo: "))
    elif tabla == "Empleado":
        datos.append(input("Ingrese ID empleado: "))
        datos.append(input("Ingrese nombre: "))
        datos.append(input("Ingrese apellido: "))
        datos.append(input("Ingrese contacto: "))
        datos.append(input("Ingrese cargo: "))
    elif tabla == "Reserva":
        datos.append(input("Ingrese ID reserva: "))
        datos.append(input("Ingrese ID cliente: "))
        datos.append(input("Ingrese ID vehículo: "))
        datos.append(input("Ingrese fecha de reserva (YYYY-MM-DD): "))
        datos.append(input("Ingrese fecha de inicio (YYYY-MM-DD): "))
        datos.append(input("Ingrese fecha de fin (YYYY-MM-DD): "))
    elif tabla == "Devolucion":
        datos.append(input("Ingrese ID devolución: "))
        datos.append(input("Ingrese ID alquiler: "))
        datos.append(input("Ingrese fecha de devolución (YYYY-MM-DD): "))
        datos.append(input("Ingrese monto a pagar: "))
        datos.append(input("Ingrese daño (opcional): "))
    elif tabla == "Ingreso":
        datos.append(input("Ingrese ID ingreso: "))
        datos.append(input("Ingrese fecha (YYYY-MM-DD): "))
        datos.append(input("Ingrese monto: "))
        datos.append(input("Ingrese descripción: "))
        datos.append(input("Ingrese ID alquiler (opcional): "))
    elif tabla == "Egreso":
        datos.append(input("Ingrese ID egreso: "))
        datos.append(input("Ingrese fecha (YYYY-MM-DD): "))
        datos.append(input("Ingrese monto: "))
        datos.append(input("Ingrese descripción: "))
        datos.append(input("Ingrese ID mantenimiento (opcional): "))
        datos.append(input("Ingrese ID empleado (opcional): "))
    return datos

def menu_consultas():
    while True:
        print("Seleccione la consulta que desea realizar:")
        print("1. Vehículos más alquilados")
        print("2. Ingresos por vehículo por rango de fechas")
        print("3. Vehículos disponibles")
        print("4. Vehículos reservados por entregar")
        print("5. Clientes con mayor facturación por fechas")
        print("6. Equipos pendientes por mantenimiento")
        print("7. Volver al menú anterior")

        opcion_consulta = input("Opción: ")

        if opcion_consulta == "1":
            vehiculosMasAlquilados()
        elif opcion_consulta == "2":
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            ingresosPorVehiculoPorRangoFechas(fecha_inicio, fecha_fin)
        elif opcion_consulta == "3":
            vehiculosDisponibles()
        elif opcion_consulta == "4":
            vehiculosReservadosPorEntregar()
        elif opcion_consulta == "5":
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            clientesConMayorFacturacionPorFechas(fecha_inicio, fecha_fin)
        elif opcion_consulta == "6":
            equiposPendientesPorMantenimiento()
        elif opcion_consulta == "7":
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú principal
menu_principal()
