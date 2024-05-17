-- Crear la tabla de vehículos de carga
CREATE TABLE VehiculosCarga (
    ID INT PRIMARY KEY,
    Marca VARCHAR(100),
    CapacidadCarga DECIMAL(10,2),
    Disponible BIT DEFAULT 1
);

-- Insertar datos de ejemplo en la tabla de vehículos de carga
INSERT INTO VehiculosCarga (ID, Marca, CapacidadCarga) VALUES
(1, 'Marca1', 10.5),
(2, 'Marca2', 12.3),
(3, 'Marca3', 15.0);

-- Crear la tabla de clientes
CREATE TABLE Clientes (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Contacto VARCHAR(100)
);

-- Insertar datos de ejemplo en la tabla de clientes
INSERT INTO Clientes (ID, Nombre, Apellido, Contacto) VALUES
(1, 'Juan', 'Perez', 'juan@example.com'),
(2, 'Maria', 'Gomez', 'maria@example.com');

-- Crear la tabla de alquileres
CREATE TABLE Alquileres (
    ID INT PRIMARY KEY,
    IDCliente INT,
    IDVehiculo INT,
    Ubicacion VARCHAR(100),
    FechaInicio DATE,
    FechaFin DATE,
    Monto DECIMAL(10,2),
    Estado VARCHAR(50) DEFAULT 'Activo',
    FOREIGN KEY (IDCliente) REFERENCES Clientes(ID),
    FOREIGN KEY (IDVehiculo) REFERENCES VehiculosCarga(ID)
);

-- Insertar datos de ejemplo en la tabla de alquileres
INSERT INTO Alquileres (ID, IDCliente, IDVehiculo, Ubicacion, FechaInicio, FechaFin, Monto) VALUES
(1, 1, 1, 'Ubicacion1', '2024-05-15', '2024-05-20', 200.00),
(2, 2, 3, 'Ubicacion2', '2024-05-17', '2024-05-22', 250.00);

-- Crear la tabla de mantenimiento
CREATE TABLE Mantenimiento (
    ID INT PRIMARY KEY,
    IDVehiculo INT,
    Descripcion VARCHAR(200),
    Fecha DATE,
    Costo DECIMAL(10,2),
    FOREIGN KEY (IDVehiculo) REFERENCES VehiculosCarga(ID)
);

-- Insertar datos de ejemplo en la tabla de mantenimiento
INSERT INTO Mantenimiento (ID, IDVehiculo, Descripcion, Fecha, Costo) VALUES
(1, 1, 'Cambio de aceite', '2024-05-10', 50.00),
(2, 3, 'Reparación de frenos', '2024-05-12', 120.00);

-- Crear la tabla de empleados
CREATE TABLE Empleados (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Contacto VARCHAR(100),
    Cargo VARCHAR(100)
);

-- Insertar datos de ejemplo en la tabla de empleados
INSERT INTO Empleados (ID, Nombre, Apellido, Contacto, Cargo) VALUES
(1, 'Luis', 'Martinez', 'luis@example.com', 'Conductor'),
(2, 'Ana', 'Lopez', 'ana@example.com', 'Mecanico');

-- Crear la tabla de reservas
CREATE TABLE Reservas (
    ID INT PRIMARY KEY,
    IDCliente INT,
    IDVehiculo INT,
    FechaReserva DATE,
    FechaInicio DATE,
    FechaFin DATE,
    FOREIGN KEY (IDCliente) REFERENCES Clientes(ID),
    FOREIGN KEY (IDVehiculo) REFERENCES VehiculosCarga(ID)
);

-- Insertar datos de ejemplo en la tabla de reservas
INSERT INTO Reservas (ID, IDCliente, IDVehiculo, FechaReserva, FechaInicio, FechaFin) VALUES
(1, 1, 2, '2024-05-01', '2024-05-15', '2024-05-20'),
(2, 2, 1, '2024-05-02', '2024-05-17', '2024-05-22');

-- Crear la tabla de devoluciones
CREATE TABLE Devoluciones (
    ID INT PRIMARY KEY,
    IDAlquiler INT,
    FechaDevolucion DATE,
    MontoAPagar DECIMAL(10,2),
    Daño VARCHAR(200),
    FOREIGN KEY (IDAlquiler) REFERENCES Alquileres(ID)
);

-- Insertar datos de ejemplo en la tabla de devoluciones
INSERT INTO Devoluciones (ID, IDAlquiler, FechaDevolucion, MontoAPagar, Daño) VALUES
(1, 1, '2024-05-21', 50.00, 'Ninguno'),
(2, 2, '2024-05-23', 70.00, 'Rasguño en el lateral');

-- Crear la tabla de ingresos
CREATE TABLE Ingresos (
    ID INT PRIMARY KEY,
    Fecha DATE,
    Monto DECIMAL(10,2),
    Descripcion VARCHAR(200),
    IDAlquiler INT NULL,
    FOREIGN KEY (IDAlquiler) REFERENCES Alquileres(ID)
);

-- Insertar datos de ejemplo en la tabla de ingresos
INSERT INTO Ingresos (ID, Fecha, Monto, Descripcion, IDAlquiler) VALUES
(1, '2024-05-21', 200.00, 'Pago por alquiler', 1),
(2, '2024-05-23', 250.00, 'Pago por alquiler', 2);

-- Crear la tabla de egresos
CREATE TABLE Egresos (
    ID INT PRIMARY KEY,
    Fecha DATE,
    Monto DECIMAL(10,2),
    Descripcion VARCHAR(200),
    IDMantenimiento INT NULL,
    IDEmpleado INT NULL,
    FOREIGN KEY (IDMantenimiento) REFERENCES Mantenimiento(ID),
    FOREIGN KEY (IDEmpleado) REFERENCES Empleados(ID)
);

-- Insertar datos de ejemplo en la tabla de egresos
INSERT INTO Egresos (ID, Fecha, Monto, Descripcion, IDMantenimiento, IDEmpleado) VALUES
(1, '2024-05-10', 50.00, 'Costo de cambio de aceite', 1, NULL),
(2, '2024-05-23', 70.00, 'Pago por reparación de frenos', 2, NULL),
(3, '2024-05-15', 1500.00, 'Salario empleado', NULL, 1),
(4, '2024-05-15', 1600.00, 'Salario empleado', NULL, 2);
