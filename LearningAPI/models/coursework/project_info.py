from django.db import models

class ProjectInfo(models.Model):
    """Information for a Project"""
    description = models.CharField(max_length=256)
    template_url = models.CharField(max_length=256)
    project = models.OneToOneField("Project", on_delete=models.CASCADE, related_name="info")