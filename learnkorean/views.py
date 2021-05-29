from rest_framework import generics, mixins, views
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
import random


class UserView(views.APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        user = request.user
        user_obj = User.objects.get(username=user.username)
        serializer = UserSerializers(user_obj)
        return Response(serializer.data)


class Register(views.APIView):
    def post(self, request):
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False, "message": "User was Created!"})
        return Response({"error": True, "message": "User Not Created!"})


class WordOfLessonView(views.APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = WordSerializer

    def get(self, request, lesson, format=None):
        query = Word.objects.filter(lesson=lesson).prefetch_related('lesson')
        data = []
        serializers = WordSerializer(query, many=True)
        for word in serializers.data:
            fab_query = Favorite.objects.filter(user=request.user).filter(id=word['id'])
            if fab_query:
                word['favorite'] = fab_query[0].isFavorite
            else:
                word['favorite'] = False
            data.append(word)
        return Response(data)


class GrammarOfLessonView(views.APIView):
    serializer_class = GrammarSerializer
   # permission_classes = [IsAuthenticated, ]
    def get(self, request, lesson, format=None):
        grammars = Grammar.objects.filter(lesson=lesson).prefetch_related('lesson')
        serializer = self.serializer_class(grammars, many=True)
        return Response(serializer.data)


class ReadingOfLessonView(views.APIView):
    serializer_class = ReadingSerializer
   # permission_classes = [IsAuthenticated, ]
    def get(self, request, lesson, format=None):
        readings = Reading.objects.filter(lesson=lesson).prefetch_related('lesson')
        serializer = self.serializer_class(readings, many=True)
        return Response(serializer.data)


class ListeningOfLessonView(views.APIView):
    serializer_class = ListeningSerializer
   # permission_classes = [IsAuthenticated, ]
    def get(self, request, lesson, format=None):
        listenings = Listening.objects.filter(lesson=lesson).prefetch_related('lesson')
        serializer = self.serializer_class(listenings, many=True)
        return Response(serializer.data)


class WordOfTopicView(views.APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = WordSerializer

    def get(self, request, topic_word, format=None):
        query = Word.objects.filter(topic_word=topic_word).prefetch_related('topic_word')
        data = []
        serializers = WordSerializer(query, many=True)
        for word in serializers.data:
            fab_query = Favorite.objects.filter(user=request.user).filter(id=word['id'])
            if fab_query:
                word['favorite'] = fab_query[0].isFavorite
            else:
                word['favorite'] = False
            data.append(word)
        return Response(data)



class WordAllView(views.APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = WordSerializer

    def get(self, request, format=None):
        query = Word.objects.all()
        data = []
        serializers = WordSerializer(query, many=True)
        for word in serializers.data:
            fab_query = Favorite.objects.filter(user=request.user).filter(id=word['id'])
            if fab_query:
                word['favorite'] = fab_query[0].isFavorite
            else:
                word['favorite'] = False
            data.append(word)
        return Response(data)


class LessonAllViews(views.APIView):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    serializer_class = LessonSerializer

    def get(self, request, format=None):
        lessons = Lesson.objects.all()
        serializer = self.serializer_class(lessons, many=True)
        return Response(serializer.data)


class TopicAllViews(views.APIView):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    serializer_class = TopicWordSerializer

    def get(self, request, format=None):
        topics = TopicWord.objects.all()
        serializer = self.serializer_class(topics, many=True)
        return Response(serializer.data)


class GrammarAllView(views.APIView):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    serializer_class = GrammarSerializer

    def get(self, request, format=None):
        grammar = Grammar.objects.all()
        serializer = self.serializer_class(grammar, many=True)
        return Response(serializer.data)


class ReadingAllView(views.APIView):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    serializer_class = ReadingSerializer

    def get(self, request, format=None):
        reading = Reading.objects.all()
        serializer = self.serializer_class(reading, many=True)
        return Response(serializer.data)


class ListeningAllView(views.APIView):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    serializer_class = ListeningSerializer

    def get(self, request, format=None):
        listening = Listening.objects.all()
        serializer = self.serializer_class(listening, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)


#my view
@api_view(['GET'])
def randomQuizByLesson(request, lesson):
    totalQuizs = Quiz.objects.filter(lesson=lesson).prefetch_related('lesson')
    randomQuizs = random.sample(list(totalQuizs), len(totalQuizs))
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        data = request.data["id"]
        # print(data)
        try:
            word_obj = Word.objects.get(id=data)
            # print(data)
            user = request.user
            single_favorite_word = Favorite.objects.filter(user=user).filter(word=word_obj).first()
            if single_favorite_word:
                print("single_favorite_word")
                ccc = single_favorite_word.isFavorite
                single_favorite_word.isFavorite = not ccc
                single_favorite_word.save()
            else:
                Favorite.objects.create(
                    word=word_obj, user=user, isFavorite=True)
            response_msg = {'error': False}
        except:
            response_msg = {'error': True}
        return Response(response_msg)












# продакт фэйворитс
# class ProductView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     authentication_classes = [TokenAuthentication, ]
#
#     def get(self, request):
#         query = Product.objects.all()
#         data = []
#         serializers = ProductSerializer(query, many=True)
#         for product in serializers.data:
#             fab_query = Favorire.objects.filter(user=request.user).filter(product_id=product['id'])
#             if fab_query:
#                 product['favorit'] = fab_query[0].isFavorit
#             else:
#                 product['favorit'] = False
#             data.append(product)
#         return Response(data)
#
#
# class FavoritView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     authentication_classes = [TokenAuthentication, ]
#
#     def post(self, request):
#         data = request.data["id"]
#         # print(data)
#         try:
#             product_obj = Product.objects.get(id=data)
#             # print(data)
#             user = request.user
#             single_favorit_product = Favorire.objects.filter(
#                 user=user).filter(product=product_obj).first()
#             if single_favorit_product:
#                 print("single_favorit_product")
#                 ccc = single_favorit_product.isFavorit
#                 single_favorit_product.isFavorit = not ccc
#                 single_favorit_product.save()
#             else:
#                 Favorire.objects.create(
#                     product=product_obj, user=user, isFavorit=True)
#             response_msg = {'error': False}
#         except:
#             response_msg = {'error': True}
#         return Response(response_msg)