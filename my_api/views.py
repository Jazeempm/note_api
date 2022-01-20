from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from my_api.serializers import UserSerializer, NotesSerializer, ImageSerializer, CustomTokenObtainPairSerializer
from .models import Note,NotesImage


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class NotesViewSet(ModelViewSet):

    queryset = Note.objects.order_by('-created')
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        print(request.FILES)
        images_data=request.data.getlist('notesimage_set')
        print("images_data",images_data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note=self.perform_create(serializer)

        for data in images_data:
            a=NotesImage(note=note,image=data)
            a.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DeleteImageView(APIView):
    def get(self,request,id):
        image=NotesImage.objects.get(id=id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ImageUploadView(APIView):
    def post(self,request,id):
        note=Note.objects.get(id=id)
        image_data = request.data.getlist('notesimage')

        for data in image_data:
            img=NotesImage(note=note,image=data)
            img.save()
        return Response(status=status.HTTP_201_CREATED)



class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
