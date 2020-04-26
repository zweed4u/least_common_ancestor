package main

import (
	"fmt"
)

type Node struct {
	Left  *Node
	Info  int
	Right *Node
}

// value receiver - simple toString method for Node
func (n Node) String() string {
	return fmt.Sprintf("%d", n.Info)
}

func lca(root Node, v1 int, v2 int) Node {
	// sort vertices such that v1 is lesser/Left then v2 Right
	if v1 > v2 {
		v1, v2 = v2, v1
	}

	curr_node := root
	if curr_node.Info == v1 || curr_node.Info == v2 {
		return curr_node
	}
	if v1 < curr_node.Info && curr_node.Info < v2 {
		return curr_node
	}
	for {
		if curr_node.Left == nil || curr_node.Right == nil {
			break
		}
		if v1 < curr_node.Info && curr_node.Info < v2 {
			return curr_node
		}
		if curr_node.Info == v1 || curr_node.Info == v2 {
			return curr_node
		}
		if v1 < curr_node.Info && v2 < curr_node.Info {
			curr_node = *curr_node.Left
		} else if v1 > curr_node.Info && v2 > curr_node.Info {
			curr_node = *curr_node.Right
		}
	}
	return root
}

/*
EXAMPLE 1
                5
        3              8
    2       4       6
1                       7
*/
func main() {
	root := Node{nil, 5, nil}
	exampleTree := root
	exampleTree.Left = &Node{nil, 3, nil}
	exampleTree.Left.Left = &Node{nil, 2, nil}
	exampleTree.Left.Right = &Node{nil, 4, nil}
	exampleTree.Left.Left.Left = &Node{nil, 1, nil}
	exampleTree.Right = &Node{nil, 8, nil}
	exampleTree.Right.Left = &Node{nil, 6, nil}
	exampleTree.Right.Left.Right = &Node{nil, 7, nil}

	v1, v2 := 3, 1
	lca := lca(exampleTree, v1, v2)
	fmt.Println("Least common ancestor:", lca)
}
