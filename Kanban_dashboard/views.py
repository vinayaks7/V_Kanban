from django.shortcuts import render
from rest_framework import generics, status
from django.http import JsonResponse
from rest_framework.response import Response

from Kanban_dashboard.models import Task_Table,User_Table
from Kanban_dashboard.serializers import KanbanSerializer2,KanbanSerializer1


# Create your views here.
class AddRetrieveView(generics.ListCreateAPIView):
    # create task
    def post(self, request, *args, **kwargs):
        try:
            new_task = KanbanSerializer2(data=request.data)

            if new_task.is_valid(raise_exception=True):
                new_task.save()
                response_data  = {
                    'result': "Success"
                }
        except Exception as e:

                response_data  = {
                    'result': "Error" + str(e)
                }


        return JsonResponse(response_data )


    # to get all tasks for dashboard
    def get(self, request, *args, **kwargs):
        try:
            all_entries = Task_Table.objects.all()
            serialised_data = KanbanSerializer2(all_entries, many=True).data

            return JsonResponse(serialised_data, safe=False)
        except Exception as e:
            response_data = {
                'result': "Error" + str(e)
            }

            return  JsonResponse(response_data, safe=False)



class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # to edit a task
    def put(self, request, *args, **kwargs):

        try:
            task = Task_Table.objects.get(task_id = request.data['task_id'])
            new_task = KanbanSerializer2(task,data=request.data)

            if new_task.is_valid(raise_exception=True):
                new_task.save()
                dict = {
                    'result': "Success"
                }
        except Exception as e:
            dict = {
                'result': "Error" +str(e)
            }

        return JsonResponse(dict,safe=False)


    # to delete a task
    def delete(self, request, *args, **kwargs):
        try:
            task_id = request.data['task_id']

            if task_id:
                queryset = Task_Table.objects.filter(task_id=task_id)

                if not queryset:
                    return Response({'msg': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
                queryset.delete()
                return Response({'msg': 'Task deleted'}, status=status.HTTP_200_OK)
            else:

                return Response({'msg': 'Error'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg':str(e)})

# for edit modal
class DetailsOfSingleTask(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        try:
            all_entries = Task_Table.objects.filter(task_id=request.data['task_id'])
            serialised_data = KanbanSerializer2(all_entries, many=True).data
            return JsonResponse(serialised_data, safe=False)
        except Exception as e:
            return JsonResponse({'msg':str(e)})

# for drop down in add task modal
class GetAllUsers(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            all_entries = User_Table.objects.all()
            serialised_data = KanbanSerializer1(all_entries, many=True).data
            return JsonResponse(serialised_data, safe=False)
        except Exception as e:
            return JsonResponse({'msg': str(e)})

# for showing the name of the user in modal
class GetSingleUsername(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            all_entries = Task_Table.objects.filter(task_id=request.GET['task_id'])
            serialised_data = KanbanSerializer2(all_entries, many=True).data

            all_entries2 = User_Table.objects.filter(user_id=serialised_data[0]['user_id'])
            serialised_data2 = KanbanSerializer1(all_entries2, many=True).data
            return JsonResponse(serialised_data2[0]['user_name'], safe=False)
        except Exception as e:
            return JsonResponse({'msg': str(e)})


# for authentication
class CompareSingleUser(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            all_entries = User_Table.objects.filter(user_name=request.GET['user_name'])
            serialised_data = KanbanSerializer1(all_entries, many=True).data
            if serialised_data[0]['password'] == request.GET['password']:
                response_data = {
                    'module': "get",
                    'code': "200 OK",
                    'message': "Success"
                }
            else:
                response_data = {
                    'module': "get",
                    'message': "Wrong password"
                }


            return JsonResponse(response_data, safe=False)
        except Exception as e:
            return JsonResponse({'msg': str(e)})



#for sorting all tasks based on priority
class SortTasksPriority(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            all_entries = Task_Table.objects.all().order_by('task_priority','task_deadline')
            serialised_data = KanbanSerializer2(all_entries, many=True).data
            return JsonResponse(serialised_data, safe=False)
        except Exception as e:
            return JsonResponse({'msg': str(e)})


# for sorting all tasks based on deadline
class SortTasksDeadline(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            all_entries = Task_Table.objects.all().order_by('-task_deadline')
            serialised_data = KanbanSerializer2(all_entries, many=True).data
            return JsonResponse(serialised_data, safe=False)
        except Exception as e:
            return JsonResponse({'msg': str(e)})

# for getting all the tasks assigned to one user
class GetAllTasksForSingleUser(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            all_entries2 = Task_Table.objects.filter(user_id=request.GET['user_id'])
            serialised_data2 = KanbanSerializer2(all_entries2, many=True).data

            return JsonResponse(serialised_data2, safe=False)
        except Exception as e:
            return JsonResponse({'msg': str(e)})







