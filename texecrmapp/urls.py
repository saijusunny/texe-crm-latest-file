from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('forgotPassword/', views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword,name='resetPassword'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('users_lst',views.users_lst, name='users_lst'),
    path('staff_home',views.staff_home, name='staff_home'),
    path('ser_cmp',views.ser_cmp, name='ser_cmp'),
    path('add_complaint',views.add_complaint, name='add_complaint'),
    path('add_user_complaint',views.add_user_complaint, name='add_user_complaint'),
    path('add_service',views.add_service, name='add_service'),
    path('add_user_service',views.add_user_service, name='add_user_service'),
    path('add_staff',views.add_staff, name='add_staff'),
    path('edit_staff/<int:id>',views.edit_staff, name='edit_staff'),
    path('save_edit_staff/<int:id>',views.save_edit_staff, name='save_edit_staff'),
    path('delete_staff/<int:id>',views.delete_staff, name='delete_staff'),
    path('orders_dta',views.orders_dta, name='orders_dta'),

    path('all_events',views.all_events, name='all_events'),
    path('add_event',views.add_event, name='add_event'),
    path('update',views.update, name='update'),
    path('remove',views.remove, name='remove'),
    path('get_date_event',views.get_date_event, name='get_date_event'),
    path('view_items_orders/<int:id>',views.view_items_orders, name='view_items_orders'),

    path('filter_date_event',views.filter_date_event, name='filter_date_event'),
    path('create_event',views.create_event, name='create_event'),
    path('add_user_order/<int:id>',views.add_user_order, name='add_user_order'),
    path('prouct_list',views.prouct_list, name='prouct_list'),

    path('cart_cust_size',views.cart_cust_size, name='cart_cust_size'),
    path('cart_change_color',views.cart_change_color, name='cart_change_color'),
    path('cart_change_meterial',views.cart_change_meterial, name='cart_change_meterial'),
    path('cart_change_model',views.cart_change_model, name='cart_change_model'),
    path('save_cart/<int:id>',views.save_cart, name='save_cart'),
    path('orders_list/<int:id>',views.orders_list, name='orders_list'),
    path('filter_order',views.filter_order, name='filter_order'),
    path('filter_order_id',views.filter_order_id, name='filter_order_id'),
    path('change_order_status',views.change_order_status, name='change_order_status'),
    path('change_order_stage',views.change_order_stage, name='change_order_stage'),
    path('pending_orders',views.pending_orders, name='pending_orders'),
    path('filter_pending',views.filter_pending, name='filter_pending'),
    path('filter_pending_id',views.filter_pending_id, name='filter_pending_id'),
    path('today_orders',views.today_orders, name='today_orders'),
    path('filter_today_id',views.filter_today_id, name='filter_today_id'),
    path('change_order_status_client',views.change_order_status_client, name='change_order_status_client'),
    path('change_order_stage_client',views.change_order_stage_client, name='change_order_stage_client'),
    path('orders_list_client/<int:id>',views.orders_list_client, name='orders_list_client'),
    #########################################################################Staff Module
    path('staff_index',views.staff_index, name='staff_index'),
    path('registrations',views.registrations, name='registrations'),
    path('icons',views.icons, name='icons'),
    ########################################################################USER MODULE
    path('user_dashboard',views.user_dashboard, name='user_dashboard'),
    path('complaint_servicess',views.complaint_servicess, name='complaint_servicess'),
    path('order_user_view',views.order_user_view, name='order_user_view'),
    path('cancel_order/<int:id>',views.cancel_order, name='cancel_order'),
    ######################################################################################
    path('logout',views.logout, name='logout'),

    
]
