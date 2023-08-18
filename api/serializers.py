from rest_framework.serializers import ModelSerializer
from base.models import User, Topic, Comment, Ballots 


class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields='__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BallotsSerializer(ModelSerializer):
    class Meta:
        model = Ballots
        fields = '__all__'
        