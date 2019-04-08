class RuleSet:
    def __init__(self, rules):
        '''Construct a new rule-set.

        Arguments:
            rules (TopRule):
                The list of top-level rules defining the rule set.
        '''
        for rule in rules:
            assert isinstance(rule, TopRule)

        self.allow = []
        self.block = []
        for rule in rules:
            if rule.type == 'allow':
                self.allow.append(rule)
            else:
                self.block.append(rule)

    def match(self, charge):
        '''Match a charge against this rule-set.

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
        '''Parse a rule-set from a list of top-level rules.

        Arguments:
            source (Sequence[str]):
                A list of top-level rules to parse.

        Returns:
            RuleSet:
                The parsed rule-set.
        '''
        rules = [TopRule.parse(source) for source in sources]
        return cls(rules)


class TopRule:
    def __init__(self, type, body):
        '''Construct a new top-level rule.

        This rule simply delegates to an underlying AND rule, but contains
        an additional `type` property used by rule-sets.

        Arguments:
            type (str):
                Either ``"allow"`` or ``"block"``.
            body (AndRule):
                An ``AndRule`` for matching charges.
        '''
        assert type == "allow" or type == "block"
        assert isinstance(body, AndRule)
        self.type = type
        self.body = body

    def match(self, charge):
        '''Match a charge against this rule.

        This returns True if the body rule matches the charge.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        return self.body.match(charge)

    @classmethod
    def parse(cls, source):
        '''Parse a top-level rule.

        The source must start with either "ALLOW:" or "BLOCK:" and the
        rest of the source is parsed as an AND rule.

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            TopRule:
                The parsed rule.
        '''
        source = source.strip()

        if source.startswith('ALLOW:'):
            type = 'allow'

        else:
            assert source.startswith('BLOCK:')
            type = 'block'

        body = AndRule.parse(source[6:])
        return cls(type, body)


class AndRule:
    def __init__(self, rules):
        '''Construct a new AND rule.

        This rule matches a charge if all sub-rules match the charge.

        Arguments:
            rules (Sequence[OrRule]):
                A list of rules, all of which must match a charge for this
                rule to match a charge.
        '''
        for rule in rules:
            assert isinstance(rule, OrRule)

        self.rules = tuple(rules)

    def match(self, charge):
        '''Match a charge against this rule.

        This returns True if all of the sub-rules match the charge.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        for rule in self.rules:
            if not rule.match(charge):
                return False
        return True

    @classmethod
    def parse(cls, source):
        '''Parse an AND rule.

        The source is parsed as zero or more OR rules separated by "AND".

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            AndRule:
                The parsed rule.
        '''
        source = source.strip()
        rule_sources = source.split('AND')
        rules = [OrRule.parse(r) for r in rule_sources]
        return cls(rules)


class OrRule:
    def __init__(self, rules):
        '''Construct a new OR rule.

        This rule matches a charge if any sub-rules match the charge.

        Arguments:
            rules (Sequence[CompareRule]):
                A list of rules, all of which must match a charge for this
                rule to match a charge.
        '''
        for rule in rules:
            assert isinstance(rule, CompareRule)

        self.rules = tuple(rules)

    def match(self, charge):
        '''Match a charge against this rule.

        This returns True if any of the sub-rules match the charge.

        Arguments:
            charge (Charge):
                A dictionary of properties of the charge.
        '''
        for rule in self.rules:
            if rule.match(charge):
                return True
        return False

    @classmethod
    def parse(cls, source):
        '''Parse an OR rule.

        The source is parsed as zero or more COMPARE rules separated by "OR".

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            OrRule:
                The parsed rule.
        '''
        source = source.strip()
        rule_sources = source.split('OR')
        rules = [CompareRule.parse(r) for r in rule_sources]
        return cls(rules)


class CompareRule:
    def __init__(self, property, value, relationship):
        '''Construct a new COMPARE rule.

        This rule matches a charge if the charge has the property associated
        with this rule, and the value of that property in the charge has the
        corresponding relationship to the value of this node.

        That is, if this rule has the property "amount", the value "1000", and
        the relationship ">=", then this rule matches all charges that contain
        the property "amount" with a value greater than or equal to 1000.

        Arguments:
            property (str):
                The property to match against. One of "amount", "card_country",
                "currency", or "ip_country".
            value (any):
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
        '''Match a charge against this rule.

        This compares a property of the charge against this rule's value.

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
        '''Parse a COMPARE rule.

        The source is parsed from a string of the form:

            "<PROPERTY> <RELATIONSHIP> <VALUE>"

        where "<PROPERTY>" is one of "amount", "card_country", "currency", or
        "ip_country"; "<RELATIONSHIP>" is one of "==", "!=", "<", "<=", ">",
        or ">="; and "VALUE" is the value corresponding to the property.

        Arguments:
            source (str):
                The source code to parse.

        Returns:
            CompareRule:
                The parsed rule.
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
    '''Evaluate a charge against a rule-set.

    Arguments:
        sources (Sequence[str]):
            A list of sources. The first entry is parsed as the `Charge` and
            the remaining entries are parsed as the `RuleSet`.
    '''
    (charge_source, *rule_sources) = sources
    charge = Charge.parse(charge_source)
    ruleset = RuleSet.parse(rule_sources)
    return ruleset.match(charge)


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
