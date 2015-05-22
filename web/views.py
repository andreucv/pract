from django.shortcuts import render, redirect
from web.models import *
from web.forms import *
from web.urls import *
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django import template
import logging
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.db.models import Q

logger = logging.getLogger(__name__)

def loginApp(request):
	if 'idioma' in request.session: idiomaPk = request.session['idioma']
	else: idiomaPk = 'Espanol'

	if request.method == 'POST':
		form = forms.AuthenticationForm(data=request.POST, request=request)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return home(request)
		context = {'languages' : Idioma.objects.all(),
				   'idioma' : Idioma.objects.get(pk=idiomaPk),
				   'loginform' : form}
		return render(request, 'web/login.html', context)
	else:
		context = {'loginform' : forms.AuthenticationForm(None),
				   'languages' : Idioma.objects.all(),
				   'idioma' : Idioma.objects.get(pk=idiomaPk)}
		return render(request, 'web/login.html', context)

def logoutApp(request):
	logout(request)
	return home(request)

def createUser(request):
	if 'idioma' in request.session: idiomaPk = request.session['idioma']
	else: idiomaPk = 'Espanol'
	if request.method == 'POST':
		form = UserForm(request.POST, language=idiomaPk)
		form2 = GroupForm(request.POST)
		if form.is_valid() and form2.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			firstname = form.cleaned_data['first_name']
			lastname = form.cleaned_data['last_name']
			group = form2.cleaned_data['name']
			user = User.objects.create_user(username, email, password)
			user.first_name = firstname
			user.last_name = lastname
			user.save()
			user.groups.add(group)
			userIn = authenticate(username = username, password = password)
			login(request, userIn)
			context = Context({'idioma': Idioma.objects.get(pk=idiomaPk),
							   'user': user})
			sendEmail(user, 'register', context)
			return home(request)
		else: 
			context = {'languages' : Idioma.objects.all(),
				       'idioma' : Idioma.objects.get(pk=idiomaPk),
				   	   'userform' : form, 
					   'groupform' : form2}
			return render(request, 'web/create.html', context)
	else:
		context = {'languages' : Idioma.objects.all(),
				   'idioma' : Idioma.objects.get(pk=idiomaPk),
				   'userform' : UserForm(None, language=idiomaPk),
				   'groupform' : GroupForm()}
		return render(request, 'web/create.html', context)

@login_required(login_url='http://127.0.0.1:8000/web/login/')
def home(request):
	if 'idioma' in request.session: idiomaPk = request.session['idioma']
	else: idiomaPk = 'Espanol'
	tecnicos = Group.objects.get(name='Administrador').user_set.all()
	admins = Group.objects.get(name='Tecnico').user_set.all()
	context = { 'ownTickets' : Ticket.objects.filter(creador=request.user).exclude(estado=Estado.objects.get(pk=4)), 
				'assignedTickets' : Ticket.objects.filter(asignado=request.user).exclude(estado=Estado.objects.get(pk=4)),
				'prioridades' : Prioridad.objects.all(),
				'estados' : Estado.objects.all(),
				'tecnicos' : tecnicos | admins,
				'isAdmin' : not(request.user.groups.filter(name='Client').exists()), 
				'languages' : Idioma.objects.all(),
				'idioma' : Idioma.objects.get(pk=idiomaPk)}
	return render(request, 'web/index.html', context)

@login_required(login_url='http://127.0.0.1:8000/web/login/')
def user(request):
	context = {'languages' : Idioma.objects.all()}
	return render(request, 'web/user.html')

def postTicket(request):
	if 'idioma' in request.session: idiomaPk = request.session['idioma']
	else: idiomaPk = 'Espanol'
	if request.method == 'POST':
		fechahora = timezone.now()
		prioridad = request.POST['prioridad']
		prioridad = Prioridad.objects.get(pk=prioridad)
		titulo = request.POST['titulo']
		texto = request.POST['texto']
		creador = request.user

		indexAdmin = int(fechahora.strftime("%s")) % Group.objects.get(name='Administrador').user_set.count()
		asignado = Group.objects.get(name='Administrador').user_set.all()[indexAdmin]

		estado = Estado.objects.get(pk=1)
		ticket = Ticket.create(creador, titulo, texto, fechahora, asignado, prioridad, estado)
		if titulo and texto:
			if ticket is not None:
				ticket.save()
				context = Context({'idioma':Idioma.objects.get(pk=idiomaPk),
								   'user': request.user,
								   'ticket': ticket})
				sendEmail(request.user, 'postNewTicket', context)
				return home(request)
		else: return home(request)
	else: return home(request)

