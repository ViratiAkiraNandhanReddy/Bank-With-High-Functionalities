import uuid


class _uuids:

    UUID_NAMESPACE_BWHF = uuid.UUID("71da99dc-ce4e-575e-a319-3083e9265046")
    # pre-generated using:
    # uuid.uuid5(
    #     uuid.NAMESPACE_URL,
    #     "https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/",
    # )

    @classmethod
    def generate_uuid5(cls, name: str) -> str:
        return str(uuid.uuid5(cls.UUID_NAMESPACE_BWHF, name))

    @classmethod
    def validate_uuid5(cls, uuid_to_validate: str) -> bool:
        try:
            uuid_obj = uuid.UUID(uuid_to_validate, version=5)
            return True
        except ValueError:
            return False
