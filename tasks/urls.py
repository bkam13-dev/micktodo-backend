from django.urls import path
from tasks import views


urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<slug:slug>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy')
]
