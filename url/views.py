from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import Url
from .serializers import UrlSerializer



# Create your views here.
@api_view(['GET'])
def get_all_urls(request):
        urls = Url.objects.all()
        serializer = UrlSerializer(urls, many=True)
        return Response({"urls": serializer.data})


@api_view(['POST'])
def url(request):
    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def redirect_view(request, code):
    url = get_object_or_404(Url, code=code)
    url.num_visits += 1  # Increment visit count
    url.save()
    return redirect(url.url)


@api_view(['GET'])
def get_url_by_id(request , code):
     url = get_object_or_404(Url , code=code)
     serializer = UrlSerializer(url, many=False)
     return Response({"url" : serializer.data})
