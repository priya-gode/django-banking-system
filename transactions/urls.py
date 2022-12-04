from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView, HomeView , ContactView,AboutView,FeedbackView ,ThanksView,LoanView

app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(),name="deposit_money"),
    path("report/", TransactionRepostView.as_view(),name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(),name="withdraw_money"),
    path("home/",HomeView.as_view(),name='home'),
    path("contact/",ContactView.as_view(),name='contact'),
    path("about/",AboutView.as_view(),name='about'),
    path("feedback/",FeedbackView.as_view(),name='feedback'),
    path("loan/",LoanView.as_view(),name='loan'),

]
