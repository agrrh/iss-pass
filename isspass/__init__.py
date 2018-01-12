import math
import requests
import logging


class ISSPass(object):
    """Class to detect if ISS is above specific location."""
    def __init__(self, lat, lon, deviation=0.25):
        self.location = (float(lat), float(lon))
        self.deviation = deviation

    def _get_iss_location(self):
        """Return ISS location."""
        api_url = 'http://api.open-notify.org/iss-now.json'
        """{
            "message": "success",
            "timestamp": 1515690245,
            "iss_position": {
                "longitude": "-167.6501",
                "latitude": "47.3412"
            }
        }"""

        res = requests.get(api_url)
        if res.status_code != 200:
            return False
        data = res.json()
        if 'message' not in data or data['message'] != 'success':
            return False
        try:
            return (
                float(data['iss_position']['latitude']),
                float(data['iss_position']['longitude'])
            )
        except KeyError:
            return False

    def is_above(self, loc=None):
        """Check if passage is between sane deviation, return True if so."""
        iss_location = loc if loc is not None else self._get_iss_location()

        if not iss_location:
            return None

        lat_abs = abs(iss_location[0] - self.location[0])
        lon_abs = abs(iss_location[1] - self.location[1])

        if math.sqrt(lat_abs**2 + lon_abs**2) < self.deviation:
            return True
        return False
