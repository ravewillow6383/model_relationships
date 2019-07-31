import json

def test_get_no_creature(client):
    res = client.get('/creatures')
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == []

def test_sample_winged_creature_fixture(sample_winged_creature):
    assert sample_winged_creature.id == 1
    assert sample_winged_creature.name == 'Flightless cormorant'