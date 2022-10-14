from ..models.airport import Airport
from ..models.country import Country
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
        - code: 400
           message: Bad request
    """
    data = airportsdata.load()
    append_data = []
    for i in data:
        append_data.append(data[i])
    for i in append_data:
        country = Country.objects.filter(country_ip=i["country"]).last()
        try:
            Airport.objects.create(
                airport_name=i["name"],
                airport_iata=i["iata"],
                airport_icao=i["icao"],
                airport_city=i["city"],
                airport_country=country,
            )
        except:
            return Response(
                {"message": "Airport already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    return Response(
        {
            "message": "Airport added successfully",
        },
        status=status.HTTP_200_OK,
    )
