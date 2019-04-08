---
title: "Run the Rules"
date: 2019-04-08
---

String problems are a popular subject of many Computer Science technical interviews because the overlying concepts can be applied to so many real world applications. This week we will work on creating an application that uses many of the techniques we've learned previously along with some other interesting elements thrown in for good measure. Since this is a significant problem (and very closely based on a real problem from a top technology company), we will only have the single problem which we will spent the entirity of the session on (45 minutes for completion).

# P1: Rules Engine
Imagine that you are working for a fintech company that processes millions of online payments from a variety of merchants. One of the features your company offers is the ability for merchants to create a custom ruleset to either **ALLOW** or **BLOCK** oncoming payments. Your task is to create a rules engine which parses a transaction feed (sent as a string), extracts the necessary information, and determines if the payment is allowed to be processed.

Rules will have the following attributes:
* **amount:** integer 
* **card_country:** string 
* **currency:** string 
* **ip_country:** string

Your rules engine should first evaluate all "allow" rules, and if none of those match, evaluate all "block" rules. If an "allow" rule matches, return **True**. If a "block" rule matches, return **False**. If no "allow" or "block" rule matches, return **True**.

* Rules will always include "allow" information before "block" information. 
* You should evaluate the rules in the order in which they are provided in the transaction string. 
* Rules can be compounded with **AND** or **OR**.
* Each rule will only ever contain a maximum of a single compound operator.
* Rules can use the following operators: ==, !=, <, <=, >=, >.

## Examples
**Input:**
```[ "CHARGE: card_country=US.Stcurrency=USD8zamount=150&ip_country.CA", "ALLOW: amount < 1000, ]```

**Output:**
```True```

The charge is allowed because the charged amount of 150 is less than the threshold of 1000. 

**Input:**
```[ "CHARGE: card_country=US&currency=USD8zamount=150&ipsountry.CA", "BLOCK: amount > 100",]```

**Output:**
```False```

The charge is blocked because the charged amount of 150 is over the threshold of 100. 

**Input:**
```[ "CHARGE: card_country=US&currency= USD8tamount=150&ip_country=CA", "ALLOW: amount < 100", "BLOCK: card_countty l= ip_country AND amount > 100", ]```

**Output:**
```False```

The first rule does not match, so we move on to the next rule. This is a compound rule that evaluates to true because the cardsountry (US) does not match the ipsountry (CA), and the amount (150) is over the limit of 100. Since we matched on a BLOCK rule, we block the charge. 


