from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


"""
from django.db import migrations


def duplicate_table_adress(apps, schema_editor):
    Address = apps.get_model('oc_lettings_site', 'Address')
    NewAddresse = apps.get_model('lettings', 'Address')
    address_list = list()
    for adress in Address.objects.all():
        new = NewAddresse(number=adress.number,
                          street=adress.street,
                          city=adress.city,
                          state=adress.state,
                          zip_code=adress.zip_code,
                          country_iso_code=adress.country_iso_code)
        address_list.append(new)
    NewAddresse.objects.bulk_create(address_list)


def duplicate_table_lettings(apps, schema_editor):
    Lettings = apps.get_model('oc_lettings_site', 'Letting')
    NewLettings = apps.get_model('lettings', 'Letting')
    lettings_list = list()
    for letting in Lettings.objects.all():
        new = NewLettings(title=letting.title,
                          address=letting.address)
        lettings_list.append(new)
    NewLettings.objects.bulk_create(lettings_list)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(duplicate_table_adress),
        migrations.RunPython(duplicate_table_lettings),
    ]
        """