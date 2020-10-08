from rest_framework import serializers

class UserDataSerializer(serializers.Serializer):
	"""this converts json objects into a generic python type"""

	ethnicity = serializers.CharField(max_length=500)
	religion = serializers.CharField(max_length=500)
	sat_score = serializers.FloatField()
	toefl_score = serializers.FloatField()