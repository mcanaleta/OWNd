from re import A
from OWNd.message import CLIMATE_MODE_COOL, CLIMATE_MODE_NAME_TO_NUM, CLIMATE_MODE_NUM_TO_NAME, CLIMATE_MODE_OFF, OWNEvent, OWNHeatingCommand, OWNLightingEvent, OWNMessage


def test_lighting_event():
    msg = OWNEvent.parse("*1*0*77##")
    assert type(msg) is OWNLightingEvent
    assert msg.who == 1
    assert msg.where == "77"
    assert not msg.is_on

def test_heating_ac_unit_set_event():
    msg = OWNMessage.parse("*#4*3#76#8*22*2*0280*0*0##")
    assert msg._set_temperature == 28
    assert msg._where == '3'
    assert msg._where_param == ['76','8']
    assert msg._mode_name == CLIMATE_MODE_COOL
    assert msg._fan_speed == 0

def test_heating_ac_unit_off_event():
    msg = OWNMessage.parse("*#4*3#77#8*22*0***##")
    assert msg._where == '3'
    assert msg._where_param == ['77','8']
    assert msg._mode_name == CLIMATE_MODE_OFF

def test_heating_ac_unit_set_command():
    msg = OWNHeatingCommand.set_ac_unit(7,5,8, CLIMATE_MODE_COOL, 23, 0)
    assert msg._raw == "*#4*3#75#8*#22*2*0230*0*15##"
    msg = OWNMessage.parse(msg._raw)
    assert type(msg) is OWNHeatingCommand

def test_heating_ac_off_command():
    msg = OWNHeatingCommand.set_ac_unit(7,7,8, CLIMATE_MODE_OFF)
    assert msg._raw == "*#4*3#77#8*#22*0**15*15##"
    msg = OWNMessage.parse(msg._raw)
    assert type(msg) is OWNHeatingCommand

def test_climate_mode():
    assert CLIMATE_MODE_NUM_TO_NAME["0"] == "off"
    assert CLIMATE_MODE_NAME_TO_NUM["off"]  == "0"