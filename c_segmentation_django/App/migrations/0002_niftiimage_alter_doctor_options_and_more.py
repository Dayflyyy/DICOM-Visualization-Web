# Generated by Django 5.0.2 on 2024-03-08 13:59

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="NIfTIImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="名称")),
                (
                    "file",
                    models.FileField(upload_to="nifti_images/", verbose_name="文件"),
                ),
                ("dimensions", models.CharField(max_length=100, verbose_name="维度")),
                ("voxel_size", models.CharField(max_length=100, verbose_name="体素大小")),
                ("data_type", models.CharField(max_length=50, verbose_name="数据类型")),
            ],
            options={
                "verbose_name": "NIfTI图像",
                "verbose_name_plural": "NIfTI图像",
            },
        ),
        migrations.AlterModelOptions(
            name="doctor",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterModelOptions(
            name="medicalrecord",
            options={"verbose_name": "病历", "verbose_name_plural": "病历"},
        ),
        migrations.AlterModelOptions(
            name="patient",
            options={"verbose_name": "病人", "verbose_name_plural": "病人"},
        ),
        migrations.AlterModelManagers(
            name="doctor",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="medicalrecord",
            name="patient",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="address",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="email",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="introduction",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="photo",
        ),
        migrations.AddField(
            model_name="doctor",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="disease",
            field=models.IntegerField(
                choices=[
                    (1, "冠状动脉粥样硬化症"),
                    (2, "心绞痛"),
                    (3, "心肌梗死"),
                    (4, "冠状动脉痉挛"),
                    (5, "冠状动脉炎"),
                    (6, "冠状动脉畸形"),
                ],
                default=1,
                verbose_name="疾病类型",
            ),
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="patient_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="App.patient",
                verbose_name="病人",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="description",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="描述"
            ),
        ),
        migrations.AddField(
            model_name="patient",
            name="doctor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="医生",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="medical_record",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="App.medicalrecord",
                verbose_name="病历",
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="age",
            field=models.IntegerField(verbose_name="年龄"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="department",
            field=models.CharField(max_length=20, verbose_name="科室"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="email",
            field=models.CharField(max_length=20, verbose_name="邮箱"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="introduction",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="简介"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="name",
            field=models.CharField(max_length=20, verbose_name="姓名"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="电话"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="photo",
            field=models.ImageField(upload_to="doctor_photo", verbose_name="头像"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="sex",
            field=models.CharField(max_length=10, verbose_name="性别"),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
        migrations.AlterField(
            model_name="medicalrecord",
            name="content",
            field=models.TextField(
                blank=True, max_length=1000, null=True, verbose_name="内容"
            ),
        ),
        migrations.AlterField(
            model_name="medicalrecord",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="医生",
            ),
        ),
        migrations.AlterField(
            model_name="medicalrecord",
            name="time_created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="medicalrecord",
            name="time_lastmodified",
            field=models.DateTimeField(auto_now=True, verbose_name="最后修改时间"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="age",
            field=models.IntegerField(verbose_name="年龄"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="name",
            field=models.CharField(max_length=20, verbose_name="姓名"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="phone",
            field=models.CharField(max_length=20, verbose_name="电话"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="sex",
            field=models.CharField(max_length=10, verbose_name="性别"),
        ),
        migrations.AddField(
            model_name="patient",
            name="ct_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="App.niftiimage",
                verbose_name="CT图像",
            ),
        ),
        migrations.DeleteModel(
            name="CTImage",
        ),
    ]
