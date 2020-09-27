#Funciones para las plataformas de los webinars:
def instrucciones_zoom(palabra_clave):
#	print('Acá estarán las instrucciones para usar Zoom')
	if palabra_clave.lower() == 'zoom':
		return '¿Qué tenes que hacer en Zoom?'

def instrucciones_jistmeet(palabra_clave):
#	print('Acá estarán las instrucciones para usar Jitsmeet')
	if palabra_clave.lower() == 'jitsmeet' or palabra_clave.lower() == 'jits meet':
		return '¿Qué tenes que hacer en JistMeet?'

def instrucciones_googlemeet(palabra_clave):
	print('Acá estarán las instrucciones para usar Google Meet')
	if palabra_clave.lower() == 'zoom':
		return '¿Qué tenes que hacer en Zoom?'
#Funciones para las plataformas educativas:
def instrucciones_google_classroom(palabra_clave):
	print('Acá estarán las instrucciones para usar Google Classroom')

def instrucciones_edmodo(palabra_clave):
	print('Acá estarán las instrucciones para usar EdModo')

def instrucciones_moodle(palabra_clave):
	print('Acá estarán las instrucciones para usar Moodle')

#Funciones de interaccion
def saludos_y_demas(palabra_clave):
#	print('Acá estan los saludos y demás')
	if palabra_clave == 'saludo':
		return 'Hola, soy Tito. ¿Cómo te puedo ayudar?'

#----> Programa principal <----

respuesta = 'none'

print(saludos_y_demas('saludo'))

while respuesta.lower() != 'chau':
	#llamo a las funciones y analisan la respuesta
	respuesta = input('Vos:  ')
	instrucciones_zoom(respuesta)
	instrucciones_jistmeet(respuesta)
	instrucciones_googlemeet(respuesta)
	instrucciones_moodle(respuesta)
	instrucciones_edmodo(respuesta)
	instrucciones_google_classroom(respuesta)






