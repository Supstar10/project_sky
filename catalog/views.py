from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Contact, Blog
from config import settings


class ProductListView(ListView):
    model = Product
    paginate_by = 4

class ContactsListView(TemplateView):
    template_name = "catalog/contact_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Contact.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product


class CreateProductListView(CreateView):
    model = Product
    fields = ("name", "price", "category", "preview", "description")
    success_url = reverse_lazy('catalog:home')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "price", "category", "preview", "description")
    success_url = reverse_lazy('catalog:home')
class BlogListView(ListView):
    model = Blog
    #queryset = Blog.objects.filter(is_published=True).order_by('-created_at')

class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("heading", "content", "preview", "count_views")
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save()
            obj.slug = slugify(obj.title)
            obj.save()
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("heading", "slug", "content", "preview", "sing_of_publication")
    success_url = reverse_lazy("catalog:blog_list")

    def get_success_url(self):
        return reverse('catalog:detail_blog', args=[self.kwargs.get('slug')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_list")

