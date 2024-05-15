-- Crear la tabla de vehículos de carga
CREATE TABLE VehiculosCarga (
    ID INT PRIMARY KEY,
    Marca VARCHAR(100),
    CapacidadCarga DECIMAL(10,2)
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
