from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'email',)
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title_korean', 'title_kazakh', 'order')


class TopicWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicWord
        fields = ('id', 'topic_name_korean', 'topic_name_kazakh', 'order')


class WordSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    topic_word = TopicWordSerializer(read_only=True)

    class Meta:
        model = Word
        fields = ('id', 'word_korean', 'word_kazakh', 'part_of_speech', 'transcription',
                  'example_korean_one', 'example_kazakh_one', 'example_korean_two', 'example_kazakh_two',
                  'example_korean_three', 'example_kazakh_three', 'lesson', 'topic_word', 'audio')


class GrammarSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Grammar
        fields = ('id', 'rule_korean', 'rule_kazakh', 'general_rule', 'example_korean_one', 'example_kazakh_one',
                  'example_korean_two', 'example_kazakh_two', 'example_korean_three', 'example_kazakh_three', 'lesson')


class ReadingSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Reading
        fields = ('id', 'dialogue_korean', 'dialogue_kazakh', 'lesson', 'audio')


class ListeningSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Listening
        fields = ('id', 'name', 'transcription', 'lesson', 'audio')


class QuizSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'body', 'answer', 'lesson')



# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"
#         depth = 1