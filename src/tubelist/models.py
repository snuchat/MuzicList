from django.conf import settings
from django.db import models

# Create your models here.

# class Singer(models.Model):
# 	singer_name		= models.CharField(max_length=50, unique=True)
# 	manage_company		= models.CharField(max_length=50)
# 	verified		= models.BooleanField(default=False)

# 	def __str__(self):
# 		return str(self.singer_name)

# 	def is_verified(self):
# 		return self.verified


# class VerifiedYoutubeURL(models.Model):
# 	url 			= models.CharField(max_length=100)
# 	song_title		= models.CharField(max_length=50)
# 	singer			= models.ForeignKey(Singer, on_delete=models.CASCADE)
# 	verified		= models.BooleanField(default=False)
# 	is_music_video		= models.BooleanField(default=False)
# 	liked_it		= models.IntegerField(default=0)

# 	def __str__(self):
# 		return str(self.song_title)
	
# 	def is_verified(self):
# 		return self.verified

class DJMusicList(models.Model):
	DJ_name		= models.ForeignKey(settings.AUTH_USER_MODEL)
	ListName	= models.CharField(max_length=100)
	Desc		= models.TextField(max_length=300)
	# list_1		= models.ForeignKey(VerifiedYoutubeURL, on_delete=models.SET_NULL, related_name="djmusiclist_1", null=True)
	# list_2		= models.ForeignKey(VerifiedYoutubeURL, on_delete=models.SET_NULL, related_name="djmusiclist_2", null=True)
	# list_3		= models.ForeignKey(VerifiedYoutubeURL, on_delete=models.SET_NULL, related_name="djmusiclist_3", null=True)
	list_1       = models.URLField(max_length=100, null=True)
	list_2       = models.URLField(max_length=100, null=True)
	list_3       = models.URLField(max_length=100, null=True)
	list_4       = models.URLField(max_length=100, null=True)
	list_5       = models.URLField(max_length=100, null=True)
	list_6       = models.URLField(max_length=100, null=True)
	list_7       = models.URLField(max_length=100, null=True)
	list_8       = models.URLField(max_length=100, null=True)
	list_9       = models.URLField(max_length=100, null=True)
	list_10       = models.URLField(max_length=100, null=True)
	list_11       = models.URLField(max_length=100, null=True)
	list_12       = models.URLField(max_length=100, null=True)
	list_13       = models.URLField(max_length=100, null=True)
	list_14       = models.URLField(max_length=100, null=True)
	list_15       = models.URLField(max_length=100, null=True)

	def __str__(self):
		return str(self.ListName)