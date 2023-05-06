from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titre': 'Classe 11',
            'description':'Entrez une courte description de la classe',
            'image':''
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'titulli', 'klasa', 'pershkrimi', 'imazhi_lendes']
        help_texts = {
            'titre': 'Psh. Matematika, Gjeografi etj',
            'description':'Vendos nje pershkrim te shkurte te lendes',
            'klasa':'Zhgjidhni klasen per te cilen do te krijoni lenden',
            'imazhi_lendes':'Mund te vendosesh nje fotografi e lendes ose mund te lihet bosh'
        }
        labels = {
            'titulli':'Titulli i lendes'
        }
        widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','titulli', 'lenda', 'video_id', 'pozicioni', ]
        help_texts = {
            'titre':'Entrez le titre de la leçon',
            'lenda':'Choisissez le sujet auquel appartient cette leçon',
            'video_id':'',
            'pozicioni':'Saisir le numéro de position ou la séquence dapprentissage '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }