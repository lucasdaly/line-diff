from Levenshtein import distance as ld

# Check to see if old_line was split into multiple lines in new_lines
# Levenshtein similarity of the actual CONTENT of the lines,
def greedy_split_match(
          

        old_line: str,
        new_lines: list[str],
        start_index: int,
        max_extra_lines: int

        # old_line : old (left) line. We are checking to see if it was split
        # new_lines : lines we are checking to see if old_line was split into
        # start_index : index in new_lines to start checking from
        # max_extra_lines : maximum number of extra lines in the new file to consider for a split


        # return type: tuple
            # list of INDICES** in new_lines that correspond to the split of old_line (if any, returns [] if no split detected)
            # and then the similarity score (float between 0 and 1)
                 ) -> tuple[list[int], float]:
     
     # make sure start_index is in range
     if start_index <0 or start_index >= len(new_lines):
         return [], 0.0
     
     # empty content string to keep adding new lines to
     combined = ""

     # variable to compare current score vs last one (for greedy)
     last_score = 0.0
     
     # if the max number of extra lines goes beyond the length of new_lines, make it the length of new_lines
     bound = min(len(new_lines), start_index + max_extra_lines + 1)

     # if bound is for some reason less than or equal to start_index (incorrect input), return no split
     if bound <= start_index:
         return [], 0.0

     # iterate through new_lines, adding the new lines one by one and checking the similarity score (greedy)
     for i in range(start_index, bound):
          
          combined += new_lines[i]
          score = lev_similarity_score(old_line, combined)

          # if score goes down, return the last indices and last score
          if score < last_score:
               return list(range(start_index, i)), last_score
          
          last_score = score
     # if it continuous growing until the end, return all the indices and the last score
     return list(range(start_index, i + 1)) ,score

# returns normalized similarity score 0 (no similarity) to 1 (same string)
def lev_similarity_score(
          
          
          line1: str,
          line2: str

          # returns ormalized Levenshtein similarity score between two strings (in this case, old line and combined new lines, but works for any two strings)

) -> float:
     
     # get max length of the two lines to have something to normalize against
     max_len = max(len(line1), len(line2))

     # in case len = 0, no div by 0
     if max_len == 0:
        return 1.0
     
     return 1 - ld(line1, line2) / max_len









