# Generated by Django 4.2 on 2023-04-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_rename_contant_comment_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(verbose_name="댓글 작성"),
        ),
    ]
