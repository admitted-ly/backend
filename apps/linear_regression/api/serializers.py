from rest_framework import serializers

class UserDataSerializer(serializers.Serializer):
	"""this converts json objects into a generic python type"""

	zip_code = serializers.CharField(max_length=50)
	sat_score = serializers.FloatField(min_value=400.0, max_value=1600.0)
	