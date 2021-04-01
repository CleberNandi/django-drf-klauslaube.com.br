from django.db.models import fields
from rest_framework import serializers
from feedly_app.models import Channel, Item


class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		exclude = ["channel"]

		