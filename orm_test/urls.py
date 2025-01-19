from django.urls import path

from orm_test import views

app_name = 'main'

urlpatterns = [
    path('', views.main),
    path('posts/<int:post_id>/', views.post_detail_view)
]