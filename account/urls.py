from django.urls import path

from account.views import HomeUserView, LoginUserView, create_user_and_company, ListUserView, LogoutUserView, \
    DeleteUserView, UpdateUserView

urlpatterns = [
    path('', HomeUserView.as_view(), name="home"),
    path('login/', LoginUserView.as_view(), name='login'),
    # path('condo/create/', CompanyCreateView.as_view(), name="condo_create"),
    # # path('create/', UserCreateView.as_view(), name="create"),
    path('create/', create_user_and_company, name="create"),
    path('list/', ListUserView.as_view(), name="list"),
    path('logout/', LogoutUserView.as_view(), name="logout"),
    # path('password/<int:pk>/', ChangePasswordView.as_view(), name='password'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update'),
    # path('profile/<int:pk>/', ProfileUserView.as_view(), name='profile'),
    # path('detail/<int:pk>/', DetailUserView.as_view(), name='detail'),
    # path('password-reset/', ResetPasswordView.as_view(), name='reset'),
    # path('password-reset/done/', ResetPasswordDoneView.as_view(), name='reset_done'),
    # path('password-reset/confirm/<uidb64>/<token>', ResetPasswordConfirmView.as_view(), name='reset_confirm'),
    # path('password-reset/complete/', ResetPasswordCompleteView.as_view(), name='reset_complete'),
    #
]
