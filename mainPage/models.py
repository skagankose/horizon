from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class CustomPerson(models.Model):
	fullName = models.CharField(max_length=200, default='')
	avatar = models.ImageField(upload_to='mainPage/static/img/', blank=True, null=True)
	createdDate = models.DateTimeField(default=timezone.now)
	updatedDate = models.DateTimeField(default=timezone.now)
	slug= models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.fullName)
		try:
			this = CustomPerson.objects.get(pk=self.pk)
			if this.avatar != self.avatar and this.avatar != 'mainPage/static/img/avatar.png':
				this.avatar.delete(save=False)
		except: pass
		super(CustomPerson, self).save(*args, **kwargs)

	def __str__(self):
		return self.fullName


class TwitterAccount(models.Model):
	relatedPerson = models.ForeignKey(CustomPerson, related_name="twitterAccount", blank=True, null=True)
	userID = models.IntegerField(default=0)
	screenName = models.CharField(max_length=200, default='')
	fullName = models.CharField(max_length=200, default='')
	joined = models.CharField(max_length=200, default='')
	description = models.TextField()
	url = models.TextField()
	likeCount = models.IntegerField(default=0)
	followersCount = models.IntegerField(default=0)
	followeeCount = models.IntegerField(default=0)
	language = models.CharField(max_length=50, default='')
	listedCount = models.IntegerField(default=0)
	location = models.CharField(max_length=50, default='')
	twitterCount = models.IntegerField(default=0)
	timeZone = models.CharField(max_length=50, default='')
	profileBackground = models.CharField(max_length=300, default='')
	profileBanner = models.CharField(max_length=300, default='')
	profileImage = models.CharField(max_length=300, default='')


	def __str__(self):
		return ("%s" % (self.fullName))

	class Meta:
		ordering = ('-pk',)


class Tweet(models.Model):
	relatedAccount = models.ForeignKey(TwitterAccount, related_name="tweets", blank=True, null=True)
	tweetID = models.IntegerField(default=0)
	text = models.TextField(default='')
	cleanedText = models.TextField(default='')
	coordinates = models.TextField(default='', blank=True, null=True)
	country = models.CharField(max_length=100, default='')
	countryCode = models.CharField(max_length=100, default='')
	countryFull = models.CharField(max_length=100, default='')
	placeID = models.IntegerField(default=0)
	placeType =  models.CharField(max_length=50, default='')
	createdDate = models.DateTimeField(default=timezone.now)
	hashtags = models.TextField(default='')
	urls = models.TextField(default='')
	mentions = models.TextField(default='')
	liked = models.IntegerField(default=0)
	retweets = models.IntegerField(default=0)
	replyUserID = models.IntegerField(default=0, blank=True, null=True)
	replyTweetID = models.IntegerField(default=0, blank=True, null=True)
	retweetTweetID = models.IntegerField(default=0, blank=True, null=True)
	language = models.CharField(max_length=50, default='')
	quoteTweetID = models.IntegerField(default=0)

	class Meta:
		ordering = ('-createdDate',)

	def __str__(self):
		return ("%s %s" % (self.relatedAccount, self.pk))
