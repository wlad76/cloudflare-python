# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .action import Action
from .matcher import Matcher
from ...._models import BaseModel

__all__ = ["EmailCatchAllRule"]


class EmailCatchAllRule(BaseModel):
    id: Optional[str] = None
    """Routing rule identifier."""

    actions: Optional[List[Action]] = None
    """List actions for the catch-all routing rule."""

    enabled: Optional[Literal[True, False]] = None
    """Routing rule status."""

    matchers: Optional[List[Matcher]] = None
    """List of matchers for the catch-all routing rule."""

    name: Optional[str] = None
    """Routing rule name."""

    tag: Optional[str] = None
    """Routing rule tag. (Deprecated, replaced by routing rule identifier)"""
