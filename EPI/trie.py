#usr/local/bin/pythonn
import string
import unittest

class Node:
    def __init__(self, val=''):
        self.val = val
        # storage o(n) per node
        # this will really be a dictionary later
        self.children = {}

    def is_leaf(self):
        # a node with no children is a leaf
        return len(self.children.keys()) == 0


    def __repr__(self):
        sb = '' + self.val
        for k in self.children.keys():
            sb += str(self.children[k])

        return sb

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        # to insert a word into the trie tree
        # we need to split the word in chars and walk the tree
        word = list(word)
        node = self.root

        def insert_char(word, node ):
            c = word[0]
            # if node has a child at char c keep on going
            # else insert it
            if node.children.get(c) is None:
                node.children[c] = Node(c)
            if len(word) > 1:
                insert_char(word[1:], node.children[c])

        insert_char(word, node)


    def search(self, word):
        """
        Returns true if the word is in the trie.
        It has to be an exact match
        :type word: str
        :rtype: bool
        """
        word = list(word)
        node = self.root
        # traverse tree starting at root
        # search returns true only for exact hits
        def search_word(word, node):
            c = word[0]
            node = node.children.get(c)
            if len(word) == 1 and node is not None and node.is_leaf():
                # if node is leaf this word exists on the tree
                return True
            if node.children.get(c) is None:
                return False
            else:
                # keep on searching
                return search_word(word[1:], node.children[c])

        return search_word(word, node)


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        def search_word(word, node):
            c = word[0]
            node = node.children.get(c)
            if len(word) == 1 and node is not None:
                # if node is leaf this word exists on the tree
                return True
            if node.children.get(c) is None:
                return False
            else:
                # keep on searching
                return search_word(word[1:], node.children[c])

        node = self.root
        return search_word(prefix, node)


if __name__=="__main__":

    class Testing(unittest.TestCase):

        def setUp(self):
            self.trie = Trie()

        def test_happy_case_search(self):
            self.trie.insert("apple")
            print self.trie.root.children
            self.assertTrue(self.trie.search("apple"))

        def no_run_test_happy_case_startsWith(self):
            self.trie.insert("apple")
            self.assertFalse(self.trie.search("app"))
            self.assertTrue(self.trie.startsWith("app"))
            trie.insert("app");
            self.assertTrue(self.trie.search("app"))

    unittest.main().result

