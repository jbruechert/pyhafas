import pytz

from pyhafas.profile.base import BaseProfile


class OEBBProfile(BaseProfile):
    """
    Profile of the HaFAS of ÖBB - Austrian Railway - Regional and long-distance trains throughout Austria and most parts of Europe
    """
    baseUrl = "https://fahrplan.oebb.at/bin/mgate.exe"
    defaultUserAgent = "DB Navigator/19.10.04 (iPhone; iOS 13.1.2; Scale/2.00)"

    salt = 'OWDL4fE4ixNiPBBm'
    addChecksum = True

    locale = 'de-AT'
    timezone = pytz.timezone('Europe/Vienna')

    requestBody = {
        "client": {
            "type": "IPH",
            "id": "OEBB",
            "v": "6030600",
            "name": "oebbPROD-ADHOC"
        },
        "ver": "1.45",
        "lang": "de",
        "auth": {
            "type": "AID",
            "aid": "OWDL4fE4ixNiPBBm"
        },
    }

    availableProducts = {
        'long_distance_express': [1],  # ICE
        'long_distance': [2, 4, 8],  # IC/EC
        'regional': [16],  # RB/RE/IR
        'suburban': [32],  # S
        'bus': [64],  # BUS
        'ferry': [128],  # F
        'subway': [256],  # U
        'tram': [512],  # T
        'taxi': [1024]  # Group Taxi
    }

    defaultProducts = [
        'long_distance_express',
        'long_distance',
        'regional',
        'suburban',
        'bus',
        'ferry',
        'subway',
        'tram',
        'taxi'
    ]
