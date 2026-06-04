import socket


class connection:

    @staticmethod
    def is_connected() -> bool:

        try:

            # Attempt to establish a temporary socket connection
            # to Cloudflare's public DNS server. If the connection
            # succeeds within the timeout period, internet access
            # is considered available.

            with socket.create_connection(
                address=("1.1.1.1", 53),  # Cloudflare DNS
                timeout=3,  # 3 seconds timeout
            ):

                # The connection was created successfully.
                # Returning True confirms network connectivity.

                return True

        except (OSError, socket.timeout):

            # Connection could not be established successfully.
            # This usually indicates no active internet access.

            return False
