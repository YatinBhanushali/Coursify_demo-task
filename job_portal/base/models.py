from django.db import models

# Create your models here.
class Job(models.Model):
    Company_name = models.CharField(max_length=50)
    Job_post = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    stipend = models.CharField(max_length=100)
    job_description = models.CharField(max_length=1000)
    requirements = models.CharField(max_length=200)

    def __str__(self):
        return self.Job_post

class Employee_Details(models.Model):
    job = models.ForeignKey(
        Job, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False)
    email_id = models.CharField(max_length=200, null=False)
    highest_education = models.CharField(max_length=200, null=False)
    interview_date = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name