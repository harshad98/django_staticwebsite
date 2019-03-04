from django.shortcuts import render

posts = [
    {
        'author': 'harshad',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'augest 27'

    },
    {
        'author': ' jane harshad',
        'title': 'blog post 2',
        'content': 'first222 post content',
        'date_posted': 'augest 27'

    }




]



def home(request):
    context = {
         'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')




