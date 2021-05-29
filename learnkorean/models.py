import gtts
import tempfile
from django.db import models
from django.core.files import File
from django.contrib.auth.models import User


class Lesson(models.Model):
    title_korean = models.CharField(max_length=100, default='1 Сабақ. ', unique=True)
    title_kazakh = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.title_korean

    class Meta:
        verbose_name = 'Сабақ'
        verbose_name_plural = 'Сабақтар'
        ordering = ['order']


class TopicWord(models.Model):
    topic_name_korean = models.CharField(max_length=100, unique=True)
    topic_name_kazakh = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.topic_name_kazakh

    class Meta:
        verbose_name = 'Тақырып'
        verbose_name_plural = 'Тақырыптар'
        ordering = ['order']


class Word(models.Model):
    PART_OF_SPEECH_CHOICES = [
        ('Зат', 'Зат есім'),
        ('Сын', 'Сын есім'),
        ('Сан', 'Сан есім'),
        ('Ес', 'Есімдік'),
        ('Ет', 'Етістік'),
        ('Ү', 'Үстеу'),
        ('Еліктеу', 'Еліктеу сөздер'),
        ('Ш', 'Шылау'),
        ('О', 'Одағай'),
    ]

    word_korean = models.CharField(max_length=100, unique=True)
    word_kazakh = models.CharField(max_length=100, unique=True)
    part_of_speech = models.CharField(max_length=100, choices=PART_OF_SPEECH_CHOICES, default='Зат есім')
    transcription = models.CharField(max_length=150, default='[]')
    example_korean_one = models.CharField(max_length=250)
    example_kazakh_one = models.CharField(max_length=250)
    example_korean_two = models.CharField(max_length=250)
    example_kazakh_two = models.CharField(max_length=250)
    example_korean_three = models.CharField(max_length=250)
    example_kazakh_three = models.CharField(max_length=250)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    topic_word = models.ForeignKey(TopicWord, on_delete=models.CASCADE)
    audio = models.FileField()

    # audio = models.FileField(upload_to='audio/', blank=True)
    #
    # def save(self, *args, **kwargs):
    #     audio = gtts(text=self.word_korean, lang='ko', slow=True)
    #
    #     with tempfile.TemporaryFile(mode='w') as f:
    #         audio.write_to_fp(f)
    #         file_name = '{}.mp3'.format(self.word_vocab)
    #         self.audio.save(file_name, File(file=f))
    #
    #     super(Word, self).save(*args, **kwargs)

    #audio

    def __str__(self):
        return self.word_kazakh

    class Meta:
        verbose_name = 'Сөз'
        verbose_name_plural = 'Сөздер'


class Favorite(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.Case)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return f"wordID ={self.word.id}user={self.user.username}|ISFavorite={self.isFavorite}"

    class Meta:
        verbose_name = 'Сөз'
        verbose_name_plural = 'Менің сөздігім'


class Grammar(models.Model):
    rule_korean = models.CharField(max_length=100, unique=True)
    rule_kazakh = models.CharField(max_length=100, unique=True)
    general_rule = models.CharField(max_length=255, unique=True)
    example_korean_one = models.CharField(max_length=250)
    example_kazakh_one = models.CharField(max_length=250)
    example_korean_two = models.CharField(max_length=250)
    example_kazakh_two = models.CharField(max_length=250)
    example_korean_three = models.CharField(max_length=250)
    example_kazakh_three = models.CharField(max_length=250)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.rule_kazakh

    class Meta:
        verbose_name = 'Грамматика'
        verbose_name_plural = 'Грамматикалар'


class Reading(models.Model):
    dialogue_korean = models.CharField(max_length=255, unique=True)
    dialogue_kazakh = models.CharField(max_length=255, unique=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    audio = models.FileField()

    def __str__(self):
        return self.dialogue_kazakh

    class Meta:
        verbose_name = 'Оқылым'
        verbose_name_plural = 'Оқылымдар'


class Listening(models.Model):
    name = models.CharField(max_length=100, unique=True)
    transcription = models.CharField(max_length=255, unique=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    audio = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тыңдалым'
        verbose_name_plural = 'Тыңдалымдар'


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жаттығу'
        verbose_name_plural = 'Жаттығулар'





# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Product(models.Model):
#     title = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     marcket_price = models.PositiveIntegerField()
#     selling_price = models.PositiveIntegerField()
#     description = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#
# class Favorire(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.Case)
#     isFavorit = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"productID ={self.product.id}user={self.user.username}|ISFavorite={self.isFavorit}"