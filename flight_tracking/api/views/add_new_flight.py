from ..models.flight import Flight
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import airportsdata


@api_view(["POST"])
def add_new_flight(request):
    """Get new flight info
    ---
    parameters:
        - data: string
    responseMessages:
        - code: 200
          message: Success
        - code: 404
          message: Not found
    """

    departures_flights = request.data.get("departures")
    arrivals_flights = request.data.get("arrivals")

    """for flight in departures_flights:
        Flight.objects.create(
            flight_number=flight["number"],
            departure_airport=flight["departure_airport"],
            arrival_airport=flight["arrival_airport"],
            departure_time=flight["departure_time"],
            arrival_time=flight["arrival_time"],
            aircraft_type=flight["aircraft_type"],
            airline=flight["airline"],
            country_departure=flight["country_departure"],
            country_arrival=flight["country_arrival"],
        )
    """
    print(departures_flights[0])
    print(arrivals_flights[0])
    data = airportsdata.load()
    append_data = []
    for i in data:
        append_data.append(data[i])
    print(append_data[0])
    return Response(
        {
            "sample_date": departures_flights[0],
            "flight_number": departures_flights[0]["number"],
            "departure_airport": departures_flights[0]["movement"]["airport"]["icao"],
            "arrival_airport": arrivals_flights[0]["movement"]["airport"]["iata"],
        },
        status=status.HTTP_200_OK,
    )
