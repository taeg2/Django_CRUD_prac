from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    #Meta 클래스는 serializer를 통해 생성하고 싶은 모델과 바꾸고 싶은 데이터 셋을 나타냄
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'complete']