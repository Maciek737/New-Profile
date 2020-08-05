from django.views.generic import ListView, CreateView, UpdateView # new
from django.urls import reverse_lazy # new
from .forms import ProfileForm # new
from django.views.generic import ListView
from .models import Profile


class HomePageView(ListView):
    model = Profile
    template_name = 'home.html'


class CreateProfileView(CreateView,ListView): # new
    model = Profile
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('add_profile')

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['name','picture']
    success_url = reverse_lazy('add_profile')