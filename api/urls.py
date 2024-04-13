from django.urls import path
from .views import add_reaction, delete_reaction, list_reactions

urlpatterns = [
    path('reactions/', list_reactions),
    path('reactions/add/', add_reaction, name='add-reaction'),
    path('reactions/delete/<int:reaction_id>/', delete_reaction),
]