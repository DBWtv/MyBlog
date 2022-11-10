from django.urls import path
from .views import profile_veiw, reg_user

urlpatterns = [
    path('profile/', profile_veiw, name='profile'),
    path('new_profile/', reg_user, name='reg_user'),

]