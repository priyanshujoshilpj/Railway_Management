from django.urls import path
from . import views


urlpatterns = [
    path("", views.Index.as_view()),
    path('create', views.Create.as_view()),  
    path('read',views.Read.as_view()),  
    path('edit/<int:id>', views.Update.as_view()),  
    path('update/<int:id>', views.Update.as_view()),  
    path('delete/<int:id>', views.Delete.as_view()),  
]
