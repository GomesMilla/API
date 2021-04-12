from rest_framework import viewsets
from adm.models import Channel
from adm.serializers import *

# nossa views


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(
            channel=self.kwargs["channel_pk"])
