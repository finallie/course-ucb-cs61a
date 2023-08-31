def prune_min(t):
    """Prune the tree mutatively.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    if t.is_leaf():
        return
    prune_min(t.branches[0])
    prune_min(t.branches[1])
    if t.branches[0].label < t.branches[1].label:
        t.branches.pop(1)
    else:
        t.branches.pop(0)


def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth)
    level have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    import functools
    import operator

    def helper(depth, t):
        if depth % 2 == 0:
            i, j = 0, len(t.branches) - 1
            while i < j:
                t.branches[i].label, t.branches[j].label = (
                    t.branches[j].label,
                    t.branches[i].label,
                )
                i += 1
                j -= 1
        for b in t.branches:
            helper(depth + 1, b)

    helper(0, t)


def link_pop(lnk, index=-1):
    """Implement the pop method for a Linked List.

    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> removed = link_pop(lnk)
    >>> print(removed)
    5
    >>> print(lnk)
    <1 2 3 4>
    >>> link_pop(lnk, 2)
    3
    >>> print(lnk)
    <1 2 4>
    >>> link_pop(lnk)
    4
    >>> link_pop(lnk)
    2
    >>> print(lnk)
    <1>
    """
    if index == -1:
        while lnk.rest is not Link.empty:
            pre, lnk = lnk, lnk.rest
        removed = lnk.first
        pre.rest = lnk.rest
    else:
        while index != 1:
            lnk = lnk.rest
            index -= 1
        removed = lnk.rest.first
        lnk.rest = lnk.rest.rest
    return removed


def crispr_gene_insertion(lnk_of_genes, insert):
    """Takes a linked list of genes and returns the genes with the INSERT codon added the correct number of times.

    >>> link = Link(Link("AUG", Link("GCC", Link("ACG"))), Link(Link("ATG", Link("AUG", Link("ACG", Link("GCC"))))))
    >>> print(link)
    <<AUG GCC ACG> <ATG AUG ACG GCC>>
    >>> crispr_gene_insertion(link, "TTA")
    >>> print(link)
    <<AUG TTA GCC ACG> <ATG AUG TTA TTA ACG GCC>>
    >>> link = Link(Link("ATG"), Link(Link("AUG", Link("AUG")), Link(Link("AUG", Link("GCC")))))
    >>> print(link)
    <<ATG> <AUG AUG> <AUG GCC>>
    >>> crispr_gene_insertion(link, "TTA") # first gene has no AUG so unchanged, 2nd gene has 2 AUGs but only first considered for insertion
    >>> print(link)
    <<ATG> <AUG TTA TTA AUG> <AUG TTA TTA TTA GCC>>
    >>> link = Link.empty # empty linked list of genes returns Link.empty
    >>> crispr_gene_insertion(link, "TTA")
    >>> print(link)
    ()
    """
    "*** YOUR CODE HERE ***"

    def insert(n):
        nonlocal lnk_of_genes
        if lnk_of_genes is Link.empty:
            return
        gene = lnk_of_genes.first
        while gene is not Link.empty:
            if gene.first == "AUG":
                for _ in range(n):
                    gene.rest = Link("TTA", gene.rest)
                break
            gene = gene.rest
        lnk_of_genes = lnk_of_genes.rest
        insert(n + 1)

    insert(1)


def transcribe(dna):
    """Takes a string of DNA and returns a Python list with the RNA codons.

    >>> DNA = "TACCTAGCCCATAAA"
    >>> transcribe(DNA)
    ['AUG', 'GAU', 'CGG', 'GUA', 'UUU']
    """
    dict = {"A": "U", "T": "A", "G": "C", "C": "G"}
    return [
        dict[dna[i]] + dict[dna[i + 1]] + dict[dna[i + 2]]
        for i in range(0, len(dna), 3)
    ]


def partition_gen(n):
    """
    >>> partitions = [sorted(p) for p in partition_gen(4)]
    >>> for partition in sorted(partitions): # note: order doesn't matter
    ...     print(partition)
    [1, 1, 1, 1]
    [1, 1, 2]
    [1, 3]
    [2, 2]
    [4]
    """

    def yield_helper(num, segment):
        if num == 0:
            yield []
        elif num > 0 and segment > 0:
            for small_part in yield_helper(num - segment, segment):
                yield small_part + [segment]
            yield from yield_helper(num, segment - 1)

    yield from yield_helper(n, n)


def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]

    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand

    return random


random = make_test_random()

# Phase 1: The Player Class


class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135
    >>> p1.speech(p2)
    >>> p1.votes
    13
    >>> p1.popularity
    148
    >>> p2.votes
    10
    >>> p2.popularity
    99
    >>> for _ in range(4):  # 0.1, 0.2, 0.3, 0.4
    ...     p1.debate(p2)
    >>> p2.debate(p1)
    >>> p2.popularity
    49
    >>> p2.debate(p1)
    >>> p2.popularity
    0
    """

    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        "*** YOUR CODE HERE ***"
        probability = max(0.1, self.popularity / (self.popularity + other.popularity))
        if random() < probability:
            self.popularity += 50
        else:
            self.popularity = max(0, self.popularity - 50)

    def speech(self, other):
        "*** YOUR CODE HERE ***"
        self.votes += self.popularity // 10
        self.popularity += self.popularity // 10
        other.popularity -= other.popularity // 10

    def choose(self, other):
        return self.speech


# Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> winner is g.winner()
    True
    >>> g.turn
    10
    >>> p1.votes = p2.votes
    >>> print(g.winner())
    None
    """

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over():
            if self.turn % 2 == 0:
                self.p1.choose(self.p2)(self.p2)
            else:
                self.p2.choose(self.p1)(self.p1)
            self.turn += 1
        return self.winner()

    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    def winner(self):
        "*** YOUR CODE HERE ***"
        return (
            self.p1
            if self.p1.votes > self.p2.votes
            else (self.p2 if self.p2.votes > self.p1.votes else None)
        )


# Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> p1.popularity = p2.popularity
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity += 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> p2.choose(p1) == p2.speech
    True
    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity <= other.popularity:
            return self.debate
        else:
            return self.speech


class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> # Additional correctness tests
    >>> p2.choose(p1) == p2.speech
    True
    """

    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity == 0:
            return self.debate
        else:
            return self.speech


def deck(suits, ranks):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and ranks. Each element in the returned list should be of the form
    [suit, rank].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    return [[suit, rank] for suit in suits for rank in ranks]


def intersection(lst_of_lsts):
    """Returns a list of distinct elements that appear in every list in
    lst_of_lsts.

    >>> lsts1 = [[1, 2, 3], [1, 3, 5]]
    >>> intersection(lsts1)
    [1, 3]
    >>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
    >>> intersection(lsts2)
    [4]
    >>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    >>> intersection(lsts3)         # No number appears in all lists
    []
    >>> lsts4 = [[3, 3], [1, 2, 3, 3], [3, 4, 3, 5]]
    >>> intersection(lsts4)         # Return list of distinct elements
    [3]
    """
    # elements = []
    "*** YOUR CODE HERE ***"
    s = set(lst_of_lsts[0])
    for lst in lst_of_lsts[1:]:
        s = {x for x in lst if x in s}
    return sorted(list(s))


import re


def party_planner(text):
    """
    Returns all strings representing valid phone numbers with 314, 510, 310, or 514 area codes.
    The area code may or may not be surrounded by parentheses. Valid phone numbers
    have 10 digits and follow this format: XXX-XXX-XXXX, where each X represents a digit.

    >>> party_planner("(408)-996-3325, (510)-658-7400, (314)-3333-22222")
    True
    >>> party_planner("314-826-0705, (510)-314-3143, 408-267-7765")
    True
    >>> party_planner("5103143143")
    False
    >>> party_planner("514-300-2002, 310-265-4242") # invite your friends in LA and Montreal
    True
    """
    return bool(
        re.search(
            r"(^|\s)((314|510|310|514)|(\((314|510|310|514)\)))-\d{3}-\d{4}[,\s$]", text
        )
    )


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return "Tree({0}{1})".format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = "  " * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


#
# Brackulator
#

# A dictionary from pairs of matching brackets to the operators they indicate.
brackets = {("[", "]"): "+", ("(", ")"): "-", ("<", ">"): "*", ("{", "}"): "/"}

