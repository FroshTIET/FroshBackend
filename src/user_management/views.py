from django.http.response import Http404

from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import status


from user_management.models import Student
from user_management.paginators import GenericFroshPaginator
from user_management.serializers import ScoreBoardSerializer, StudentSerializer

# Create your views here.


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "get_auth_token": reverse("api_token_auth", request=request, format=format),
            "my_details": reverse("my-details", request=request, format=format),
        }
    )


class StudentListView(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        if self.request.user.is_staff:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class StudentDetailView(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, *args, **kwargs):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


class MyDetailsView(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get_object(self, user, *args, **kwargs):
        try:
            return Student.objects.get(user=user)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        student = self.get_object(request.user)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


class LeaderBoard(generics.ListAPIView):
    queryset = Student.objects.all().order_by("-points")
    serializer_class = ScoreBoardSerializer
    pagination_class = GenericFroshPaginator


class setFireBaseToken(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [IsAuthenticated]    


    def post(self, request, format=None):
        
        try:
            firebase_token = request.data['token']
            request.user.profile.firebase_token = firebase_token
            request.user.profile.save()
        except KeyError:
            return Response(status=400,)
    
        content = {'status': 'ok'}
        return Response(content)
                        