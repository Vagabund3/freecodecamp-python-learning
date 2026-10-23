def add_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()
    if key in settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


test_settings = {"bright": "low", "volume": "high"}


def update_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
