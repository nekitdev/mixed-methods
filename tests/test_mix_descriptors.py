from mix_descriptors import mix_descriptors

TYPE = 13
INSTANCE = 42


class Type:
    @classmethod
    def type_method(cls) -> int:
        return TYPE

    def instance_method(self) -> int:
        return INSTANCE

    method = mix_descriptors(type_method, instance_method)


def test_mixed_method() -> None:
    assert Type.method() == TYPE

    instance = Type()

    assert instance.method() == INSTANCE
