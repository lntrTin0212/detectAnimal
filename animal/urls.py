from xml.etree.ElementInclude import include
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views as snippet
from . import views as animal
# from . import cloudinary as cloud
urlpatterns = [
    path('animal/', animal.animal),
]

urlpatterns = format_suffix_patterns(urlpatterns)