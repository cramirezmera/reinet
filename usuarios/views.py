# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import *
from django.contrib.auth.forms import UserCreationForm
from models import *
from django.contrib.auth.decorators import login_required

def index(request):
	return render_to_response('USUARIO_index.html')

def ingresar(request):
	c={}
	c.update(csrf(request))
	return render_to_response('USUARIO_sign-in.html',c)

def auth_view(request):
	name=request.POST.get('Email', '')
	password=request.POST.get('password', '')
	user=auth.authenticate(username=name, password=password)
		
	if user is not None:
		auth.login(request, user)
		request.session['id_user']=request.user.id
		personas=Persona.objects.raw('SELECT * FROM persona WHERE user_ptr_id =%s',request.user.id)
		p=personas[0]
		request.session['id_persona']=p.idpersona
		#print p.idpersona
		return HttpResponseRedirect('/perfil')
	else:
		return HttpResponseRedirect('/invalid')
	
def loggedin(request):
	print request.session['id_user']
	return render_to_response('USUARIO_profile.html', {'full_name': request.user.username})
	
def invalid(request):
	return render_to_response('invalid.html')

def logout(request):
	auth.logout(request)
	print "LA VARIABLE DE SESSION LOGOUT", request.session['id_user']
	return render_to_response('USUARIO_index.html')

def register(request):
	if request.method=='POST':
		form=PersonaForm(request.POST)
	
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ingresar/')
		else:
			print form.is_valid()
	else:
		form=PersonaForm()

	args={}
	args.update(csrf(request))
	for f in form:
		print f.id_for_label
	args['form']=form
	return render_to_response('USUARIO_sign-up.html', args)

def register_success(request):
	return render_to_response('USUARIO_index.html')
	
def create(request):
	if request.POST:
		form=UsuarioForm2(request.POST)
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/usuarios/all')
	
	else:
		form=UsuarioForm2()
	
	args={}
	args.update(csrf(request))
	args['form']= form
	return render_to_response('USUARIO_sign-up.html', args)

@login_required(login_url='/ingresar/')
def perfil_view(request):
	id_session=request.session['id_user']
	
	id_persona=request.session['id_persona']
	print id_session, id_persona
	user1=User.objects.get(id=id_session)
	#personas=Persona.objects.raw('SELECT * FROM persona WHERE user_id=%s',id_session)
	#p=personas[0]
	#request.session['id_persona']=p.idpersona
	#print request.session['id_persona']
	#print personas[0].idpersona
	args={}
	args['usuario']=user1
	persona=Persona.objects.get(idpersona=id_persona)
	args['persona']=persona
	return render_to_response('USUARIO_profile.html',args)

@login_required(login_url='/ingresar/')
def mensajes_view(request):
	return render_to_response('USUARIO_inbox.html')


def inicio_view(request):
	return render_to_response('USUARIO_inicio.html')
