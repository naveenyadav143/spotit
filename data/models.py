from django.db import models

class ItemPost(models.Model):
    # True = Lost item, False = Found item
    is_lost = models.BooleanField()       # NEW (replaces type)

    title = models.CharField(max_length=200)
    description = models.TextField()
    location_text = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts/", null=True, blank=True) 

    contact_name = models.CharField(max_length=100)
    contact_method = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Lost" if self.is_lost else "Found"
        return f"{status}: {self.title}"
