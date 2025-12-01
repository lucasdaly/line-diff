import Levenshtein
import sklearn


def hamming_distance(a:int, b:int) ->int:
    return(a^b).bit_count()

def levenshtein_similarity(s: str, t:str) ->float:
    if not s and not t:
        return 1.0
    dist = Levenshtein.distance(s,t)
    max_len = max(len(s), len(t))
    return 1.0-dist/max_len