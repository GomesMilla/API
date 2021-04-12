from django.contrib import admin
from django.urls import include, path

from rest_framework_nested import routers
from adm.api import *

api_router = routers.DefaultRouter()
api_router.register(r"channels", ChannelViewSet),

channels_router = routers.NestedDefaultRouter(
    api_router, r"channels", lookup="channel")
channels_router.register(r"items", ItemViewSet,
                         basename="channel-items")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_router.urls)),
    path("api/", include(channels_router.urls)),
]
