# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from api.views import RamView

router = routers.DefaultRouter()
# router.register(r'ram', views.RamViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('ram/', RamView.as_view()),
    path('ram/<int:id>/', RamView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]