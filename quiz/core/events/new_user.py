"""Simple implementation of observer design patter.

This is an alternative of avoid using Django signals since it is considered an
anti-pattern.
"""
import logging
from typing import Callable, Set

logger = logging.getLogger(__name__)

subscribers: Set[Callable] = set()


def subscribe(handler: Callable):
    """Subscribe to new user event."""
    logger.info('handler subscribes to new user event - {handler}',
                extra={'handler': handler.__name__})
    subscribers.add(handler)


def notify(state):
    """Notify state of a new user."""
    logger.info('notifying a new user')
    for handler in subscribers:
        handler(state)
