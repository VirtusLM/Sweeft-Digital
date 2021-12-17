
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from urlshortener.models import URL
from urlshortener.views import shortener
from .serializers import URLSerializer



class URLShortener(APIView):
	def post(self, request):

		if 'short_url' in request.data:
			del request.data['short_url']	

		random = shortener()
		index = URL(short_url=random)

		serializer = URLSerializer(index, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'short_url':request.build_absolute_uri('/') + random}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomURLShortener(APIView):
	def post(self, request):

		serializer = URLSerializer(data=request.data)
		
		if serializer.is_valid():
			if not 'short_url' in request.data:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			serializer.save()
			return Response({'short_url':request.build_absolute_uri('/') + request.data['short_url']}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
