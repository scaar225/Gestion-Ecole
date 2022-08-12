""" Ce module contient l'ensemble des formulaire du projet """
from django.forms import ModelForm

from inscription.models import Etudiant


class InscriptionForms(ModelForm):
    """ formulaire d'inscription """
    class Meta: # pylint: disable = missing-docstring

        model = Etudiant
        # fields = ('nom','prenom')
        fields = '__all__'
