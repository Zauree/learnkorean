
from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("word/<int:lesson>/", WordOfLessonView.as_view()),  # сол лессондағы сөздер
    path('favorites/', FavoriteView.as_view()),
    path("grammar/<int:lesson>/", GrammarOfLessonView.as_view()),  # сол лессондағы грамматика
    path("reading/<int:lesson>/", ReadingOfLessonView.as_view()),  # сол лессондағы оқылым
    path("listening/<int:lesson>/", ListeningOfLessonView.as_view()),  # сол лессондағы тыңдалым

    path("wordoftopic/<int:topic_word>/", WordOfTopicView.as_view()),  # сол топиктағы(тақырыnтағы) сөздер

    path('lessons/', LessonAllViews.as_view()),      # барлық лессондар без фильтра
    path('topics/', TopicAllViews.as_view()),    # барлық топиктар без фильтра
    path('grammars/', GrammarAllView.as_view()),  # барлық грамматикалар без фильтра
    path('words/', WordAllView.as_view()),        # барлық cөздер без фильтра
    path('readings/', ReadingAllView.as_view()),  # барлық оқылымдар без фильтра
    path('listenings/', ListeningAllView.as_view()),  # барлық тыңдалымдар без фильтра


    path('user/', UserView.as_view()),
    path('login/', obtain_auth_token),
    path('register/', Register.as_view()),

    path("hello/", helloAPI),
  #  path("quiz/<int:id>", randomQuiz),    # тура ағайдың логикасы бойынша
    path("quiz/<int:lesson>/", randomQuizByLesson),       # лессонға байланыста prefetch бар менде жақсы істеп тұр, осы істемей жатса жоғарыдағы ағайдікі






    # бұрыңғылар вдруг керек болса
    # path("word", WordView.as_view()),                                    # сөздер лессонға қатысты шығаруы мүмкін
    # path("lesson/<int:lesson>/word/", WordByLessonView.as_view()),       # сол лессондағы сөздер
    # path("word/lesson/<int:lesson>/", WordByLessonView.as_view()),       # сол лессондағы сөздер
    # path("word/topic/<int:topic_word>/", WordByTopicView.as_view()),     # сол топиктағы сөздер
    # path('products/', ProductView.as_view()),
    # path('favorit/', FavoritView.as_view()),

]