from django.db import models

class Month(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    num_days = models.IntegerField()
    start_day = models.IntegerField()

    def __str__(self):
        return f"{self.get_month_display()} {self.year}"

    def get_month_display(self):
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return month_names[self.month - 1]

class Task(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    day = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task on {self.month.get_month_display()} {self.day}, {self.month.year}"
