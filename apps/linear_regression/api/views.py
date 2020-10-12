from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.linear_regression.api.serializers import UserDataSerializer
from apps.linear_regression.utils.helper import get_colleges_list

class RecommendCollege(APIView):
	serializer_class = UserDataSerializer
	
	def post(self, request):
		"""
			This endpoint returns a list of colleges based on some variables.
			this endpoint expects a post request with a user's SAT score and zip code.
			The variables must be defined in this format:
			sat_score
			zip_code
		"""
	
		colleges_list = get_colleges_list(request.data['sat_score'], request.data['zip_code'])
		data = colleges_list[0]

		if len(data) > 0:
			return Response(data, status=status.HTTP_200_OK)
		else:
			return Response("Ooops!! We couldn't match you with any college", status=status.HTTP_200_OK)