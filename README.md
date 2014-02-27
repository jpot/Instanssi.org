Instanssi.org website project
=============================

What is this ?
--------------
This project right here is the website of instanssi.org demoparty. It contains the main website (main2012),
Kompomaatti (our compo entry management interface), and Arkisto (our entry archive site). Most
of the comments and language used is in Finnish, because the programmers weren't interested in 
internationalization :D

This project has been originally developed for Instanssi 2012. Project is still alive and current development
focus is to provide web site for Instanssi 2014.

License
-------
MIT. Please refer to `LICENSE` for more information.

Mikä on tämä ?
--------------
En jaksa kirjoittaa suomeksi, lue ylläolevat :D

Ympäristön asentaminen Windowsille
----------------------------------
1. Asenna Python, 2.6 tai 2.7 on ok (http://www.python.org). Varmista, että pythonin juurikansio (se josta löytyy python.exe)
   ja scripts-kansiot ovat windowsin PATHissa. Kannattaa ladata 32bit versio, vaikka olisikin 64bit windows. Helpompi saada
   kirjastot. Mikäli ehdottomasti haluat asentaa 64bit versiot, niin osa paketeista on ladattavissa osoitteesta 
   http://www.lfd.uci.edu/~gohlke/pythonlibs/ .
2. Asenna setuptools (http://pypi.python.org/pypi/setuptools). 
3. Asenna PIP (http://pypi.python.org/pypi/pip) komennolla `easy_install pip`.
4. Asenna kappaleessa "Projektin asentaminen" mainitut kirjastot PIP:llä.

Ympäristön asentaminen Linuxeille
---------------------------------
1. Asenna PIP distrosi paketinhallinnalla, esim. `apt-get install python-pip`.
2. Asenna kappaleessa "Projektin asentaminen" mainitut kirjastot joko käyttäen PIP:iä tai distrosi pakettienhallintaa. 
   PIL-kirjaston asennus käyttäen PIP:ä saattaa vaatia jotain lisäkirjastoja kääntämiseen. Lisäkirjastojen asentamisen
   saattaa pystyä välttämään asentamalla PIL:n suoraan distron pakettienhallinnasta, esim. `apt-get install python-imaging` tjsp.
   Mikäli asennat virtualenv:n, kannattaa käyttää PIL-kirjaston sijasta PILLOW-kirjastoa.

Projektin asentaminen
---------------------
1. Kloonaa tämä projekti gitillä (git clone ...).
2. Kopioi `settings.py-dist` tiedostoksi `settings.py`.
2. Suorita syncdb projektihakemistossa (`python manage.py syncdb`).
3. Suorita migrate projektihakemistossa (`python manage.py migrate`).
4. Testaa ajamalla runserver (`python manage.py runserver`). Jos gittiin ilmestyy tietokantamallimuutoksia, saattaa
   joskus olla tarpeen suorittaa migrate ja syncdb uudelleen.

Kirjastot
---------
* [Django 1.6 tai uudempi] (https://www.djangoproject.com/download/) `pip install django`
* [python-social-auth] (https://github.com/omab/python-social-auth) `pip install python-social-auth`
* [django-countries] (https://bitbucket.org/smileychris/django-countries) `pip install django-countries`
* [PIL] (http://www.pythonware.com/products/pil/) `pip install pil`
* [django-imagekit] (https://github.com/jdriscoll/django-imagekit) `pip install django-imagekit`
* [South] (http://south.aeracode.org/) `pip install south`
* [django-crispy-forms] (http://django-crispy-forms.readthedocs.org/) `pip install django-crispy-forms`
* [reportlab] (http://www.reportlab.com/software/opensource/rl-toolkit/download/) `pip install reportlab`
* [django-twitter-tag] (https://github.com/coagulant/django-twitter-tag) `pip install django-twitter-tag`
* [django_tables2] (http://django-tables2.readthedocs.org) `pip install django-tables2`
* [django-debug-toolbar] (http://django-debug-toolbar.readthedocs.org) `pip install django-debug-toolbar`

Onelineri kirjastojen asentamiseen
----------------------------------
Seuraava koodirimpsu hakee kaikki tarpeelliset python-kirjastot ja dependenssit.

    pip install django python-social-auth django-countries django-imagekit django-twitter-tag django-tables2 django-debug-toolbar django-crispy-forms south reportlab pil

Testitapausten ajaminen
-----------------------

testing/ -hakemistossa on esimerkkejä Robot Framework - Selenium 2 -testeistä, joilla voidaan automatisoida nettisivujen klikkailua.

Testien ajamiseen tarvitset robotframework-selenium2library -palikan:

    pip install robotframework-selenium2library

Tämän jälkeen testin voi ajaa testing-hakemistossa komennolla

    pybot -d output/ testinnimi.txt

Testi tuottaa output-hakemistoon testiraportin ja kuvakaappauksen lopputilastaan.
