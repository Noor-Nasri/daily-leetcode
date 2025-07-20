# not my solution at all, already did a contest today (a solid 4/4!) so I dont want to read a hard

from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.name = ""
        self.marked = False  # for deletion

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        
        # Step 1: Build the trie
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                    node.children[folder].name = folder
                node = node.children[folder]

        # Step 2: Serialize each subtree
        serial_map = defaultdict(list)  # signature -> list of nodes

        def serialize(node):
            if not node.children:
                return "()"
            serials = []
            for child in sorted(node.children):
                serials.append(f"({child}{serialize(node.children[child])})")
            serial = ''.join(serials)
            serial_map[serial].append(node)
            return serial

        serialize(root)

        # Step 3: Mark duplicates
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.marked = True

        # Step 4: Collect remaining paths
        res = []

        def collect(node, path):
            for name, child in node.children.items():
                if not child.marked:
                    res.append(path + [name])
                    collect(child, path + [name])

        collect(root, [])
        return res