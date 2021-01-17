from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CreateUserProfileSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user= User(email=self.validated_data['email'],
        username=self.validated_data['username'])
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!= password2:
            raise serializers.ValidationError({'password':'Doest match'})
        user.set_password(password)
        #user = User.objects.create(**validated_data)
        #user.set_password(validated_data['password'])
        user.save()
        profile=Profile.objects.create(name=user.username, email=user.email)
        profile.save()
        
        return user

class RoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Round
        fields=['id','rounds','question','answer']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Profile
        fields=['id','name','email','score','curr_round']
