import datetime
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, render_to_response  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import Store, Backroom, MountedCabinet, MusicLocation, NetMusic, Scale, WiFiAndNetPrinter, AddtionalFields
from .forms import StorePostForm, BRPostForm, MCPostForm, MLPostForm, NMPostForm, SPostForm, WFNPPostForm, AdditionalForm

error_message = 'Message would be lost, please click below link re-fill it.'
cancel_message = 'Do you want to canel this form? If yes, all of information woul be lost.'
succ_message = 'Thank you submitted your information. You can input telephone number as below input field see the detail.'
in_valid_usr_message = 'You are not valid user.'

def del_sessions(request):
    if 'store_id' in request.session:
        del request.session['store_id']
    if 'store_modi_id' in request.session:
        del request.session['store_modi_id']
    if 'br_id' in request.session:
        del request.session['br_id']
    if 'br_modi_id' in request.session:
        del request.session['br_modi_id']
    if 'mc_id' in request.session:
        del request.session['mc_id']
    if 'mc_modi_id' in request.session:
        del request.session['mc_modi_id']
    if 'wfnp_id' in request.session:
        del request.session['wfnp_id']
    if 'wfnp_modi_id' in request.session:
        del request.session['wfnp_modi_id']
    if 'nm_id' in request.session:
        del request.session['nm_id']
    if 'nm_modi_id' in request.session:
        del request.session['nm_modi_id']
    if 'ml_id' in request.session:
        del request.session['ml_id']
    if 'm_modi_id' in request.session:
        del request.session['ml_modi_id']
    if 'cs_id' in request.session:
        del request.session['cs_id']
    if 'cs_modi_id' in request.session:
        del request.session['cs_modi_id']
		
		
def online_wel(request):
    
    del_sessions(request)
    return render(request, 'form_wel.html')

# Create your views here.
def store_post_create(request):

    if request.method == 'POST':
        if 'store_modi_id' in request.session:
            old_store_obj = get_object_or_404(Store, pk = request.session['store_modi_id'])
            form = StorePostForm(request.POST or None, instance = old_store_obj)
        else:  
            form = StorePostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            
            if 'store_modi_id' in request.session:
                request.session['store_id'] = request.session['store_modi_id']
            else: 
                request.session['store_id'] = post.pk 
            return HttpResponseRedirect(reverse(br_post_create))
    else:
        if 'store_id' in request.session.keys():
            instance = get_object_or_404(Store, pk = request.session['store_id'])
            form = StorePostForm(instance = instance)
            request.session['store_modi_id'] = request.session['store_id']
        else: 
            form = StorePostForm()
    return render(request, 'form_info_1.html', {'form': form})        
    
    
    
def br_post_create(request):

    if request.method == 'POST':
        if 'br_modi_id' in request.session:
            old_br_obj = get_object_or_404(Backroom, pk = request.session['br_modi_id'])
            form = BRPostForm(request.POST or None, instance = old_br_obj)
        else:
            form = BRPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit = False)
                
            # get store object, and relate with Backroom 
            if 'store_id' in request.session:
                store = get_object_or_404(Store, pk = request.session['store_id'])
            else:
                return render(request, 'form_wel.html', {'error_message': error_message})    

            post.store = store
            post.save()
            
            if 'br_modi_id' in request.session:
                request.session['br_id'] = request.session['br_modi_id']
            else: 
                request.session['br_id'] = post.pk 
            
            return HttpResponseRedirect(reverse(mc_post_create))
    else:
        
        if 'store_id' in request.session.keys() and 'br_id' in request.session.keys():
            instance = get_object_or_404(Backroom, pk = request.session['br_id'])
            form = BRPostForm(instance = instance)
            request.session['br_modi_id'] = request.session['br_id']
            
        else: 
            form = BRPostForm()
        
    return render(request, 'form_br_2.html', {'form': form})    
    
    
