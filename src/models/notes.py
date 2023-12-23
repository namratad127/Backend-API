# src/models/notes.py
from django.db import models

class Notes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(default="", max_length=500)
    link = models.CharField(default="", max_length=200)
    description = models.CharField(default="", max_length=500)
    tag = models.CharField(default="others", max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Notes, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'notes'
        app_label = 'src'# src/models/notes.py
from django.db import models

class Notes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(default="", max_length=500)
    link = models.CharField(default="", max_length=200)
    description = models.CharField(default="", max_length=500)
    tag = models.CharField(default="others", max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Notes, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'notes'
        app_label = 'src'