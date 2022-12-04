# Generated by Django 1.11.13 on 2018-07-11 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kilpailun nimi (max 32 merkkiä).', max_length=32, verbose_name='Nimi')),
                ('description', models.TextField(verbose_name='Kuvaus')),
                ('participation_end', models.DateTimeField(help_text='Tämän jälkeen kilpailuun ei voi enää osallistua.', verbose_name='Deadline osallistumiselle.')),
                ('start', models.DateTimeField(help_text='Kilpailun aloitusaika.', verbose_name='Kilpailun alku')),
                ('end', models.DateTimeField(blank=True, help_text='Kilpailun päättymisaika.', null=True, verbose_name='Kilpailun loppu')),
                ('score_type', models.CharField(help_text='Pisteiden tyyppi (km, m, sek, ...). Maksimipituus 8 merkkiä.', max_length=8, verbose_name='Pisteiden tyyppi')),
                ('score_sort', models.IntegerField(choices=[(0, 'Korkein tulos ensin'), (1, 'Matalin tulos ensin')], default=0, help_text='Onko suurimman vai pienimmän tuloksen saavuttanut voittaja?', verbose_name='Pisteiden järjestely')),
                ('show_results', models.BooleanField(default=False, help_text='Näytä kilpailun tulokset.', verbose_name='Näytä tulokset')),
                ('active', models.BooleanField(default=True, help_text='Onko kilpailu aktiivinen, eli näytetäänkö se kompomaatissa kaikille.', verbose_name='Aktiivinen')),
                ('hide_from_archive', models.BooleanField(default=False, help_text='Piilotetaanko kilpailun tulokset arkistosta ? Tämä ylikirjoittaa eventin asetuksen.', verbose_name='Piilotus arkistosta')),
            ],
            options={
                'verbose_name': 'kilpailu',
                'verbose_name_plural': 'kilpailut',
            },
        ),
        migrations.CreateModel(
            name='CompetitionParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(default='', help_text='Nimimerkki jolla haluat osallistua.', max_length=32, verbose_name='Osallistujan nimi')),
                ('score', models.FloatField(blank=True, default=0, help_text='Kilpailijan saavuttamat pisteet', verbose_name='Pisteet')),
                ('disqualified', models.BooleanField(default=False, help_text='Suoritus on diskattu sääntörikon tai teknisten virheiden takia.', verbose_name='Diskattu')),
                ('disqualified_reason', models.TextField(blank=True, verbose_name='Diskauksen syy')),
            ],
            options={
                'verbose_name': 'ilmoittautuminen',
                'verbose_name_plural': 'ilmoittautumiset',
            },
        ),
        migrations.CreateModel(
            name='Compo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kompon nimi (max 32 merkkiä).', max_length=32, verbose_name='Nimi')),
                ('description', models.TextField(verbose_name='Kuvaus')),
                ('adding_end', models.DateTimeField(help_text='Tämän jälkeen kompoon ei voi enää lähettää uusia entryjä. Muokkaus toimii vielä.', verbose_name='Deadline entryjen lisäyksille')),
                ('editing_end', models.DateTimeField(help_text='Tämän jälkeen entryjen tiedostoja tai muita tietoja ei voi enää muokata.', verbose_name='Deadline entryjen muokkauksille')),
                ('compo_start', models.DateTimeField(help_text='Kompon alkamisaika tapahtumassa (tapahtumakalenteria varten).', verbose_name='Kompon aloitusaika')),
                ('voting_start', models.DateTimeField(help_text='Alkamisaika entryjen äänestykselle.', verbose_name='Äänestyksen alkamisaika')),
                ('voting_end', models.DateTimeField(help_text='Päättymisaika entryjen äänestykselle.', verbose_name='Äänestyksen päättymisaika')),
                ('entry_sizelimit', models.IntegerField(default=134217728, help_text='Kokoraja entrytiedostoille (tavua).', verbose_name='Kokoraja entryille')),
                ('source_sizelimit', models.IntegerField(default=134217728, help_text='Kokoraja sorsatiedostoille (tavua).', verbose_name='Kokoraja sorsille')),
                ('formats', models.CharField(default='zip|7z|gz|bz2', help_text='Entrypaketille sallitut tiedostopäätteet pystyviivalla eroteltuna, esim. "png|jpg".', max_length=128, verbose_name='Sallitut tiedostopäätteet')),
                ('source_formats', models.CharField(default='zip|7z|gz|bz2', help_text='Entryn lähdekoodipaketille sallitut tiedostopäätteet pystyviivalla eroteltuna', max_length=128, verbose_name='Sallitut lähdekoodipaketin päätteet')),
                ('image_formats', models.CharField(default='png|jpg', help_text='Entryn pikkukuvalle sallitut tiedostopäätteet pystyviivalla eroteltuna', max_length=128, verbose_name='Sallitut kuvatiedoston päätteet')),
                ('active', models.BooleanField(default=True, help_text='Onko kompo aktiivinen, eli näytetäänkö se kompomaatissa kaikille.', verbose_name='Aktiivinen')),
                ('show_voting_results', models.BooleanField(default=False, help_text='Näytä äänestustulokset.', verbose_name='Näytä tulokset')),
                ('entry_view_type', models.IntegerField(choices=[(0, 'Ei mitään'), (1, 'Youtube ensin, sitten kuva'), (2, 'Vain kuva'), (3, '(deprecated)')], default=0, help_text='Ilmoittaa millainen näkymä näytetään entryn tiedoissa. Latauslinkki näytetään aina.', verbose_name='Entryesittely')),
                ('hide_from_archive', models.BooleanField(default=False, help_text='Piilottaa kompon tulokset arkistosta. Tämä asetus ohittaa tapahtuman tiedoissa valitun asetuksen.', verbose_name='Piilotus arkistosta')),
                ('hide_from_frontpage', models.BooleanField(default=False, help_text='Piilottaa kompon nimen ja kuvauksen tapahtuman etusivulta. Käytä esim. jos kompon kuvaus on vielä suunnitteilla.', verbose_name='Piilotus etusivulta')),
                ('is_votable', models.BooleanField(default=True, help_text='Teosta voi ylipäätään äänestää (Pois esim. robocodelle).', verbose_name='Äänestettävissä')),
                ('thumbnail_pref', models.IntegerField(choices=[(0, 'Vaadi erillinen pikkukuva.'), (1, 'Käytä pikkukuvana teoksen tiedostoa (Toimii vain png/jpg-tiedostoille).'), (2, 'Salli pikkukuva (ei vaadittu).'), (3, 'Älä salli pikkukuvaa.')], default=2, help_text='Pikkukuvan luonti ja asettaminen.', verbose_name='Pikkukuvan asetukset')),
            ],
            options={
                'verbose_name': 'kompo',
                'verbose_name_plural': 'kompot',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nimi tuotokselle', max_length=64, verbose_name='Nimi')),
                ('description', models.TextField(help_text='Voi sisältää mm. tietoja käytetyistä tekniikoista, muuta sanottavaa.', verbose_name='Kuvaus')),
                ('creator', models.CharField(help_text='Tuotoksen tekijän tai tekijäryhmän nimi', max_length=64, verbose_name='Tekijä')),
                ('entryfile', models.FileField(help_text='Tuotospaketti.', upload_to='kompomaatti/entryfiles/', verbose_name='Tiedosto')),
                ('sourcefile', models.FileField(blank=True, help_text='Lähdekoodipaketti.', upload_to='kompomaatti/entrysources/', verbose_name='Lähdekoodi')),
                ('imagefile_original', models.ImageField(blank=True, help_text='Edustava kuva teokselle. Ei pakollinen, mutta suositeltava.', upload_to='kompomaatti/entryimages/', verbose_name='Kuva')),
                ('youtube_url', models.URLField(blank=True, help_text='Linkki teoksen Youtube-videoon.', verbose_name='Youtube URL')),
                ('disqualified', models.BooleanField(default=False, help_text='Entry on diskattu sääntörikon tai teknisten ongelmien takia. DISKAUS ON TEHTÄVÄ ENNEN ÄÄNESTYKSEN ALKUA!', verbose_name='Diskattu')),
                ('disqualified_reason', models.TextField(blank=True, help_text='Diskauksen syy.', verbose_name='Syy diskaukseen')),
                ('archive_score', models.FloatField(blank=True, help_text='Arkistoidun entryn kompossa saamat pisteet. Mikäli tätä ei määritetä, lasketaan pisteet suoraan äänestystuloksista.', null=True, verbose_name='Pisteet')),
                ('archive_rank', models.IntegerField(blank=True, help_text='Arkistoidun entryn kompossa saama sijoitus. Tämä voidaan laskea myös pistemääristä automaattisesti.', null=True, verbose_name='Sijoitus')),
            ],
            options={
                'verbose_name': 'tuotos',
                'verbose_name_plural': 'tuotokset',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Tapahtuman nimi', max_length=64, unique=True, verbose_name='Nimi')),
                ('date', models.DateField(help_text='Tapahtuman päivämäärä (alku)', verbose_name='Päivämäärä')),
                ('archived', models.BooleanField(default=False, help_text='Saa näyttää arkistossa', verbose_name='Arkistoitu')),
                ('mainurl', models.URLField(blank=True, help_text='URL Tapahtuman pääsivustolle', verbose_name='Tapahtuman pääsivu')),
            ],
            options={
                'verbose_name': 'tapahtuma',
                'verbose_name_plural': 'tapahtumat',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherinfo', models.TextField(help_text='Muita yhteystietoja, mm. IRC-tunnus (verkon kera), jne.', verbose_name='Muut yhteystiedot')),
            ],
            options={
                'verbose_name': 'profiili',
                'verbose_name_plural': 'profiilit',
            },
        ),
        migrations.CreateModel(
            name='TicketVoteCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, help_text='Aika jolloin avain assosioitiin käyttäjälle.', null=True, verbose_name='Aikaleima')),
                ('associated_to', models.ForeignKey(blank=True, help_text='Käyttäjä jolle avain on assosioitu', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Käyttäjä')),
                ('event', models.ForeignKey(blank=True, help_text='Tapahtuma, johon äänestysavain on assosioitu', null=True, on_delete=django.db.models.deletion.CASCADE, to='kompomaatti.Event', verbose_name='Tapahtuma')),
            ],
            options={
                'verbose_name': 'lippuäänestusavain',
                'verbose_name_plural': 'lippuäänestysavaimet',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(verbose_name='Sijoitus')),
                ('compo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompomaatti.Compo', verbose_name='kompo')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompomaatti.Entry', verbose_name='tuotos')),
            ],
            options={
                'verbose_name': 'ääni',
                'verbose_name_plural': 'äänet',
            },
        ),
        migrations.CreateModel(
            name='VoteCodeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Lyhyt aneluteksti admineille :)', verbose_name='Kuvaus')),
                ('status', models.IntegerField(choices=[(0, 'Odottaa hyväksyntää'), (1, 'Hyväksytty'), (2, 'Hylätty')], default=0, verbose_name='Tila')),
                ('event', models.ForeignKey(help_text='Tapahtuma, johon äänestysoikeutta pyydetään', null=True, on_delete=django.db.models.deletion.CASCADE, to='kompomaatti.Event', verbose_name='Tapahtuma')),
                ('user', models.ForeignKey(help_text='Pyynnön esittänyt käyttäjä', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Käyttäjä')),
            ],
            options={
                'verbose_name': 'äänestyskoodipyyntö',
                'verbose_name_plural': 'äänestyskoodipyynnöt',
            },
        ),
        migrations.CreateModel(
            name='VoteGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kompomaatti.Compo', verbose_name='kompo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='käyttäjä')),
            ],
            options={
                'verbose_name': 'ääniryhmä',
                'verbose_name_plural': 'ääniryhmät',
            },
        ),
        migrations.AddField(
            model_name='vote',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='kompomaatti.VoteGroup'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='käyttäjä'),
        ),
    ]
