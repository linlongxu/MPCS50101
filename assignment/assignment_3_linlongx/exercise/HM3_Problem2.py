def is_number(astring):
    try:
        float(astring)
        return True
    except:
        return False