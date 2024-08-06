import re

markdown_blocks_paragraph = "paragraph"
markdown_blocks_heading = "heading"
markdown_blocks_code = "code"
markdown_blocks_quote = "quote"
markdown_blocks_unordered_list = "unordered_list"
markdown_blocks_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks =  markdown.split('\n\n')
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return markdown_blocks_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return markdown_blocks_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return markdown_blocks_paragraph
        return markdown_blocks_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return markdown_blocks_paragraph
        return markdown_blocks_unordered_list
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return markdown_blocks_paragraph
        return markdown_blocks_unordered_list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return markdown_blocks_paragraph
            i += 1
        return markdown_blocks_ordered_list
    return markdown_blocks_paragraph
