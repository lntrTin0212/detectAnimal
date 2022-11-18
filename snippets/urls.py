from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views as snippet
from animal import views as animal

urlpatterns = [
    path('snippets/', snippet.snippet_list),
    path('snippets/<int:pk>/', snippet.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)