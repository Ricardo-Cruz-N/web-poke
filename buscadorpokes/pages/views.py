from .models import Page
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.admin.views.decorators import  staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .forms import PageForm

class StaffRequiredMixing(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixing, self).dispatch(request, *args, **kwargs)

class PokeListView(ListView):
    model = Page

class PokeDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PokePageCreate(CreateView):
    model = Page
    form_class = PageForm
    def get_success_url(self):
        return reverse('pages:pages')