def mc_post_create(request):

    if request.method == 'POST':
        if 'mc_modi_id' in request.session:
            old_mc_obj = get_object_or_404(MountedCabinet, pk = request.session['mc_modi_id'])
            form = MCPostForm(request.POST or None, instance = old_mc_obj)
        else:
            form = MCPostForm(request.POST or None, request.FILES or None)
            
        if form.is_valid():
            post = form.save(commit = False)
            
            # get store object, and relate with MountedCabinet 
            if 'store_id' in request.session:
                store = get_object_or_404(Store, pk = request.session['store_id'])
            else:
                return render(request, 'form_wel.html', {'error_message': error_message})    

            post.store = store
            post.save()
            if 'mc_modi_id' in request.session:
                request.session['mc_id'] = request.session['mc_modi_id']
            else: 
                request.session['mc_id'] = post.pk 
            
            return HttpResponseRedirect(reverse(ml_post_create))
    else:
        if 'store_id' in request.session and 'mc_id' in request.session:
            instance = get_object_or_404(MountedCabinet, pk = request.session['mc_id'])
            form = MCPostForm(instance = instance)
            request.session['mc_modi_id'] = request.session['mc_id']
            
        else: 
            form = MCPostForm()
        
    return render(request, 'form_mc_3.html', {'form': form})
    
    
def ml_post_create(request):

    if request.method == 'POST':
        if 'ml_modi_id' in request.session:
            old_ml_obj = get_object_or_404(MusicLocation, pk = request.session['ml_modi_id'])
            form = MLPostForm(request.POST or None, instance = old_ml_obj)
        else:
            form = MLPostForm(request.POST or None, request.FILES or None)
            
        if form.is_valid():
            post = form.save(commit = False)
            
            # get store object, and relate with MusicLocation 
            if 'store_id' in request.session:
                store = get_object_or_404(Store, pk = request.session['store_id'])
            else:
                return render(request, 'form_wel.html', {'error_message': error_message})    
            
            post.store = store
            post.save()
            if 'ml_modi_id' in request.session:
                request.session['ml_id'] = request.session['ml_modi_id']
            else: 
                request.session['ml_id'] = post.pk 
            
            return HttpResponseRedirect(reverse(nm_post_create))
    else:
        if 'store_id' in request.session and 'ml_id' in request.session:
        
            instance = get_object_or_404(MusicLocation, pk = request.session['ml_id'])
            form = MLPostForm(instance = instance)    
            request.session['ml_modi_id'] = request.session['ml_id']
            
        else: 
            form = MLPostForm()
        
    return render(request, 'form_ml_4.html', {'form': form})            
    
    
def nm_post_create(request):

    if request.method == 'POST':
        if 'nm_modi_id' in request.session:
            old_nm_obj = get_object_or_404(NetMusic, pk = request.session['nm_modi_id'])
            form = NMPostForm(request.POST or None, instance = old_nm_obj)
        else:
            form = NMPostForm(request.POST or None, request.FILES or None)
            
        if form.is_valid():
            post = form.save(commit = False)
            
            # get store object, and relate with NetMusic 
            if 'store_id' in request.session:
                store = get_object_or_404(Store, pk = request.session['store_id'])
            else:
                return render(request, 'form_wel.html', {'error_message': error_message})    
            
            post.store = store
            post.save()
            if 'nm_modi_id' in request.session:
                request.session['nm_id'] = request.session['nm_modi_id']
            else: 
                request.session['nm_id'] = post.pk 
            
            return HttpResponseRedirect(reverse(sc_post_create))
    else:
        if 'store_id' in request.session and 'nm_id' in request.session:
            instance = get_object_or_404(NetMusic, pk = request.session['nm_id'])
            form = NMPostForm(instance = instance)    
            request.session['nm_modi_id'] = request.session['nm_id']
            
        else: 
            form = NMPostForm()

    return render(request, 'form_nm_5.html', {'form': form})        

    
