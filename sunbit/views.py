from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'sunbit/index.html', {})

@login_required(login_url='login')
def home(request):
    return render(request, 'sunbit/home.html', {})

@login_required(login_url='login')
def market(request):
    return render(request, 'sunbit/market.html', {})

@login_required(login_url='login')
def deposit(request):
    return render(request, 'sunbit/deposit.html', {})

@login_required(login_url='login')
def asset(request):
    return render(request, 'sunbit/asset.html', {})

@login_required(login_url='login')
def btc(request):
    return render(request, 'sunbit/assets/btc.html', {})

@login_required(login_url='login')
def usdc(request):
    return render(request, 'sunbit/assets/usdc.html', {})

@login_required(login_url='login')
def eth(request):
    return render(request, 'sunbit/assets/eth.html', {})

@login_required(login_url='login')
def usd(request):
    return render(request, 'sunbit/assets/usd.html', {})

@login_required(login_url='login')
def cny(request):
    return render(request, 'sunbit/assets/cny.html', {})

@login_required(login_url='login')
def hkd(request):
    return render(request, 'sunbit/assets/hkd.html', {})

@login_required(login_url='login')
def jpy(request):
    return render(request, 'sunbit/assets/jpy.html', {})

@login_required(login_url='login')
def gbp(request):
    return render(request, 'sunbit/assets/gbp.html', {})

@login_required(login_url='login')
def eur(request):
    return render(request, 'sunbit/assets/eur.html', {})

@login_required(login_url='login')
def usdt(request):
    return render(request, 'sunbit/assets/usdt.html', {})

@login_required(login_url='login')
def trade(request):
    return render(request, 'sunbit/trade.html', {})

@login_required(login_url='login')
def recharge(request):
    return render(request, 'sunbit/recharge.html', {})

@login_required(login_url='login')
def show(request):
    return render(request, 'sunbit/show.html', {})

@login_required(login_url='login')
def profile(request):
    return render(request, 'sunbit/profile.html', {})


