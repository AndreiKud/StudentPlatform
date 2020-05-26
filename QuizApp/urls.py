from django.conf.urls import url
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [url(regex=r'^$',
                   view=login_required(QuizListView.as_view()),
                   name='quiz_index'),

               url(regex=r'^category/$',
                   view=login_required(CategoriesListView.as_view()),
                   name='quiz_category_list_all'),

               url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                   view=login_required(ViewQuizListByCategory.as_view()),
                   name='quiz_category_list_matching'),

               url(regex=r'^progress/$',
                   view=login_required(QuizUserProgressView.as_view()),
                   name='quiz_progress'),

               url(regex=r'^marking/$',
                   view=login_required(QuizMarkingList.as_view()),
                   name='quiz_marking'),

               url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                   view=login_required(QuizMarkingDetail.as_view()),
                   name='quiz_marking_detail'),

               #  passes variable 'quiz_name' to quiz_take view
               url(regex=r'^(?P<slug>[\w-]+)/$',
                   view=login_required(QuizDetailView.as_view()),
                   name='quiz_start_page'),

               url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                   view=login_required(QuizTake.as_view()),
                   name='quiz_question'),
               ]
