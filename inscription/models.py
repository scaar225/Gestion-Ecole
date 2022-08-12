from django.db import models
# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.IntegerField()
    classe = models.CharField(max_length=50)
    
    def __str__(self) -> str:
    	 return self.nom +"  "+ self.prenom
    

    