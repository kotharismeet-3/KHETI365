from django.urls import path
import uuid
from .views import (
    home,
    ListingListView,
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView,
    ListingListView
)

urlpatterns = [
    path('', home, name='home'),
    path('listing', ListingListView.as_view(), name='listing'),
    path('listing/create', ListingCreateView.as_view(), name='create-listing'),
    path('listing/<uuid:pk>/update',
         ListingUpdateView.as_view(),
         name='update-listing'
         ),
    path('listing/<uuid:pk>/delete',
         ListingDeleteView.as_view(),
         name='delete-listing'
         ),
    path('listing/<uuid:pk>/', ListingListView.as_view(), name='listing-detail'),
]
