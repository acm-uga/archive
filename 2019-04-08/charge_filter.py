'''A program for checking charges against a ruleset.

See the CSIP website for details of the problem:
http://csip.uga.edu/problems/2019-04-08/README

There are two parsing problems in this program: parsing the charge and parsing
the ruleset. Below, we describe the two languages in `Augmented Backus–Naur
form (ABNF) <https://en.wikipedia.org/wiki/Augmented_Backus-Naur_form>`_ .

The charge language is simple::

    charge     =  "CHARGE:" key-value "&" key-value "&" key-value "&" key-value
    key-value  =  key "=" value
    key        =  "amount" / "card_country" / "currency" / "ip_country"
    value      =  1*(ALPHA / DIGIT / "_")

Essentially, the charge starts with the prefix "CHARGE:" followed by four
key-value pairs separated by ampersands. Each key-value pair is written with an
equals sign as the separator. There are four possible keys, and every charge
will contain each key exactly once. The values are strings of alphanumeric
characters or the underscore. The amount value is interpreted as an integer and
the rest are interpreted as strings.

The charges are simple enough to parse. We can strip off the prefix, split on
the ampersand to get key-value strings, then split each key-value string on the
equals to get key-value pairs. The key-value pairs can then be passed to the
dictionary constructor. This logic is implemented on the `Charge` class.

The rule language is more complicated. The instructions provide a few
limitations that we could rely on, like there only being one "AND" or "OR", but
it's actually easier to write out a grammar for the language that is general
enough to handle more complex compounds. The grammar looks like this::

    rule          =  ("ALLOW:" / "BLOCK:") or-expr
    or-expr       =  and-expr *("OR" and-expr)
    and-expr      =  compare-expr *("AND" compare-expr)
    compare-expr  =  key ("==" / "!=" / "<" / "<=" / ">" / ">=") value
    key           =  "amount" / "card_country" / "currency" / "ip_country"
    value         =  1*(ALPHA / DIGIT / "_")

Essentially, a rule starts with a prefix of either "ALLOW:" or "BLOCK:" followed
by an OR-expression. An OR-expression is one or more AND-expressions separated
by "OR". An AND-expression is one or more comparison-expressions separated by
"AND". And a comparison-expression is a key-value pair separated by a comparison
operator. The keys and values are defined just as they are in the charge
language.

We implement this language with a simple recursive-descent parser. We have
classes for rules, OR-expressions, AND-expressions, and comparison-expressions.
Each of these has a ``parse`` method to construct an instance of the class from
a string. The parse method for rules calls the parse method for OR-expressions,
which in turn calls the parse method for AND-expressions, and finally that calls
the parse method for comparison-expressions. This recursive-ish nature is where
we get the term recursive-descent parser. Instances of these classes form a tree
that mirrors the structure of the grammar. This is called an abstract syntax
tree.

Each of these classes also have a ``match`` method which checks if an
expression applies to a charge. Just like the ``parse`` methods, the ``match``
method at each layer of the tree calls into the ``match`` method of the lower
level of the tree. This technique is called an abstract syntax tree interpreter.

To combine multiple rules, we have a top-level class for rulesets. The ruleset
class also has a ``parse`` method, but it takes in a list of strings, one for
each rule. Instead of a ``match`` method, the rulset has a ``check_charge``
method which returns true if the charge should be allowed and false if it should
be blocked.
'''

class RuleSet:
    def __init__(self, rules):
        '''Construct a new ruleset.

        Arguments:
            rules (Rule):
                The list of top-level rules defining the ruleset.
        '''
        for rule in rules:
            assert isinstance(rule, Rule)

        self.allow = []
        self.block = []
        for rule in rules:
            if rule.type == 'allow':
                self.allow.append(rule)
            else:
                self.block.append(rule)

    def check_charge(self, charge):
        '''Returns True if the charge should be allowed.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        for rule in self.allow:
            if rule.match(charge):
                return True

        for rule in self.block:
            if rule.match(charge):
                return False

        return True

    @classmethod
    def parse(cls, sources):
        '''Parse a ruleset from a list of top-level rules.

        Arguments:
            source (Sequence[str]):
                A list of top-level rules to parse.

        Returns:
            RuleSet:
                The parsed ruleset.
        '''
        rules = [Rule.parse(source) for source in sources]
        return cls(rules)


class Rule:
    def __init__(self, type, body):
        '''Construct a new rule.

        This rule simply delegates to an underlying OR-expression, but contains
        an additional `type` property used by rulesets.

        Arguments:
            type (str):
                Either ``"allow"`` or ``"block"``.
            body (OrExpr):
                An ``OrExpr`` for matching charges.
        '''
        assert type == "allow" or type == "block"
        assert isinstance(body, OrExpr)
        self.type = type
        self.body = body

    def match(self, charge):
        '''Match a charge against this rule.

        This returns True if the body expression matches the charge.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        return self.body.match(charge)

    @classmethod
    def parse(cls, source):
        '''Parse a rule.

        The source must start with either "ALLOW:" or "BLOCK:" and the
        rest of the source is parsed as an OR-expression.

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            Rule:
                The parsed rule.
        '''
        source = source.strip()

        if source.startswith('ALLOW:'):
            type = 'allow'

        else:
            assert source.startswith('BLOCK:')
            type = 'block'

        body = OrExpr.parse(source[6:])
        return cls(type, body)


