from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .api.views import FormViewSet, SubmissionViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("forms", FormViewSet)
router.register("submissions", SubmissionViewSet)

app_name = "api-form"
urlpatterns = router.urls
