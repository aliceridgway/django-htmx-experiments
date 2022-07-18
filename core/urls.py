from django.urls import path

from . import views, views_ajax

urlpatterns = [
    path("", views.index, name="index"),
]

ajax_url_patterns = [
    path("add", views_ajax.add_todo, name="add"),
    path("complete/<int:pk>", views_ajax.complete, name="complete"),
    path("delete/<int:pk>", views_ajax.delete, name="delete"),
    path("todos/filter/<str:status>", views_ajax.filter_list, name="filter-todos"),
    path("todos/all", views_ajax.get_all_todos, name="all-todos"),
]


urlpatterns += ajax_url_patterns
