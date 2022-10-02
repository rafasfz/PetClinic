from django.urls import path

from .views import (
    ClientView,
    ClientAddView,
    ClientEditView,
    ClientDeleteView,
    ClientDetailView,
    PetAddView, 
    PetView, 
    PetEditView, 
    PetDeleteView,
)

urlpatterns = [
    path('', ClientView.as_view(), name='clients'),
    path('<int:id>/', ClientDetailView.as_view(), name='clients_detail'),
    path('add/', ClientAddView.as_view(), name='clients_add'),
    path('edit/<int:id>/', ClientEditView.as_view(), name='clients_edit'),
    path('delete/<int:id>/', ClientDeleteView.as_view(), name='clients_delete'),

    path('pets/', PetView.as_view(), name='pets'),
    path('pets/add/', PetAddView.as_view(), name='pets_add'),
    path('pets/edit/<int:id>/', PetEditView.as_view(), name='pets_add'),
    path('pets/delete/<int:id>/', PetDeleteView.as_view(), name='pets_delete'),
]
