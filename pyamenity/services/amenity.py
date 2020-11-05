from datetime import datetime
from datetime import timezone
from typing import Any

import requests


class Amenity:
    URL_STATISTICS = "https://d1va2v45wuqutp.cloudfront.net/v1/permits/policies/issue/statistics"

    def __init__(self, scope: str):
        self._client = requests.Session()
        self._scope = scope

    def _get_statistics(self) -> dict[str, Any]:
        now = datetime.now(timezone.utc)
        valid = now.date()
        self._client.get(self.URL_STATISTICS, params={
            'scope': self._scope,
            'viewpoint': viewpoint.isoformat(),
            'valid': valid.isoformat(),
        })
