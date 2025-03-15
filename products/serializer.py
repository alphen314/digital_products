from .models import File , Product , Catagory
from rest_framework import serializers


class Catagoryserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catagory
        fields = ('title','descreption','avatar','url')


class Fileserializer(serializers.ModelSerializer):
    file_type= serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('id','title','file','file_type')
    def get_file_type(self,obj):
        return obj.get_file_type_display()


class Productserializer(serializers.HyperlinkedModelSerializer):
    catagories = Catagoryserializer(many=True)
    files = Fileserializer(many=True)
    # foo = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id','title','descreption','avatar','catagories','files','url')
    # def get_foo(self,obj):
    #     return obj.id


