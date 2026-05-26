from blocktype import BlockType

def is_ul_block(block):
    lines = block.split("\n")
    for line in lines:
        if len(line) >= 2:
            if line[0] != '-' or line[1] != ' ':
                return False
    
    return True

def is_ol_block(block):
    lines = block.split("\n")
    line_no = 1
    for line in lines:
        if len(line) <= 2:
            return False
        # TODO: use regex here, line number can be any number of digits
        if ord(line[0]) != line_no or line[1] != '.':
            return False
        line_no += 1

    return True

def is_quote_block(block):
    lines = block.split("\n")
    for line in lines:
        if len(line) <= 1:
            return False
        if line[0] != '<':
            return False
    
    return True

def is_code_block(block):
    lines = block.split("\n")
    print("code", lines)
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return True
    
    return False

def block_to_block_type(block):
    # remove any surrounding whitespace in case
    block = block.strip()

    if len(block) <= 2:
        return BlockType.PARAGRAPH
        
    if block.startswith('-') and is_ul_block(block):
        return BlockType.UNORDERED_LIST
    
    if block.startswith('1') and is_ol_block(block):
        return BlockType.ORDERED_LIST
    
    if block.startswith('<') and is_quote_block(block):
        return BlockType.QUOTE

    if block.startswith('# '):
        return BlockType.HEADING
    
    if is_code_block(block):
        return BlockType.CODE
    
    return BlockType.PARAGRAPH