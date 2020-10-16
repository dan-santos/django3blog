from django.http import HttpResponse
# No django, cada view que nos criamos deve ser construida em uma def

def hello_world(request):

    return HttpResponse('Hello World')
