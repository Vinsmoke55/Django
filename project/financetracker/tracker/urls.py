from django.urls import path
from . import views


urlpatterns=[
	path("",views.ChartView,name="chart"),
	path("form",views.TransactionFormView,name="form")
]