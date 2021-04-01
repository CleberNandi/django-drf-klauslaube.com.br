from rest_framework import viewsets
from feedly_app.models import Channel
from feedly_app.serializers import ChannelSerializer


class ChannelViewSet(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer
	