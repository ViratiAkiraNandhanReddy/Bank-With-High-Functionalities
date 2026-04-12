import os
import json
import subprocess

DIR_PATH: str = str(os.environ.get("LOCALAPPDATA")) + r"\Bank-With-High-Functionalities"


def Open_Browser_For_Specified_URL(url: str) -> None:
    """
    Opens the given URL using the system's default browser via Windows shell command.
    Windows-only functionality.

    ### Parameters
    - **url** (`str`): The URL to be opened in the browser.

    ### Returns
    - `None`

    ### Example
    ```python
    Open_Browser_For_Specified_URL("https://www.example.com")
    ```

    ### Notes
    - Requires Windows operating system
    - Ensure system has a default browser configured
    - Uses `subprocess.run()` to execute shell command
    - Errors are logged to log files
    """

    try:
        subprocess.run(f"START {url}", shell=True)

    except:
        raise NotImplementedError


def Open_Browser_For_Specified_Internal_File(file_dir: str) -> None:
    """
    Open an internal file in the default web browser using file:// URL.

    Converts the provided file path to a `file:///` URL and opens it in the system's
    default browser. Windows-only functionality.

    ### Parameters
    - **file_dir** (`str`): The absolute or relative path of the internal file to open.

    ### Returns
    - `None`

    ### Example
    ```python
    Open_Browser_For_Specified_Internal_File("C:/<...>/Bank-With-High-Functionalities/LICENSE")
    ```

    ### Notes
    - Requires Windows operating system
    - File path is internally converted to valid `file:///` URL format
    - Backslashes are automatically converted to forward slashes
    - Uses `subprocess.run()` to execute command via Windows shell
    - Default browser must be configured on the system
    - Errors are logged to log files
    """

    try:
        subprocess.run(
            ["cmd", "/c", "START", "", f'file:///{file_dir.replace("\\\\", "/")}'],
            shell=True,
        )

    except:
        raise NotImplementedError


def get_hvr_accent_color(accent_color: str, depth: float = 0.8) -> str:
    """
    Calculate a hover accent color by darkening the original accent color.

    This function takes an RGB hex color code and returns a darker version of it
    suitable for hover effects in UI design. The depth parameter controls how much
    darker the hover color will be compared to the original.

    ### Parameters
    - **accent_color** (`str`): The original accent color in RGB hex format (e.g., "#RRGGBB").
    - **depth** (`float`, optional): A value between 0 and 1 that determines how much darker the hover color will be. Default is 0.8.

    ### Returns
    - `str`: The calculated hover accent color in RGB hex format.

    ### Example
    ```python
    original_color = "#21968B"
    hover_color = get_hvr_accent_color(original_color, depth=0.8)
    print(hover_color)  # Output will be a darker shade of #21968B
    ```

    ### Notes
    - The function assumes the input color is a valid RGB hex code.
    - The depth parameter should be between 0 and 1; values closer to 0 will produce a much darker color, while values closer to 1 will produce a slightly darker color.
    - Errors are logged to log files if the input color format is invalid.
    """

    try:
        r = int(accent_color[1:3], 16)
        g = int(accent_color[3:5], 16)
        b = int(accent_color[5:7], 16)

        r = max(0, min(255, int(r * depth)))
        g = max(0, min(255, int(g * depth)))
        b = max(0, min(255, int(b * depth)))

        return f"#{r:02X}{g:02X}{b:02X}"

    except:
        raise NotImplementedError


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
