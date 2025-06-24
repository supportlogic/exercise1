
from django.db import models


TITLE_LENGTH = 512

class Customer(models.Model):
    """
    Represents a customer entity with a name, optional address, and creation timestamp.
    """
    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class DataSource(models.Model):
    """
    Represents a data source belonging to a customer, with a name, optional description, and creation timestamp.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='data_sources')
    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.customer.name})"

class Item(models.Model):
    """
    Represents an item belonging to a data source, with a name, optional details, and creation timestamp.
    """
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name='items')

    # Add fields for item details

    def __str__(self):
        return f"Item {self.pk}"
