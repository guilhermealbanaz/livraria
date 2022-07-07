from django.db import models

class Categoria(models.Model):
    description = models.CharField(max_length=100)

class Editora(models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return self.name.capitalize()

class Livro(models.Model):
    titulo = models.CharField(max_length=255)   
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_length=7, decimal_places=2)
    categoria = models.ForeignKey()