def postComment(request):
	if 'idioma' in request.session: idiomaPk = request.session['idioma']
	else: idiomaPk = 'Espanol'
	if request.method == 'POST':
		fechahora = timezone.now()
		texto = request.POST['comment']
		tecnico = request.user
		ticket = Ticket.objects.get(pk=request.POST['ticket'])
		comentario = Comentario.create(tecnico, texto, fechahora)

		if comentario is not None:
			comentario.save()
			ticket.comentarios.add(comentario)
			context = Context({'idioma':Idioma.objects.get(pk=idiomaPk),
							   'user': request.user,
							   'ticket': ticket})
			sendEmail(request.user, 'postNewComment', context)
			return home(request)

def searchTicket(request):
	if 'idioma' in request.session: idiomaPk = request.session['idioma']
	else: idiomaPk = 'Espanol'
	if request.method == 'POST':
		words = request.POST['words']
		if words:
			tickets = Ticket.objects.filter(reduce(lambda x, y: x | y, [Q(texto__contains=word) for word in words]))
			if 'all' in words: tickets = Ticket.objects.all()
			tecnicos = Group.objects.get(name='Administrador').user_set.all()
			admins = Group.objects.get(name='Tecnico').user_set.all()
			context = { 'ownTickets' : Ticket.objects.filter(creador=request.user).exclude(estado=Estado.objects.get(pk=4)), 
						'assignedTickets' : Ticket.objects.filter(asignado=request.user).exclude(estado=Estado.objects.get(pk=4)),
						'searchedTickets' : tickets,
						'prioridades' : Prioridad.objects.all(),
						'estados' : Estado.objects.all(),
						'tecnicos' : tecnicos | admins,
						'isAdmin' : not(request.user.groups.filter(name='Client').exists()), 
						'languages' : Idioma.objects.all(),
						'idioma' : Idioma.objects.get(pk=idiomaPk)}
			return render(request, 'web/index.html', context)
	return home(request)

def deleteTicket(request):
	if request.method == 'POST':
		ticket = Ticket.objects.get(pk=request.POST['ticket'])
		ticket.delete()
		return home(request)

def deleteComment(request):
	if request.method == 'POST':
		comment = Comentario.objects.get(pk=request.POST['comment'])
		comment.delete()
		return home(request)

def updateTicket(request):
	if 'idioma' in request.session: idiomaPk = request.session['idioma']
	else: idiomaPk = 'Espanol'
	if request.method == 'POST':
		ticket = Ticket.objects.get(pk=request.POST['ticket'])
		ticket.prioridad = Prioridad.objects.get(pk=request.POST['prioridad'])
		ticket.asignado = User.objects.get(username=request.POST['tecnico'])
		ticket.estado = Estado.objects.get(pk=request.POST['estado'])
		contextUpdate = Context({'idioma' : Idioma.objects.get(pk=idiomaPk),
						   		 'user' : request.user,
						   		 'ticket': ticket})
		if ticket.estado.pk == 4:
			sendEmail(ticket.creador, 'finalizedTicket', contextUpdate) 
		else:
			sendEmail(ticket.creador, 'updateTicket', contextUpdate)
			contextUpdate = Context({'idioma' : Idioma.objects.get(pk=idiomaPk),
							   		 'user' : ticket.asignado,
							   		 'ticket': ticket})
			sendEmail(ticket.asignado, 'newTicket', contextUpdate)
		ticket.save()
		return home(request)

def sendEmail(user, email_template, context):
	emailTexto = get_template('emails/'+email_template+'.txt')
	emailHtml = get_template('emails/'+email_template+'.html')

	emailTexto = emailTexto.render(context)
	emailHtml = emailHtml.render(context)

	msg = EmailMultiAlternatives('CAU Fabrica SL', emailTexto, 'infocaufabrica@gmail.com', [user.email])
	msg.attach_alternative(emailHtml, "text/html")
	msg.send()

def changeLanguage(request):
	if request.method == 'GET':
		request.session['idioma'] = request.GET['language']
		return redirect(request.GET['redirect'])
	else:
		return redirect(request.GET['redirect'])
