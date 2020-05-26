from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.contrib import messages
from .models import StudyProject, Review
from .forms import ProjectReviewForm


def home(request):
    return render(request, 'PlatformApp/home.html')


def about(request):
    return render(request, 'PlatformApp/about.html')


def webinar_test(request):
    return render(request, 'PlatformApp/webinar.html')


class StudyProjectUpdateView(UpdateView):
    model = StudyProject
    fields = ['title', 'description', 'customer', 'executor',
              'date_created', 'date_deadline', 'author', 'status']


class StudyProjectDetailView(FormMixin, DetailView):
    form_class = ProjectReviewForm
    model = StudyProject

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(project=self.get_object())
        context["review_form"] = ProjectReviewForm()

        return context

    def get_initial(self):
        return ({'project-detail': self.get_object()})

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(StudyProject, pk=kwargs["pk"])
        form = ProjectReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.project = project
            review.save()
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        is_valid = super().form_valid(form)
        if is_valid:
            messages.success(self.request, u"Ваш отзыв добавлен!")

        return is_valid


class StudyProjectListView(ListView):
    model = StudyProject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DoneStudyProjectListView(ListView):
    model = StudyProject
    template_name = 'PlatformApp/done_studyproject_list.html'

    def get_queryset(self):
        queryset = StudyProject.objects.filter(
            status=StudyProject.STATUS_READY)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MyStudyProjectListView(ListView):
    model = StudyProject
    template_name = 'PlatformApp/my_studyproject_list.html'

    def get_queryset(self):
        queryset = StudyProject.objects.filter(
            executor=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudyProjectCreateView(CreateView):
    model = StudyProject
    fields = ['title', 'description', 'date_deadline']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return "/platform/"


class ReviewCreateView(CreateView):
    model = Review
    fields = ['mark', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return "/platform/"
