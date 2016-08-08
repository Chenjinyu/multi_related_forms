import os, datetime
from django.db import models

# Create your models here.

STATES_CHOICES = (
 ('Alabama', 'Alabama'), ('Alaska', 'Alaska'),  ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), 
 ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), 
 ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), 
 ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'),('Maryland', 'Maryland'), 
 ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), 
 ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), 
 ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), 
 ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), 
 ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'),  ('Texas', 'Texas'),  ('Utah', 'Utah'),  ('Vermont', 'Vermont'),  
 ('Virginia', 'Virginia'),  ('Washington', 'Washington'),  ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming'),
)

# for state field select list
class State(models.Model):
    state_name = models.CharField(max_length = 30)
     
    def __str__(self):
        return self.state_name
		

class Store(models.Model):
    # this field sometims it's a number, sometimes it some letters.
    store_number = models.CharField(max_length = 20, null = False) 
    address = models.CharField(max_length = 100, null = False)
    city = models.CharField(max_length = 30, null = False)
    state = models.CharField(max_length=20, choices = STATES_CHOICES, null = False)
    zip_code = models.CharField(max_length = 5, null = False)
    tel =  models.CharField(null = False, max_length = 10)
    mgr = models.CharField(max_length = 30, null = False)
    is_publish = models.BooleanField(default = False)
    publish_datetime = models.DateTimeField(null = True, auto_now = False, auto_now_add = False)
    is_finished = models.BooleanField(default = False)
    
    
    def __str__(self):
        return str(self.pk) + ' Store Number: ' + self.store_number + ' Manager: ' + self.mgr + ' Tel: ' + self.tel
	
def upload_location(instance, filename):
    filename, ext = os.path.splitext(filename.lower())
    filename = "%s_%s%s" % (filename, datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"), ext)
    return filename
    
		
class Photo(models.Model):
    '''
    this is used for store to storeage multi-photos.
    '''
    photo = models.ImageField(blank=True, null=True, upload_to = upload_location )
    store  = models.ForeignKey(Store)
	


# for v information with table row 1,2,3     
class Backroom(models.Model):
    is_valid = models.BooleanField(default = False)
    backroom_notes = models.TextField(blank = True)
    image = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    is_need_move = models.BooleanField(default = False)
    move_motes = models.TextField(blank = True)
    relatve_time = models.PositiveIntegerField()
    store = models.ForeignKey(Store)

    def __str__(self):
        return str(self.pk) + '->' + str(self.store.pk) + ' (BackRoom)Store Number: ' + self.store.store_number
	

# for MountedCabinet with table row 4
class MountedCabinet(models.Model):
    mounted_cabinet_notes = models.TextField(blank = True)
    image = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    store = models.ForeignKey(Store)

    def __str__(self):
        return str(self.pk) + '->' + str(self.store.pk) + ' (MountedCabinet)Store Number: ' + self.store.store_number	

		
# for MusicLocatioon with table row 5
class MusicLocation(models.Model):
    music_loc_des = models.TextField(blank = True)
    image = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    store = models.ForeignKey(Store)

    def __str__(self):
        return str(self.pk) + '->' + str(self.store.pk) + ' (MusicLocatioon)Store Number: ' + self.store.store_number	

		
# for table row 6,7 
class NetMusic(models.Model):
    is_net_music_valid = models.BooleanField(default = False)
    net_music_notes = models.TextField(blank = True)
    image = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    
    music_dataline_des = models.TextField(blank = True)
    store = models.ForeignKey(Store)
	
    def __str__(self):
        return str(self.pk) + '->' + str(self.store.pk) + ' (NetMusic)Store Number: ' + self.store.store_number	

		
# for table row 8
class Scale(models.Model):
    scale_line_des = models.TextField(blank = True)
    image = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    store = models.ForeignKey(Store)
	
    def __str__(self):
        return str(self.pk) + '->' + str(self.store.pk) + ' (Scale)Store Number: ' + self.store.store_number	


#for table row 9, 10
class WiFiAndNetPrinter(models.Model):
    is_valid = models.BooleanField(default = False)
    no_indicate_singal_des = models.TextField(blank = True)
    net_printer_des = models.TextField(blank = True)
    image = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    store = models.ForeignKey(Store)

    def __str__(self):
        return str(self.pk) + '->' + str(self.store.pk) + ' (WiFiAndNetPrinter)Store Number: ' + self.store.store_number	


class AddtionalFields(models.Model):
    comments = models.TextField(blank = True)
    image_1 = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    image_2 = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    image_3 = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    image_4 = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    image_5 = models.ImageField(upload_to = upload_location, 
                                                null = True,
                                                blank = True)
    store = models.ForeignKey(Store, default = None)
	
    def __str__(self):
        return str(self.pk) + '->' + str(self.store.pk) + ' (AddtionalFields)Store Number: ' + self.store.store_number