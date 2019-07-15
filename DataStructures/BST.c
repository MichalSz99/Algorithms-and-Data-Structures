#include <stdio.h>
#include <stdlib.h>


 struct tree { //definition of vertex of tree
	int val;
	struct tree *left;
	struct tree *right;
};

 struct tree *insert(struct tree *node, int x) { //insert new element into tree
	if(!node) {
		node=(struct tree*)malloc(sizeof(struct tree));
		node->val = x;
		node->left = NULL;
		node->right = NULL;
	}
	else if(node->val > x)
	     node->left = insert(node->left,x);
	else if(node->val < x)
			node->right = insert(node->right,x);
	return (node);
}


  struct tree *search(struct tree *root, int x) { // looking for element in tree
	struct tree *ptr = root;
	while(ptr) {
		if(x > ptr->val)
		     ptr=ptr->right;
		else if(x < ptr->val)
		     ptr = ptr->left;
		else
		    break;
	}
	return ptr;
 }


 void deleteTree(struct tree *node) { // deleting tree from memory
	if(node != NULL) {
		deleteTree(node->left);
		deleteTree(node->right);
		free(node);
	}
 }


 int max (struct tree *root) //looking for the biggest element in tree
{
    struct tree *BST = root;
    int n = root->val;
    while(BST->right != NULL) {
		BST  = BST -> right;
		n = BST -> val;
	}
	return n;
}


 int height (struct tree *root)
{
	if(root == NULL)
        return 0;
    else{
		int maxL = height(root->left);
		int maxR = height(root->right);
		if (maxL > maxR)
            return maxL + 1;
        else
            return maxR + 1;
    }
}


 void preorder(struct tree *node) {
	if(node != NULL) {
	    printf("%d ", node->val);
		preorder(node->left);
		preorder(node->right);
	}
}


void inorder(struct tree *node) {
    if(node != NULL) {
        inorder(node->left);
        printf("%d ", node->val);
        inorder(node->right);
    }
}

void postorder(struct tree *node) {
    if(node != NULL) {
        postorder(node->left);
        postorder(node->right);
        printf("%d ", node->val);
    }
}
int main(){
    FILE *in = fopen("data.txt", "r");
    int x;
    struct tree *BST = NULL;
    while (fscanf(in, "%d", &x) != EOF)
        BST = insert(BST, x);
    fclose(in);
    printf("Height of BST: %d \n", height(BST));
    printf("The biggest element: %d \n", max(BST));
    printf("Preorder: ");
    preorder(BST);
    printf("\nInorder: ");
    inorder(BST);
    printf("\nPostorder: ");
    postorder(BST);
    printf("\nRight child of 17 is %d", search(BST,17)->right->val);

}
