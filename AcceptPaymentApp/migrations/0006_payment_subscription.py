# Generated by Django 2.2.6 on 2020-02-16 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_generalinfo'),
        ('AcceptPaymentApp', '0005_remove_payment_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paymob_payment', to='app.Package'),
        ),
    ]
