#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys

def bubbleSort(array):
    swapHappened = True
    while swapHappened:
        swapHappened = False
        for x in range(0, len(array)-1):
            if array[x].attrib['subject'] > array[x+1].attrib['subject']:
                # Swap data
                array[x], array[x+1] = array[x+1], array[x]
                swapHappened = True

def get_tag_uri(element):
    if element.tag[0] == "{":
        uri = element.tag[1:].partition("}")[0]
    else:
        uri = None
    return uri

def main():

    # Take in nzb file as first argument
    tree = ET.parse(sys.argv[1])
    # Get root of XML ElementTree
    root = tree.getroot()
    # Try to find the URI associated with the namespace
    try:
        uri = get_tag_uri(root[0])
    except:
        print "Whoops, it looks like there are no files in this nzb."
        sys.exit(-1)
    # Set namespace to null so we get a properly formatted xml file on output
    ET.register_namespace('', uri)
    # Build list of child elements of the root
    child_list = []
    for child in root:
        child_list.append(child)
    # Remove all child elements from the root; We'll add them back sorted
    for child in child_list:
        root.remove(child)
    # Sort all the child elements based on 'subject' field which is filename
    bubbleSort(child_list)
    # Append sorted child elements back onto the root
    for child in child_list:
        root.append(child)
    # Rebuild element tree
    tree = ET.ElementTree(root)
    # Output the new sorted nzb
    tree.write(sys.argv[1])

if __name__ == "__main__":
    main()
