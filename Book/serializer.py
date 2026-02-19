from rest_framework import serializers
from Book.models import ListOfBooks, BookImages


class BookImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookImages
        fields = ['image']


class AccessBookSerializer(serializers.ModelSerializer):
    images=BookImagesSerializer(many=True)

    class Meta:
        model = ListOfBooks
        fields = ["id","title","author","price","is_published","images"]
        extra_kwargs = {"Is_published":{"write_only":True}}

    def create(self, validated_data):
        images_data=validated_data.pop('images',[])
        book=ListOfBooks.objects.create(**validated_data)
        for image_data in images_data:
            BookImages.objects.create(book=book, **image_data)
        return book