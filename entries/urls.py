from django.urls import path
from . import views

appname= 'entries'
urlpatterns=[
    path('edit_profile/', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('', views.EntryListView.as_view(), name='entry_list'),
    path('<int:pk>/', views.EntryDetailView.as_view(), name='entry_detail'),
    path('create/', views.EntryCreateView.as_view(), name='entry_create'),
    path('<int:pk>/update/', views.EntryUpdateView.as_view(), name='entry_update'),
    path('<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_confirm_delete'),
]