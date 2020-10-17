from django.shortcuts import render

# a funcao "render" renderiza um template para devolver ao browser
# os templates devem ficar sempre na pasta "templates" do app em questao

def hello_blog(request):
    # A variavel data sera o response ao template, isto eh, agora podemos usar essa variavel no arquivo html do template
    # Isso eh possivel gracas ao framework que o django utiliza internamente chamado "ginger", no qual podemos inserir
    # codigos basicos de python dentro do aquivo html.

    # Mais intrucoes de uso no arquivo index.html
    lista = ['Python', 'Django', 'Linux']
    data = {'name': 'Curso de Django 3', 'lista': lista}
    return render(request, 'index.html', data)