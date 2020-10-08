from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.linear_regression.api.serializers import UserDataSerializer


class RecommendCollege(APIView):
	serializer_class = UserDataSerializer
	
	def post(self, request):
		"""
			This endpoint returns a list of colleges based on some variables.
			this endpoint expects a post request with a user's SAT, TOEFL scores.
		"""
		serializer = self.serializer_class(request.data)

		#we will make a call to our machine learning function below
		#and pass it the serializer data above

		return Response(serializer.data, status=status.HTTP_200_OK)