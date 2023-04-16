from mixed_methods import mixed_method

TYPE = 13
INSTANCE = 42


class Type:
    @classmethod
    def type_method(cls) -> int:
        return TYPE

    def instance_method(self) -> int:
        return INSTANCE

    method = mixed_method(type_method, instance_method)


def test_mixed_method() -> None:
    assert Type.method() == TYPE

    instance = Type()

    assert instance.method() == INSTANCE
