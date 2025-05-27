r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

1. ^
 
    Anchors the match to the beginning of the string.

2. [\w\.-]+

    [] → Character class, matches any one character inside it.

    \w → Matches any word character: letters (a-z, A-Z), digits (0-9), or underscore _.

    \. → Matches a literal dot (.) (escaped because dot is special in regex).

    - → Matches a literal hyphen -.

    + → One or more of the above characters.

✅ So this part matches the username in the email, like john.doe.
3. @

    Matches the literal @ symbol (required in all email addresses).

4. [\w\.-]+

    Same as earlier: domain name part, like gmail, my-company, sub.domain.

5. \.

    Matches a literal dot (.) between the domain and the TLD.

6. \w{2,}

    Matches 2 or more word characters (TLD like com, org, co, edu, etc.).

7. $

    Anchors the match to the end of the string.