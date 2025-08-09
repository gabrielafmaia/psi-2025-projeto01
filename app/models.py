from django.db import models

class Site(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.FileField(upload_to='logo/')
    copyright = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Inicio(models.Model):
    titulo_apresentacao = models.CharField(max_length=50)
    subtitulo_apresentacao = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banner-inicio/')
    titulo_conteudo = models.CharField(max_length=100)
    subtitulo_conteudo = models.CharField(max_length=50)
    texto = models.TextField()
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.titulo_apresentacao

class Elenco(models.Model):
    titulo_apresentacao = models.CharField(max_length=50)
    subtitulo_apresentacao = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banner-elenco/')

    def __str__(self):
        return self.titulo_apresentacao

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    personagem = models.CharField(max_length=100)
    idade = models.IntegerField()
    local_nascimento = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Atores"

class Sobre(models.Model):
    titulo_apresentacao = models.CharField(max_length=50)
    subtitulo_apresentacao = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banner-sobre/')
    titulo_conteudo = models.CharField(max_length=100)
    subtitulo_conteudo = models.CharField(max_length=50)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='imagem/')

    def __str__(self):
        return self.titulo_apresentacao