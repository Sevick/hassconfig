mod = hass.states.get("input_text.log_level_integration").state
is_on = hass.states.get("input_boolean.log_level_integration").state == "on"
level = "debug" if is_on else "info"
hass.services.call(
    "logger",
    "set_level",
    {mod: level}
)