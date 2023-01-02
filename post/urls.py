from django.urls import path
from .import views
urlpatterns = [
    path('',views.home ,name='home'),
    path('listes_articles/', views.list_post,name='listes_articles'),
    path('details/<str:id>/', views.details , name='details'),
    path('create/', views.createArticle,name='create'),
    path('update/<str:id>/',views.update, name='update'),
    path('apropos/',views.apropos,name='apropos'),
    path('contact/',views.contact,name='contact'),
]

