from django.db import models

# username:rk password:hello1234
class Person(models.Model):
  name = models.CharField(max_length=250)
  def __str__(self):
    return self.name

  
class Users(models.Model):
  name = models.CharField(max_length=250)
  how = (
    ('W', 'Work'),
    ('C', 'College'),
    ('F', 'Family')
  )
  company = models.CharField(max_length = 1, choices=how)
  def __str__(self):
    return self.name

  
class Social(models.Model):
  acc = models.ForeignKey(Users, on_delete=models.CASCADE)
#   account_names = models.CharField(max_length=250)
  Facebook = models.CharField(max_length=250)
  Instagram = models.CharField(max_length=250)
  Snapchat = models.CharField(max_length=250)
  def __str__(self):
    return "facebook: " + self.Facebook + " Instagram: " + self.Instagram + " Snapchat: " + self.Snapchat