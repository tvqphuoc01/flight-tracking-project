from ..models.airport import Airport
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import airportsdata


@api_view(["POST"])
def add_airport(request):
    """Add new airport info
    ---
    responseMessages:
        - code: 200
           message: Success
    """
    data = airportsdata.load()
    append_data = []
    for i in data:
        append_data.append(data[i])
    for i in append_data:
        try:
            newAirport = Airport.objects.create(
                name=i["name"],
                iata=i["iata"],
                icao=i["icao"],
                city=i["city"],
                country_ip=i["country"],
            )
            newAirport.save()
        except Exception as e:
            print(e)
    return Response(
        {
            "message": "Airport added successfully",
        },
        status=status.HTTP_200_OK,
    )
