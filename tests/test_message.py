from OWNd.message import CLIMATE_MODE_COOL, CLIMATE_MODE_HEAT, OWNEvent, OWNHeatingCommand, OWNLightingEvent, OWNMessage


def test_lighting_event():
    msg = OWNEvent.parse("*1*0*77##")
    assert type(msg) is OWNLightingEvent
    assert msg.who == 1
    assert msg.where == "77"
    assert not msg.is_on

def test_heating_ac_unit_event():
    msg = OWNMessage.parse("*#4*3#76#8*22*2*0280*0*0##")
    assert msg._set_temperature == 28
    assert msg._where == '3'
    assert msg._where_param == ['76','8']
    assert msg._mode_name == CLIMATE_MODE_COOL
    assert msg._fan_speed == 0
