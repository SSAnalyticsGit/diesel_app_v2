from django.db import models




class RequestManager(models.Manager):
    
    def get_queryset(self):
        
        '''overrider all objects.all() queries return all requests.'''
        
        return super().get_queryset()
    
    
    def all_pending_requests(self):
        '''gets all pending requests'''
        
        return super().get_queryset().filter(noc_status = 'pending').order_by('-requestdate')
    
    def all_cancelled_requests(self):
        return super().get_queryset().filter(noc_status = 'cancelled').order_by('-requestdate')
    
    
    def all_rejected_requests(self):
        return super().get_queryset().filter(noc_status = 'rejected').order_by('-requestdate')
    
    def all_approved_requests(self):
        
        '''get all approved requests'''
        return super().get_queryset().filter(noc_status = 'confirmed').order_by('-requestdate')
    
    def cto_all_pending_requests(self):
        return super().get_queryset().filter(noc_status='confirmed', cto_status = 'pending').order_by('-requestdate') #using the noc_status for definition. Approved by Manager goes to CTO waiting list
                
    
    def cto_all_cancelled_requests(self):
        return super().get_queryset().filter(cto_status = 'cancelled').order_by('-requestdate')
    
    
    def cto_all_rejected_requests(self):
        return super().get_queryset().filter(cto_status = 'rejected').order_by('-requestdate')
    
    def cto_all_approved_requests(self):
        
        '''get all approved requests'''
        return super().get_queryset().filter(cto_status = 'approved').order_by('-requestdate')
    
    