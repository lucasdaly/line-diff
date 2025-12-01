import Levenshtein
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def hamming_distance(a:int, b:int) ->int:
    return(a^b).bit_count()

def levenshtein_similarity(s: str, t:str) ->float:
    if not s and not t:
        return 1.0
    dist = Levenshtein.distance(s,t)
    max_len = max(len(s), len(t))
    return 1.0-dist/max_len

def calculate_cosine(contextline1, contextline2):
    tfdif = TfidfVectorizer()
    vecs = tfdif.fit_transform([contextline1, contextline2])
    score = cosine_similarity(vecs[0], vecs[1])[0][0]
    return score

def combinedscore(line1,line2,contextline1,context1,context2):
    return levenshtein_similarity(line1,line2)*0.6 + 0.4*calculate_cosine(context1,context2)
    