""" Ce module contient l'ensemble des formulaire du projet """
from django.forms import ModelForm
from django import forms
from inscription.models import Etudiant


class InscriptionForms(ModelForm):
    """ formulaire d'inscription """
    class Meta: # pylint: disable = missing-docstring

        model = Etudiant
        fields = ('nom','prenom','age','classe')
        # = '__all__'
        
    
        widgets = {
		"nom":  forms.TextInput(attrs={'class': 'form-control'}),
		"prenom":  forms.TextInput(attrs={'class': 'form-control'}),
		"age":  forms.TextInput(attrs={'class': 'form-control'}),
		"classe":  forms.TextInput(attrs={'class': 'form-control'}),
		}
        
    def clean_nom(self):
        nom = self.cleaned_data['nom']
        if not nom:
            raise forms.ValidationError('Ce champ est requis')
        return nom 
    
    def  clean_age(self):
        age = self.cleaned_data['age']
        if not age:
            raise forms.ValidationError('Ce champ est requis')
        age = str(age)
        if not age.isnumeric():
            raise forms.ValidationError('l\'age doit etre un nombre')
        return age
    
        
    def  clean_prenom(self):
        prenom = self.cleaned_data['prenom']
        if not prenom:
            raise forms.ValidationError('Ce champ est requis')
        return prenom
    
        
    def  clean_classe(self):
        classe = self.cleaned_data['classe']
        if not classe:
            raise forms.ValidationError('Ce champ est requis')
        return classe 
 

    