
#######################################  ADMINISTRADOR ##########################################
CREATE TABLE Administrador(
			IdUsuario INT NOT NULL PRIMARY KEY,
			CONSTRAINT user UNIQUE(IdUsuario),
			aNombre VARCHAR(10),
			Passw VARCHAR(10));

################## CONDUCTOR ######################
CREATE TABLE Conductor(
			Cedula CHAR(10) NOT NULL,
			IdConductor INT AUTO_INCREMENT PRIMARY KEY,
			cNombre VARCHAR(50),
			NoLicencia CHAR(10),
			Fecha_Ingreso DATE,
			Fecha_Nacimiento DATE,
			IdUsuario INT,
			FOREIGN KEY (IdUsuario) REFERENCES Administrador(IdUsuario));

########################################     UNIDAD    #############################################
CREATE TABLE Unidad(
			IdUnidad INT AUTO_INCREMENT PRIMARY KEY,
			Matricula CHAR(8) NOT NULL,
			Capacidad INT,
			Anio_Fab CHAR(5),
			Fecha_Adquisicion DATE,
			IdUsuario INT,
			FOREIGN KEY (IdUsuario) REFERENCES Administrador(IdUsuario));

######################################  ESTACION  ###############################################
CREATE TABLE Estacion(
			IdEstacion INT AUTO_INCREMENT PRIMARY KEY,
			eNombre CHAR(20),
			Direccion CHAR(50)); 

################# RECORRIDO ######################
CREATE TABLE Recorrido(
			IdRecorrido INT AUTO_INCREMENT PRIMARY KEY,
			Fecha DATE NOT NULL,
			NoPasajeros INT NOT NULL,
			Hora_Salida TIME NOT NULL,
			Hora_Llegada TIME NOT NULL,
			IdEstacion_Salida INT,
			IdEstacion_Llegada INT,
			IdUsuario INT,
			FOREIGN KEY (IdEstacion_Salida) REFERENCES Estacion(IdEstacion),
			FOREIGN KEY (IdEstacion_Llegada) REFERENCES Estacion(IdEstacion),
			FOREIGN KEY (IdUsuario) REFERENCES Administrador(IdUsuario));

########### CONDUCTOR_BUS_RECORRIDO ###################3
CREATE TABLE Conductor_Bus_Recorrido(
			IdRecorrido INT AUTO_INCREMENT,
			IdConductor INT,
			IdUnidad INT,
			FOREIGN KEY (IdRecorrido) REFERENCES Recorrido(IdRecorrido),
			FOREIGN KEY (IdConductor) REFERENCES Conductor(IdConductor),
			FOREIGN KEY (IdUnidad) REFERENCES Unidad(IdUnidad));
