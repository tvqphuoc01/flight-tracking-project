from ..models.airport import Airport
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_airport_info(request, airport_code):
    """Get airport info by airport code
    ---
    parameters:
        - airport_code: string
    responseMessages:
        - code: 200
          message: Success
        - code: 404
          message: Not found
    """
    try:
        airport = Airport.objects.get(iata=airport_code)
        return Response(
            {
                "airport_code": airport.iata,
                "airport_name": airport.name,
                "airport_city": airport.city,
                "airport_country_ip": airport.country_ip,
            },
            status=status.HTTP_200_OK,
        )
    except Airport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
