from django.conf.urls import include, url
from rest_framework.authtoken import views as authviews

urlpatterns = [
    url(r'^', include('tweets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth', authviews.obtain_auth_token),
]
