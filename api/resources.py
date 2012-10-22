from tastypie.resources import ModelResource
from api.models import Activity

class ActivityResource(ModelResource):
    class Meta:
        queryset = Activity.objects.all()
        allowed_methods = ['get']
