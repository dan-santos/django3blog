from django.db import models

# todo model precisa ser uma classe
# a superclasse indica pro django que a classe é deve ser tranformada em uma tabela sql

# enums (TextChoices)
# pode ser feito para muitas coisas, como para reduzir espaco no banco de dados, pois, ao inves de salvar o
# conteudo completo da variavel (nome da categoria), salva apenas sua abreviacao
class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia',
    CR = 'CR', 'Curiosidades',
    GR = 'GR', 'Geral'

# todo campo eh tratado como um ___Field, que indica que aquele atributo será uma coluna da tabela
# CharField == varchar()
# Para ver todos os tipos permitidos: https://docs.djangoproject.com/pt-br/3.1/ref/models/fields/
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2, # siglas
        choices=Categories.choices, # setando o enum
        default=Categories.GR # setando qual dos marcadores do enum sera o padrao
    )

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.__repr__()

