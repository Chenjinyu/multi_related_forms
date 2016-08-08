from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Store, Backroom, MountedCabinet, MusicLocation, NetMusic, Scale, WiFiAndNetPrinter, AddtionalFields

from onlineform.attrs_override import *

class StorePostForm(forms.ModelForm):
    
    class Meta:
        model = Store
        widgets = {
            'store_number': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'address': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'city': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'state': forms.Select(attrs = {'class': SELECT_CSS}),
            'zip_code': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'tel': forms.TextInput(attrs = {'class': INPUT_CSS}),
            'mgr': forms.TextInput(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'store_number': _(S_NUM_LBL),
            'address': _(S_ADDRESS_LBL),
            'city': _(S_CITY_LBL),
            'state': _(S_STATE_LBL),
            'zip_code': _(S_ZIP_LBL),
            'tel': _(S_TEL_LBL),
            'mgr': _(S_MGR_LBL),
		}
        exclude = ['is_publish', 'publish_datetime', 'is_finished']
		
		
		
class BRPostForm(forms.ModelForm):
    class Meta:
        model = Backroom
        widgets = {
            'backroom_notes': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'image': forms.FileInput(attrs = {'class': INPUT_CSS}),
            'move_motes': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'relatve_time': forms.NumberInput(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'is_valid': _(BR_IS_VALID_LBL),
            'backroom_notes': _(BR_BACKROOM_NOTES_LBL),
            'is_need_move': _(BR_IS_NEED_MOVE_LBL),
            'move_motes': _(BR_MOVE_NOTES_LBL),
            'relatve_time': _(BR_RELATIVE_TIME_LBL),
            'image': _(BR_IMAGE_LBL),
		}
        exclude = ['store']
		
		
class MCPostForm(forms.ModelForm):
    class Meta:
        model = MountedCabinet
        widgets = {
            'mounted_cabinet_notes': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'image': forms.FileInput(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'mounted_cabinet_notes': _(MC_NOTES_LBL),
            'image': _(MC_IMAGE_LBL),
        }
        exclude = ['store']

		
		
class MLPostForm(forms.ModelForm):
    class Meta:
        model = MusicLocation
        widgets = {
            'music_loc_des': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'image': forms.FileInput(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'music_loc_des': _(ML_DES_LBL),
            'image': _(ML_IMAGE_LBL),
        }
        exclude = ['store']
		
		
class NMPostForm(forms.ModelForm):
    class Meta:
        model = NetMusic
        widgets = {
            'net_music_notes': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'image': forms.FileInput(attrs = {'class': INPUT_CSS}),
            'music_dataline_des': forms.Textarea(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'is_net_music_valid': _(NM_IS_NET_MUSIC_VALID_LBL),
            'net_music_notes': _(NM_NET_MUSIC_PHOTO_NOTE_LBL),
            'image': _(NM_IMAGE_LBL),
            'music_dataline_des': _(NM_DATALINE_DES_LBL),
        }
        exclude = ['store']
		
		
class SPostForm(forms.ModelForm):
    class Meta:
        model = Scale
        widgets = {
            'scale_line_des': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'image': forms.FileInput(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'scale_line_des': _(SC_LINE_DES_LBL),
            'image': _(SC_IMAGE_LBL),
        }
        exclude = ['store']
		

class WFNPPostForm(forms.ModelForm):
    class Meta:
        model = WiFiAndNetPrinter
        widgets = {
            'no_indicate_singal_des': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'net_printer_des': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'image': forms.FileInput(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'is_valid': _(WFNP_IS_VALID_LBL),
            'no_indicate_singal_des': _(WFNP_NO_INDICATE_SINGAL_DSC_LBL),
            'net_printer_des': _(WFNP_NET_PRINTER_DES_LBL),
            'image': _(WFNP_IMAGE_LBL),
        }
        exclude = ['store']
		
		
class AdditionalForm(forms.ModelForm):
    
    class Meta:
        model = AddtionalFields
        widgets = {
            'comments': forms.Textarea(attrs = {'class': INPUT_CSS}),
            'image_1' : forms.FileInput(attrs = {'class': INPUT_CSS}),
            'image_2' : forms.FileInput(attrs = {'class': INPUT_CSS}),
            'image_3' : forms.FileInput(attrs = {'class': INPUT_CSS}),
            'image_4' : forms.FileInput(attrs = {'class': INPUT_CSS}),
            'image_5' : forms.FileInput(attrs = {'class': INPUT_CSS}),
        }
        labels = {
            'comments': _(ADDI_COMMENTS_LBL),
            'image_1': _(ADDI_IMAGE_LBL),
            'image_2': _(ADDI_IMAGE_LBL),
            'image_3': _(ADDI_IMAGE_LBL),
            'image_4': _(ADDI_IMAGE_LBL),
            'image_5': _(ADDI_IMAGE_LBL),
        }
        exclude = ['store']