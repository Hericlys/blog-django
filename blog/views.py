from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from blog.models import Post, Page
from django.views.generic import ListView


PER_PAGE = 9

class PostListView(ListView):
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'page_title': 'home -'}
        )
        return context


class CreatedByListView(PostListView):
    pass


def page(request, slug):
    page = Page.objects.filter(is_published=True, slug=slug).first()
    return render(
        request, 'blog/pages/page.html',
        {
            'page': page,
            'page_title': page.title,
        }
    )


def post(request, slug):
    post = Post.objects.get_published().filter(slug=slug).first()
    return render(
        request, 'blog/pages/post.html',
        {
            'post': post,
        }
    
    )


def created_by(request, author_pk):
    posts = Post.objects.get_published().filter(created_by__pk=author_pk)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def tags(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def search(request):
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value)
    )


    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'search_value': search_value,
        }
    )
