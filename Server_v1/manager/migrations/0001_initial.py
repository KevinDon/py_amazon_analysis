# Generated by Django 2.1.5 on 2019-06-28 09:49

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileDv',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Creator Id')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('is_active', models.IntegerField(verbose_name='Active')),
                ('group_id', models.CharField(max_length=100, verbose_name='Group Id')),
                ('group_name', models.CharField(max_length=100, verbose_name='Group Name')),
                ('dep_id', models.CharField(max_length=100, verbose_name='Department Id')),
                ('dep_name', models.CharField(max_length=100, verbose_name='Department Name')),
                ('nick', models.CharField(max_length=100, verbose_name='Nick')),
                ('ding_talk_account', models.CharField(max_length=100, verbose_name='Ding Talk Account')),
            ],
            options={
                'verbose_name_plural': 'User Profile',
                'db_table': 'view_i_auth_user_profile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiPermissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('type', models.IntegerField(choices=[(0, 'Operation'), (1, 'Data')], default=1, null=True, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Permission Type',
                'verbose_name_plural': 'Permission Type',
                'db_table': 'auth_api_permission',
            },
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('code', models.CharField(blank=True, max_length=50, verbose_name='Department Code')),
                ('leaf', models.IntegerField(default=0, verbose_name='Leaf')),
                ('level', models.IntegerField(default=0, verbose_name='Level')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.DepartmentModel')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Department',
                'db_table': 'auth_department',
            },
        ),
        migrations.CreateModel(
            name='GroupProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('code', models.CharField(blank=True, max_length=50, verbose_name='Group Code')),
            ],
            options={
                'verbose_name': 'Group Profile',
                'verbose_name_plural': 'Group Profile',
                'db_table': 'auth_group_profile',
            },
        ),
        migrations.CreateModel(
            name='TokenModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'db_table': 'auth_token',
            },
        ),
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('nick', models.CharField(blank=True, max_length=60, null=True, verbose_name='nick')),
                ('ding_talk_account', models.CharField(blank=True, max_length=60, verbose_name='ding talk account')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_department', to='manager.DepartmentModel')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profile',
                'db_table': 'auth_user_profile',
            },
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Group',
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='PermissionModel',
            fields=[
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permission',
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='userprofilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tokenmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='groupprofilemodel',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group_profile', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='groupprofilemodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.GroupProfileModel'),
        ),
        migrations.AddField(
            model_name='apipermissionmodel',
            name='permission',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_permission', to='auth.Permission'),
        ),
    ]
