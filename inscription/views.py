from django.shortcuts import render
from inscription.models import Etudiant
from inscription.forms import InscriptionForms

# Create your views here.
def acceuil(request):
    return render(request, 'acceuil.html')


def liste(request):
    liste_Etudiant = Etudiant.objects.all()
    return render(request,'liste.html',{'liste_Etudiant':liste_Etudiant })

def ajout(request):
    inscription = InscriptionForms()
    if request.method=="POST":
        inscription=InscriptionForms(request.POST)
    context = {'inscription':inscription}
    

    return render(request,'ajout.html', context)
