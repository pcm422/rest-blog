from django.urls import path, include
from rest_framework import routers

from blog.views import api_view_set_views

app_name = 'view_set_api'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', api_view_set_views.UserViewSet, 'user')
router.register(r'blogs', api_view_set_views.BlogViewSet, 'blog')

urlpatterns = [
    # path('', api_views.blog_list, name='blog_list'),
    path('', include(router.urls))
]