from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
#복잡한 url 패턴이 올 것을 감안해 r이라는 접두사를 붙여서 url을 생성한다.
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]

'''
from .views import TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path("/", TaskListCreateAPIView.as_view, name="task-list"),
    path("/<int:pk>/", TaskDetailAPIView.as_view, name="task-detail"),
]
'''