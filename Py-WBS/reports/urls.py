from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('create/', views.report_create, name='report_create'),
    path('<int:pk>/edit/', views.report_edit, name='report_edit'),
    path('<int:pk>/delete/', views.report_delete, name='report_delete'),
    path('get_project_details/<int:pk>/', views.get_project_details, name='get_project_details'),
]
