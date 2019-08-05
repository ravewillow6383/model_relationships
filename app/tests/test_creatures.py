import json
import pytest
from app import db

def test_get_no_creature(client):

    res = client.get("/creature")

    assert res.status_code == 200

    assert json.loads(res.data.decode()) == []

@pytest.mark.skip
def test_create_creature(client):

    res = client.post("/creature", data={"name": "Birds"})

    assert res.status_code == 200

def test_sample_creature(sample_creature):

    assert sample_creature.id == 1

    assert sample_creature.name == "Birds"

def test_get_creature_by_id(client, sample_creature):
    res = client.get(f"/creature/{sample_creature.id}")

    creature_dict = json.loads(res.data.decode())

    assert creature_dict["name"] == "Birds"

@pytest.mark.skip
def test_create_creature_and_check(client):

    client.post("/creature", data={"name": "Birds"})

    res = client.get("/creature")

    creature = json.loads(res.data.decode())

    assert len(creature) == 1

    assert creature[0]["name"] == "Birds"

def test_create_creature_and_fetch(client, sample_creature):

    res = client.get(f"/creature/{sample_creature.id}")

    assert res.status_code == 200

    creature_dict = json.loads(res.data.decode())

    assert creature_dict["name"] == "Birds"

def test_update_creature(client, sample_creature):

    res = client.put(f"/creature/{sample_creature.id}", data={"name": "The Reptiles"})

    assert res.status_code == 200

    assert json.loads(res.data.decode()) == sample_creature.id

    res = client.get(f"/creature/{sample_creature.id}")

    creature_dict = json.loads(res.data.decode())

    assert creature_dict["name"] == "The Reptiles"

def test_get_creature_with_winged_creature(client, sample_winged_creature):
    res = client.get(f"/creature/{sample_winged_creature.creature_id}")

    creature_dict = json.loads(res.data.decode())

    assert creature_dict["winged_creature"][0]["name"] == "Flightless cormorant"

def test_delete_creature(client, sample_creature):

    res = client.delete(f"/creature/{sample_creature.id}")

    assert res.status_code == 200


from app.models import Creature, Winged_Creature
