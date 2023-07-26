from django.shortcuts import render

def index(request):
    context = {
        'page_title' : 'blog',
    }
    
    return render(request, 'blog/pages/index.html', context=context)


