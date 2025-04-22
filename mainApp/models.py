from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    msg = models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.email
    
class Enquiry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    adhar = models.FileField(upload_to="uploads",default="",null=True,blank=True)
    pan = models.FileField(upload_to="uploads",default="",null=True,blank=True)
    certificate = models.FileField(upload_to="uploads",default="",null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.email
    
class Partners(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default='')
    link = models.CharField(max_length=500,default='')
    logo = models.ImageField(upload_to="uploads",default="",null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name

class Newsletter(models.Model): 
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.id)+" "+self.email



class Gallery(models.Model): 
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads",default="",null=True,blank=True)



class Testimonial(models.Model): 
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    name = models.CharField(max_length=200,default='')
    designation = models.CharField(max_length=100,default='')
    message = models.CharField(max_length=500,default='')

    def __str__(self):
        return str(self.id)+" "+self.name