from rest_framework import viewsets
from feedly_app.models import Channel, Item
from feedly_app.serializers import ChannelSerializer, ItemSerializer


class ChannelViewSet(viewsets.ModelViewSet):
	queryset = Channel.objects.all()
	serializer_class = ChannelSerializer


class ItemViewSet(viewsets.ModelViewSet):
	serializer_class = ItemSerializer
	
	def get_queryset(self):
		return Item.objects.filter(
			channel=self.kwargs['channel_pk']
		)