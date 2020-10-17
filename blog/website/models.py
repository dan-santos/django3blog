from django.db import models

# todo model precisa ser uma classe
# a superclasse indica pro django que a classe é deve ser tranformada em uma tabela sql

# todo campo eh tratado como um ___Field, que indica que aquele atributo será uma coluna da tabela
# CharField == varchar()
# Para ver todos os tipos permitidos: https://docs.djangoproject.com/pt-br/3.1/ref/models/fields/
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
