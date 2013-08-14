######## Procedure ObtenerConductores #####
drop procedure PRGetConductor;
delimiter //
CREATE PROCEDURE PRGetConductor()
BEGIN
SELECT IdConductor,Cedula,cNombre
FROM Conductor;
END //
delimiter ;
call PRGetConductor()

######## Procedure Obtener Unidades ###########
delimiter //
CREATE PROCEDURE PRGetUnidad()
BEGIN
SELECT idUnidad,Capacidad
FROM Unidad;
END //
delimiter ;
call PRGetUnidad

######### Procedure IngresarUnidad #########
delimiter //
CREATE PROCEDURE PRInsertUnidad
		(IN Matricul CHAR(8),
		 IN Capacid INT,
		 IN Anio_F CHAR(5),
		 IN Fecha_A DATE) BEGIN
INSERT INTO Unidad (Matricula, Capacidad, Anio_Fab, Fecha_Adquisicion, IdUsuario) VALUES (Matricul, Capacid, Anio_F, Fecha_A, 1);
END //
delimiter ;

call PRInsertUnidad('1234523456', '200', '1987', '2002/04/04')

######### Procedure IngresarConductor #########
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
drop Procedure PRInsertRecorrido
######### Procedure IngresarRecorrido #########
delimiter //
CREATE PROCEDURE PRInsertRecorrido
		(IN fech DATE,
		 IN idConductor INTEGER,
		 IN idUnidad INTEGER,
		 IN NPasajeros INTEGER,
		 IN Hora_S TIME,
		 IN Hora_L TIME,
		 IN Id_estacion_S INTEGER,
		 IN Id_estacion_ll INTEGER)BEGIN
INSERT INTO Recorrido(Fecha, NoPasajeros, Hora_Salida, Hora_Llegada, IdEstacion_Salida, IdEstacion_Llegada, IdUsuario ) VALUES(fech,NPasajeros,Hora_S,Hora_L,Id_estacion_S,Id_estacion_ll,1); 
INSERT INTO Conductor_Bus_Recorrido(IdConductor,IdUnidad) VALUES(idConductor,idUnidad);
END //
delimiter ;

#call PRInsertRecorrido(1,'2013/02/08',1,1,45,'11:00:00','11:30:00',1,2);
call PRInsertRecorrido('2013/02/08',1,1,45,'11:00:00','11:30:00',1,2);
call PRInsertRecorrido('2013/02/25',2,2,30,'13:00:00','13:45:00',1,2);

Select * from Recorrido
Select * from Conductor_Bus_Recorrido


####### Query Recorrido por fecha ###############
drop procedure PRQueryRecorridoFecha;	
delimiter //
CREATE PROCEDURE PRQueryRecorridoFecha	
		(IN FechaInicial DATE,
		 IN FechaFinal	 DATE)BEGIN
SELECT c.cNombre AS Conductor,cbr.IdUnidad AS Unidad,r.NoPasajeros AS Numero_Pasajeros,e.eNombre AS Estacion_Salida,e1.eNombre AS Estacion_Llegada,r.Hora_Salida,r.Hora_Llegada
FROM Conductor_Bus_Recorrido cbr,Conductor c,Estacion e,Recorrido r,Estacion e1
WHERE (cbr.IdRecorrido=r.IdRecorrido AND cbr.IdConductor=c.IdConductor 
AND r.IdEstacion_Salida=e.idEstacion AND r.IdEstacion_Llegada=e1.IdEstacion 
AND r.Fecha between FechaInicial AND FechaFinal);
END //
delimiter ;

CALL PRQueryRecorridoFecha('2013/02/08','2013/02/21');

######## Query Recorrido por Conductor ############
DROP PROCEDURE PRQueryRecorridoConductor;
delimiter //
CREATE PROCEDURE PRQueryRecorridoConductor
		(IN CI CHAR(10))BEGIN
SELECT cbr.IdUnidad AS Unidad,r.NoPasajeros AS Numero_Pasajeros,e.eNombre AS Estacion_Salida,e1.eNombre AS Estacion_Llegada,r.Hora_Salida,r.Hora_Llegada
FROM Conductor_Bus_Recorrido cbr,Conductor c,Estacion e,Recorrido r,Estacion e1
WHERE (cbr.IdRecorrido=r.IdRecorrido AND cbr.IdConductor=c.IdConductor 
AND r.IdEstacion_Salida=e.idEstacion AND r.IdEstacion_Llegada=e1.IdEstacion 
AND c.Cedula=CI);
END //
delimiter ;
CALL PRQueryRecorridoConductor('0931100345');

##### Query Recorrido por Unidad ###############
DROP  PROCEDURE IF EXISTS PRQueryRecorridoUnidad;
delimiter //
CREATE PROCEDURE PRQueryRecorridoUnidad
        (IN ID INTEGER) BEGIN
SELECT r.Fecha,r.Hora_Salida,r.Hora_Llegada,r.NoPasajeros AS Numero_Pasajeros,e.eNombre AS Estacion_Salida, e1.eNombre AS Estacion_Llegada
FROM Conductor_Bus_Recorrido cbr,Unidad u,Estacion e,Recorrido r,Estacion e1
WHERE (cbr.IdRecorrido=r.IdRecorrido AND cbr.IdUnidad=u.IdUnidad 
AND r.IdEstacion_Salida=e.idEstacion AND r.IdEstacion_Llegada=e1.IdEstacion 
AND u.IdUnidad=ID);
END //
delimiter ;

call PRQueryRecorridoUnidad(1);

#### Query Recorrido por fecha #######
delimiter // 
CREATE PROCEDURE PRQueryRecorridoHora 
        (IN HoraInicial TIME, 
         IN HoraFinal TIME)BEGIN 
SELECT r.Fecha,c.cNombre AS Conductor,cbr.IdUnidad AS Unidad,r.NoPasajeros AS Numero_Pasajeros,e.eNombre AS Estacion_Salida,e1.eNombre AS Estacion_Llegada 
FROM Conductor_Bus_Recorrido cbr,Conductor c,Estacion e,Recorrido r,Estacion e1 
WHERE (cbr.IdRecorrido=r.IdRecorrido AND cbr.IdConductor=c.IdConductor AND r.IdEstacion_Salida=e.idEstacion AND r.IdEstacion_Llegada=e1.IdEstacion AND r.Hora_Salida between HoraInicial AND HoraFinal); 
END // 
delimiter ; 
CALL PRQueryRecorridoHora('06:00:00','09:30:00');
select * from Unidad



