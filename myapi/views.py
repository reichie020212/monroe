import ast
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from myapi.functions import get_fuel_tank
from myapi.functions import get_fuel_consumption
from myapi.functions import get_maximum_mins


class AirplaneSolutionAPIView(views.APIView):
    """API for Airplane fuel solution
    This API accepts two query parameters namely id_list and passenger_list
    id_list and passenger_list values will be partnered to each other with respect to their index position
    For example, index 0 of id_list will be partner to index 0 if passenger_list
    If id_list and passenger_list count is not equal, excess values will be ignored"""

    parser_classes = [
        JSONParser
    ]

    def get(self, request, *args, **kwargs):
        id_list = request.GET.get('id_list') or None
        passenger_list = request.GET.get('passenger_list') or None
        try:
            id_list = ast.literal_eval(id_list)
        except Exception:
            return Response(
                "id_list must be a list of numbers",
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            passenger_list = ast.literal_eval(passenger_list)
        except Exception:
            return Response(
                "passenger_list must be a list of numbers",
                status=status.HTTP_400_BAD_REQUEST,
            )

        info = []
        for airplane_id, passenger in zip(id_list, passenger_list):
            if type(airplane_id) not in [int, float]:
                return Response(
                    "There is a string in your id_list",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if type(passenger) not in [int, float]:
                return Response(
                    "There is a string in your passenger_list",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            fuel_tank = get_fuel_tank(airplane_id)
            fuel_consumption = get_fuel_consumption(airplane_id, passenger)
            maximum_mins = get_maximum_mins(fuel_tank, fuel_consumption)
            info.append({
                'airplane_id': airplane_id,
                'passenger_count': passenger,
                'fuel_consumption_per_minute': fuel_consumption,
                'maximum_minutes_able_to_fly': maximum_mins,
            })

        return Response(
            info,
            status=status.HTTP_200_OK,
        )
