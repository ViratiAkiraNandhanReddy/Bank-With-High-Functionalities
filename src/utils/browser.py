import os
from pathlib import Path


class browser:

    @staticmethod
    def open_url(url: str) -> bool:
        """
        ### Open a URL using the system's default browser.

        This method uses the native Windows shell URL association
        mechanism through `os.startfile()` to launch the provided
        URL in the user's configured *default* web browser.

        Compared to `webbrowser.open()`, this approach provides
        more reliable browser launching behavior on Windows systems,
        particularly when browsers are fully closed before invocation.

        ### Parameters

        - **url** (`str`)
            The target URL to open.

        ### Returns

        - `bool`
            - `True` if the browser launch request succeeds
            - `False` if validation fails or the URL cannot be opened

        ### Example

        ```python
        browser.open_url("https://github.com")
        ```

        ### Notes

        - Automatically prepends `https://` if no scheme is provided
        - Uses native Windows URL/file association handling
        - Avoids unsafe subprocess shell execution
        - Designed primarily for Windows environments
        """

        # Validate input type and reject empty/whitespace-only values.
        if not isinstance(url, str) or not url.strip():
            return False

        # Normalize leading/trailing whitespace.
        url = url.strip()

        if not url.startswith(("http://", "https://")):

            # Automatically prepend HTTPS scheme if missing.
            # This improves usability for inputs such as:
            # "github.com" instead of "https://github.com".

            url = f"https://{url}"

        try:

            # Use the native Windows shell association system
            # to launch the URL with the user's default browser.
            os.startfile(url)

            return True

        except OSError:

            # Use the native Windows shell association system
            # to launch the URL with the user's default browser.

            return False

    @staticmethod
    def open_internal_html_file(file_path: str) -> bool:
        """
        ### Open a local HTML file using the system's default browser.

        This method is restricted exclusively to `.html`
        and `.htm` files for security and behavioral consistency.

        The target file is opened using the native Windows
        shell association system through `os.startfile()`.

        ### Parameters

        - **file_path** (`str`)
            Absolute or relative path to the HTML file.

        ### Returns

        - `bool`
            - `True` if the file launch request succeeds
            - `False` if validation or launch fails

        ### Example

        ```python
        browser.open_internal_html_file(
            r"docs\\index.html"
        )
        ```

        ### Notes

        - Only `.html` and `.htm` files are allowed
        - Uses native Windows browser/file associations
        - Prevents unsupported file-type execution
        - Automatically normalizes file paths
        - Avoids unsafe subprocess shell execution
        - Designed primarily for Windows environments
        """

        if not isinstance(file_path, str) or not file_path.strip():

            # Validate the provided input type and reject
            # empty or whitespace-only values early before
            # performing any filesystem operations.

            return False

        # Normalize the path and resolve it into an absolute filesystem path.
        normalized_path: Path = Path(file_path.strip()).expanduser().resolve()

        if not normalized_path.exists():

            # Ensure the target file actually exists before
            # attempting to open it through the operating system.

            return False

        # Restrict execution strictly to supported HTML-based file extensions.
        if normalized_path.suffix.lower() not in (".html", ".htm"):

            return False

        try:

            # Open the HTML file using the system's
            # default browser association.
            os.startfile(str(normalized_path))

            return True

        except OSError:

            # Return False if Windows fails to launch
            # the associated browser/application.

            return False
