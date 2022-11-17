from rest_framework import serializers
from blog.models import Posts

class PostSerilizers(serializers.ModelSerializer):
    pass
    class Meta:
        model = Posts
        fields = ['id','author','title','content']