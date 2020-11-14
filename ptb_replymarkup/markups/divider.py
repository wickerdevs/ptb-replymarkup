from ptb_replymarkup.markups import *
from ptb_replymarkup.markups.base import BaseMarkup

class MarkupDivider(BaseMarkup):
    """An InlineMarkupButton with no attached callback used to divide sections of the ForwarderMarkup"""
    def __init__(self, title):
        super().__init__(self, {Callbacks.NONE: title}, cols=1)