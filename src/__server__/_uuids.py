import uuid


class _uuids:

    @classmethod
    def generate(cls) -> str:

        return str(uuid.uuid4())

    @classmethod
    def validate(cls, value: str) -> bool:

        try:

            uuid_obj = uuid.UUID(value)

            return uuid_obj.version == 4

        except ValueError:

            return False
