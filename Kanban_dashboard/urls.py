from django.urls import path

from Kanban_dashboard.views import AddRetrieveView, UpdateDeleteView, \
    DetailsOfSingleTask, GetAllUsers,GetSingleUsername,CompareSingleUser,SortTasksPriority,\
    SortTasksDeadline,GetAllTasksForSingleUser


urlpatterns = [
    path('home/', AddRetrieveView.as_view()),
    path('udpdate_delete/', UpdateDeleteView.as_view()),
    path('details_of_single_task/', DetailsOfSingleTask.as_view()),
    path('get_all_users/',GetAllUsers.as_view()),
    path('get_single_username/',GetSingleUsername.as_view()),
    path('compare_single_user/',CompareSingleUser.as_view()),
    path('sort_tasks_priority/',SortTasksPriority.as_view()),
    path('sort_tasks_deadline/',SortTasksDeadline.as_view()),
    path('get_all_tasks_for_single_user/',GetAllTasksForSingleUser.as_view()),
]