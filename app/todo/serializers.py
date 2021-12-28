from rest_framework import serializers
from todo.models import ToDo


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'date', 'title', 'detail', 'complete')
