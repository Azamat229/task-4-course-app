from .serializers import CourseListSerializer, CourseDetailSerializer, CourseCreateSerializer
from .models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


class CourseListView(APIView):
    """ Course List """

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseListSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        course = CourseCreateSerializer(data=request.data)
        if course.is_valid():
            course.save()
            return Response(course.data, status=status.HTTP_201_CREATED)
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    """ Course Detail """

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# class CourseCreateView(APIView):
#     """ Create Course"""
