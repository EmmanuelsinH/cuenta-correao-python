
class CuentaCorreo:
    def __init__(self, email, contrasena):
        if "@" not in email:
            raise ValueError("Email inválido")
        self._email = email
        self._contrasena = contrasena

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        if len(nueva_contrasena) >= 6:
            self._contrasena = nueva_contrasena
        else:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")

    @contrasena.deleter
    def contrasena(self):
        print("Contraseña eliminada")
        del self._contrasena


# Uso
c = CuentaCorreo("correo@mail.com", "123456")
print(c.contrasena)
c.contrasena = "abcdef"
print(c.contrasena)
del c.contrasena
