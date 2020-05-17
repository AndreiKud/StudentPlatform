from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class StudyProject(models.Model):
    STATUS_READY = 'ЗАКРЫТЫЙ'
    STATUS_NOT_READY = 'ОТКРЫТЫЙ'
    STATUS_CHOISES = (
        (STATUS_READY, 'Закрытый'),
        (STATUS_NOT_READY, 'Открытый'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()

    customer = models.CharField(max_length=100, default="empty")
    executor = models.CharField(max_length=100, default="empty")

    date_created = models.DateTimeField(default=timezone.now, verbose_name="Created on")
    date_deadline = models.DateTimeField(default=timezone.now, verbose_name="Deadline on")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    status = models.CharField(max_length=100, choices=STATUS_CHOISES, default=STATUS_NOT_READY)

    # For querying convenience.
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


class Review(models.Model):
    MARK_NONE = 'БЕЗ ОЦЕНКИ'
    MARK_SUPERBAD = 'УЖАСНО'
    MARK_BAD = 'ПЛОХО'
    MARK_NORM = 'УДОВЛЕТВОРИТЕЛЬНО'
    MARK_GOOD = 'ХОРОШО'
    MARK_EXCELLENT = 'ОТЛИЧНО'
    MARK_CHOISES = (
        (MARK_NONE, 'Без оценки'),
        (MARK_SUPERBAD, 'Ужасно'),
        (MARK_BAD, 'Плохо'),
        (MARK_NORM, 'Удовлетворительно'),
        (MARK_GOOD, 'Хорошо'),
        (MARK_EXCELLENT, 'Отлично'),
    )

    project = models.ForeignKey(StudyProject, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.CharField(max_length=100, choices=MARK_CHOISES, default=MARK_NONE)

    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return 'Review by {}'.format(self.author)


# class StudyTest(models.Model):
#     title =


# class StudyTestQuestion(models.Model):
#     question = models.TextField()
