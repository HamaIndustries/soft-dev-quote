from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallons_requested', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=255)),
                ('delivery_date', models.DateField()),
                ('suggested_price_per_gallon', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
