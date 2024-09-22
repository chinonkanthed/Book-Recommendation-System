# Generated by Django 4.2.11 on 2024-08-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recommend", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="pdf_url",
        ),
        migrations.AddField(
            model_name="book",
            name="read_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="book",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name="UserBook",
        ),
    ]