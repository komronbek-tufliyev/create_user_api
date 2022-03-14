from django.shortcuts import render
from .forms import CreateUserForm
from django.views.generic import FormView


# Create your views here.
class CreateUserView(FormView):
    form_class = CreateUserForm
    template_name = 'create_user.html'
    success_url = '/users/add/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


