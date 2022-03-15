from . import views
from django.conf.urls import url
from django.urls import path, re_path
from pages.views import author_profiles, ChangePassword, DevProfileView, home, my_profile, portfolio, update_profile

app_name = 'pages'

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^author_profiles/(?P<id>[0-9]+)/$',
            author_profiles, name='author_profiles'),
    path('change-password/', ChangePassword.as_view(
        template_name='pages/change_password.html'), name='change-password'),
    path('my_profile/', my_profile, name='my_profile'),
    path('my_profile/update/', update_profile, name='update_profile'),
    path('password_success/', views.password_success, name='password_success'),
    path('developer_profile/', DevProfileView.as_view(), name='developer_profile'),
]
