from django.db import models

class Site(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.FileField(upload_to='logos/')
    copyright = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Inicio(models.Model):
    titulo_apresentacao = models.CharField(max_length=50)
    subtitulo_apresentacao = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banners-inicio/')
    titulo_conteudo = models.CharField(max_length=50)
    subtitulo_conteudo = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return self.titulo_apresentacao
    
class CarrosselItem(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='imagens-carrossel/')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Itens do Carrossel"

class Elenco(models.Model):
    titulo_apresentacao = models.CharField(max_length=50)
    subtitulo_apresentacao = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banners-elenco/')

    def __str__(self):
        return self.titulo_apresentacao

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    personagem = models.CharField(max_length=100)
    idade = models.IntegerField()
    local_nascimento = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens-cast/')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Atores"

class Sobre(models.Model):
    titulo_apresentacao = models.CharField(max_length=50)
    subtitulo_apresentacao = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banners-sobre/')
    svg = models.FileField(upload_to='svgs/')

    def __str__(self):
        return self.titulo_apresentacao

class SecaoSobre(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100, blank=True)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Seções do Sobre"