class OrExpr:
    def __init__(self, exprs):
        '''Construct a new OR-expression.

        This expression matches a charge if any sub-expression matches the
        charge.

        Arguments:
            exprs (Sequence[AndExpr]):
                A list of AND-expressions, one of which must match a charge for
                this expression to match a charge.
        '''
        for expr in exprs:
            assert isinstance(expr, AndExpr)

        self.exprs = tuple(exprs)

    def match(self, charge):
        '''Match a charge against this expr.

        This returns True if any of the sub-expressions match the charge.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        for expr in self.exprs:
            if expr.match(charge):
                return True
        return False

    @classmethod
    def parse(cls, source):
        '''Parse an OR-expression.

        The source is parsed as zero or more AND-expressions separated by "OR".

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            OrExpr:
                The parsed expression.
        '''
        exprs = [AndExpr.parse(r) for r in source.split('OR')]
        return cls(exprs)


class AndExpr:
    def __init__(self, exprs):
        '''Construct a new AND-expression.

        This expression matches a charge if all sub-expressions match the
        charge.

        Arguments:
            exprs (Sequence[CompareExpr]):
                A list of comparison-expressions, all of which must match a
                charge for this expression to match a charge.
        '''
        for expr in exprs:
            assert isinstance(expr, CompareExpr)

        self.exprs = tuple(exprs)

    def match(self, charge):
        '''Match a charge against this expression.

        This returns True if all of the sub-expressions match the charge.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        for expr in self.exprs:
            if not expr.match(charge):
                return False
        return True

    @classmethod
    def parse(cls, source):
        '''Parse an AND-expression.

        The source is parsed as zero or more comparison-expressions separated
        by "AND".

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            AndExpr:
                The parsed expression.
        '''
        exprs = [CompareExpr.parse(r) for r in source.split('AND')]
        return cls(exprs)


class CompareExpr:
    def __init__(self, property, value, relationship):
        '''Construct a new comparison-expression.

        This expression matches a charge if the charge the value of that
        property in the charge has the corresponding relationship to the
        value of this expression.

        That is, if this expression has the property "amount", the value 1000,
        and the relationship ">=", then this expression matches all charges
        where the amount is greater than or equal to 1000.

        Arguments:
            property (str):
                The property to match against. One of "amount", "card_country",
                "currency", or "ip_country".
            value (int or str):
                The value used in the comparison.
            relationship (str):
                The relationship of the comparison. One of "==", "!=", "<",
                "<=", ">", or ">=".
        '''
        assert property in ("amount", "card_country", "currency", "ip_country")
        assert relationship in ("==", "!=", "<", "<=", ">", ">=")

        # "amount" properties are compared as integers, not strings.
        if property == "amount":
            value = int(value)

        self.property = property
        self.value = value
        self.relationship = relationship

    def match(self, charge):
        '''Match a charge against this expression.

        This compares a property of the charge against this expression's value.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        if self.property not in charge:
            return False

        if self.relationship == "==":
            return charge[self.property] == self.value
        elif self.relationship == "!=":
            return charge[self.property] != self.value
        elif self.relationship == "<":
            return charge[self.property] < self.value
        elif self.relationship == "<=":
            return charge[self.property] <= self.value
        elif self.relationship == ">":
            return charge[self.property] > self.value
        elif self.relationship == ">=":
            return charge[self.property] >= self.value
        else:
            assert False  # Unreachable

    @classmethod
    def parse(cls, source):
        '''Parse a comparison-expression.

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            CompareExpr:
                The parsed expression.
        '''
        if '==' in source:
            (property, value) = source.split('==')
            relationship = '=='
        elif '!=' in source:
            (property, value) = source.split('!=')
            relationship = '!='
        elif '<=' in source:
            (property, value) = source.split('<=')
            relationship = '<='
        elif '<' in source:
            (property, value) = source.split('<')
            relationship = '<'
        elif '>=' in source:
            (property, value) = source.split('>=')
            relationship = '>='
        elif '>' in source:
            (property, value) = source.split('>')
            relationship = '>'
        else:
            assert False, 'unknown comparison'

        property = property.strip()
        value = value.strip()
        return cls(property, value, relationship)


class Charge(dict):
    @classmethod
    def parse(cls, source):
        '''Parse a CHARGE.

        The source is parsed from a string of the form

            "CHARGE: <KEY_VALUE_PAIRS>"

        where "<KEY_VALUE_PAIRS>" is a string of pairs "<PROPERTY>=<VALUE>"
        separated by "&".
        '''
        assert source.startswith('CHARGE:')
        source = source[7:]
        source = source.strip()
        properties = source.split("&")
        key_values = (kv.split("=") for kv in properties)
        charge = cls(key_values)

        # "amount" properties are compared as integers, not strings.
        if 'amount' in charge:
            charge['amount'] = int(charge['amount'])

        return charge


def main(sources):
    '''Evaluate a charge against a ruleset.

    Arguments:
        sources (Sequence[str]):
            A list of sources. The first entry is parsed as the `Charge` and
            the remaining entries are parsed as the `RuleSet`.
    '''
    (charge_source, *rule_sources) = sources
    charge = Charge.parse(charge_source)
    ruleset = RuleSet.parse(rule_sources)
    return ruleset.check_charge(charge)


if __name__ == '__main__':
    assert main([
        "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
        "ALLOW: amount < 1000",
    ]) == True

    assert main([
        "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
        "BLOCK: amount > 100",
    ]) == False

    assert main([
        "CHARGE: card_country=US&currency= USD&amount=150&ip_country=CA",
        "ALLOW: amount < 100",
        "BLOCK: card_country != CA AND amount > 100",
    ]) == False
