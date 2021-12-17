from django.db import models


class URL(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	click_times = models.PositiveIntegerField(default=0)
	long_url = models.URLField(max_length=250)
	short_url = models.CharField(max_length=10, unique=True, blank=True)
	

	class Meta:
		ordering = ["-created"]


	def __str__(self):
		return self.long_url