def sc_post_create(request):

    if request.method == 'POST':
        if 'cs_modi_id' in request.session:
            old_cs_obj = get_object_or_404(Scale, pk = request.session['cs_modi_id'])
            form = SPostForm(request.POST or None, instance = old_cs_obj)
        else:
            form = SPostForm(request.POST or None, request.FILES or None)
            
        if form.is_valid():
            post = form.save(commit = False)
            
            # get store object, and relate with Scale 
            if 'store_id' in request.session:
                store = get_object_or_404(Store, pk = request.session['store_id'])
            else:
                return render(request, 'form_wel.html', {'error_message': error_message})    
            
            post.store = store
            post.save()
            
            if 'cs_modi_id' in request.session:
                request.session['cs_id'] = request.session['cs_modi_id']
            else: 
                request.session['cs_id'] = post.pk 
            
            return HttpResponseRedirect(reverse(wfnp_post_create))
    else:
        if 'store_id' in request.session and 'cs_id' in request.session:
            instance = get_object_or_404(Scale, pk = request.session['cs_id'])
            form = SPostForm(instance = instance)    
            request.session['cs_modi_id'] = request.session['cs_id']
        else: 
            form = SPostForm()

    return render(request, 'form_sc_6.html', {'form': form})        


def wfnp_post_create(request):

    if request.method == 'POST':
        if 'wfnp_modi_id' in request.session:
            old_wfnp_obj = get_object_or_404(WiFiAndNetPrinter, pk = request.session['wfnp_modi_id'])
            form = WFNPPostForm(request.POST or None, instance = old_wfnp_obj)
        else:
            form = WFNPPostForm(request.POST or None, request.FILES or None)
            
        if form.is_valid():
            post = form.save(commit = False)
            
            # get store object, and relate with WiFiAndNetPrinter 
            if 'store_id' in request.session:
                store = get_object_or_404(Store, pk = request.session['store_id'])
            else:
                return render(request, 'onlineform_welcome.html', {'error_message': error_message})    
            
            post.store = store
            post.save()
            
            if 'wfnp_modi_id' in request.session:
                request.session['wfnp_id'] = request.session['wfnp_modi_id']
            else: 
                request.session['wfnp_id'] = post.pk 
                
            messages.add_message(request, messages.INFO, 'you have finished.')
            
            return HttpResponseRedirect(reverse(addtional_fields))
    else:
        if 'store_id' in request.session and 'wfnp_id' in request.session:
            instance = get_object_or_404(WiFiAndNetPrinter, pk = request.session['wfnp_id'])
            form = WFNPPostForm(instance = instance)
            request.session['wfnp_modi_id'] = request.session['wfnp_id']
            
        else: 
            form = WFNPPostForm()

    return render(request, 'form_wf_np_7.html', {'form': form})


def addtional_fields(request):
    
    if request.method == 'POST':
    
        form = AdditionalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit = False)
            
            if 'store_id' in request.session:
                store = get_object_or_404(Store, pk = request.session['store_id'])
                mgr_tel = store.tel
                store.is_publish = True
                store.publish_datetime = datetime.datetime.now()
            else:
                return render(request, 'form_wel.html', {'error_message': error_message})    
                
            post.store = store
            post.save()
            store.save()
            
            del_sessions(request)
            
            #return HttpResponseRedirect(reverse(online_wel), {'succ_message': succ_message})
            return render(request, 'form_wel.html', {'succ_message': succ_message + ' Your tel: ' + mgr_tel})
        else:
            print(form.errors)
            
    else:
        form = AdditionalForm()

    return render(request, 'form_addi_8.html', {'form': form})        


