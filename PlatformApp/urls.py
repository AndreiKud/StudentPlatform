from django.urls import path
from . import views as platfrom_views


# FIXME
import sys
sys.path.append('/UserApp')
from UserApp import views as user_views


urlpatterns = [
    path("", platfrom_views.home, name="platform-home"),
    path("about/", platfrom_views.about, name="platform-about"),
    path("registration/", user_views.register, name="user-registration"),
]