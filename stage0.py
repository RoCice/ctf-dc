import requests
from env import config
import json
from utils.auth import IntersightAuth
from pprint import pprint

def getNTPPolicies():
    """connect and authenticate to Intersight and retrieve the ntp policies configured in this intersight tenant

    Returns
    ----------
    response_json
        Json Format of Response of the ntp policies

    Raises
    -------
    NotImplementedError
        If no ntp policies are set or the resource does not get found
    """

    try:
        auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'], api_key_id=config['INTERSIGHT_API_KEY'])
        BASE_URL='https://www.intersight.com/api/v1'
        url = f"{BASE_URL}/ntp/Policies"

        response = requests.get(url, auth=auth)
        response_json = response.json()

        return response_json

    except:
        raise NotImplementedError("No NTP policies are set!")




def main():

    test_req = getNTPPolicies()
    pprint(test_req, indent=4)



if __name__ == "__main__":
    # execute only if run as a script
    main()




