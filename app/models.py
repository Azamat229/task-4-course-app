from django.db import models

PH = "PHONE"
FACE = "FACEBOOK"
EM = "EMAIL"

TYPE_CHOICES = (
    (PH, "Phone"),
    (FACE, "Facebook"),
    (EM, "Email")
)


class Category(models.Model):
    name = models.CharField(max_length=1300)
    img_path = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address


class Contact(models.Model):
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=EM)
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='courses')  # если удалим поле категории то поле будет Null
    logo = models.CharField(max_length=120)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
