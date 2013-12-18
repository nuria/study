package week4;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 10/2/13
 * Time: 6:41 AM
 * To change this template use File | Settings | File Templates.
 */

import java.util.Iterator;
import java.util.ArrayList;

public class BST<Key extends Comparable<Key>, Value> {

    private Node root = null;

    /**
     * keep traversing until we find a good place to put it.
     * two cases:
     * 1) leaf
     * 2) middle with children
     * *
     */

    public void put(Key key, Value value) {
        root = put(key, value, root);
    }

    public Node put(Key key, Value value, Node node) {
        if (node == null) {
            return new Node(key, value);
        }
        int cmp = key.compareTo(node.getKey());

        if (cmp < 0) {
            node.setLeft(put(key, value, node.getLeft()));
        } else if (cmp > 0) {
            node.setRight(put(key, value, node.getRight()));
        } else {
            //is equals
            node.setValue(value);
        }
        node.count = 1 + size(node.left) + size(node.right);
        return node;
    }

    /**
     * Floor , largest key <= than a given key
     */
    public Key floor(Key key) {
        return _floor(this.root, key, null);
    }

    private Key _floor(Node node, Key key, Node prior) {
        if (node == null) {
            if (prior != null) {
                return prior.getKey();
            } else {
                return null;
            }
        }

        int compare = node.getKey().compareTo(key);

        if (compare == 0) {
            //easy case, return itself
            return key;
        } else if (compare > 0) {
            //current node is bigger than key,return prior
            return prior.getKey();
        } else {
            //current node is smaller than key
            return _floor(node.getRight(), key, node);
        }


    }


    /**Ceiling largest key >= than a given key **/
    /**public Value ceiling(Key key){

     }  **/

    /**
     * number of nodes in the subtree  rooted at that node
     * (includes root)*
     */
    public int size() {
        return root.getCount();
    }

    /**
     * number of nodes in the subtree  rooted at that node
     * (includes root) *
     */
    public int size(Node node) {
        if (node == null) {
            return 0;
        } else {
            return node.count;
        }
    }

    /**
     * How many keys <  than k *
     */
    public int rank(Key key) {
        return rank(key, this.root);
    }

    private int rank(Key key, Node node) {
        int counter = 0;
        if (node == null) {
            return counter;
        }

        int compare = key.compareTo(node.getKey());

        if (compare == 0) {
            if (node.getLeft() != null) {
                counter = node.getLeft().getCount();
            }
        } else if (compare < 0) {
            // key is smaller than node key.keep processing on left tree
            counter = rank(key, node.getLeft());
        } else {
            //key is bigger than node key, rank is at least as big as the left tree +1
            if (node.getLeft() != null) {
                counter = node.getLeft().getCount();
            }
            counter = counter + 1 + rank(key, node.getRight());
        }
        return counter;
    }

    /**
     * @param key
     * @return
     */
    public Value get(Key key) {
        Node current = root;

        while (current != null) {
            int compare = key.compareTo(current.getKey());
            if (compare > 0) {
                current = current.getRight();
            } else if (compare < 0) {
                current = current.getLeft();
            } else {
                return current.getValue();
            }
        }

        return null;

    }

    public Node getNode(Key key) {
        Node current = root;

        while (current != null) {
            int compare = key.compareTo(current.getKey());
            if (compare > 0) {
                current = current.getRight();
            } else if (compare < 0) {
                current = current.getLeft();
            } else {
                return current;
            }
        }

        return null;

    }

    /**
     * easy case of delete *
     */
    public void deleteMin() {

        this.root = deleteMin(root);

    }

    /**
     * Find a node with empty left tree
     * Swap that node with its right tree if any
     *
     * @param node
     * @return
     */
    private Node deleteMin(Node node) {

        if (node.getLeft() == null) {
            return node.getRight();
        }
        node.setLeft(deleteMin(node.getLeft()));

        node.count = size(node.getLeft()) + size(node.getRight()) + 1;
        return node;
    }

    /**
     * case 0, node we want to delete has no children
     *
     * @param key
     */
    public void delete(Key key) {
        Node node = this.getNode(key);
        if (node == null) {
            return;
        }
        if (node.getLeft() == null && node.getRight() == null) {
            node = null;
        }
    }

    /**
     * serializing a tree for inspect it *
     */
    public String toString() {
        // assuming root is not null
        // put nodes i an array, dynamically resize?
        // cheating assume size
        ArrayList<String> keys = new ArrayList<String>();
        if (this.root == null) {
            return "[]";
        }

        int i = 0;

        ArrayList<Node> nodes = new ArrayList<Node>();

        keys.add(i, root.getKey().toString() + "[" + root.getCount() + "]");

        nodes.add(root);
        //use array as a queue
        while (nodes.size() > 0) {

            Node current = nodes.remove(0);

            if (current.getLeft() != null) {
                keys.add(2 * i + 1, current.getLeft().getKey().toString() + "[" + current.getLeft().getCount() + "]");
                nodes.add(current.getLeft());
            } else {
                keys.add(2 * i + 1, "E");
            }
            if (current.getRight() != null) {
                keys.add(2 * i + 2, current.getRight().getKey().toString() + "[" + current.getRight().getCount() + "]");
                nodes.add(current.getRight());
            } else {
                keys.add(2 * i + 2, "E");
            }
            i++;
        }
        StringBuffer sb = new StringBuffer();

        for (String k : keys) {
            sb.append(k + " ,");
        }

        return sb.toString();
    }
    //   public Iterator<Key> Iterator(){}


    private class TreeIterator implements Iterator {

        private Node current;

        public TreeIterator() {
            this.current = BST.this.root;
        }

        @Override
        public boolean hasNext() {
            if (current != null && (current.getLeft() != null || current.getRight() != null)) {
                return true;
            }
            return false;

        }

        //does this return stuff in order?
        @Override
        public Object next() {
            return null;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException("there is no remove in this iterator");
        }

    }

    private class Node {

        private Key key;

        private Value value;

        private Node left;

        private Node right;

        private int count = 1;

        public Node(Key key, Value value) {
            this.key = key;
            this.value = value;
        }


        private int getCount() {
            return count;
        }

        private void setCount(int count) {
            this.count = count;
        }

        private Node getRight() {
            return right;
        }

        private void setRight(Node right) {
            this.right = right;
        }

        private Node getLeft() {
            return left;
        }

        private void setLeft(Node left) {
            this.left = left;
        }


        private Key getKey() {
            return key;
        }


        private void setKey(Key key) {
            this.key = key;
        }


        private Value getValue() {
            return value;
        }

        private void setValue(Value value) {
            this.value = value;
        }


        public String toString() {
            return this.getKey().toString();
        }
    }
}
