create database prueba2;
use prueba2;
create table clientes( id_cliente INT primary key, nombre_cliente varchar(500), ciudad varchar(500), email varchar(500));
create table ventas (id_venta int primary key, fecha_venta varchar(500), id_cliente int, id_producto int, cantidad int, precio_unitario int, vanta_total int);
create table productos (id_producto int primary key, nombre_producto varchar (500), categoria varchar(500), precio int);

/*creación llaves foraneas*/
alter table ventas add foreign key(id_cliente) references clientes(id_cliente);
alter table ventas add foreign key(id_producto) references productos(id_producto);

alter table ventas change vanta_total total_venta varchar(500);

/*select * from clientes;*/
/*select * from productos;*/
/*select * from ventas;*/

/*CONSULTAS*/
/*Top 5 productos más vendidos.*/
SELECT p.id_producto, p.nombre_producto, SUM(v.cantidad) AS total_vendido
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.id_producto
ORDER BY total_vendido DESC
LIMIT 5;

/*CANTIDAD DE VENTAS POR MES*/
SELECT
    YEAR(STR_TO_DATE(v.fecha_venta, '%Y-%m-%d')) AS anio,
    MONTH(STR_TO_DATE(v.fecha_venta, '%Y-%m-%d')) AS mes,
    SUM(v.total_venta) AS total_ventas
FROM ventas v
GROUP BY anio, mes
ORDER BY anio DESC, mes DESC;
