# Generated by Django 1.11.13 on 2018-07-11 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(help_text='Tapahtuman alkamisaika.', verbose_name='Alku')),
                ('end', models.DateTimeField(blank=True, help_text='Tapahtuman loppumisaika.', null=True, verbose_name='Loppu')),
                ('description', models.TextField(blank=True, verbose_name='Kuvaus')),
                ('title', models.CharField(help_text='Lyhyt otsikko.', max_length=128, verbose_name='Otsikko')),
                ('presenters', models.CharField(blank=True, help_text='Esityksen pitäjät tms.', max_length=256, verbose_name='Henkilöt')),
                ('presenters_titles', models.CharField(blank=True, help_text='Henkilön arvo-, ammatti- tai virkanimike.', max_length=256, verbose_name='Nimikkeet')),
                ('place', models.CharField(blank=True, help_text='Tarkka paikka tapahtuma-areenalla', max_length=64, verbose_name='Paikka')),
                ('icon_original', models.ImageField(blank=True, help_text='Kuva 1 tapahtumalle.', upload_to='programme/images/', verbose_name='Kuva 1')),
                ('icon2_original', models.ImageField(blank=True, help_text='Kuva 2 tapahtumalle.', upload_to='programme/images/', verbose_name='Kuva 2')),
                ('email', models.EmailField(blank=True, help_text='Tapahtumaan liittyvä sähköposti-osoite (esim. esiintyjän).', max_length=254, verbose_name='Sähköposti')),
                ('home_url', models.URLField(blank=True, help_text='Tapahtumaan liittyvä URL.', verbose_name='Kotiurli')),
                ('twitter_url', models.URLField(blank=True, help_text='Tapahtumaan liittyvä Twitter-url.', verbose_name='Twitter')),
                ('github_url', models.URLField(blank=True, help_text='Tapahtumaan liittyvä Github-url', verbose_name='Github')),
                ('facebook_url', models.URLField(blank=True, help_text='Tapahtumaan liittyvä facebook-url.', verbose_name='Facebook')),
                ('linkedin_url', models.URLField(blank=True, help_text='Tapahtumaan liittyvä LinkedIn-url.', verbose_name='LinkedIn')),
                ('wiki_url', models.URLField(blank=True, help_text='Tapahtumaan liittyvä Wikipedia-url.', verbose_name='Wikipedia')),
                ('gplus_url', models.URLField(blank=True, help_text='Tapahtumaan liittyvä Google Plus-url.', verbose_name='Google+')),
                ('event_type', models.IntegerField(choices=[(0, 'Yksinkertainen'), (1, 'Yksityiskohtainen')], default=0, help_text='Määrittää tapahtuman tyypin. Yksityiskohtaiset tapahtumat näkyvät etusivun tapahtumalistassa.', verbose_name='Tapahtuman tyyppi')),
                ('active', models.BooleanField(default=True, help_text='Deaktivoidut piilotetaan.', verbose_name='Aktiivinen')),
            ],
            options={
                'verbose_name': 'ohjelmatapahtuma',
                'verbose_name_plural': 'ohjelmatapahtumat',
            },
        ),
    ]
