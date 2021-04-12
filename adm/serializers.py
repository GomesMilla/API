from rest_framework import serializers

from adm.models import *

# nosso 'form'


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "description",
            "link",
            "title",
        ]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ["channel"]
