from django.urls import path

from . import views

from .views import ContentAsList, DetailedContent, CreateContent, UpdateContent, DeleteContent


urlpatterns = [
    path('', ContentAsList.as_view(), name='panel-main'),
    path('content/<int:pk>/', DetailedContent.as_view(), name='detail-content'),
    path('content/new/', CreateContent.as_view(), name='create-content'),
    path('content/<int:pk>/update/', UpdateContent.as_view(), name='update-content'),
    path('content/<int:pk>/delete/', DeleteContent.as_view(), name='delete-content'),
]
