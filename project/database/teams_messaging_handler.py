from msal import ConfidentialClientApplication
from msal.authority import AuthorityBuilder, AZURE_PUBLIC

import requests

def get_graph_token():
    tenant_id = "e912b08a-72a2-427d-8461-061edb5feb58"
    application_id = "ee605c29-96a0-4df7-ba3a-882ac8fb3f0e"
    RESOURCE = ["https://graph.microsoft.com/.default"]

    secret = "BhN8Q~c4ayIxJmFlBPQ6rO_BN6BC-VWrymT4xcLr"

    azure_authority = AuthorityBuilder(AZURE_PUBLIC, tenant=tenant_id)
    context = ConfidentialClientApplication(application_id, client_credential=secret, authority=azure_authority,
                                            verify=False)

    token = context.acquire_token_for_client(RESOURCE)

    return token


def invoke_teams_api():
    token = get_graph_token()
    headers = {
        'Authorization': 'Bearer '+token['access_token'],
        'Content-Type': 'application/json'
    }

    resp = requests.get("https://graph.microsoft.com/v1.0/teams", headers=headers)
    print(resp)


invoke_teams_api()