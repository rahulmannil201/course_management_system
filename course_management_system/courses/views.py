from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer


class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Instructor'

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsInstructor]

class CourseDetailView(genericView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsInstructor]