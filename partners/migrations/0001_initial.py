# Generated by Django 3.1.1 on 2020-09-04 14:28

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import partners.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100, verbose_name='First Name')),
                ('LastName', models.CharField(max_length=50, verbose_name='Last Name')),
                ('Email', models.EmailField(max_length=255, verbose_name='Email address')),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('AccountType', models.PositiveSmallIntegerField(choices=[(1, 'INDIVIDUAL'), (2, 'COMPANY')], verbose_name='Account Type')),
                ('BusinessName', models.CharField(blank=True, max_length=200, null=True, verbose_name='Business Name')),
                ('RegistertionNo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Registration No')),
                ('Address1', models.CharField(max_length=255, verbose_name='Address 1')),
                ('Address2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address 2')),
                ('City', models.CharField(max_length=255, verbose_name='City')),
                ('State', models.CharField(max_length=255, verbose_name='State/County')),
                ('Country', django_countries.fields.CountryField(max_length=2)),
                ('Remittance', models.PositiveSmallIntegerField(choices=[(1, 'BANK'), (2, 'CARD')], verbose_name='Remittance Method')),
                ('Verified', models.BooleanField(db_index=True, default=False, verbose_name='Verified')),
                ('Enabled', models.BooleanField(db_index=True, default=False, verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'Partners',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DisplayName', models.CharField(max_length=255, verbose_name='Display Name')),
                ('ServiceLocation', models.CharField(db_index=True, max_length=255, verbose_name='Service Location')),
                ('PaymentMethod', models.PositiveSmallIntegerField(choices=[(1, 'CASH'), (2, 'ONLINE')], verbose_name='Payment Method')),
                ('Enabled', models.BooleanField(db_index=True, default=False, verbose_name='Enabled')),
                ('Partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='partner_profiles', to='partners.partners')),
                ('Services', models.ManyToManyField(db_index=True, related_name='profile_services', to='website.Services', verbose_name='Services Offered')),
            ],
            options={
                'verbose_name': 'Profiles',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='ProfileImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to=partners.models.rename_upload_path)),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='partners.profiles', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Profile Images',
                'verbose_name_plural': 'Profile Images',
            },
        ),
    ]
