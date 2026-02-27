from django.db import models

class Todolist(models.Model):
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.designation

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom