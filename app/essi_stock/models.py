from django.db import models


class Categorite(models.Model):
    name = models.CharField(max_length= 100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoriteLevelOne(models.Model):
    categorite = models.ForeignKey(Categorite, related_name='categorites_level_one', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoriteLevelTwo(models.Model):
    categorite_level_1 = models.ForeignKey(CategoriteLevelOne, related_name='categorites_level_two', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    categorite = models.ForeignKey(Categorite, related_name='categorites', on_delete=models.CASCADE)
    categorite_level_1 = models.ForeignKey(CategoriteLevelOne, related_name='categorites_level_one', on_delete=models.CASCADE)
    categorite_level_2 = models.ForeignKey(CategoriteLevelTwo, related_name='items', on_delete=models.CASCADE)
    marque = models.CharField(max_length=50)
    reference = models.CharField(max_length=200)
    image = models.CharField(max_length=3000)
    price = models.CharField(max_length=200)