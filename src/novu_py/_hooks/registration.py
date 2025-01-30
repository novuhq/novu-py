from .novuhook import NovuHooks
from .types import Hooks


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


def init_hooks(hooks: Hooks):
    # pylint: disable=unused-argument
    my_hook = NovuHooks()
    hooks.register_before_request_hook(my_hook)
    hooks.register_after_success_hook(my_hook)
