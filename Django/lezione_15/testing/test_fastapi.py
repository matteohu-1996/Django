import pytest
from fastapi.testclient import TestClient
from main import app

# 1 facciamo le fixture di setup
def client():
    with TestClient(app) as test_client:
        yield test_client

#    print("siamo dopo lo Yield")
    # posto dove metteremo "Teardown" = Chiusura di file, sessioni,
    # connessioni ecc

# def client_r():
#    with TestClient(app) as test_client:
#       return test_client
#    print("siamo dopo il return")


# Funzione di test dell'api
def test_read_main(client):
    response = client.get("/") # otteniamo il percorso root dell'api
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}
