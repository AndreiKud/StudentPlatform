from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.urls import reverse

fs = FileSystemStorage(location='/proj_files')


class StudyProject(models.Model):
    STATUS_READY = 'ЗАКРЫТЫЙ'
    STATUS_NOT_READY = 'ОТКРЫТЫЙ'
    STATUS_CHOISES = (
        (STATUS_READY, 'Закрытый'),
        (STATUS_NOT_READY, 'Открытый'),
    )

    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)

    customer = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='project_customer', verbose_name='Заказчик', blank=True)
    executor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, related_name='project_executor', verbose_name='Исполнитель', blank=True)

    date_created = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')
    date_deadline = models.DateTimeField(
        default=timezone.now, verbose_name='Срок выполения')
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='project_author', verbose_name='Создатель проекта')

    attached_file = models.FileField(
        upload_to='proj_files', null=True, verbose_name='Прикрепленные файлы', blank=True)

    status = models.CharField(
        max_length=100, choices=STATUS_CHOISES, default=STATUS_NOT_READY, verbose_name='Статус')

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

    project = models.ForeignKey(
        StudyProject, on_delete=models.CASCADE, verbose_name='Проект')
    content = models.TextField(verbose_name='Текст')
    date_created = models.DateTimeField(
        default=timezone.now, verbose_name='Дата написания')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    mark = models.CharField(
        max_length=100, choices=MARK_CHOISES, default=MARK_NONE, verbose_name='Оценка')

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return 'Review by {}'.format(self.author)


class Qualification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    done_projects_count = models.IntegerField()

    def __str__(self):
        return 'Qualification for {}'.format(self.user)
