import os.path
from django.db import models
import pandas as pd

# Create your models here.
class VisualDateImportance(models.Model):
    title = models.TextField(max_length=255)
    image = models.ImageField()
    table = models.FileField()

    def __str__(self):
        return self.title

    def get_array(self):
        df = pd.read_csv(self.table)
        headers = list(df.to_dict().keys())
        column1 = df[headers[0]]
        column2 = df[headers[1]]
        res = [headers]
        for i in range(len(column1)):
            l = [column1[i], column2[i]]
            res.append(l)
        return res

class VisualDateGeography(models.Model):
    title = models.TextField(max_length=255)
    image = models.ImageField()
    table = models.FileField()

    def __str__(self):
        return self.title

    def get_array(self):
        df = pd.read_csv(self.table)
        headers = list(df.to_dict().keys())
        column1 = df[headers[0]]
        column2 = df[headers[1]]
        res = [headers]
        for i in range(len(column1)):
            l = [column1[i], column2[i]]
            res.append(l)
        return res

class VisualDateSkills(models.Model):
    title = models.TextField(max_length=255)
    image = models.ImageField()
    table = models.FileField()

    def __str__(self):
        return self.title

    def get_array(self):
        df = pd.read_csv(self.table)
        headers = list(df.to_dict().keys())
        column1 = df[headers[0]]
        column2 = df[headers[1]]
        res = [headers]
        for i in range(len(column1)):
            l = [column1[i], column2[i]]
            res.append(l)
        return res