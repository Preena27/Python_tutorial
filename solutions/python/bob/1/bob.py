def response(hey_bob):
    s = hey_bob.strip()
    if not s:
        return "Fine. Be that way!"
    has_letter = any(c.isalpha() for c in s)
    is_yelling = has_letter and s.upper() == s
    is_question = s.endswith("?")
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."

        