def online_list(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return render(request, 'form_wel.html', {'error_message': in_valid_usr_message})
    #form_list = Store.objects.all()
    form_list = Store.objects.all().filter(is_publish = True).order_by('-publish_datetime')
    paginator = Paginator(form_list, 30)
    
    page = request.GET.get('page')
    try:
        forms = paginator.page(page)
    except PageNotAnInteger:
        forms = paginator.page(1)
    except EmptyPage:
        forms = paginator.page(paginator.num_pages)
		
    return render(request, 'form_list.html', {'forms' : forms})
	

def online_detail(request, pk):
    if not request.user.is_staff and not request.user.is_superuser:
        return render(request, 'form_wel.html', {'error_message': in_valid_usr_message})
    try:
	
        store_row = Store.objects.get(pk = pk)
        if store_row.backroom_set.all().count():
            br_row = store_row.backroom_set.all()[0]
        else: br_row = None
		
        if store_row.mountedcabinet_set.all().count():
            mc_row = store_row.mountedcabinet_set.all()[0]
        else: mc_row = None
		
        if store_row.musiclocation_set.all().count():
            ml_row = store_row.musiclocation_set.all()[0]
        else: ml_row = None
		
        if store_row.netmusic_set.all().count():
            nm_row = store_row.netmusic_set.all()[0]
        else: nm_row = None
		
        if store_row.scale_set.all().count():
            sc_row = store_row.scale_set.all()[0]
        else: sc_row = None
		
        if store_row.wifiandnetprinter_set.all().count():
            wfnp_row = store_row.wifiandnetprinter_set.all()[0]
        else: wfnp_row = None
		
        if store_row.addtionalfields_set.all().count():
            addi_row = store_row.addtionalfields_set.all()[0]
        else: addi_row = None
		
        
    except Store.DoesNotExist:
        raise Http404("Online Form does not exist.")
        
    return render(request, 'form_detail.html', {'store_row': store_row, 
									   'br_row': br_row,
									   'mc_row': mc_row,
									   'ml_row': ml_row,
									   'nm_row': nm_row,
									   'sc_row': sc_row,
									   'wfnp_row': wfnp_row,
									   'addi_row': addi_row,
									   })


def online_del(request):
    if 'store_id' in request.session:
        store = get_object_or_404(Store, pk = request.session['store_id'])
        store.delete()
        del_sessions(request)
    data = {'info_message': 'You have cancelled this online form, you can click below link fill again. Thanks.', 'result': 1}
    return JsonResponse(data)
	

	
#-------- user login ------------
def user_login(request):
    if request.method == 'POST':
        usr = request.POST.get('id_username', '')
        pwd = request.POST.get('is_password', '')

        user = auth.authenticate(username = usr, password = pwd)
	
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse(online_list))
        else:
            return render(request, 'login.html', {'error_message': 'Your username or password is invalid, please check it again.'})
    else:
        return render(request, 'login.html')

		
def user_logout(request):
    auth.logout (request)
    return HttpResponseRedirect(reverse(user_login))
	
	
	
def customer_check(request):
    if request.method == 'POST':
        tel = request.POST.get('id_tel', '')
        if tel:
            form_list = Store.objects.all().filter(is_publish = True).filter(tel = tel).order_by('-publish_datetime')
            if form_list.count() is 0:	
                return render(request, 'form_wel.html', {'error_message': 'There is not any form relatived with the telephone number [%s] , please check your telephone again.' % tel})
				
            paginator = Paginator(form_list, 10)
    
            page = request.GET.get('page')
            try:
                forms = paginator.page(page)
            except PageNotAnInteger:
                forms = paginator.page(1)
            except EmptyPage:
                forms = paginator.page(paginator.num_pages)
		
            return render(request, 'form_list.html', {'forms' : forms, 'is_customer' : True})
    else:
        return render(request, 'form_wel.html', {'error_message': 'Refresh leads session lost, please re-fill your telephone number.'})
            

def customer_detail(request, pk):
    try:
        store_row = Store.objects.get(pk = pk)
        if store_row.backroom_set.all().count():
            br_row = store_row.backroom_set.all()[0]
        else: br_row = None
		
        if store_row.mountedcabinet_set.all().count():
            mc_row = store_row.mountedcabinet_set.all()[0]
        else: mc_row = None
		
        if store_row.musiclocation_set.all().count():
            ml_row = store_row.musiclocation_set.all()[0]
        else: ml_row = None
		
        if store_row.netmusic_set.all().count():
            nm_row = store_row.netmusic_set.all()[0]
        else: nm_row = None
		
        if store_row.scale_set.all().count():
            sc_row = store_row.scale_set.all()[0]
        else: sc_row = None
		
        if store_row.wifiandnetprinter_set.all().count():
            wfnp_row = store_row.wifiandnetprinter_set.all()[0]
        else: wfnp_row = None
		
        if store_row.addtionalfields_set.all().count():
            addi_row = store_row.addtionalfields_set.all()[0]
        else: addi_row = None
		
        
    except Store.DoesNotExist:
        raise Http404("Survery Form does not exist")
        
    return render(request, 'form_detail.html', {
									   'store_row': store_row, 
									   'br_row': br_row,
									   'mc_row': mc_row,
									   'ml_row': ml_row,
									   'nm_row': nm_row,
									   'sc_row': sc_row,
									   'wfnp_row': wfnp_row,
									   'addi_row': addi_row,
									})