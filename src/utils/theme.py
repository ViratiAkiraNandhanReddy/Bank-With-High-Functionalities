class colors:

    @staticmethod
    def get_hover_accent_color(
        accent_color: str,
        depth: float = 0.80,
    ) -> str:
        """
        ### Generate a darker hover-state variation of a HEX accent color.

        This method is primarily intended for UI hover effects,
        button interactions, and interactive accent styling.

        The provided HEX color is darkened by multiplying each
        RGB channel by the specified depth value.

        ### Parameters

        - **accent_color** (`str`)
            Base HEX color in `#RRGGBB` format.

        - **depth** (`float`, optional)
            Darkening multiplier between `0.0` and `1.0`.

            - Lower values produce darker colors
            - Higher values preserve more of the original color

            > Defaults to `0.80`.

        ### Returns

        - `str`
            Darkened HEX color in `#RRGGBB` format.

        ### Example

        ```python
        hover_color = colors.get_hover_accent_color(
            "#21968B",
            depth=0.80,
        )
        ```

        ### Notes

        - Only supports full 6-character HEX colors
        - Output is automatically normalized to uppercase
        - Values are internally clamped for RGB safety
        - Invalid inputs raise `ValueError`
        """

        if not isinstance(accent_color, str):

            # Ensure the provided accent color is a string
            # before performing HEX processing operations.

            raise ValueError("Accent color must be a string.")

        # Normalize whitespace and casing.
        accent_color = accent_color.strip().upper()

        if len(accent_color) != 7 or not accent_color.startswith("#"):

            # Validate standard HEX color structure.
            # Supported format:
            # - "#RRGGBB"

            raise ValueError("Accent color must be in '#RRGGBB' format.")

        # Clamp depth value to safe RGB multiplier range.
        depth = max(0.0, min(1.0, depth))

        try:

            # Extract RED channel from HEX string.
            r: int = int(accent_color[1:3], 16)

            # Extract GREEN channel from HEX string.
            g: int = int(accent_color[3:5], 16)

            # Extract BLUE channel from HEX string.
            b: int = int(accent_color[5:7], 16)

        except ValueError:

            # Raised when invalid HEX characters exist,
            # such as non-hexadecimal symbols.

            raise ValueError("Accent color contains invalid HEX values.")

        # Apply hover darkening multiplier to RED channel
        # while preserving valid RGB bounds.
        r = max(0, min(255, int(r * depth)))

        # Apply hover darkening multiplier to GREEN channel
        # while preserving valid RGB bounds.
        g = max(0, min(255, int(g * depth)))

        # Apply hover darkening multiplier to BLUE channel
        # while preserving valid RGB bounds.
        b = max(0, min(255, int(b * depth)))

        # Rebuild and return the normalized hover HEX color.
        return f"#{r:02X}{g:02X}{b:02X}"
