from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from api.models import FeedbackUser
from api.serializers import UserSerializer

class UserList(APIView):
    """
    List all Users or create a new instance
    """
    def get(self, request, format=None):
        user = FeedbackUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance
    """
    def get_obj(self, pk):
        try:
            return FeedbackUser.objects.get(pk=pk)
        except FeedbackUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_obj(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_obj(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_obj(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

