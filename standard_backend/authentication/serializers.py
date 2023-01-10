from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import currentUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # for any additional fields you'd like to add to the JWT sent back in response
        # add below using the token["field name"] = user.name_of_property
        # token["is_student"] = user.is_student

        token["status"] = user.status
        token["icon"] = user.icon

        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=currentUser.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = currentUser
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'status', 'icon')

    def create(self, validated_data):

        user = currentUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            status=validated_data['status'],
            icon=validated_data['icon']

            # If added new columns through the User model, add them in this
            # create method. Example below:

            # is_student=validated_data['is_student']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentUser
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ['username', 'password', 'email',
                  'first_name', 'last_name', 'status', 'icon']