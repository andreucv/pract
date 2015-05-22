from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
import json

class Comentario(models.Model):
	tecnico = models.ForeignKey(User)
	texto = models.CharField(max_length=500)
	fechahora = models.DateTimeField()

	def __str__(self):
		return str(self.id)

	@classmethod
	def create(cls, tecnico, texto, fechahora):
		ticket = cls(tecnico=tecnico, texto=texto, fechahora=fechahora)
		return ticket

class Prioridad(models.Model):
	nombre = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre

class Estado(models.Model):
	nombre = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre

class Ticket(models.Model):
	creador = models.ForeignKey(User, related_name='creador')
	titulo = models.CharField(max_length=20)
	texto = models.CharField(max_length=500)
	fechahora = models.DateTimeField()
	asignado = models.ForeignKey(User, related_name='asignado')

	prioridad = models.ForeignKey(Prioridad)
	estado = models.ForeignKey(Estado)

	comentarios = models.ManyToManyField(Comentario)
	
	def __str__(self):
		return str(self.id)

	@classmethod
	def create(cls, creador, titulo, texto, fechahora, asignado, prioridad, estado):
		ticket = cls(creador=creador, titulo=titulo, texto=texto, fechahora=fechahora, asignado=asignado, prioridad=prioridad, estado=estado)
		return ticket

class Idioma(models.Model):
	idioma = models.CharField(max_length=30, primary_key=True)
	titulo = models.CharField(max_length=40)
	registro = models.CharField(max_length=40)
	ayuda = models.CharField(max_length=40)
	nombreusuario = models.CharField(max_length=40)
	contrasena = models.CharField(max_length=40)
	entra = models.CharField(max_length=40)
	actualizar = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	confirmaemail = models.CharField(max_length=40)
	nombre = models.CharField(max_length=40)
	apellido = models.CharField(max_length=40)
	nuevaincidencia = models.CharField(max_length=400)
	tituloincidencia = models.CharField(max_length=400)
	cuerpoincidencia = models.CharField(max_length=400)
	comentarioHora = models.CharField(max_length=20)
	enviar = models.CharField(max_length=400)
	salir = models.CharField(max_length=400)
	asignar = models.CharField(max_length=40)
	buscar = models.CharField(max_length=40)
	prioridad = models.CharField(max_length=40)
	estado = models.CharField(max_length=40)
	comentarios = models.CharField(max_length=40)
	nuevoComentario = models.CharField(max_length=40)
	ticketscreados = models.CharField(max_length=400)
	ticketsasignados = models.CharField(max_length=400)
	ticketsbuscados = models.CharField(max_length=40)
	cambiaridioma = models.CharField(max_length=400)
	buscaincidencia = models.CharField(max_length=40)
	bienvenida = models.CharField(max_length=200)
	subbienvenida = models.CharField(max_length=100)
	nombreempresa = models.CharField(max_length=100)
	eNoHayTickets = models.CharField(max_length=400)
	eYaExisteUsuario = models.CharField(max_length=400)
	emailSr = models.CharField(max_length=10)
	emailNombreCompleto = models.CharField(max_length=20)
	emailNombreUsuario = models.CharField(max_length=20)
	emailTicketId = models.CharField(max_length=50)
	emailTicketModificado = models.CharField(max_length=50)
	emailTicketEstado = models.CharField(max_length=50)
	emailTicketAsignado = models.CharField(max_length=50)
	emailTicketNuevo = models.CharField(max_length=50)
	emailTicketComentarios = models.CharField(max_length=50)
	emailTicketFinalizado = models.CharField(max_length=50)
	tituloEmailRegistro = models.CharField(max_length=50)
	graciasEmailRegistro = models.CharField(max_length=50)
	tituloEmailPost = models.CharField(max_length=50)

class IdiomaAdmin(admin.ModelAdmin):
	list_display = ('idioma', 'titulo', 'registro', 'ayuda', 'nombreusuario', 'contrasena', 'entra', 'confirmaemail', 
					'nombre', 'apellido', 'eNoHayTickets', 'nuevaincidencia', 'tituloincidencia', 'cuerpoincidencia',
					'enviar', 'salir', 'buscar', 'ticketscreados', 'ticketsasignados', 'ticketsbuscados', 'cambiaridioma', 'bienvenida',
					'subbienvenida', 'buscaincidencia', 'nombreempresa', 'email', 'actualizar', 'asignar', 'prioridad', 
					'estado', 'comentarios', 'emailSr', 'emailNombreCompleto', 'emailNombreUsuario', 'tituloEmailRegistro', 
					'graciasEmailRegistro', 'tituloEmailPost', 'comentarioHora', 'emailTicketId', 'emailTicketModificado', 
					'emailTicketEstado', 'emailTicketAsignado', 'emailTicketNuevo', 'emailTicketComentarios', 'emailTicketFinalizado', 'nuevoComentario')
	list_editable = ('titulo', 'registro', 'ayuda', 'nombreusuario', 'contrasena', 'entra', 'confirmaemail', 
					'nombre', 'apellido', 'eNoHayTickets', 'nuevaincidencia', 'tituloincidencia', 'cuerpoincidencia',
					'enviar', 'salir', 'buscar', 'ticketscreados', 'ticketsasignados', 'ticketsbuscados', 'cambiaridioma', 'bienvenida',
					'subbienvenida', 'buscaincidencia', 'nombreempresa', 'email', 'actualizar', 'asignar', 'prioridad', 
					'estado', 'comentarios', 'emailSr', 'emailNombreCompleto', 'emailNombreUsuario', 'tituloEmailRegistro', 
					'graciasEmailRegistro', 'tituloEmailPost', 'comentarioHora', 'emailTicketId', 'emailTicketModificado', 
					'emailTicketEstado', 'emailTicketAsignado', 'emailTicketNuevo', 'emailTicketComentarios', 'emailTicketFinalizado', 'nuevoComentario')