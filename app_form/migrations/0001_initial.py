# Generated by Django 4.2.6 on 2023-12-09 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DuplicateChild',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('first_barangay', models.CharField(max_length=255)),
                ('second_barangay', models.CharField(max_length=255)),
                ('isDuplicate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryChild',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(default='Not specified', max_length=255)),
                ('surname', models.CharField(default='Not specified', max_length=100)),
                ('firstname', models.CharField(default='Not specified', max_length=100)),
                ('middlename', models.CharField(default='Not specified', max_length=100)),
                ('suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('fullAddress', models.CharField(default='Not specified', max_length=255)),
                ('houseNumberAndStreet', models.CharField(default='Not specified', max_length=255)),
                ('sitio', models.CharField(default='Not specified', max_length=255)),
                ('pt', models.CharField(choices=[('Permanent', 'Permanent'), ('Transient', 'Transient')], default='', max_length=30)),
                ('lengthOfStay', models.CharField(default='Not specified', max_length=255, null=True)),
                ('lengthOfStayType', models.CharField(choices=[('Year/s', 'Year/s'), ('Month/s', 'Month/s'), ('Week/s', 'Week/s')], default='Not specified', max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Not specified', max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('aim', models.IntegerField(default=0)),
                ('barangay', models.CharField(choices=[('Alapang', 'Alapang'), ('Alno', 'Alno'), ('Ambiong', 'Ambiong'), ('Balili', 'Balili'), ('Bahong', 'Bahong'), ('Beckel', 'Beckel'), ('Betag', 'Betag'), ('Bineng', 'Bineng'), ('Cruz', 'Cruz'), ('Lubas', 'Lubas'), ('Pico', 'Pico'), ('Poblacion', 'Poblacion'), ('Puguis', 'Puguis'), ('Shilan', 'Shilan'), ('Tawang', 'Tawang'), ('Wangal', 'Wangal')], default='Not specified', max_length=200)),
                ('birthWeight', models.FloatField(default=0)),
                ('birthOrder', models.CharField(default='Not specified', max_length=255)),
                ('currentCaregiver', models.CharField(default='Not specified', max_length=255)),
                ('fatherSurname', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('fatherFirstName', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('fatherMiddleName', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('fatherSuffix', models.CharField(blank=True, max_length=10, null=True)),
                ('fatherAge', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('fatherEthnicity', models.CharField(blank=True, choices=[('OTHERS', 'Others'), ('AGGAY', 'AGGAY'), ('AKEANON/AKLANON', 'Akeanon/Aklanon'), ('APAYAO/YAPAYAO', 'Apayao/Yapayao'), ('AYANGAN', 'Ayangan'), ('BALANGAO/BALIWON', 'Balangao/Baliwon'), ('BIKOL/BICOL', 'Bikol/Bicol'), ('BISAYA/BINISAYA', 'Bisaya/Binisaya'), ('BONTOK/BINONTOK', 'Bontok/Binontok'), ('CEBUANO', 'Cebuano'), ('HAMTIKANON', 'Hamtikanon'), ('HILIGAYNON,ILONGGO', 'Hiligaynon,Ilonggo'), ('IBALOI/INIBALOI', 'Ibaloi/Inibaloi'), ('IBANAG', 'Ibanag'), ('IBONTOC', 'Ibontoc'), ('IFUGAO', 'Ifugao'), ('KALANGUYA/IKALAHAN', 'Kalanguya/Ikalahan'), ('ILOCANO', 'Ilocano'), ('IRANON', 'Iranon'), ('ITNEG', 'Itneg'), ('KALINGA', 'Kalinga'), ('KANKANAI/KANKANAEY', 'Kankanai/Kankanaey'), ('KAPAMPANGAN', 'Kapampangan'), ('KARAO', 'Karao'), ('KINALINGA', 'Kinalinga'), ('KINIRAY-A', 'Kiniray-a'), ('MARANAO', 'Maranao'), ('MASBATENO/MASBATEAN', 'Masbateno/Masbatean'), ('PANGASINAN/PANGGALATO', 'Pangasinan/Panggalato'), ('SURIGAONON', 'Surigaonon'), ('TAGALOG', 'Tagalog'), ('TAUSUG', 'Tausug'), ('WARAY', 'Waray')], default='Not specified', max_length=100, null=True)),
                ('fatherOccupation', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('fatherReligion', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('fatherContact', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('motherSurname', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('motherFirstName', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('motherMiddleName', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('motherAge', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('motherEthnicity', models.CharField(blank=True, choices=[('OTHERS', 'Others'), ('AGGAY', 'AGGAY'), ('AKEANON/AKLANON', 'Akeanon/Aklanon'), ('APAYAO/YAPAYAO', 'Apayao/Yapayao'), ('AYANGAN', 'Ayangan'), ('BALANGAO/BALIWON', 'Balangao/Baliwon'), ('BIKOL/BICOL', 'Bikol/Bicol'), ('BISAYA/BINISAYA', 'Bisaya/Binisaya'), ('BONTOK/BINONTOK', 'Bontok/Binontok'), ('CEBUANO', 'Cebuano'), ('HAMTIKANON', 'Hamtikanon'), ('HILIGAYNON,ILONGGO', 'Hiligaynon,Ilonggo'), ('IBALOI/INIBALOI', 'Ibaloi/Inibaloi'), ('IBANAG', 'Ibanag'), ('IBONTOC', 'Ibontoc'), ('IFUGAO', 'Ifugao'), ('KALANGUYA/IKALAHAN', 'Kalanguya/Ikalahan'), ('ILOCANO', 'Ilocano'), ('IRANON', 'Iranon'), ('ITNEG', 'Itneg'), ('KALINGA', 'Kalinga'), ('KANKANAI/KANKANAEY', 'Kankanai/Kankanaey'), ('KAPAMPANGAN', 'Kapampangan'), ('KARAO', 'Karao'), ('KINALINGA', 'Kinalinga'), ('KINIRAY-A', 'Kiniray-a'), ('MARANAO', 'Maranao'), ('MASBATENO/MASBATEAN', 'Masbateno/Masbatean'), ('PANGASINAN/PANGGALATO', 'Pangasinan/Panggalato'), ('SURIGAONON', 'Surigaonon'), ('TAGALOG', 'Tagalog'), ('TAUSUG', 'Tausug'), ('WARAY', 'Waray')], default='Not specified', max_length=100, null=True)),
                ('motherOccupation', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('motherReligion', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('motherContact', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverSurname', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverFirstName', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverMiddleName', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverSuffix', models.CharField(blank=True, max_length=10, null=True)),
                ('caregiverRelationship', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverEthnicity', models.CharField(blank=True, choices=[('OTHERS', 'Others'), ('AGGAY', 'AGGAY'), ('AKEANON/AKLANON', 'Akeanon/Aklanon'), ('APAYAO/YAPAYAO', 'Apayao/Yapayao'), ('AYANGAN', 'Ayangan'), ('BALANGAO/BALIWON', 'Balangao/Baliwon'), ('BIKOL/BICOL', 'Bikol/Bicol'), ('BISAYA/BINISAYA', 'Bisaya/Binisaya'), ('BONTOK/BINONTOK', 'Bontok/Binontok'), ('CEBUANO', 'Cebuano'), ('HAMTIKANON', 'Hamtikanon'), ('HILIGAYNON,ILONGGO', 'Hiligaynon,Ilonggo'), ('IBALOI/INIBALOI', 'Ibaloi/Inibaloi'), ('IBANAG', 'Ibanag'), ('IBONTOC', 'Ibontoc'), ('IFUGAO', 'Ifugao'), ('KALANGUYA/IKALAHAN', 'Kalanguya/Ikalahan'), ('ILOCANO', 'Ilocano'), ('IRANON', 'Iranon'), ('ITNEG', 'Itneg'), ('KALINGA', 'Kalinga'), ('KANKANAI/KANKANAEY', 'Kankanai/Kankanaey'), ('KAPAMPANGAN', 'Kapampangan'), ('KARAO', 'Karao'), ('KINALINGA', 'Kinalinga'), ('KINIRAY-A', 'Kiniray-a'), ('MARANAO', 'Maranao'), ('MASBATENO/MASBATEAN', 'Masbateno/Masbatean'), ('PANGASINAN/PANGGALATO', 'Pangasinan/Panggalato'), ('SURIGAONON', 'Surigaonon'), ('TAGALOG', 'Tagalog'), ('TAUSUG', 'Tausug'), ('WARAY', 'Waray')], default='Not specified', max_length=100, null=True)),
                ('caregiverAge', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverOccupation', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverReligion', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('caregiverContact', models.CharField(blank=True, default='Unknown', max_length=255, null=True)),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChildHealthInfo',
            fields=[
                ('childHealth_id', models.AutoField(primary_key=True, serialize=False)),
                ('dow', models.DateField(blank=True, null=True)),
                ('weight', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('muac', models.FloatField(default=0)),
                ('vac', models.CharField(choices=[('Ongoing', 'Ongoing'), ('None', 'None'), ('FIC', 'FIC'), ('CIC', 'CIC'), ('INC', 'INC'), ('None', 'None')], default='No', max_length=10)),
                ('deworming', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('bpe', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('disability', models.CharField(choices=[('Cleft Palate', 'Cleft Palate'), ('Cerebral Palsy', 'Cerebral Palsy'), ('Congenital Heart Disease', 'Congenital Heart Disease'), ('Hydrocepalus', 'Hydrocepalus'), ('Down Syndrome', 'Down Syndrome'), ('Global Development Delay', 'Global Development Delay'), ('Others', 'Others')], default='Not specified', max_length=100)),
                ('quarter', models.CharField(default='1st Quarter', max_length=20)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('getYear', models.IntegerField(blank=True, null=True)),
                ('weightForAge', models.CharField(blank=True, default='', max_length=50)),
                ('weightForLength', models.CharField(blank=True, default='', max_length=50)),
                ('lengthForAge', models.CharField(blank=True, default='', max_length=50)),
                ('vaccinationRemarks', models.CharField(blank=True, default='', max_length=100)),
                ('vitAOneHTIU', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUOneYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUOneSixYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUTwoYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUTwoSixYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUThreeYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUThreeSixYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUFourYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUFourSixYear', models.DateField(blank=True, null=True)),
                ('vitATwoHTIUFiveYear', models.DateField(blank=True, null=True)),
                ('dewormingOneYear', models.DateField(blank=True, null=True)),
                ('dewormingOneSixYear', models.DateField(blank=True, null=True)),
                ('dewormingTwoYear', models.DateField(blank=True, null=True)),
                ('dewormingTwoSixYear', models.DateField(blank=True, null=True)),
                ('dewormingThreeYear', models.DateField(blank=True, null=True)),
                ('dewormingThreeSixYear', models.DateField(blank=True, null=True)),
                ('dewormingFourYear', models.DateField(blank=True, null=True)),
                ('dewormingFourSixYear', models.DateField(blank=True, null=True)),
                ('dewormingFiveYear', models.DateField(blank=True, null=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_form.primarychild')),
            ],
        ),
    ]
