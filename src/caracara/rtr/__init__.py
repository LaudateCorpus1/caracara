"""RTR Toolbox."""
from ._api import FalconAPI
from ._single_target import SingleTarget
from ._scripts import Scripts
from ._files import Files
from .._toolbox import Toolbox


class RTRToolbox(Toolbox):
    """RTR Toolbox."""

    def __init__(self: object, verbose: bool = True, **kwargs):
        """Open the toolbox."""
        super().__init__(api=FalconAPI(**kwargs), verbose=verbose)

        self.scripts = Scripts(api=self.api)
        self.single_target = SingleTarget(api=self.api)
        self.files = Files(api=self.api)


__all__ = ["RTRToolbox"]
