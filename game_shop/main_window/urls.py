from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.show_homepage),
    path('Signup_page', views.show_regpage),
    path('checkuser', views.checkuser),
    path('signup', views.sign_up),
    path('orders_archam', views.show_orderpage_archam),
    path('orders_caribian', views.show_orderpage_caribian),
    path('orders_cringe', views.show_orderpage_cringe),
    path('create_order_caribian', views.create_order_caribian),
    path('create_order_archam', views.create_order_archam),
    path('create_order_cringe', views.create_order_cringe),
    path('my_orders', views.show_my_orders),
    path('get_order_table', views.get_my_orders)
] + static(settings.STATIC_URL, document_rootr=settings.STATIC_ROOT)
