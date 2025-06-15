from typing import Optional
import requests

from exceptions import AuthenticationError, NetworkError, ResourceNotFoundError

BASE_URL = "https://dsp2-technical-test.iliad78.net/"


def stancer_get_data(url: str, token: str) -> dict:
    try:
        response = requests.get(
            url=BASE_URL + url,
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )
        if response.status_code == 401:
            raise AuthenticationError("Token expiré ou invalide")
        elif response.status_code == 404:
            raise ResourceNotFoundError(f"Ressource {url} introuvable.")
        if response.status_code != 200:
            raise Exception(response.json()["detail"])
        return response.json()
    except requests.exceptions.Timeout:
        raise NetworkError("Token request timed out.")
    except Exception as err:
        raise err

def stancer_get_token(
    username: str,
    password: str,
    grant_type: Optional[str] = None,
    scope: Optional[str] = None,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
) -> str:
    try:
        response = requests.post(
            BASE_URL + "oauth/token",
            data={
                "grant_type": grant_type,
                "username": username,
                "password": password,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
            },
            timeout=2,
        )
        if response.status_code == 401:
            raise AuthenticationError(f"Identifiants invalides.")
        elif response.status_code != 200:
            raise Exception(response.json()["detail"])
        return response.json()["access_token"]
    except requests.exceptions.Timeout:
        raise NetworkError("Token request timed out.")
    except Exception as err:
        raise err