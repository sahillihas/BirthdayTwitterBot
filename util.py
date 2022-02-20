def trimDescription(description):
    val = 190
    position = description.rfind(".", 0, val)
    lenDes = len(description)
    if lenDes > val:
        if position < 0:
            position = description.rfind(" ", 0, val - 3)
            return description[:position] + "..."
        return description[:position]
    else:
        return description


def removeSpace(string):
    return string.replace(" ", "")
