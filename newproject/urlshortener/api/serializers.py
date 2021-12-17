from rest_framework import serializers
from urlshortener.models import URL


class URLSerializer(serializers.ModelSerializer):
	class Meta:
		model = URL
		fields = ['long_url', 'short_url']


