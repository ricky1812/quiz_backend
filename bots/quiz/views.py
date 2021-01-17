from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        
        'rounds': reverse('round-list', request=request, format=format),
        'profiles': reverse('profile-list',request=request, format=format),
        'users': reverse('users-list', request=request, format=format),
    })

class roundList(generics.ListCreateAPIView):
    queryset=Round.objects.all()
    serializer_class=RoundSerializer

class roundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Round.objects.all()
    serializer_class=RoundSerializer

class userList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=CreateUserProfileSerializer

class profileList(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

class getRounds(APIView):
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):

        player=Profile.objects.get(name=request.user.username)
        current_round=Round.objects.get(rounds=player.curr_round)
        serializer= RoundSerializer(current_round)
        return Response({"question":serializer.data})

@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer=CreateUserProfileSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user=serializer.save()
            data['response']="succesful register"
            data['email']=user.email
            data['username']=user.username
            token=Token.objects.get(user= user).key
            data['token']=token
        else:
            data=serializer.errors

        return Response(data)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)