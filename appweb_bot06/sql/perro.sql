CREATE DATABASE perro;

USE perro;

CREATE TABLE perro(
    numero int NOT NULL PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    pais varchar(30) NOT NULL,
    caracteristicas varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO perro (numero, nombre, pais, caracteristicas) VALUES 
 (1, 'Cervi', 'Francia','Raza: Pitbull color negro/blanco es juguetona'),
(2, 'Laska', 'Uruguay','Raza:Rotwailer color negro/cafe'),
(3, 'Canelo', 'España','Raza: delmon color cafe es muy grande');

SHOW TABLES;
DESCRIBE perro;

SELECT * FROM perro;

CREATE USER 'perron'@'localhost' IDENTIFIED BY 'perron.2019';
GRANT ALL PRIVILEGES ON perro.* TO 'perron'@'localhost';
FLUSH PRIVILEGES;
