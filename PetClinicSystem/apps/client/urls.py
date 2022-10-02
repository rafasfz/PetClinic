from django.urls import path

from .views import ClientView, ClientAddView, ClientEditView, ClientDeleteView, ClientDetailView

urlpatterns = [
    path('', ClientView.as_view(), name='clients'),
    path('<int:id>/', ClientDetailView.as_view(), name='clients_detail'),
    path('add/', ClientAddView.as_view(), name='clients_add'),
    path('edit/<int:id>/', ClientEditView.as_view(), name='clients_edit'),
    path('delete/<int:id>/', ClientDeleteView.as_view(), name='clients_delete'),
]
