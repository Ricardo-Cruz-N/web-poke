from django.urls import path
from . import views
from .views import PokeListView, PokeDetailView, PokePageCreate
pages_patterns = ([
    path('', PokeListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', PokeDetailView.as_view(), name='page'),
    path('create/', PokePageCreate.as_view(), name='create'),
],'pages')