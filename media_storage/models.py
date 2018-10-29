from django.db import models

class Recording(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Recording'

