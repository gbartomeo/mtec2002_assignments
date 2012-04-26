# Create your views here.

from django.template import Context, loader


from django.http import HttpResponse
def index(request):
    t = loader.get_template('hello/index.html')
    mylist = ["hola", "ciao", "aloha"]
    d = {"greeting": "hello", "mylist": mylist}
    c = Context(d)
    return HttpResponse(t.render(c))