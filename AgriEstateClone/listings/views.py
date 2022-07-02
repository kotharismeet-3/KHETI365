from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Listing
#from .forms import ListingForm
from django.urls import reverse_lazy
import datetime
import uuid
# Create your views here.


def home(request):
    return render(request, 'home.html')


class ListingListView(ListView):
    model = Listing
    template_name = 'listing.html'
    listings = Listing.objects.all()
    context_object_name = 'listings'
    # ordering = [-'list_date']


class ListingDetailView(DetailView):
    model = Listing
    template_name = 'details.html'


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = '__all__'
    template = 'listings/listing_form.html'
    success_url = reverse_lazy('listing')
    #form_class = ListingForm

    '''def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.id = uuid.uuid4()
        form.instamce.list_date = datetime.datetime.now()
        # print(super().form_valid(form))
        return super().form_valid(form)
    if form_valid(self, form):
        form.save()'''


class ListingUpdateView(LoginRequiredMixin, UserPassesTestMixin, FormView, UpdateView):
    model = Listing
    fields = '__all__'
    template = 'listings/listing_form.html'
    success_url = reverse_lazy('listing')
    '''def test_func(self):
        listing = self.get_object()
        #print(self.request.user, listing.owner)
        if(self.request.user == listing.owner):
            return True
        else:
            return False'''


class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = '/'

    def test_func(self):
        listing = self.get_object()
        #print(self.request.user, listing.owner)
        if(self.request.user == listing.owner):
            return True
        else:
            return False
