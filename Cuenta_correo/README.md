# Cuenta de Correo en Python

Este proyecto es una implementación simple de una clase en Python que representa una cuenta de correo electrónico.

## Descripción

La clase CuentaCorreo permite gestionar una cuenta de correo, encapsulando la contraseña y controlando su acceso mediante propiedades. También incluye validaciones básicas para mejorar la seguridad de los datos.

## Funcionalidades

* Encapsulamiento de la contraseña
* Uso de propiedades (@property, setter y deleter)
* Validación de longitud mínima de la contraseña
* Eliminación controlada de la contraseña

## Tecnologías

* Python

## Ejemplo de uso

Python
c = CuentaCorreo("correo@mail.com", "123456")
print(c.contrasena)

c.contrasena = "abcdef"
print(c.contrasena)

del c.contrasena


## Aprendizajes

Este proyecto fue desarrollado para practicar conceptos de:

* Programación orientada a objetos (POO)
* Encapsulamiento de datos
* Uso de getters y setters en Python
* Validación de atributos
