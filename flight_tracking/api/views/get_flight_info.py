from ..models.flight import Flight
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_flight_info(request, flight_id):
    """Get flight info by flight id
    ---
    parameters:
        - flight_id: string
    responseMessages:
        - code: 200
          message: Success
        - code: 404
          message: Not found
    """
    try:
        flight = Flight.objects.get(id=flight_id)
        return Response(flight.to_dict(), status=status.HTTP_200_OK)
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
