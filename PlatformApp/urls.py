from UserApp import views as user_views
from django.urls import path
from . import views as platfrom_views
from django.contrib.auth import views as auth_views


# FIXME
import sys
sys.path.append('/UserApp')


urlpatterns = [
    path("", platfrom_views.home, name="platform-home"),
    path("about/", platfrom_views.about, name="platform-about"),

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
    path("projects/new/", platfrom_views.StudyProjectCreateView.as_view(),
         name="project-new"),

    path('projects/<int:pk>/', platfrom_views.StudyProjectDetailView.as_view(), name='project-detail'),
#     path('projects/<int:pk>/add_review/', platfrom_views.add_review, name='project-add-review'),
]
