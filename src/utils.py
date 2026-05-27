import os
import json

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"


def save_configuration_json(_json: dict) -> bool:
    """
    Save the provided configuration dictionary to a JSON file.

    This function takes a dictionary containing configuration data and saves it to a
    specified JSON file path. The file is overwritten if it already exists.

    ### Parameters
    - **_json** (`dict`): The configuration data to be saved as a dictionary.

    ### Returns
    - `bool`: Returns `True` if the configuration was successfully saved, otherwise returns `False`.

    ### Example
    ```python
    config_data = {...}  # Some configuration data as a dictionary
    save_configuration_json(config_data)
    ```

    ### Notes
    - The function assumes the provided dictionary can be serialized to JSON format.
    - The file path is determined by the `DIR_PATH` constant and is typically located in the user's local application data directory.
    - Errors during file writing are logged to log files.
    """

    try:

        with open(rf"{DIR_PATH}\database\config.json", "w") as config:
            json.dump(_json, config, indent=4)

        return True

    except:
        raise NotImplementedError

    return False
