from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    """
    model data 를 json type 으로 변경시켜서
    api 를 통해 통신이 가능하게 만들어주는 클래스
    """

    class Meta:
        model = Quiz
        field = ('title', 'body', 'answer')
