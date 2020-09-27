class Webinar:
	"""docstring for Zoom"""
	def __init__(self, nombre, tipo_de_aplicacion, informacion, descargar_celular, descargar_computadora, navegador):
		self.nombre = nombre
		self.tipo_de_aplicacion = tipo_de_aplicacion
		self.informacion = informacion
		self.descargar_celular = descargar_celular
		self.descargar_computadora = descargar_computadora
		self.navegador = navegador
	
	def crear_cuenta(self):
		print('Intrucciones para crear una cuenta')

	def loguearse(self):
		print('Instrucciones para loguearse')

	def entrar_reunion():
		print('Instrucciones para entrar a una reunión')

def datos(palabra_clave = ''):
	if palabra_clave.lower() == 'zoom':
		return('Zoom', 'Webinar', 'aplicación para realizar reuniones virtuales', True, True, False)
	elif palabra_clave.lower() == 'googlemeet' or palabra_clave.lower() == 'meet' or palabra_clave.lower() == 'google meet':
		return('Google Meet', 'Webinar', 'aplicación para realizar reuniones virtuales', True, False, True)
	elif palabra_clave.lower() == 'jistmeet' or palabra_clave.lower() == 'jist meet' or palabra_clave.lower() == 'jist':
		return('Jist Meet', 'Webinar', 'aplicación para realizar reuniones virtuales', True, False, True)


def analisis_pregunta_usuario(pregunta_usuario):
	for palabra in pregunta_usuario.split():
		if palabra == 
def saludos():
	return 'Hola soy TITO. ¿Cómo te puedo ayudar?'

#----> Programa principal <----

respuesta = 'none'
print(saludos())
while respuesta.lower() != 'chau':
	respuesta = input('Vos:  ')
	analisis_pregunta_usuario(respuesta)














