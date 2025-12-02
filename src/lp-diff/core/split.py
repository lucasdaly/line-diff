from Levenshtein import distance as lev_diff



# Check to see if old_line was split into multiple lines in right_lines
def detect_split(
          

        old_line: str,
        right_lines: list[str],
        start_index: int,
        max_extra_lines: int

        # old_line : old (left) line. We are checking to see if it was split
        # right_lines : lines we are checking to see if old_line was split into
        # start_index : index in right_lines to start checking from
        # max_extra_lines : maximum number of extra lines in the new file to consider for a split

                 ) -> list[int]:
     


     pass