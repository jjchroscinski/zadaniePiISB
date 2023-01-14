from rest_framework import routers
from django.urls import include, path
from .views import *

router = routers.DefaultRouter()
router.register(r'aktorzy', AktorViewSet)
router.register(r'rezyserzy', RezyserViewSet)
router.register(r'filmy', FilmViewSet)
router.register(r'oceny', OcenaViewSet)
router.register(r'users', UserViewSet)

urlpatterns=[
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]