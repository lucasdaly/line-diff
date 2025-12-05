from similarity import combinedscore

def getcontext(lines, index, context_size=3):
    start = max(0, index-context_size)
    end = min(len(lines),index+context_size+1)
    return " ".join(lines[start:end])

def compare(old_lines,new_lines,candidate_sets,threshold=0.7):
    final_matches = []
    used_new_lines= set()

    for i, candidates in enumerate(candidate_sets):
        if not candidates:
            continue
    
        best_score = 0
        best_match = -1

        for new_line_num in candidates:
            new_idx = new_line_num-1
        
            if new_idx in used_new_lines:
                continue

            oldcontext = getcontext(old_lines, i)
            newcontext = getcontext(new_lines, new_idx)

            score = combinedscore(old_lines[i], new_lines[new_idx], oldcontext, newcontext)

            if score > best_score and score >= threshold:
                best_score=score
                best_match=new_idx
        
        if best_match!=-1:
            final_matches.append((i, best_match, best_score))
            used_new_lines.add(best_match)
    return final_matches
