from rest_framework.routers import DefaultRouter
from django.urls import  path,include
from .views import *
from readers.views import AllReaders
router = DefaultRouter()
router.register('genres',AllGenres)
router.register('books',AllBooks)
router.register('readers',AllReaders)
router.register('comments',CommentWrite)
urlpatterns = [
    path('',include(router.urls)),
    path('more',MoreViewed.as_view())
]