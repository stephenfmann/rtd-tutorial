"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

def mixing_bowls(n_bowls,n_hands=2,shake=False)->bool:
    """
    Do some mixing.

    Here's a new paragraph.

    Parameters
    ----------
    n_bowls : int
        Number of bowls.
    n_hands : int
        Number of hands to use for mixing the food in the bowls.
        The default is 2.
    shake : bool
        Whether to shake the bowls at the same time. The default is False.

    Returns
    -------
    bool
        True if successful, False otherwise.
    
    """

    if n_bowls>0 and n_hands>0 and shake==False: return True

    return False
