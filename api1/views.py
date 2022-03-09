
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework import  response
# from rest_framework import status
from rest_framework.response import Response
from .models import Employee,News1
from .serializers import EmployeeSerializer
from django.contrib.auth.decorators import login_required
import stripe
stripe.api_key="sk_test_51KMp9NSDFmlIF8i8R1VXbv9KMdVI1yrghYxnteLwVsltFVezFw2NM7dhC1uksqZhT8EoEJOvrz1MNjMR2gK4BAbg00fCQCFLbI"

class EmployeeList(APIView):
    
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        employee1=Employee.objects.all()
        serializer=EmployeeSerializer(employee1,many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

@login_required
def news(request):
    news=News1.objects.all()
    return render(request,'news.html',{'news':news})


#DONATION USING STRIPE

@login_required
def index(request):

	return render(request, 'index.html')

@login_required
def charge(request):
	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount,
			currency='inr',
			description="Donation"
			)
		
	



	return redirect(reverse('success', args=[amount]))

@login_required
def successMsg(request, args):
	amount = args
	return render(request, 'success.html', {'amount':amount})