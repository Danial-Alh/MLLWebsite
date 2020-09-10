from django.urls import include, path, re_path

from posts.views import PrivateStreamformStorageView

urlpatterns = [
    re_path('^(?P<path>.*)$', PrivateStreamformStorageView.as_view())
]