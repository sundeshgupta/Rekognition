# from rest_framework.decorators import api_view
from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.IMAGE_FR.as_view(), name='image_api'),
    path('old_video/', views.VIDEO_FR.as_view(), name='video_api'),
    path('embed/', views.EMBEDDING.as_view(), name='embed_api'),
    path('video/', views.ASYNC_VIDEOFR.as_view(), name='celery_test_api'),
    path('feedback/', views.FeedbackFeature.as_view(), name='feedback_api'),
    path('nsfw/', views.NSFW_Recognise.as_view(), name='nsfw'),
    path('ytstream/', views.STREAM_VIDEO_FR.as_view(), name='youtube_process'),
    path('simface/', views.SIMILAR_FACE.as_view(), name='similar_face'),

]
