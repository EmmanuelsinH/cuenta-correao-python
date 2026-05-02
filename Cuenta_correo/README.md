# CuentaCorreo (Python)

Proyecto simple en Python que implementa una clase para representar una cuenta de correo electrónico con encapsulamiento de contraseña.

---

## Descripción

Este proyecto demuestra conceptos básicos de Programación Orientada a Objetos (POO) en Python, enfocándose en:

- Encapsulamiento de atributos
- Uso de propiedades (`@property`, setter y deleter)
- Validación de datos
- Control de acceso a atributos sensibles

---

## Funcionalidades

- Crear una cuenta con email y contraseña
- Validar longitud mínima de la contraseña
- Modificar la contraseña de forma controlada
- Eliminar la contraseña de manera segura

---

## Ejemplo de uso

```python
c = CuentaCorreo("correo@mail.com", "123456")
print(c.contrasena)

c.contrasena = "abcdef"
print(c.contrasena)

del c.contrasena
```

---

## Objetivo del proyecto

Practicar conceptos fundamentales de POO en Python aplicados a un caso sencillo pero realista de manejo de datos sensibles.

---

## Tecnologías

- Python 3
