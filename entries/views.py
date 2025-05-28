from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Entry, Profile
from .forms import EntryForm, ProfileForm

class EntryListView(LoginRequiredMixin, ListView): #Lists all users journal entries
    model = Entry
    context_object_name = 'entries'

    def get_queryset(self): #Only show entries of logged in user
        return Entry.objects.filter(user=self.request.user)


class EntryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView): #Journal entry per id/pk
    model = Entry

    def test_func(self): #Only allows access if entry belongs to user
        entry = self.get_object()
        return entry.user == self.request.user 

class EntryCreateView(LoginRequiredMixin, CreateView): #POST
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('entries:entry_list') #Redirects to entry list if success

    def form_valid(self, form): #Assigns logged in user as author before saving
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EntryUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): #To update and edit journal entry
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('entries:entry_list')

    def test_func(self): #Allows users to only edit their own entries
        entry = self.get_object()
        return entry.user == self.request.user
    
class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #To delete journal entry
    model = Entry
    success_url = reverse_lazy('entries:entry_list')

    def test_func(self): #Allows users to only delete their own entries
        entry = self.get_object()
        return entry.user == self.request.user
    


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'entries/edit_profile.html'
    success_url = reverse_lazy('entries:entry_list')

    def get_object(self, queryset=None):
        # Return the current user's profile only
        return self.request.user.profile