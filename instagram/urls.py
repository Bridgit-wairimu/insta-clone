from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$',views.welcome,name = 'welcome'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^NewPost/', views.NewPost, name='newpost'),
    url(r'^EditProfile/', views.EditProfile, name='edit_profile'),
    url(r'^comment/', views.comment, name='one_post'),
    url(r'^signup/', views.Signup, name='signup'),
    url(r'^like/', views.like, name='likepage')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    