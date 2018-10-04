from django.conf.urls import include, url
from .views import MachineLearningView
from web import views

urlpatterns = [
    url(
        r'^$',
        MachineLearningView.as_view(),
        name='machine-learning'),
]