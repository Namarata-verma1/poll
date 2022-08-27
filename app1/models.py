from django.db import models

# Create your models here.
class Customer_Class(models.Model):
    cust_name = models.CharField("User Name",default="",max_length=100)
    cust_m_no = models.PositiveIntegerField(verbose_name="Mobile no",default=00000000,max_length=10)
    cust_email = models.CharField(default="",max_length=100)
    cust_password = models.CharField(default="",max_length=100)

class Author_Class(models.Model):
    p_name = models.CharField("User Name",default="",max_length=100)
    p_m_no = models.PositiveIntegerField(verbose_name="Mobile no",default=00000000,max_length=10)
    p_email = models.CharField(default="",max_length=100)
    p_password = models.CharField(default="",max_length=100)
    
    def __str__(self):
        return self.p_name

class Poll(models.Model):
    #author = models.ForeignKey('Customer_Class',default=0,on_delete=models.CASCADE)
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count