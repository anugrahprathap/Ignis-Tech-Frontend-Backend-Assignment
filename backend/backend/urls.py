"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import EventListAPIView,LoginAPIView,UserAPIView,FollowEvent,LikedEventsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/events/', EventListAPIView.as_view(), name='event-list'),
    path('api/login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('api/user/', UserAPIView.as_view(), name='user_api'),
    path('api/events/<int:event_id>/follow/', FollowEvent.as_view(), name='follow-event'),
    path('api/liked-events/', LikedEventsAPIView.as_view(), name='liked-events'),



]