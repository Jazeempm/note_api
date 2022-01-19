from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from my_api.models import NotesImage, Note

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", "email")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesImage
        fields="__all__"

class NotesSerializer(serializers.ModelSerializer):
    notesimage_set=ImageSerializer(many=True,read_only=True)

    class Meta:
        model=Note
        depth = 1
        fields=["id","title","content","created","notesimage_set"]



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'username': self.user.username})
        return data
