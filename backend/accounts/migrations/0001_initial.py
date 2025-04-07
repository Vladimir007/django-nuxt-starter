from django.utils.timezone import now

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(name='User', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ('first_name', models.CharField(max_length=150, verbose_name='first name')),
            ('last_name', models.CharField(max_length=150, verbose_name='last name')),
            ('password', models.CharField(max_length=128, verbose_name='password')),

            ('is_superuser', models.BooleanField(
                verbose_name='superuser status', default=False,
                help_text='Designates that this user has all permissions without explicitly assigning them.',
            )),
            ('is_staff', models.BooleanField(
                verbose_name='staff status', default=False,
                help_text='Designates whether the user can log into this admin site.',
            )),
            ('is_active', models.BooleanField(
                verbose_name='active', default=False,
                help_text='Designates whether this user should be treated as active. '
                          'Unselect this instead of deleting accounts.',
            )),

            ('date_joined', models.DateTimeField(default=now, verbose_name='date joined')),
            ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),

            ('groups', models.ManyToManyField(
                to='auth.group', related_name='user_set', related_query_name='user',
                verbose_name='groups', blank=True,
                help_text='The groups this user belongs to. '
                          'A user will get all permissions granted to each of their groups.',
            )),
            ('user_permissions', models.ManyToManyField(
                to='auth.permission', related_name='user_set', related_query_name='user',
                verbose_name='user permissions', blank=True,
                help_text='Specific permissions for this user.',
            )),
        ], options={
            'db_table': 'accounts',
            'swappable': 'AUTH_USER_MODEL',
            'verbose_name': 'User',
            'verbose_name_plural': 'Users',
        }),
    ]
