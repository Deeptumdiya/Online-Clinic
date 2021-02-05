from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    spcl=models.CharField(max_length=50)

    @staticmethod
    def get_doc_obj(username):
        return Doctor.objects.get(username=name)