"""Main module."""
from gendiff.builder import make_diff
from gendiff.differ import generate_diff
from gendiff.formatters.stylish import plain_format
from gendiff.parse import parsing

__all__ = (
    "generate_diff",
    "parsing",
    "make_diff",
    "plain_format",
   
)
