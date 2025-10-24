from django.db import models


class schUpdate(models.Model):
    title = models.CharField(max_length = 320)
    subject = models.TextField(blank=True)
    content = models.TextField(max_length = 600, blank = True)
    pic = models.ImageField( upload_to='pictures/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add = True)



class candidateDetails(models.Model):
    StuName = models.CharField(max_length=100)
    DOB = models.DateField(blank=True , null = True)
    religion = models.TextField(blank=True , max_length=50)
    nationality = models.CharField(max_length=50)
    fLang = models.CharField(max_length=20, blank=True)
    oLang = models.CharField(max_length=50, blank = True)
    address = models.CharField(max_length=100 , blank = True)
    healthCon = models.CharField(max_length=150, blank=True) #health concerns

class ftherDetails(models.Model):
    FtherName = models.TextField(max_length=150 , blank=True)
    email = models.EmailField(unique=True )
    eduQualification = models.TextField(max_length=150 , blank = True)
    profession = models.CharField(max_length=150 , blank = True)
    desingation = models.CharField(max_length=150 , blank=True)
    phone = models.CharField(max_length=20 , unique=True)


class mtherDetails(models.Model):
    FtherName = models.TextField(max_length=150 , blank=True)
    email = models.EmailField(unique=True )
    eduQualification = models.TextField(max_length=150 , blank = True)
    profession = models.CharField(max_length=150 , blank = True)
    desingation = models.CharField(max_length=150 , blank=True)
    phone = models.CharField(max_length=20 , unique=True)


class GuardDetails(models.Model):
    FtherName = models.TextField(max_length=150 , blank=True)
    email = models.EmailField(unique=True )
    eduQualification = models.TextField(max_length=150 , blank = True)
    profession = models.CharField(max_length=150 , blank = True)
    desingation = models.CharField(max_length=150 , blank=True)
    phone = models.CharField(max_length=20 , unique=True)


class emergencyContact1 (models.Model):
    relation = models.CharField(max_length=150 , blank=True)
    contact = models.CharField(max_length=150 , blank=True)


class emergencyContact2 (models.Model):
    relation = models.CharField(max_length=150 , blank=True)
    contact = models.CharField(max_length=150 , blank=True)

class emergencyContact3 (models.Model):
    relation = models.CharField(max_length=150 , blank=True)
    contact = models.CharField(max_length=150 , blank=True)





class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('admissions', 'Admissions Inquiry'),
        ('general', 'General Information'),
        ('feedback', 'Feedback'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
