from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('todo/update/<int:todo_id>/', update_user_todo, name='update_user_todo'),
    path('todo/delete/<int:todo_id>/', delete_user_todo, name='delete_user_todo'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
    path('signup/', signup, name='signup'),
    path('confirm/', confirm, name='confirm'),
    path('success/', success, name='success'),
    path('logout/', signout, name='logout'),
    path('login/', user_login, name='login'),

    path('reset_password/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
