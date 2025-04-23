from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()

    def _str_(self):
        return self.title

class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skills = models.TextField(blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    score = models.FloatField(default=0.0)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"


    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class Interview(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date = models.DateTimeField()
    video_link = models.URLField()
    score = models.IntegerField(null=True)

    def _str_(self):
        return f"Interview with {self.candidate.first_name} {self.candidate.last_name}"
