from django.urls import path, include
from blog import views

app_name = "blog"

urlpatterns = [
    path(
        '',
        views.PostListView.as_view(),
        name='index'
    ),

    path(
        'page/<slug:slug>/',
        views.PageDetailView.as_view(),
        name='page'
    ),

    path(
        'post/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post'
    ),

    path(
        'created_by/<int:author_pk>/',
        views.CreatedByListView.as_view(),
        name='created_by'
    ),

    path(
        'category/<slug:slug>/',
        views.CategoryListView.as_view(),
        name='category'
    ),

    path(
        'tags/<slug:slug>/',
        views.TagsListView.as_view(),
        name='tags'
    ),

    path(
        'search/',
        views.SearchListView.as_view(),
        name='search'
    ),

    path(
        'page_404',
        views.page_404,
        name='page_404'
    )
]

