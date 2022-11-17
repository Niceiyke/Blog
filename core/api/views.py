from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PostSerilizers
from blog.models import Posts


class ListCreatePost(ListCreateAPIView):
    queryset =Posts.objects.all()
    serializer_class =PostSerilizers


class SinglePost(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class =PostSerilizers
    lookup_fields = ['id']

