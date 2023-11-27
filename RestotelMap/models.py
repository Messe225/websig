from django.contrib.gis.db import models
# Create your models here.
class Catego(models.Model):
    libelle = models.CharField(verbose_name ="Libellé", unique=True, max_length=100)

    class Meta: 
     verbose_name_plural = "Catégories"
    
    def _str_(self):
        return self.libelle
    
class Local(models.Model):
    ville = models.CharField(verbose_name ="Ville", unique=True, null=True,blank=True, max_length=100)
    commune = models.CharField(verbose_name ="Commune",null=True,blank=True, max_length=100)
    quartier = models.CharField(verbose_name ="Quartier",null=True,blank=True, max_length=100)

    class Meta: 
     verbose_name_plural = "Localisation"
    
    def _str_(self):
        return self.ville
    
class Etabl(models.Model):
    nom = models.CharField(verbose_name ="Nom", max_length=100)
    catego = models.ForeignKey(Catego, verbose_name="Catégorie", on_delete=models.CASCADE)
    telephone = models.CharField(verbose_name ="Téléphone",null=True,blank=True, max_length=100)
    local = models.ForeignKey(Local, verbose_name="Localisation", null=True,blank=True, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name ="Latitude")  
    longitude = models.FloatField(verbose_name ="Longitude") 
    geom = models.MultiPointField(srid=4326) 

    class Meta: 
     verbose_name_plural = "Etablissement"
    
    def _str_(self):
        return self.nom

class Appartenir(models.Model):
    etab = catego = models.ForeignKey(Etabl, verbose_name= "Etablissement", on_delete=models.CASCADE)
    catego =  models.ForeignKey(Catego, verbose_name= "Catégorie", on_delete=models.CASCADE)
   
    class Meta: 
     verbose_name_plural = "Service"
    
    def _str_(self):
        return self.etablissement