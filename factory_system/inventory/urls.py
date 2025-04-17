from django.urls import path
from .views import BoardListView, board_create, board_update, board_delete

urlpatterns = [
    path('', BoardListView.as_view(), name='board_list'),
    path('create/', board_create, name='board_create'),
    path('<int:pk>/edit/', board_update, name='board_update'),
    path('<int:pk>/delete/', board_delete, name='board_delete'),
]
