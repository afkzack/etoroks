from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('trade/', views.trade, name='trade'),
    path('asset/', views.asset, name='asset'),
    path('profile/', views.profile, name='profile'),
    path('deposit/', views.deposit, name='deposit'),
    path('recharge/', views.recharge, name='recharge'),
    path('asset-btc/', views.btc, name='btc'),
    path('asset-usdc/', views.usdc, name='usdc'),
    path('asset-eth/', views.eth, name='eth'),
    path('asset-usd/', views.usd, name='usd'),
    path('asset-cny/', views.cny, name='cny'),
    path('asset-hkd/', views.hkd, name='hkd'),
    path('asset-jpy/', views.jpy, name='jpy'),
    path('asset-gbp/', views.gbp, name='gbp'),
    path('asset-eur/', views.eur, name='eur'),
    path('asset-usdt/', views.usdt, name='usdt'),

]