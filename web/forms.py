#encoding:utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from web.models import *
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
	idioma = 'Espanol'

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

	def __init__(self, *args, **kwargs):
		idioma = kwargs.pop('language')
		super(UserForm, self).__init__(*args, **kwargs)
		nombreusuario = Idioma.objects.values_list('idioma', 'nombreusuario').filter(idioma=idioma)[0][1]
		self.fields['username'].widget=forms.TextInput(attrs={'placeholder' : nombreusuario})
		self.fields['username'].label=nombreusuario
		self.fields['username'].help_text = ''
		password = Idioma.objects.values_list('idioma', 'contrasena').filter(idioma=idioma)[0][1]
		self.fields['password'].widget=forms.PasswordInput(attrs={'placeholder' : password})
		self.fields['password'].label=password
		email = Idioma.objects.values_list('idioma', 'email').filter(idioma=idioma)[0][1]
		self.fields['email'].widget=forms.TextInput(attrs={'placeholder' : email})
		self.fields['email'].label=email
		first_name = Idioma.objects.values_list('idioma', 'nombre').filter(idioma=idioma)[0][1]
		self.fields['first_name'].widget=forms.TextInput(attrs={'placeholder' : first_name})
		self.fields['first_name'].label = first_name
		last_name = Idioma.objects.values_list('idioma', 'apellido').filter(idioma=idioma)[0][1]
		self.fields['last_name'].widget=forms.TextInput(attrs={'placeholder' : last_name})
		self.fields['last_name'].label=last_name

class GroupForm(forms.ModelForm):
	name = forms.ModelChoiceField(required=True, queryset=Group.objects.all(), label='Grupo')
	class Meta:
		model = Group
		fields = ('name',)

	def clean(self):
		group = self.cleaned_data.get('name')
		if not group:
			raise forms.ValidationError('Choose a group')