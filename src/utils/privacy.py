class masking:

    @staticmethod
    def mask_email(
        email_address: str,
        max_length: int = 32,
        mask_char: str = "*",
    ) -> str:

        if "@" not in email_address:

            # Validate basic email structure before processing.
            # Prevents invalid split operations and malformed input handling.

            return "invalid-email"

        # Split only once to safely preserve domains containing additional '@'
        # characters in malformed or edge-case inputs.
        username, domain = email_address.strip().split("@", 1)

        if not username or not domain:

            # Ensure both username and domain sections exist.
            # Prevents incomplete email structures such as '@gmail.com'
            # or 'admin@'.

            return "invalid-email"

        # Normalize whitespace to avoid inconsistent masking behavior.
        username = username.strip()
        domain = domain.strip()

        # Handle very short usernames separately to avoid
        # overexposing identity details.
        if len(username) <= 2:

            # Preserve only the first visible character while masking
            # remaining characters consistently.

            masked_username: str = username[0] + (mask_char * max(len(username) - 1, 0))

        else:

            # Preserve the first and last username characters
            # while masking all middle characters for recognizable
            # but privacy-safe identity confirmation.

            masked_username = (
                username[0] + (mask_char * (len(username) - 2)) + username[-1]
            )

        # Reconstruct masked email address.
        masked_email: str = f"{masked_username}@{domain}"

        if len(masked_email) > max_length:

            # Enforce a fixed maximum display length for UI consistency.
            # Prevents layout overflow and abrupt geometry shifts in
            # authentication/recovery interfaces.

            # Calculate how many characters exceed the allowed limit.
            overflow: int = len(masked_email) - max_length

            # Ensure domain truncation remains safe and visually meaningful.
            if overflow < len(domain) - 3:

                # Truncate the beginning portion of the domain and prepend
                # ellipsis to preserve recognizable trailing identity.
                domain = "..." + domain[overflow + 3 :]

            # Rebuild the final masked email after domain truncation.
            masked_email = f"{masked_username}@{domain}"

        # Return the securely masked and UI-safe email address.
        return masked_email
