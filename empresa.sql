drop database empresa;
/*CREACION DE LA BD 28-11-21*/
create database empresa;

use empresa;

/****CREACION DE TABLAS****/
create table if not exists proveedor(
	id_proveedor int not null auto_increment,
	nombre varchar(50),
    direccion varchar(45),
    primary key (id_proveedor)
);

create table productos(
	codigo int not null auto_increment,
    nombre varchar(50),
    precio float,
    id_proveedor int,
    primary key (codigo),
    constraint fk_productos_proveedor foreign key (id_proveedor) references proveedor(id_proveedor)
);

create table cliente(
	dni int not null,
    nombre varchar(45) not null,
    fechaNac date,
    telefono varchar(9) unique not null,
    primary key (dni)
);


create table cliente_producto(
	cliente_dni int,
    producto_codigo int,
    primary key (cliente_dni, producto_codigo),
    foreign key (cliente_dni) references cliente(dni),
    foreign key (producto_codigo) references productos(codigo)
);

/*INSERTAR DATOS*/

/*tabla proveedor*/
insert into proveedor (nombre,direccion) values ('banquetera_ale','santiago 469');
insert into proveedor (nombre,direccion) values ('elpinis_banquetera','Valparaiso 555');
insert into proveedor (nombre,direccion) values ('banquetera_losfallos','san antonio 6969');

/*tabla productos*/
insert into productos (nombre,precio,id_proveedor) values ('jamon a lo pobre',60100,1);
insert into productos (nombre,precio,id_proveedor) values ('filete ahumado',33999,2);
insert into productos (nombre,precio,id_proveedor) values ('bistec a lo rico',20100,3);
insert into productos (nombre,precio,id_proveedor) values ('papas con pure',10990,3);

/*insertar cliente*/
insert into cliente (dni,nombre,fechaNac,telefono) values (181633220,'ricardo','1992-12-24',961558125);

/*CONSULTAS*/
select * from cliente;




