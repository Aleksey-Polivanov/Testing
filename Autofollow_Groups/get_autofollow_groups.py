from typing import Optional

import requests
import json

f = open('constants.json')
constants = json.load(f)

# ___________________Requests___________________
def get_autoffolow_groups(location_info: Optional[dict]) -> dict:
    url = constants['base_url'] + "Know/user/groups"
    headers = {"knowSessionId": constants['oleh_session_id']}
    body = {
        "LocationInfo": location_info,
        "AutoFollowingGroups": {
            "CurrentPage": 1,
            "PageSize": 30
        }
    }

    response = requests.post(url, json=body, headers=headers)
    return response.json()

# ______________________________________________

# ____________________Tests_____________________
def autofollow_US_Georgia_County_Muscogee(self):
    print("test_autofollow_US_Georgia_Muscogee_County")

    location = {
        "Country": "United States",
        "State": "Georgia",
        "County": "Muscogee County",
        "City": "Columbus",
        "Latitude": 32.4796289,
        "Longitude": -84.8983554
    }

    res = get_autoffolow_groups(location)
    self.assertEqual(res["responseCode"], 100)

    # self.assertEqual(res["responseCode"], 100)
    # assert res["responseObject"]["groups"]
    # assert len(res["responseObject"]["groups"]) == 3
    # assert res["responseObject"]["autoFollowingGroupIds"]
    # assert len(res["responseObject"]["autoFollowingGroupIds"]) == 3
    # assert "dbfbeb11-4da7-447f-8586-4ec6a1209d05" in res["responseObject"]["autoFollowingGroupIds"]  # Know NEWS!
    # assert "39f4b06d-bc3d-423e-b934-1d470fe555d6" in res["responseObject"]["autoFollowingGroupIds"]  # Georgia
    # assert "bcee640b-7beb-4817-b0be-9d247cec9683" in res["responseObject"]["autoFollowingGroupIds"]  # Muscogee County

def autofollow_US_Georgia_County_Chatham(self):
    print("test_autofollow_US_Georgia_Chatham_County")
    location = {
        "Country": "United States",
        "State": "Georgia",
        "County": "Chatham County",
        "City": "Savannah",
        "Latitude": 31.9995518,
        "Longitude": -81.1195685
    }

    res = get_autoffolow_groups(location)
    self.assertEqual(res["responseCode"], 100)

    # assert res["responseObject"]["groups"]
    # assert len(res["responseObject"]["groups"]) == 3
    # assert res["responseObject"]["autoFollowingGroupIds"]
    # assert len(res["responseObject"]["autoFollowingGroupIds"]) == 3
    # assert "dbfbeb11-4da7-447f-8586-4ec6a1209d05" in res["responseObject"]["autoFollowingGroupIds"]  # Know NEWS!
    # assert "39f4b06d-bc3d-423e-b934-1d470fe555d6" in res["responseObject"]["autoFollowingGroupIds"]  # Georgia
    # assert "ae896ec6-ee28-4ca3-b694-0eebb447a07e" in res["responseObject"]["autoFollowingGroupIds"]  # Chatham County

def autofollow_US_Kentucky_Fayette_County_Lexington(self):
    print("test_autofollow_US_Kentucky_Fayette_County_Lexington")
    location = {
        "Country": "United States",
        "State": "Kentucky",
        "County": "Fayette County",
        "City": "Lexington",
        "Latitude": 38.044978,
        "Longitude": -84.50262
    }

    res = get_autoffolow_groups(location)
    self.assertEqual(res["responseCode"], 100)

    # assert res["responseObject"]["groups"]
    # assert res["responseObject"]["autoFollowingGroupIds"]
    # assert "dbfbeb11-4da7-447f-8586-4ec6a1209d05" in res["responseObject"]["autoFollowingGroupIds"]  # Know NEWS!
    # assert "37f5f3e2-e786-4bc7-95c6-0c578cfb197b" in res["responseObject"]["autoFollowingGroupIds"]  # Lexington

def autofollow_no_location(self):
    print("test_autofollow_no_location")
    location = None

    res = get_autoffolow_groups(location)
    self.assertEqual(res["responseCode"], 100)

    # assert res["responseObject"]["groups"]
    # assert res["responseObject"]["autoFollowingGroupIds"]
    # assert len(res["responseObject"]["autoFollowingGroupIds"])
    # assert "dbfbeb11-4da7-447f-8586-4ec6a1209d05" in res["responseObject"]["autoFollowingGroupIds"]  # Know NEWS!

def test_autofollow_no_location(self):
    print("test_autofollow_no_location")
    location = None

    res = get_autoffolow_groups(location)
    self.assertEqual(res["responseCode"], 100)

    # assert res["responseObject"]["groups"]
    # assert res["responseObject"]["autoFollowingGroupIds"]
    # assert len(res["responseObject"]["autoFollowingGroupIds"])
    # assert "dbfbeb11-4da7-447f-8586-4ec6a1209d05" in res["responseObject"]["autoFollowingGroupIds"]  # Know NEWS!
