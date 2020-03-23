from backapp import api_views as views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewset)
router.register(r'employee', views.EmployeeViewset)
