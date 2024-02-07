from random import choice, randint
def get_response(user_input: str) -> str:
    lowered : str = user_input.lower()
    if lowered == "":
        return "well you are silent"
    elif "hello" in lowered:
        return "Hello there"
    elif "roll dice" in lowered:
        return str(randint(1,6))

    raise NotImplementedError("Implement this function")
