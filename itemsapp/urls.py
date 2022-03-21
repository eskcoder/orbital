from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter

from itemsapp.models import Item
from .import views


router= SimpleRouter()
router.register('items', views.ItemViewSet,basename=Item)
urlpatterns = router.urls
