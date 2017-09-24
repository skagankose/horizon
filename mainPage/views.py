from django.shortcuts import render
from .models import *
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
# from .helpers.userRetriever import *
from .helpers import userRetriever
from .helpers import massAdd
from django.template.defaulttags import register
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@register.filter
def bigger(link):
	return(link.replace("_normal", ""))

@register.filter
def twitterLink(screenName):
	return("https://www.twitter.com/" + screenName)

def index(request):
	context = {}
	return render(request, 'index.html', context)

def twitter(request):
	accounts = TwitterAccount.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(accounts, 10)

	try:
		accounts = paginator.page(page)
	except PageNotAnInteger:
		accounts = paginator.page(1)
	except EmptyPage:
		accounts = paginator.page(paginator.num_pages)

	context = {"accounts":accounts}
	return render(request, 'twitter.html', context)

# add account
def userSearch(request):
	if request.method == 'POST':
		inputText = request.POST['textSearch']
	else:
		inputText = None

	message = userRetriever.getUser(inputText)
	messageV2 = userRetriever.getTweet(inputText)

	accounts = TwitterAccount.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(accounts, 10)

	try:
		accounts = paginator.page(page)
	except PageNotAnInteger:
		accounts = paginator.page(1)
	except EmptyPage:
		accounts = paginator.page(paginator.num_pages)

	context = {"accounts":accounts, "message":message}
	return render(request, 'ajaxSearch.html', context)

# mass add accounts
def addTogether(request):

	message = massAdd.main()

	accounts = TwitterAccount.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(accounts, 10)

	try:
		accounts = paginator.page(page)
	except PageNotAnInteger:
		accounts = paginator.page(1)
	except EmptyPage:
		accounts = paginator.page(paginator.num_pages)

	context = {"accounts":accounts,"message":message,}
	return render(request, 'ajaxSearch.html', context)

# search account
def userSearchV2(request):
	if request.method == 'POST':
		inputText = request.POST['textSearch']
	else:
		inputText = None

	accounts = TwitterAccount.objects.filter(fullName__icontains = inputText)
	page = request.GET.get('page', 1)
	paginator = Paginator(accounts, 10)

	try:
		accounts = paginator.page(page)
	except PageNotAnInteger:
		accounts = paginator.page(1)
	except EmptyPage:
		accounts = paginator.page(paginator.num_pages)

	context = {"accounts":accounts}
	return render(request, 'ajaxSearch.html', context)

def account(request, userName):
	account = TwitterAccount.objects.get(screenName=userName)
	tweets = Tweet.objects.filter(relatedAccount=account)[:10]
	context = {"account":account, 'tweets':tweets}
	return render(request, 'account.html', context)
