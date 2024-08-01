def spamicity(w, pbad, pgood):
    if w in pbad and w in pgood:
        return pbad[w] / (pbad[w] + pgood[w])
    else:
        return None