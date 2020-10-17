from django.shortcuts import render

# a funcao "render" renderiza um template para devolver ao browser
# os templates devem ficar sempre na pasta "templates" do app em questao

def hello_blog(request):
    return render(request, 'index.html')