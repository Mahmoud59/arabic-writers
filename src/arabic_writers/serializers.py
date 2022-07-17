from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            "id": int(instance[0].strip('\n')) if type(instance[0]) is str
            else instance[0],
            "book_name": instance[1].strip('\n'),
            "author_name": instance[2].strip('\n'),
            "book_country": instance[3].strip('\n')
        }
