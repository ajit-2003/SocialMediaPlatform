from django.urls import path
from . import views

urlpatterns = [
    path('document/<int:doc_id>/', views.document_editor, name='document_editor'),
    path('document/', views.document_editor, name='document_editor_no_id'),
    path('group/<int:group_id>/', views.group_chat, name='group_chat'),
    path('create-group/', views.create_group, name='create_group'),
]
