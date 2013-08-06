#######################################  ADMINISTRADOR ##########################################
CREATE TABLE Administrador(
			IdUsuario INT NOT NULL PRIMARY KEY,
			CONSTRAINT user UNIQUE(IdUsuario),
			aNombre VARCHAR(10),
			Passw VARCHAR(10));

INSERT INTO Administrador VALUES(1,'admin','1234');

######################################  ESTACION  ###############################################
CREATE TABLE Estacion(
			IdEstacion INT AUTO_INCREMENT PRIMARY KEY,
			eNombre CHAR(20),
			Direccion CHAR(50));

INSERT INTO Estacion VALUES(null,'Piscina Olimpica','Esmeraldas y Hurtado');
INSERT INTO Estacion VALUES(null,'Terminal Terrestre','Av. Benjamin Rosales');
INSERT INTO Estacion VALUES(null,'Campus Prosperina','Km 30.5, Vía Perimetral');
INSERT INTO Estacion VALUES(null,'Acacias','Av. 25 de Julio y Av. Aurora Estrada');
INSERT INTO Estacion VALUES(null,'Pollos el Ecanto','Av. Gabriel Roldos y Av. Cornell Gomez');
INSERT INTO Estacion VALUES(null,'Duran','Banco Pichincha, Duran');
INSERT INTO Estacion VALUES(null,'Orquideas','Redondel de entrada a las Orquideas');

######################################  Conductor_Bus_Recorrido  #############################

CREATE TABLE Conductor_Bus_Recorrido(
			IdRecorrido INT,
			IdConductor INT,
			IdUnidad INT,
			FOREIGN KEY (IdRecorrido) REFERENCES Recorrido(IdRecorrido),
			FOREIGN KEY (IdConductor) REFERENCES Conductor(IdConductor),
			FOREIGN KEY (IdUnidad) REFERENCES Unidad(IdUnidad));
			

########################################     UNIDAD    #############################################
CREATE TABLE Unidad(
			IdUnidad INT AUTO_INCREMENT PRIMARY KEY,
			Matricula CHAR(8) NOT NULL,
			Capacidad INT,
			Anio_Fab CHAR(5),
			Fecha_Adquisicion DATE,
			IdUsuario INT,
			FOREIGN KEY (IdUsuario) REFERENCES Administrador(IdUsuario)); 

delimiter //
CREATE PROCEDURE PRInsertUnidad
		(IN Matricul CHAR(8),
		 IN Capacid INT,
		 IN Anio_F CHAR(5),
		 IN Fecha_A DATE) BEGIN
INSERT INTO Unidad (Matricula, Capacidad, Anio_Fab, Fecha_Adquisicion, IdUsuario) VALUES (Matricul, Capacid, Anio_F, Fecha_A, 1);
END //
delimeter ;

call PRInsertUnidad('1234523456', '200', '1987', '2002/04/04')

UPDATE Unidad SET matricula='GAY-237', Anio_Fab='2009',Fecha_Adquisicion='2011/02/23'
where IdUnidad = 2;

ALTER TABLE Unidad MODIFY Anio_Fab char(5);

INSERT INTO Unidad VALUES(null,'GHJ-513',35,'2002','2008/04/02',1);
INSERT INTO Unidad VALUES(null,'GPK-1534',50,'2011','2012/08/29',1);
INSERT INTO Unidad VALUES(null,'GHJ-513',35,'2002','2008/07/07',1);
INSERT INTO Unidad VALUES(null,'GMW-934',35,'2007','2012/05/14',1);
INSERT INTO Unidad VALUES(null,'GQW-3273',50,'2012','2013/04/05',1);

########################################     CONDUCTOR    #############################################

CREATE TABLE Conductor(
			Cedula CHAR(10) NOT NULL,
			IdConductor INT AUTO_INCREMENT PRIMARY KEY,
			cNombre VARCHAR(50),
			NoLicencia CHAR(10),
			Fecha_Ingreso DATE,
			Fecha_Nacimiento DATE,
			IdUsuario INT,
			FOREIGN KEY (IdUsuario) REFERENCES Administrador(IdUsuario));

delimiter //
CREATE PROCEDURE PRInsertConductor
		(IN CI CHAR(10),
		 IN Nombre VARCHAR(50),
		 IN NLicencia CHAR(10),
		 IN Fecha_Ing DATE,
		 IN Fecha_Nac DATE) BEGIN
INSERT INTO Conductor (Cedula, cNombre, NoLicencia, Fecha_Ingreso, Fecha_Nacimiento, IdUsuario)VALUES(CI, Nombre,NLicencia,Fecha_Ing, Fecha_Nac,1);
END //
delimiter ;

call PRInsertConductor('0988759621','Eduardo Zavala','0988759621','2002/04/04','1970/05/10');
INSERT INTO Conductor(Cedula, cNombre, NoLicencia, Fecha_Ingreso, Fecha_Nacimiento, IdUsuario) VALUES('0931191118', 'Alejandro Chanaba','0931191118','2001/02/10','1980/05/09',1);

########################################     RECORRIDO    #############################################

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

#Drop PROCEDURE PRInsertRecorrido
delimiter //
CREATE PROCEDURE PRInsertRecorrido
		(IN IdRecorrido INTEGER,
		 IN fech DATE,
		 IN idConductor INTEGER,
		 IN idUnidad INTEGER,
		 IN NPasajeros INTEGER,
		 IN Hora_S TIME,
		 IN Hora_L TIME,
		 IN Id_estacion_S INTEGER,
		 IN Id_estacion_ll INTEGER)BEGIN 
INSERT INTO Recorrido(Fecha, NoPasajeros, Hora_Salida, Hora_Llegada, IdEstacion_Salida, IdEstacion_Llegada, IdUsuario ) VALUES(fech,NPasajeros,Hora_S,Hora_L,Id_estacion_S,Id_estacion_ll,1); 
INSERT INTO Conductor_Bus_Recorrido VALUES(idRecorrido,idConductor,idUnidad);
END //
delimiter ;

call PRInsertRecorrido(1,'2013/02/08',1,1,45,'11:00:00','11:30:00',1,2);
