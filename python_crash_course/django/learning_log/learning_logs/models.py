from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Um tópico sobre o que o usuário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Retorna um string que representa o modelo"""
        return self.text

class Entry(models.Model):
    """Uma entrada especifica para cada Topico criado"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Retornando uma string para representar esse modelo"""
        return self.text[:50] + "..."
