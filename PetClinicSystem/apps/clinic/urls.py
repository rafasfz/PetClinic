from django.urls import path

from .views import (
    DrugAddView,
    DrugView,
    DrugDeleteView,
    VeterinaryAddView,
    VeterinaryView,
    VeterinaryEditView,
    VeterinaryDeleteView,
    VeterinaryDetailView,
    AppointmentView,
    AppointmentDetailView,
    AppointmentAddView,
    AppointmentEditView,
)

urlpatterns = [
    path('drugs/', DrugView.as_view(), name='drugs'),
    path('drugs/add/', DrugAddView.as_view(), name='drugs_add'),
    path('drugs/delete/<int:id>/', DrugDeleteView.as_view(), name='drugs_delete'),
    
    path('veterinaries/', VeterinaryView.as_view(), name='veterinaries'),
    path('veterinaries/<int:id>/', VeterinaryDetailView.as_view(), name='veterinaries_detail'),
    path('veterinaries/add/', VeterinaryAddView.as_view(), name='veterinaries_add'),
    path('veterinaries/edit/<int:id>/', VeterinaryEditView.as_view(), name='veterinaries_edit'),
    path('veterinaries/delete/<int:id>/', VeterinaryDeleteView.as_view(), name='veterinaries_delete'),

    path('appointments/', AppointmentView.as_view(), name='appointments'),
    path('appointments/<int:id>/', AppointmentDetailView.as_view(), name='appointments_detail'),
    path('appointments/add/', AppointmentAddView.as_view(), name='appointments_add'),
    path('appointments/edit/<int:id>/', AppointmentEditView.as_view(), name='appointments_edit'),
]
