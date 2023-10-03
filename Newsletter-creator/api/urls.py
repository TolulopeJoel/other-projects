from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('posts', views.PostViewset, basename='posts')
router.register('subscribers', views.SubscriberViewset, basename='subscribers')

urlpatterns = router.urls
