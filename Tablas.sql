
CREATE TABLE Administrador(
			IdUsuario INT NOT NULL PRIMARY KEY,
			CONSTRAINT user UNIQUE(IdUsuario),
			aNombre VARCHAR(10),
			Passw VARCHAR(10));


CREATE TABLE Conductor(
			Cedula CHAR(10) NOT NULL,
			IdConductor INT AUTO_INCREMENT PRIMARY KEY,
			cNombre VARCHAR(50),
			NoLicencia CHAR(10),
			Fecha_Ingreso DATE,
			Fecha_Nacimiento DATE,
			IdUsuario INT,
			FOREIGN KEY (IdUsuario) REFERENCES Administrador(IdUsuario));

CREATE TABLE Unidad(
			IdUnidad INT AUTO_INCREMENT PRIMARY KEY,
			Matricula CHAR(8) NOT NULL,
			Capacidad INT,
			Anio_Fab CHAR(5),
			Fecha_Adquisicion DATE,
			IdUsuario INT,
			FOREIGN KEY (IdUsuario) REFERENCES Administrador(IdUsuario)); 

CREATE TABLE Estacion(
			IdEstacion INT AUTO_INCREMENT PRIMARY KEY,
			eNombre CHAR(20),
			Direccion CHAR(50));

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

CREATE TABLE Conductor_Bus_Recorrido(
			IdRecorrido INT,
			IdConductor INT,
			IdUnidad INT,
			FOREIGN KEY (IdRecorrido) REFERENCES Recorrido(IdRecorrido),
			FOREIGN KEY (IdConductor) REFERENCES Conductor(IdConductor),
			FOREIGN KEY (IdUnidad) REFERENCES Unidad(IdUnidad));
			
INSERT INTO Administrador VALUES(1,'admin','1234')



INSERT INTO Estacion VALUES(null,'Piscina Olimpica','Esmeraldas y Hurtado')
INSERT INTO Estacion VALUES(null,'Terminal Terrestre','Av. Benjamin Rosales')
INSERT INTO Estacion VALUES(null,'Campus Prosperina','Km 30.5, Vía Perimetral');
INSERT INTO Estacion VALUES(null,'Acacias','Av. 25 de Julio y Av. Aurora Estrada');
INSERT INTO Estacion VALUES(null,'Pollos el Ecanto','Av. Gabriel Roldos y Av. Cornell Gomez');
INSERT INTO Estacion VALUES(null,'Duran','Banco Pichincha, Duran');
INSERT INTO Estacion VALUES(null,'Orquideas','Redondel de entrada a las Orquideas');

INSERT INTO Unidad VALUES(null,'GHJ-513',35,'2002','2008/04/02',1);
INSERT INTO Unidad VALUES(null,'GPK-1534',50,'2011','2012/08/29',1);
INSERT INTO Unidad VALUES(null,'GHJ-513',35,'2002','2008/07/07',1);
INSERT INTO Unidad VALUES(null,'GMW-934',35,'2007','2012/05/14',1);
INSERT INTO Unidad VALUES(null,'GQW-3273',50,'2012','2013/04/05',1);

UPDATE Unidad SET matricula='GAY-237', Anio_Fab='2009',Fecha_Adquisicion='2011/02/23'
where IdUnidad = 2;

ALTER TABLE Unidad MODIFY Anio_Fab char(5)
select * from estacionAnio_Fab
select * from Unidad
delimiter //

CREATE PROCEDURE PRInsertRecorrido
		(IN idRecorrido INTEGER,
		 IN fecha DATE,
		 IN idConductor INTEGER,
		 IN idUnidad INTEGER,
		 IN NoPasajeros INTEGER,
		 IN Hora_Salida TIME,
		 IN Hora_Llegada TIME,
		 IN Id_estacion_Salida INTEGER,
		 IN Id_estacion_llegada INTEGER)BEGIN 
INSERT INTO Recorrido VALUES(idRecorrido,fecha,NoPasajeros,Hora_Salida,Hora_Llegada,Id_estacion_Salida,Id_estacion_llegada,1); 
INSERT INTO conductor_bus_recorrido(idRecorrido,idConductor,idUnidad);
END //
delimiter ;
call PRInsertRecorrido(1,'2013/02/08',1,1,45,'11:00:00','11:30:00',1,2)

