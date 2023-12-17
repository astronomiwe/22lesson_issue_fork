from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class PostListView(ListView):
    pass


class PostCreateView(CreateView):
    pass


class PostDetailView(DetailView):
    pass

class PostUpdateView(UpdateView):
    pass


class PostDeleteView(DeleteView):
    pass