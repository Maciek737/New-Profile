

from django.urls import path

from .views import HomePageView, CreateProfileView, ProfileUpdate

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', CreateProfileView.as_view(), name='add_profile'),
    path('<pk>/update', ProfileUpdate.as_view())
]