from django.shortcuts import render
from .models import Post, Email
# Create your views here.

def index(request):
    emailB = Email.objects.all()
    listaEmails = []
    for i in emailB:
        listaEmails.append(i.emails2)
    
    if 'email' in request.POST:
        emailL = request.POST['email']
        if emailL in listaEmails:
            print("Ja existe")

        else:
            s = Email(emails2=emailL)
            s.save()
            print("Salvou o Email:", emailL)
    print(listaEmails)
    # Cookies
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    posts = Post.objects.all().order_by('-id')
    data = {
        'post_list': posts,
        'num_visits': num_visits,
    }
    return render(request, 'core/index.html', data)

def contato(request):
    return render(request, 'core/contato.html')

def sobre(request):
    return render(request, 'core/sobre.html')  

def blog(request):
    posts = Post.objects.all().order_by('-id')
    data = {
        'post_list': posts,
    }
    return render(request, 'core/blog.html', data)

def detail(request, id):
    post = Post.objects.get(id=id)
    total = (post.price + post.graphics + post.optimization + post.gameplay + post.difficulty) / 5
    data = {
        'post':post,
        'total':total
    }
    return render(request, 'core/gamesingle.html', data) 
    