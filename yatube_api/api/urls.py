from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from django.urls import include, path

from .views import PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]