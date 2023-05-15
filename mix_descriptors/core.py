from abc import abstractmethod as required
from typing import Callable, Concatenate, Generic, Optional, Type, TypeVar, Union, final, overload

from attrs import frozen

__all__ = ("MixDescriptors", "mix_descriptors")

T = TypeVar("T")

P = TypeVar("P", covariant=True)
Q = TypeVar("Q", covariant=True)
R = TypeVar("R", covariant=True)
S = TypeVar("S", covariant=True)

MUST_IMPLEMENT = "types derived from `{}` must implement `{}`"
GET = "__get__"


class Descriptor(Protocol[T, P, Q]):
    @overload
    def __get__(self, instance: None, type: Type[T]) -> P:
        ...

    @overload
    def __get__(self, instance: T, type: Optional[Type[T]] = None) -> Q:
        ...

    @required
    def __get__(self, instance: Optional[T], type: Optional[Type[T]] = None) -> Union[P, Q]:
        ...


@final
@frozen()
class MixDescriptors(Descriptor[T, P, R], Generic[T, P, Q, R, S]):
    """Represents types that mix descriptors."""

    type_descriptor: Descriptor[T, P, Q].
    """The descriptor to use for types."""
    instance_descriptor: Descriptor[T, R, S]
    """The descriptor to use for instances."""

    @overload
    def __get__(self, instance: None, type: Type[T]) -> P:
        ...

    @overload
    def __get__(self, instance: T, type: Optional[Type[T]] = None) -> R:
        ...

    def __get__(
        self, instance: Optional[T], type: Optional[Type[T]] = None
    ) -> Union[P, R]:
        if instance is None:
            return self.type_method.__get__(instance, type)

        return self.instance_method.__get__(instance, type)


def mix_descriptors(
    type_descriptor: Descriptor[T, P, Q]
    instance_descriptor: Descriptor[T, R, S],
) -> MixDescriptors[T, P, Q, R, S]:
    """Mixes descriptors.

    Arguments:
        type_descriptor: The descriptor to use for types.
        instance_descriptor: The descriptor to use for instances.

    Returns:
        The created [`MixDescriptors[T, P, Q, R, S]`][mix_descriptors.core.MixDescriptors] instance.
    """
    return MixDescriptors(type_descriptor, instance_descriptor)
