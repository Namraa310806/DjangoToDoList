from django.urls import include, path

from app import views

urlpatterns = [
    path('',views.home),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('blogpost/<str:slug>/',views.blogpost),
    path('search/',views.search)
]
