from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page or index
    path('recommend/', views.recommend_ui, name='recommend_ui'),
    path('recommend_books/', views.recommend, name='recommend_books'),
    path('book/<str:book_title>/', views.book_detail, name='book_detail'),
    path('recommendations/', views.recommendation_page, name='recommendation_page'),
]