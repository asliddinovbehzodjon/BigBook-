from rest_framework.routers import DefaultRouter
from django.urls import  path,include
from .views import *
from readers.views import AllReaders,BotUsersAll,TimeInfo
router = DefaultRouter()
router.register('genres',AllGenres)
router.register('books',AllBooks)
router.register('readers',AllReaders)
router.register('comments',CommentWrite)
router.register('botusers',BotUsersAll)
urlpatterns = [
    path('',include(router.urls)),
    path('more',MoreDownloaded.as_view()),
    path('search/<str:key>/',SearchBook.as_view()),
    path('status',TimeInfo.as_view())
    path('moregenre/<int:genre>/<int:id>/',MoreGenre.as_view())
]