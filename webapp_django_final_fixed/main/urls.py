from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("chat/", views.chat_view, name="chat"),
    path("email/", views.email_view, name="email"),
    path("listprop/", views.listprop_view, name="listprop"),
    path("profile/", views.profile_view, name="profile"),
    path("signup/", views.signup_view, name="signup"),
    path("user/", views.user_view, name="user"),
    path("search/", views.search_view, name="search"),
    
    # Hostel detail and booking routes
    path("hostel/<int:hostel_id>/", views.hostel_detail_view, name="hostel_detail"),
    path("hostel/<int:hostel_id>/book/", views.book_hostel_view, name="book_hostel"),
    path("hostel/<int:hostel_id>/review/", views.add_review_view, name="add_review"),
    path("booking/confirmation/", views.booking_confirmation_view, name="booking_confirmation"),
    path('my-bookings/', views.my_bookings_view, name='my_bookings'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking_view, name='cancel_booking'),
    path('all-deals/', views.all_deals_view, name='all_deals'),
    path('help-center/', views.help_center_view, name='help_center'),
    path('hostel-awards/', views.hostel_awards_view, name='hostel_awards'),
    
    # API endpoints for Flask integration
    path("api/hostels/", views.api_hostels_view, name="api_hostels"),
    path("api/hostels/<int:hostel_id>/", views.api_hostel_detail_view, name="api_hostel_detail"),
    path("api/hostels/<int:hostel_id>/book/", views.api_book_hostel_view, name="api_book_hostel"),
    path('api/user-bookings/<int:user_id>/', views.api_user_bookings_view, name='api_user_bookings'),
    path('api/cancel-booking/<int:booking_id>/', views.api_cancel_booking_view, name='api_cancel_booking'),
    path('api/bookings/', views.api_bookings_view, name='api_bookings'),  # New endpoint
]
