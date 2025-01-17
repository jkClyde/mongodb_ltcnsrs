from django.db import models
from datetime import datetime

housing_CHOICES = (
    ('Permanent', 'Permanent'),
    ('Transient', 'Transient'),
)
lengthofstay_choices = (
    ('Year/s','Year/s'),
    ('Month/s','Month/s'),
    ('Week/s','Week/s'),
)
gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
bpe_choices = (
    ('Yes', 'Yes'),
    ('No', 'No')
)
vac_choices = (
    ('Ongoing', 'Ongoing'),
    ('None', 'None'),
    ('FIC','FIC'),
    ('CIC','CIC'),
    ('INC','INC'),
    ('None','None'),
)
deworming_choices = (
    
    ('Yes', 'Yes'),
    ('No', 'No')
)
relationship_choices = (
    ('Mother', 'Mother'),
    ('Father', 'Father'),
    ('Guardian', 'Guardian'),
    ('', 'not specified')
)
barangay_choices = (
    ("Alapang", "Alapang"),
    ("Alno", "Alno"),
    ("Ambiong", "Ambiong"),
    ("Balili", "Balili"),
    ("Bahong", "Bahong"),
    ("Beckel", "Beckel"),
    ("Betag", "Betag"),
    ("Bineng", "Bineng"),
    ("Cruz", "Cruz"),
    ("Lubas", "Lubas"),
    ("Pico", "Pico"),
    ("Poblacion", "Poblacion"),
    ("Puguis", "Puguis"),
    ("Shilan", "Shilan"),
    ("Tawang", "Tawang"),
    ("Wangal", "Wangal"),
)
ethnicity_choices = (
    ('OTHERS', 'Others'),
    ('AGGAY', 'AGGAY'),
    ('AKEANON/AKLANON', 'Akeanon/Aklanon'),
    ('APAYAO/YAPAYAO', 'Apayao/Yapayao'),
    ('AYANGAN', 'Ayangan'),
    ('BALANGAO/BALIWON', 'Balangao/Baliwon'),
    ('BIKOL/BICOL', 'Bikol/Bicol'),
    ('BISAYA/BINISAYA', 'Bisaya/Binisaya'),
    ('BONTOK/BINONTOK', 'Bontok/Binontok'),
    ('CEBUANO', 'Cebuano'),
    ('HAMTIKANON', 'Hamtikanon'),
    ('HILIGAYNON,ILONGGO', 'Hiligaynon,Ilonggo'),
    ('IBALOI/INIBALOI', 'Ibaloi/Inibaloi'),
    ('IBANAG', 'Ibanag'),
    ('IBONTOC', 'Ibontoc'),
    ('IFUGAO', 'Ifugao'),
    ('KALANGUYA/IKALAHAN', 'Kalanguya/Ikalahan'),
    ('ILOCANO', 'Ilocano'),
    ('IRANON', 'Iranon'),
    ('ITNEG', 'Itneg'),
    ('KALINGA', 'Kalinga'),
    ('KANKANAI/KANKANAEY', 'Kankanai/Kankanaey'),
    ('KAPAMPANGAN', 'Kapampangan'),
    ('KARAO', 'Karao'),
    ('KINALINGA', 'Kinalinga'),
    ('KINIRAY-A', 'Kiniray-a'),
    ('MARANAO', 'Maranao'),
    ('MASBATENO/MASBATEAN', 'Masbateno/Masbatean'),
    ('PANGASINAN/PANGGALATO', 'Pangasinan/Panggalato'),
    ('SURIGAONON', 'Surigaonon'),
    ('TAGALOG', 'Tagalog'),
    ('TAUSUG', 'Tausug'),
    ('WARAY', 'Waray'),

)


