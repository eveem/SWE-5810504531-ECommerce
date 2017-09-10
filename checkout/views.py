from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def checkout(request):
	if request.method == 'POST':
		token = request.POST['stripeToken']
	context = {'publishKey': publishKey}
	template = 'checkout.html'
	return render(request, template, context)