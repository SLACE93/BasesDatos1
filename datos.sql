#### Administrador ########
INSERT INTO Administrador VALUES(1,'admin','1234');

 ### ESTACIONES #####
INSERT INTO Estacion VALUES(null,'Piscina Olimpica','Esmeraldas y Hurtado');
INSERT INTO Estacion VALUES(null,'Terminal Terrestre','Av. Benjamin Rosales');
INSERT INTO Estacion VALUES(null,'Campus Prosperina','Km 30.5, Vía Perimetral');
INSERT INTO Estacion VALUES(null,'Acacias','Av. 25 de Julio y Av. Aurora Estrada');
INSERT INTO Estacion VALUES(null,'Pollos el Ecanto','Av. Gabriel Roldos y Av. Cornell Gomez');
INSERT INTO Estacion VALUES(null,'Duran','Banco Pichincha, Duran');
INSERT INTO Estacion VALUES(null,'Orquideas','Redondel de entrada a las Orquideas');

######## UNIDADADES ###########
INSERT INTO Unidad VALUES(null,'GHJ-513',35,'2002','2008/04/02',1);
INSERT INTO Unidad VALUES(null,'GPK-1534',50,'2011','2012/08/29',1);
INSERT INTO Unidad VALUES(null,'GHJ-513',35,'2002','2008/07/07',1);
INSERT INTO Unidad VALUES(null,'GMW-934',35,'2007','2012/05/14',1);
INSERT INTO Unidad VALUES(null,'GQW-3273',50,'2012','2013/04/05',1);
INSERT INTO Unidad VALUES(null,'GDW-548',45,'2010','2010/05/06',1);
INSERT INTO Unidad VALUES(null,'GEG-6598',35,'2008','2009/10/15',1);
INSERT INTO Unidad VALUES(null,'GLK-8795',32,'2007','2007/04/16',1);
INSERT INTO Unidad VALUES(null,'GPO-879',35,'2009','2010/01/02',1);
INSERT INTO Unidad VALUES(null,'GSQE-4979',50,'2004','2001/11/10',1);
INSERT INTO Unidad VALUES(null,'GHY-1234',38,'2006','2006/04/16',1);
INSERT INTO Unidad VALUES(null,'GUY-987',45,'2003','2005/06/02',1);
INSERT INTO Unidad VALUES(null,'GAY-1235',50,'2011','2011/05/10',1);
INSERT INTO Unidad VALUES(null,'GQO-112',32,'2000','2001/07/19',1);
INSERT INTO Unidad VALUES(null,'GQA-326',50,'2002','2003/08/08',1);
INSERT INTO Unidad VALUES(null,'GPP-3659',38,'2009','2010/02/14',1);

###### CONDUCTOR ########
INSERT INTO Conductor VALUES('0165478932',NULL,'Marco Sanches','0165478932','2012/04/20','1982/11/02',1);
INSERT INTO Conductor VALUES('2589631478',NULL,'Eduardo Zavala','2589631478','2011/06/15','1975/05/10',1);
INSERT INTO Conductor VALUES('0754613524',NULL,'Daniel Puya','0754613524','2010/07/15','1983/04/10',1);
INSERT INTO Conductor VALUES('7539518524',NULL,'Flores Julio','7539518524','2009/12/25','1970/06/11',1);
INSERT INTO Conductor VALUES('6654889756',NULL,'Xavier Castro','6654889756','2012/05/08','1985/01/06',1);
INSERT INTO Conductor VALUES('4558796541',NULL,'Douglas Mejia','4558796541','2013/01/09','1987/02/14',1);
INSERT INTO Conductor VALUES('0526498786',NULL,'Galo Chancay','0526498786','2010/07/17','1976/05/27',1);
INSERT INTO Conductor VALUES('8854772310',NULL,'Carlos Pena','8854772310','2009/11/03','1988/11/03',1);
INSERT INTO Conductor VALUES('0915687946',NULL,'Jorge Choez Criollo','0915687946','2005/05/26','1979/09/03',1);
INSERT INTO Conductor VALUES('0879412054',NULL,'Juan Martin','0879412054','2004/10/15','1981/07/23',1);
INSERT INTO Conductor VALUES('0754118963',NULL,'Carlos Romero','0754118963','2002/12/15','1974/12/23',1);
INSERT INTO Conductor VALUES('0885566447',NULL,'Marco San Martin','0885566447','2010/07/12','1980/08/08',1);
INSERT INTO Conductor VALUES('9513574568',NULL,'Andres Ugalde','9513574568','2000/01/30','1965/04/14',1);

###### RECORRIDOS #########
INSERT INTO Recorrido VALUES(NULL,'2013-05-01',19,'06:45:00','08:03:38',2,3,1);
INSERT INTO Recorrido VALUES(NULL,'2013-05-01',16,'06:50:00','07:57:29',2,3,1);
INSERT INTO Recorrido VALUES(NULL,'2013-05-14',32,'16:05:00','16:59:28',3,2,1);
INSERT INTO Recorrido VALUES(NULL,'2013-05-14',22,'16:30:00','17:37:39',3,2,1);
INSERT INTO Recorrido VALUES(NULL,'2013-06-12',21,'13:00:00','13:32:12',3,4,1);
INSERT INTO Recorrido VALUES(NULL,'2013-06-12',21,'16:00:00','16:29:54',3,4,1);
INSERT INTO Recorrido VALUES(NULL,'2013-07-31',32,'07:00:00','08:24:23',2,3,1);
INSERT INTO Recorrido VALUES(NULL,'2013-07-31',49,'13:00:00','13:57:04',3,2,1);

#### CONDUCTOR_BUS_RECORRIDO ########
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,1,1);
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,1,4);
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,3,2);
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,2,7);
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,5,8);
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,3,1);
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,9,8);
INSERT INTO Conductor_Bus_Recorrido VALUES (NULL,10,11);

SELECT * FROM Recorrido;
SELECT * FROM Conductor_Bus_Recorrido;




#Select * from Administrador;
#Select * from Unidad;
#Select * from Conductor;