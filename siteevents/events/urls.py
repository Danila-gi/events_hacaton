from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('registration/', views.registration, name='registration'),
    # path('login/', views.login, name='login'),
    path('api/auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('api/auth/registration/', views.RegistrationAPIView.as_view(), name='registration'),
    path('api/auth/tags_get/', views.TagsGetAPIView.as_view(), name='tags_get'),
    path('api/auth/tags_send/', views.TagsSendAPIView.as_view(), name='tags_send'),
    path('api/auth/events_get/', views.FavouritesGetAPIView.as_view(), name='events_get'),
    path('api/auth/events_send/', views.FavouritesSendAPIView.as_view(), name='events_send'),
]