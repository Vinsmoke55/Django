from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
	# path('login/',auth_views.LoginView.as_view(),name="login"),
	# path('logout/',auth_views.LogoutView.as_view(),name='logout'),
	# path('signup/',views.signup,name='signup'),
	# path('password_rese/', auth_views.PasswordResetView.as_view(), name='password_rese'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
 #    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
 #    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]