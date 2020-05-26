from UserApp import views as user_views
from QuizApp import urls as quiz_urls
from django.urls import path, include
from . import views as platfrom_views
from django.contrib.auth import views as auth_views
from machina import urls as machina_urls


# FIXME
import sys
sys.path.append('/UserApp')
# sys.path.append('/QuizApp')


urlpatterns = [
     path("", platfrom_views.home, name="platform-home"),
     path("forum/", include(machina_urls)),
     path("about/", platfrom_views.about, name="platform-about"),
     path("quiz/", include(quiz_urls)),
     path("webinar/", platfrom_views.webinar_test, name="webinar-test"),

     path("registration/", user_views.register, name="user-registration"),
     path("profile/", user_views.profile, name="user-profile"),

     path("login/", auth_views.LoginView.as_view(template_name="UserApp/login.html"),
          name="user-login"),
     path("logout/", auth_views.LogoutView.as_view(template_name="UserApp/logout.html"),
          name="user-logout"),

     path("projects/all/", platfrom_views.StudyProjectListView.as_view(),
          name="project-all"),
     path("projects/done/", platfrom_views.DoneStudyProjectListView.as_view(),
          name="project-done"),
    path("projects/mine/", platfrom_views.MyStudyProjectListView.as_view(),
         name="project-mine"),
     path("projects/new/", platfrom_views.StudyProjectCreateView.as_view(),
          name="project-new"),

     path("qualifications/", platfrom_views.QualificationsListView.as_view(),
          name="qualifications"),

     path('projects/<int:pk>/', platfrom_views.StudyProjectDetailView.as_view(), name='project-detail'),
     path('projects/<int:pk>/update', platfrom_views.StudyProjectUpdateView.as_view(), name='project-update'),
     # path('projects/<int:pk>/download', platfrom_views.download_attachment, name='project-update'),
     # path('projects/<int:pk>/add_review/', platfrom_views.add_review, name='project-add-review'),
]
