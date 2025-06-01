import re

def parse_for_loop_c_cpp(loop_code: str):
    match = re.search(r'for\s*\((.*?);(.*?);(.*?)\)',loop_code)
    if not match:
        return None
    init = match.group(1).strip()
    condn = match.group(2).strip()
    updation = match.group(3).strip()

    start_match = re.search(r'=\s*([0-9]+)',init)
    start = int(start_match.group(1)) if start_match else 0

    end_match = re.search(r'<\s*([0-9]+)',condn)
    if not end_match:
        end_match = re.search(r'<=\s*([0-9]+)',condn)
        end = (int(end_match.group(1)) + 1) if end_match else 0
    else:
        end = int(end_match.group(1))
    
    return start,end

