
from django.contrib import admin
from django.urls import path
from LiquidGold import views
from django.contrib.auth import views as auth_views
from LiquidGold.views import SearchAppView

urlpatterns = [
    path('admin/', admin.site.urls, name='adminlogin'),
    path('', views.SiteListView, name='sitelist'),
    path('<int:id>/', views.newRequestFormView, name='makerequest'),

    #################################### Ope added ##########################################
    path('justification/<int:id>/', views.add_justification,
         name='justification_form'),
    path('justified_requests/', views.justified_requests,
         name='justified-requests'),

    path('justified_requests/<int:id>/',
         views.approve_justified_request, name='approve-detail'),
    path('approve_lt35days_requests/',
         views.approve_lt35days_requests, name='approve-requests'),
    path('approve_lt35days_requests/<int:id>',
         views.approve_lt35days_request, name='approve-request-detail'),

    path('lt35days_requests/', views.manager_justification_view, name='all-lt35days'),
    path('lt35days_requests/<int:id>/',
         views.lt35days_deatil_view, name='detailed-lt35days'),
    #####################################################################################


    path('request/pending/all', views.pending_list, name='pending_requestlist'),
    path('request/approved/all', views.approved_list,
         name='approved_requestlist'),
    path('user/', views.ManagerAllocation, name='user_account'),
    path('request/mapaproved/<int:pk>/',
         views.ManagerApproved, name='mgr_approved'),

    # --------------------------------CT0--------------------------------------------#
    path('request/cto/pending/all', views.cto_pending_list,
         name='cto_pending_requestlist'),
    path('request/cto/approved/all', views.cto_approved_list,
         name='cto_approved_requestlist'),
    path('request/cto/unapprove/<int:id>/',
         views.cto_approve_request, name='cto_approve'),
    path('request/cto/all/view/<int:id>',
         views.cto_request_view, name='cto_all_request_view'),
    path('request/cto/reject/<int:id>',
         views.cto_reject_request, name='cto_reject'),
    path('request/cto/all/view/<int:id>',
         views.cto_request_view, name='cto_all_request_view'),
    path('request/cto/unapprove/<int:id>/',
         views.cto_unapprove_request, name='cto_requestunapprove'),

    # --------------------------------CTO--------------------------------------------#

    path('request/all/view/<int:id>', views.request_view, name='all_request_view'),
    path('request/reject/<int:id>', views.reject_request, name='reject'),
    path('request/approve/<int:id>', views.approve_request, name='approve'),
    path('request/unapprove/<int:id>/',
         views.unapprove_request, name='requestunapprove'),
    path('request/rejected/all', views.request_rejected_list,
         name='request_rejected'),
    path('request/unreject/<int:id>', views.unreject_request, name='unreject'),
    path('search/', SearchAppView.as_view(), name='search'),
    path('accounts/login/',
         auth_views.LoginView.as_view(next_page='pending_requestlist'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('user/profile/', views.profile, name='user_profile'),
]
