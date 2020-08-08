# this file to define what has to be sent to the user.

from django.shortcuts import render

posts = [{
    'name': 'Aldric Pereira',
    'title': 'Don\'t really know',
    'content': 'First post',
    'date_posted': 'August 08, 2020'
},
    {
    'name': 'Aaron',
    'title': 'i really know',
    'content': 'second post',
    'date_posted': 'August 18, 2020'
}
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About!!'})
