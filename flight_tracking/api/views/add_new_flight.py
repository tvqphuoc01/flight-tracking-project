import dateutil.parser

from ..models.flight import Flight
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models.airport import Airport


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
    departure_airport = request.data.get("departure_airport")

    for flight in departures_flights:
        current_flight = Flight.objects.filter(flight_number=flight["number"]).last()
        if (
            current_flight
            and current_flight.departure_time
            != dateutil.parser.parse(flight["movement"]["scheduledTimeUtc"])
        ) or current_flight is None:
            try:
                Flight.objects.create(
                    flight_number=flight["number"],
                    departure_airport=Airport.objects.get(icao=departure_airport).iata,
                    arrival_airport=flight["movement"]["airport"]["iata"],
                    departure_time=flight["movement"]["scheduledTimeLocal"],
                    status=flight["status"],
                    airport=Airport.objects.get(icao=departure_airport),
                )
                Flight.country_arrival = Airport.objects.filter(
                    iata=Flight.arrival_airport
                ).last()["country_ip"]
                Flight.country_departure = Airport.objects.filter(
                    icao=departure_airport
                ).last()["country_ip"]
                Flight.save()
            except Exception as error:
                print(error)

    for flight in arrivals_flights:
        current_flight = Flight.objects.filter(flight_number=flight["number"]).last()
        if current_flight and current_flight.arrival_time is None:
            try:
                current_flight.arrival_time = flight["movement"]["scheduledTimeLocal"]
                current_flight.status = flight["status"]
                current_flight.save()
            except Exception as error:
                print(error)

    return Response(
        status=status.HTTP_200_OK,
    )