disability_choices = (
    ('Cleft Palate', 'Cleft Palate'),
    ('Cerebral Palsy', 'Cerebral Palsy'),
    ('Congenital Heart Disease', 'Congenital Heart Disease'),
    ('Hydrocepalus', 'Hydrocepalus'),
    ('Down Syndrome', 'Down Syndrome'),
    ('Global Development Delay', 'Global Development Delay'),
    ('None', 'None'),
    ('Others', 'Others'),
)

class PrimaryChild(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=255, default='Not specified')
    surname = models.CharField(max_length=100, default='Not specified')
    firstname = models.CharField(max_length=100, default='Not specified')
    middlename = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    fullAddress = models.CharField(max_length=255, default='Not specified')
    houseNumberAndStreet = models.CharField(max_length=255, default='Not specified')
    sitio = models.CharField(max_length=255, default='Not specified')
    pt = models.CharField(max_length=30, choices=housing_CHOICES, default='')
    lengthOfStay = models.CharField(max_length=255, null=True,blank=True)
    lengthOfStayType = models.CharField(
        max_length=100, choices=lengthofstay_choices, null=True, blank=True)
    gender = models.CharField(
        max_length=100, choices=gender_choices, default='Not specified')
    birthdate = models.DateField(null=True, blank=True)
    aim = models.IntegerField(default=0)
    barangay = models.CharField(
        max_length=200, choices=barangay_choices, default='Not specified')
    birthWeight = models.FloatField(default=0)
    birthOrder = models.CharField(max_length=255, null=True, blank=True)

    currentCaregiver = models.CharField(max_length=255, default='Not specified')
    fatherSurname = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    fatherFirstName = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    fatherMiddleName = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    fatherSuffix = models.CharField(max_length=10, blank=True, null=True)
    fatherAge = models.CharField(max_length=255,  null=True, blank=True)
    fatherEthnicity = models.CharField(
        max_length=100, choices=ethnicity_choices, null=True, blank=True)
    fatherOccupation = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    fatherReligion = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    fatherContact = models.CharField(max_length=255,  null=True, blank=True)

    motherSurname = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    motherFirstName = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    motherMiddleName = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    motherAge = models.CharField(max_length=255, null=True, blank=True)
    motherEthnicity = models.CharField(
        max_length=100, choices=ethnicity_choices, null=True, blank=True)
    motherOccupation = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    motherReligion = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    motherContact = models.CharField(max_length=255, null=True, blank=True)

    caregiverSurname = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    caregiverFirstName = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    caregiverMiddleName = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    caregiverSuffix = models.CharField(max_length=10, blank=True, null=True)
    caregiverRelationship = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    caregiverEthnicity = models.CharField(
        max_length=100, choices=ethnicity_choices, null=True, blank=True)
    caregiverAge = models.CharField(max_length=255,  null=True, blank=True)
    caregiverOccupation = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    caregiverReligion = models.CharField(max_length=255, default='Unknown', null=True, blank=True)
    caregiverContact = models.CharField(max_length=255, null=True, blank=True)

    archive = models.BooleanField(default=False) 
    def save(self, *args, **kwargs):
        caregivers = [self.fatherFirstName, self.motherFirstName, self.caregiverFirstName]
        present_caregivers = [caregiver for caregiver in caregivers if caregiver]

        if present_caregivers:
            self.currentCaregiver = '/'.join(present_caregivers)
        else:
            self.currentCaregiver = "Not specified"

        if self.houseNumberAndStreet and self.sitio:
            self.fullAddress = f"{self.houseNumberAndStreet}, {self.sitio}"
        else:
            self.fullAddress = "Not specified"

        # Merge surname, firstname, and middlename to update fullName
        if self.surname and self.firstname:
            self.fullName = f"{self.surname}, {self.firstname}"
            if self.middlename:
                self.fullName += f" {self.middlename}"
        else:
            self.fullName = "Not specified"

        # Check for duplicates based on fullName, birthdate, and barangay
        duplicates = PrimaryChild.objects.filter(
            fullName=self.fullName,
            surname=self.surname,
            firstname=self.firstname,
            middlename=self.middlename,
            birthdate=self.birthdate,
        ).exclude(id=self.id)

        if duplicates.exists():
            raise ValueError("Duplicate entry found.")

        # Calculate age and set the archive status based on age
        if self.birthdate:
            today = datetime.now().date()
            age = (today.year - self.birthdate.year) * 12 + today.month - self.birthdate.month
            self.aim = age
            
            if self.aim > 59:
                self.archive = True
            else:
                self.archive = False

        super(PrimaryChild, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullName 
    
class ChildHealthInfo(models.Model):
    childHealth_id = models.AutoField(primary_key=True)
    dow = models.DateField(null=True, blank=True)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    muac = models.FloatField(default=0)
 
    
    bpe = models.CharField(max_length=10, choices=bpe_choices, default='No')
    disability = models.CharField(
        max_length=100, choices=disability_choices, default='None')
    otherDisability = models.CharField(max_length=255, null=True, blank=True)
    child = models.ForeignKey(PrimaryChild, on_delete=models.CASCADE)
    quarter = models.CharField(max_length=20, default='1st Quarter')
    year = models.IntegerField(null=True, blank=True)  # Add a year field
    getYear = models.IntegerField(null=True, blank=True)  
    weightForAge = models.CharField(max_length=50, blank=True, default='')
    weightForLength = models.CharField(max_length=50, blank=True, default='')
    lengthForAge = models.CharField(max_length=50, blank=True, default='')

    #vitamin
    vaccinationRemarks = models.CharField(max_length=100, blank=True, default='')
    vitAOneHTIU = models.DateField(null=True, blank=True)

    #other vita by age
    vitATwoHTIUOneYear = models.DateField(null=True, blank=True)
    vitATwoHTIUOneSixYear = models.DateField(null=True, blank=True)

    vitATwoHTIUTwoYear = models.DateField(null=True, blank=True)
    vitATwoHTIUTwoSixYear = models.DateField(null=True, blank=True)

    vitATwoHTIUThreeYear = models.DateField(null=True, blank=True)
    vitATwoHTIUThreeSixYear = models.DateField(null=True, blank=True)

    vitATwoHTIUFourYear = models.DateField(null=True, blank=True)
    vitATwoHTIUFourSixYear = models.DateField(null=True, blank=True)

    vitATwoHTIUFiveYear = models.DateField(null=True, blank=True)

    #deworming 
    dewormingOneYear = models.DateField(null=True, blank=True)
    dewormingOneSixYear = models.DateField(null=True, blank=True)

    dewormingTwoYear = models.DateField(null=True, blank=True)
    dewormingTwoSixYear = models.DateField(null=True, blank=True)
    
    dewormingThreeYear = models.DateField(null=True, blank=True)
    dewormingThreeSixYear = models.DateField(null=True, blank=True)

    dewormingFourYear = models.DateField(null=True, blank=True)
    dewormingFourSixYear = models.DateField(null=True, blank=True)

    dewormingFiveYear= models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate the quarter based on the dow field
        if self.dow:
            if self.dow.month in [1, 2, 3]:
                self.quarter = '1st Quarter'
            elif self.dow.month in [4, 5, 6]:
                self.quarter = '2nd Quarter'
            elif self.dow.month in [7, 8, 9]:
                self.quarter = '3rd Quarter'
            elif self.dow.month in [10, 11, 12]:
                self.quarter = '4th Quarter'
            if self.dow.year:
                get_year = self.dow.year
                self.getYear = get_year

            # Calculate the year based on the birthdate of the child
            if self.child.birthdate:
                birth_year = self.child.birthdate.year
                self.year = birth_year
    
        super(ChildHealthInfo, self).save(*args, **kwargs)
    
class DuplicateChild(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    first_barangay = models.CharField(max_length=255)
    second_barangay = models.CharField(max_length=255)
    isDuplicate = models.BooleanField(default=False)
    