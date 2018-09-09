#-*- coding:utf-8 -*-

def test_tx_superheros():
    from tx import get_json
    assert get_json.tx_get_superheroes()
