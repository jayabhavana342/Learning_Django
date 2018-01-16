from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView

User = get_user_model()


# Create your views here.

class ProfileDetailView(DetailView):
    queryset = User.objects.filter(is_active=True)
    template_name = "profiles/user.html"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username", None)
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)
