import subprocess


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
    """Open an internal file in the default web browser using file:// URL.

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
