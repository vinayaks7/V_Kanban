from rest_framework import serializers
from Kanban_dashboard.models import Task_Table, User_Table


class KanbanSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User_Table
        fields = ('user_id', 'user_name','password')


class KanbanSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Task_Table
        fields = ('task_id', 'task_desc', 'task_status', 'task_priority', 'task_summary', 'user_id', 'task_deadline')