import os


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
