from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from home import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
