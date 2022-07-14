from django.db import models

class Categoria(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

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

    class Meta:
        verbose_name_plural = "Autores"

class Livro(models.Model):
    titulo = models.CharField(max_length=255)   
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")

    def __str__(self):
        return f'{self.titulo} ({self.quantidade})'


