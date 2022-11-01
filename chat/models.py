from django.db import models


from registration.models import Account


class Messages(models.Model):

    description = models.TextField()
    sender_name = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender1')
    receiver_name = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver1')
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.receiver_name} From: {self.sender_name}"

    class Meta:
        ordering = ('timestamp',)


class Friends(models.Model):

    name = models.ForeignKey(Account, on_delete=models.CASCADE,default=1,related_name='namee')
    friend = models.IntegerField()

    def __str__(self):
        return f"{self.friend}"

