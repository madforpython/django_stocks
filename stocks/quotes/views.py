from django.shortcuts import render , redirect
from .models import stock
from .forms import StockForm
from django.contrib import messages


# Create your views here.
def home(request):
	import requests
	import json
	#pk_bf0e2f1333eb45819e2ebf9fbb7b63e5
	if request.method == 'POST':
		ticker = request.POST['ticker']

		api_request = requests.get('https://sandbox.iexapis.com/stable/stock/'+ticker+'/quote?token=Tsk_6528e864eb8d4f008715b7d64fbec8da')

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'Error...'
			return render(request,'home.html',{'api':api})
	else:
		return render(request,'home.html',{'ticker':'Enter a ticker symbol please'})

	

	return render(request,'home.html',{'api':api})

def about(request):
	return render(request,'about.html',{})

def addstocks(request):
	import requests
	import json
	if request.method == 'POST':
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,('Stock has been added'))
			return redirect('addstocks')

	else:
		ticker = stock.objects.all()
		output = []

		for ticker_item in ticker:
			api_request = requests.get('https://sandbox.iexapis.com/stable/stock/' + str(ticker_item) + '/quote?token=Tsk_6528e864eb8d4f008715b7d64fbec8da')

			try:
				api = json.loads(api_request.content)
				output.append(api)

			except Exception as e:
				api = 'Error...' 


		return render(request,'addstocks.html',{'ticker':ticker,'output':output})

def delete(request,stock_id):
	item = stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request,('Stock has been deleted'))
	return redirect('delete_stock')

def delete_stock(request):
	ticker = stock.objects.all()
	return render(request,'delete_stock.html',{'ticker':ticker})
















