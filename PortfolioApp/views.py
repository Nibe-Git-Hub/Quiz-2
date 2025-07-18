from django.shortcuts import render
from django.contrib.auth.models import User # Required for linking to the built-in User model
from django.views.generic import DetailView, DeleteView # For Class-Based Views
from django.urls import reverse_lazy # Used for redirecting after CBV actions
from .models import Portfolio, Project # Your custom models

# Create your views here.

def applicant_list_view(request):
    applicants = User.objects.filter(portfolio__isnull=False).select_related('portfolio').order_by('username')

    context = {
        'applicants': applicants,
        'position_applying_for': 'Junior Developer'
    }
    return render(request, 'list.html', context)

class ApplicantDetailView(DetailView):
    model = User
    template_name = 'portfolio.html'
    context_object_name = 'applicant_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['portfolio'] = Portfolio.objects.get(user=self.object)
        except Portfolio.DoesNotExist:
            context['portfolio'] = None
        return context

class ApplicantDeleteView(DeleteView):
    model = User
    template_name = 'portfolio_confirm_delete.html'
    context_object_name = 'applicant_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = reverse_lazy('PortfolioApp:applicant_list')

    def form_valid(self, form):
        return super().form_valid(form)