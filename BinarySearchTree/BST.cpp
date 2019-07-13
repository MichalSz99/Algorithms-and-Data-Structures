#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

struct tree { //definition of vertex of tree
	int info;
	struct tree *left;
	struct tree *right;
};

struct tree *insert(struct tree *root, int x) { //insert new element into tree
	if(!root) {
		root=(struct tree*)malloc(sizeof(struct tree));
		root->info = x;
		root->left = NULL;
		root->right = NULL;
		return(root);
	}
	if(root->info > x)
	     root->left = insert(root->left,x);
	else {
		if(root->info < x)
			root->right = insert(root->right,x);
	}
	return(root);
}

 struct tree *search(struct tree *root, int x) { // looking for element in tree
	struct tree *ptr;
	ptr=root;
	while(ptr) {
		if(x>ptr->info)
		     ptr=ptr->right;
		else if(x<ptr->info)
		     ptr=ptr->left;
		else
		    break;
	}
	return ptr;
 }


void deleteTree(struct tree *root) { // deleting tree from memory
	if(root != NULL) {
		deleteTree(root->left);
		deleteTree(root->right);
		cout << root->info << " ";  //show elements in postorder
		free(root);
	}

}

int max (struct tree *root) //looking for the biggest element in tree
{
    struct tree *BST = root;
    int n = root ->info;
    while(BST ->right != NULL) {
		BST  = BST -> right;
		n = BST -> info;
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

void preorder(struct tree *root) { //show elements in preorder
	if(root != NULL) {
		cout << root->info << " ";
		preorder(root->left);
		preorder(root->right);
	}
}

void inorder(struct tree *root) { //show elements in inorder
	if(root != NULL) {
		inorder(root->left);
		cout << root->info << " ";
		inorder(root->right);
	}
}
int main(){

    fstream tree_in;
    int x;
    struct tree *BST = NULL;
    tree_in.open("dane.txt", ios::in);
    while (tree_in>>x && !tree_in.eof() )
            	 BST = insert(BST,x);
    tree_in.close();
	
    x = height(BST);
    cout << "Height of BST: " << x <<endl;
    x = max(BST);
    cout << "The biggest element: " << x <<endl;
    cout << "Preorder: ";
    preorder(BST);
    cout << endl <<"Inorder: ";
    inorder(BST);
    cout << endl <<"Preorder: ";
    deleteTree(BST);
    return 0;
}

