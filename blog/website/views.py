from django.shortcuts import render
from .models import Post, Contact

# a funcao "render" renderiza um template para devolver ao browser
# os templates devem ficar sempre na pasta "templates" do app em questao

def hello_blog(request):
    # A variavel data sera o response ao template, isto eh, agora podemos usar essa variavel no arquivo html do template
    # Isso eh possivel gracas ao framework que o django utiliza internamente chamado "ginger", no qual podemos inserir
    # codigos basicos de python dentro do aquivo html.

    # Mais intrucoes de uso no arquivo index.html
    lista = ['Python', 'Django', 'Linux']
    # list_posts = Post.objects.all() # equivalente a select all
    #Soh retornara posts aprovados
    list_posts = Post.objects.filter(approved=True)
    
    data = {
        'name': 'Curso de Django 3', 
        'lista': lista, 
        'posts': list_posts
    }

    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id) # Pega o post com o id passado por parametro
    return render(request, 'post_detail.html', {'post': post})

def save_form(request):
    name=request.POST['name']
    Contact.objects.create(
        name=name, 
        email=request.POST['email'], 
        message=request.POST['message']
    )
    return render(request, 'contact_success.html', {'name_contact': name})