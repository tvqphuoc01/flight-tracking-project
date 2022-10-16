from ..models.flight import Flight
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_flight_info(request, flight_number):
    """Get flight info by flight number
    ---
    parameters:
        - flight_number: string
    responseMessages:
        - code: 200
          message: Success
        - code: 404
          message: Not found
    """
    try:
        flight = Flight.objects.get(flight_number=flight_number)
        return Response(
            {
                "flight_number": flight.flight_number,
                "departure_airport": flight.departure_airport,
                "arrival_airport": flight.arrival_airport,
                "departure_time": flight.departure_time,
                "arrival_time": flight.arrival_time,
                "status": flight.status,
            },
            status=status.HTTP_200_OK,
        )
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
