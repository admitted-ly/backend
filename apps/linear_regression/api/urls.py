from django.urls import path
from apps.linear_regression.api.views import *

urlpatterns = [

    path('user/recommendations', RecommendCollege.as_view(),name="recommend-colleges"),
]