# A dictionary with left-bracket keys and corresponding right-bracket values.
left_to_right = {left: right for left, right in brackets}
left_to_operator = {left[0]: operator for left, operator in brackets.items()}

# The set of all left and right brackets.
all_brackets = set(left_to_right.keys()).union(set(left_to_right.values()))


def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('2.3')
    [2.3]
    >>> tokenize('(2 3)')
    ['(', 2, 3, ')']
    >>> tokenize('<2 3)')
    ['<', 2, 3, ')']
    >>> tokenize('<[2{12.5 6.0}](3 -4 5)>')
    ['<', '[', 2, '{', 12.5, 6.0, '}', ']', '(', 3, -4, 5, ')', '>']

    >>> tokenize('2.3.4')
    Traceback (most recent call last):
        ...
    ValueError: invalid token 2.3.4

    >>> tokenize('?')
    Traceback (most recent call last):
        ...
    ValueError: invalid token ?

    >>> tokenize('hello')
    Traceback (most recent call last):
        ...
    ValueError: invalid token hello

    >>> tokenize('<(GO BEARS)>')
    Traceback (most recent call last):
        ...
    ValueError: invalid token GO
    """
    # Surround all brackets by spaces so that they are separated by split.
    for b in all_brackets:
        line = line.replace(b, " " + b + " ")

    # Convert numerals to numbers and raise ValueErrors for invalid tokens.
    tokens = []
    for t in line.split():
        if t in all_brackets:
            tokens.append(t)
        elif coerce_to_number(t) is not None:
            tokens.append(coerce_to_number(t))
        else:
            raise ValueError("invalid token " + t)
    return tokens


def coerce_to_number(token):
    """Coerce a string to a number or return None.

    >>> coerce_to_number('-2.3')
    -2.3
    >>> print(coerce_to_number('('))
    None
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return None


def brack_read(tokens):
    """Return an expression tree for the Brackulator
    expression in tokens. Tokens in that expression are removed from tokens as
    a side effect.

    >>> brack_read(tokenize('100'))
    100
    >>> brack_read(tokenize('([])'))
    Pair('-', Pair(Pair('+', nil), nil))
    >>> print(brack_read(tokenize('<[2{12 6}](3 4 5)>')))
    (* (+ 2 (/ 12 6)) (- 3 4 5))
    >>> brack_read(tokenize('(1)(1)')) # More than one expression is ok
    Pair('-', Pair(1, nil))
    >>> brack_read(tokenize('[])')) # Junk after a valid expression is ok
    Pair('+', nil)

    >>> brack_read(tokenize('([]')) # Missing right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line

    >>> brack_read(tokenize('[)]')) # Extra right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('([)]')) # Improper nesting
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('')) # No expression
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line
    """
    if not tokens:
        raise SyntaxError("unexpected end of line")
    token = tokens.pop(0)
    if token not in all_brackets:
        return token
    elif token in left_to_right:
        "*** YOUR CODE HERE ***"
        return Pair(left_to_operator[token], read_until(tokens, left_to_right[token]))
    else:
        raise SyntaxError("unexpected " + token)


def read_until(tokens, end):
    if not tokens:
        raise SyntaxError("unexpected end of line")
    if tokens[0] != end:
        return Pair(brack_read(tokens), read_until(tokens, end))
    else:
        tokens.pop(0)
        return nil


###################################
# Support classes for Brackulator #
###################################


class Pair:
    """A pair has two instance attributes: first and second. Second must be a Pair or nil

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """

    def __init__(self, first, second):
        assert isinstance(second, Pair) or second is nil
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        assert second is nil
        return s + ")"

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            y = y.second
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        return Pair(mapped, self.second.map(fn))


class nil:
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self


nil = nil()  # Assignment hides the nil class; there is only one instance


def read_eval_print_loop():
    """Run a read-eval-print loop for the Brackulator language."""
    global Pair, nil
    from scheme_reader import Pair, nil
    from scalc import calc_eval

    while True:
        try:
            src = tokenize(input("brack> "))
            while len(src) > 0:
                expression = brack_read(src)
                print(calc_eval(expression))
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ":", err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return
