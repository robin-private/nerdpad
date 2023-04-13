from rest_framework import routers
from notes.views import NoteViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
urlpatterns = []+router.urls
