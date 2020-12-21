from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.views import generic

from photo.models import Photo, PhotoCategory


class PhotoLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_staff:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class PhotoView(PhotoLoginRequiredMixin, generic.ListView):
    model = Photo
    template_name = "photo.html"
    context_object_name = "photos"

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super(PhotoView, self).get_context_data()
        categories = PhotoCategory.objects.all()
        categories = [{"name": _.name, "description": _.description} for _ in categories]
        context_data["categories"] = categories
        category = self.request.GET.get("category", None)
        context_data["category"] = category if category else PhotoCategory.objects.order_by("-created_at").first().name
        return context_data

    def get_queryset(self):
        category_name = self.request.GET.get("category", None)
        if category_name:
            return Photo.objects.filter(category__name=category_name)
        category = PhotoCategory.objects.order_by("-created_at").first()
        return Photo.objects.filter(category=category)
