from django.db import models

class FileStorage(models.Model):
    uploaded_file = models.FileField(upload_to='uploads/')
