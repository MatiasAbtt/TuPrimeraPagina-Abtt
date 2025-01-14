from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    bio = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

class Post(models.Model):
    titulo = models.CharField(max_length=20)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
