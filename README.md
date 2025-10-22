# RETO-05-POO
## Reto 5: 
1. Create a package with all code of class *Shape*, this exersice should be conducted in two ways:
 - A unique module inside of package *Shape*
 - Individual modules that import *Shape* in inheritates from it.

## Unico modulo

 - El codigo se sube de manera que ahora puede ser usado como paquete
   
```
shape/
├── __init__.py
└── Ejercicio_Clase.py
```

## Sub division en varios modulos

 - Primero se subdivide el codigo para en caso de ser necesario poder traer una unica clase de interes 
 - Luego se une todo en la misma carpeta para ser usado como paquete
   
```
modules/
│
├── __init__.py
├── PointLine.py
├── shape.py
├── rectangle.py
├── square.py
├── triangle.py
└── typeTriangle.py
```
