## hacer no visible ciertos atreibutos o metodos de una clase
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) 
# las clases son plantillas para crear objetos (instancias)
#    
#__ es un mecanismo para restringir el acceso a ciertos componentes de un objeto.

#ENCAPSULAMIENTO EN POO CON PYTHON
class Usuario:
    
    __usuario_email = 'admin@gmail.com'
    __usuario_password = '123'
    
    def __ini__(self):
        pass
    
    def login(self,email,password):
        if email == self.__usuario_email and password == self.__usuario_password:
            print('Login exitoso')
        else:
            print('Login fallido')
            
print("LOGIN DE USUARIO")
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')

usuario = Usuario()
print(usuario.usuario_password)
usuario.login(email, password)