from django.urls import path
from .views import AccountList, AccountDetails

urlpatterns = [
    path('', AccountList.as_view()),
    path('<int:pk>/', AccountDetails.as_view()),
]