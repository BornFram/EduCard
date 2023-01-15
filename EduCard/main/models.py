from django.db import models


class Tags(models.Model):
    name = models.CharField('tag',max_length=100)


class Classes(models.Model):
    name = models.IntegerField('class')
    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField('subject',max_length=200)
    clas = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Themes(models.Model):
    name = models.CharField('theme',max_length=200)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField('item',max_length=80)
    description = models.TextField(max_length=300)
    raiting = models.FloatField(default=0)
    tag = models.ManyToManyField(Tags)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
class Tags(models.Model):
    name = models.CharField(max_length=100)


class Classes(models.Model):
    name = models.IntegerField()


class Subjects(models.Model):
    name = models.CharField(200, max_length=200)
    clas = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Themes(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)


class Items(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    raiting = models.FloatField(default=0)
    tag = models.ManyToManyField(Tags)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE)


class Users():
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    favourites = models.ManyToManyField(Items)
    shopCart = models.ManyToManyField(Items)
    #graph = models.ManyToManyField(Connections)
"""