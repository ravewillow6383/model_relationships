import json
import pytest

@pytest.mark.skip()
def test_get_no_creature(client):
    res = client.get('/creatures')
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == []

def test_sample_creature(sample_creature):
    assert sample_creature
    assert sample_creature.name == 'Birds'
    

# @pytest.mark.skip()
def test_sample_winged_creature_fixture(sample_winged_creature):
    assert sample_winged_creature.id == 1
    assert sample_winged_creature.name == 'Flightless cormorant'

@pytest.mark.skip()
def test_lone_winged_creature_fixture(lone_winged_creature):
    assert lone_winged_creature.id == 1
    assert lone_winged_creature.name == "Zburator"

@pytest.mark.skip
def test_create_creature_with_winged_creature(client, sample_creature):

    winged_creature_info = {"name": "Flightless cormorant", "creature": sample_creature.id}

    res = client.post("/winged_creature", data=winged_creature_info)

    assert res.status_code == 200

@pytest.mark.skip
def test_create_solo_winged_creature(client):

    winged_creature_info = {"name": "Zburator"}

    res = client.post("/winged_creature", data=winged_creature_info)

    assert res.status_code == 200

    res = client.get("/winged_creature")

    winged_creature = json.loads(res.data.decode())

    assert len(winged_creature) == 1

    assert winged_creature[0]['name'] == "Zburator"

    assert winged_creature[0].get('creature') is None

@pytest.mark.skip
def test_get_one_winged_creature(client, sample_creature):

    res = client.get(f"/winged_creature/{sample_creature.id}")

    creature_dict = json.loads(res.data.decode())

    assert creature_dict["name"] == "Flightless cormorant"