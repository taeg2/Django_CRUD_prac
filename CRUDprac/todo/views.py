from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import TaskSerializer

class TaskListCreateAPIView(APIView):
    #응답은 json 형태로 해야하기 때문에 항상 serializer로 포장해서 전달해야 함.
    def get(self, request):
        tasks = Task.obejects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        #serializer에게 data를 전달하면 model instance를 생성
        serializer = TaskSerializer(data=request.data)
        
        #serializer 객체가 유효한지 판단함
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data(), status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#조회 수정 삭제는 항상 pk를 요함
class TaskDetailAPIView(APIView):
    #url을 통해 전달받은 pk에 해당하는 객체를 뽑아내서 json 형태로 전달함
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    #put 연산은 request 본문에 데이터를 담고 있음
    #따라서 해당 데이터를 객체 형태로 바꿔야 함
    #pk: update할 인스턴스, request.data: 업데이트할 내용
    #put 메서드는 json 데이터를 통째로 덮어버림(그래서 모든 데이터가 다 전달 되어야 함.)
    def update(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)

        #업데이트가 잘 이뤄졌는 지 확인하고 잘 됐으면 해당 데이터를 반환해서 화면에 다시 띄워야 함
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #잘 안됐으면 400 Error를 전달함(부족한 데이터라던가 그런거)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        taks = get_object_or_404(Task, pk=pk)
        taks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
'''
