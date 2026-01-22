from django.db import models

class Degree(models.Model):
    title = models.CharField(max_length=100)  # e.g. BS Computer Science
    institution = models.CharField(max_length=100) # e.g. Your University
    year_start = models.IntegerField()
    year_end = models.IntegerField(blank=True, null=True) # Can be empty if current
    grade = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.title} at {self.institution}"