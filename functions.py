import requests


def time_convert_to24h_local_time_zone_format(fetched_time, time_offset):

    time, modifier = fetched_time.split()
    hours, minutes = time.split(":")[:-1]
    time_offset_minutes = int(time_offset % 60)
    time_offset_hours = int((time_offset - time_offset_minutes) / 60)

    if hours == "12":
        hours = "00"

    if modifier == "PM":
        hours = int(hours) + 12

    hours = int(hours) + time_offset_hours
    minutes = int(minutes) + time_offset_minutes

    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1

    if minutes < 10:
        minutes = "0" + str(minutes)

    if hours < 0:
        hours = hours + 24

    if hours >= 24:
        hours = hours - 24

    return f"{hours}:{minutes}"


def get_sunrise_sunset_times(country, date, API_KEY, API_KEY2):

    coordinates_response = requests.get(
        f"https://api.opencagedata.com/geocode/v1/json?q={country}&key={API_KEY}"
    )
    coordinates_data = coordinates_response.json()
    coordinates = {
        "latitude": coordinates_data["results"][0]["geometry"]["lat"],
        "longitude": coordinates_data["results"][0]["geometry"]["lng"],
        "timezone": coordinates_data["results"][0]["annotations"]["timezone"]["name"],
    }

    time_offset_response = requests.get(
        f"https://timezoneapi.io/api/timezone/?{coordinates['timezone']}&date={date}&token={API_KEY2}"
    )
    time_offset_data = time_offset_response.json()
    time_offset = time_offset_data["data"]["datetime"]["offset_minutes"]

    sunrise_sunset_time_response = requests.get(
        f"https://api.sunrise-sunset.org/json?lat={coordinates['latitude']}&lng={coordinates['longitude']}&date={date}"
    )
    sunrise_sunset_time_data = sunrise_sunset_time_response.json()

    sunrise_time = time_convert_to24h_local_time_zone_format(
        sunrise_sunset_time_data["results"]["sunrise"], int(time_offset)
    )
    sunset_time = time_convert_to24h_local_time_zone_format(
        sunrise_sunset_time_data["results"]["sunset"], int(time_offset)
    )

    return {
        "sunriseTime": sunrise_time,
        "sunsetTime": sunset_time,
    }, 200
