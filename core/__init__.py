'''
The core package for IgKnite.
---

License can be found here:
https://github.com/IgKniteDev/IgKnite/blob/main/LICENSE
'''


# Initialize scripts.
from dataclasses import dataclass
from datetime import datetime

from . import chain as chain
from . import datacls as datacls
from .bot import *
from .ui import *

# Set version number.
__version_info__ = ('2023', '4', '24')  # Year.Month.Day
__version__ = '.'.join(__version_info__)


# Set bot metadata.
@dataclass(frozen=True)
class BotMeta:
    '''
    A dataclass used for storing bot metadata.
    '''

    repo: str = 'https://github.com/IgKniteDev/IgKnite'
    documentation: str = 'https://igknitedev.github.io/docs'
    version: str = __version__


# Track uptime.
running_since = round(datetime.timestamp(datetime.now()))
