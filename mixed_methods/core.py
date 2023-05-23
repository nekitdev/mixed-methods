from typing import Callable, Generic, Optional, Type, TypeVar, Union, overload

from attrs import frozen
from typing_extensions import Concatenate, ParamSpec, final

__all__ = ("MixedMethod", "mixed_method")

T = TypeVar("T")

# P -> R

P = ParamSpec("P")
R = TypeVar("R")

# Q -> S

Q = ParamSpec("Q")
S = TypeVar("S")


@final
@frozen()
class MixedMethod(Generic[T, P, R, Q, S]):
    """Represents mixed methods."""

    type_method: Callable[Concatenate[Type[T], P], R]
    """The type method to use."""
    instance_method: Callable[Concatenate[T, Q], S]
    """The instance method to use."""

    @overload
    def __get__(self, instance: None, type: Type[T]) -> Callable[P, R]:
        ...

    @overload
    def __get__(self, instance: T, type: Optional[Type[T]] = None) -> Callable[Q, S]:
        ...

    def __get__(
        self, instance: Optional[T], type: Optional[Type[T]] = None
    ) -> Union[Callable[P, R], Callable[Q, S]]:
        if instance is None:
            return self.type_method.__get__(instance, type)  # type: ignore

        return self.instance_method.__get__(instance, type)  # type: ignore


def mixed_method(
    type_method: Callable[Concatenate[Type[T], P], R],
    instance_method: Callable[Concatenate[T, Q], S],
) -> MixedMethod[T, P, R, Q, S]:
    """Creates mixed methods.

    Arguments:
        type_method: The type method of the mixed method.
        instance_method: The instance method of the mixed method.

    Returns:
        The created mixed method.
    """
    return MixedMethod(type_method, instance_method)
