import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_link,
    text_type_italic
)

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        text = node.text
        parts = text.split(delimeter)
        split_nodes = []
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i],text_type_text))
            else:
                split_nodes.append(TextNode(parts[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        extracted_images = extract_markdown_images(node.text)
        original_text = node.text

        if len(extracted_images) == 0:
            new_nodes.append(node)
            continue

        for image in extracted_images:
            image_alt = image[0]
            image_link = image[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],text_type_text))
            new_nodes.append(
                TextNode(
                    image_alt,
                    text_type_image,
                    image_link
                )
            )
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)

        original_text = node.text

        if len(extracted_links) == 0:
            new_nodes.append(node)
            continue
        print(extracted_links, "<- LINKS")

        for link in extracted_links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],text_type_text))
            new_nodes.append(
                TextNode(
                    link[0],
                    text_type_link,
                    link[1]
                )
            )
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))


main()
