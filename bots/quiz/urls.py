
from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('rounds/',views.roundList.as_view(),name='round-list'),
    path('rounds/<int:pk>',views.roundDetail.as_view(),name='round-details'),
    path('profiles/',views.profileList.as_view(),name='profile-list'),
    path('users/',views.userList.as_view(),name='users-list'),
    path('',views.api_root),
    path('getrounds/',views.getRounds.as_view(),name='get-rounds'),
    path('register/',views.registration_view, name='register'),
    path('login/',obtain_auth_token,name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)