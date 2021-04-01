from django.db.models import fields
from rest_framework import serializers
from feedly_app.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = [
			"description",
			"link",
			"title",
		]