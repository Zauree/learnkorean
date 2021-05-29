from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


admin.site.register([Lesson, TopicWord, Word, Grammar, Reading, Listening, Quiz, Favorite]) #Product, Favorire, Category,