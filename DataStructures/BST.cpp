#include <iostream>
#include <fstream>

using namespace std;

class BST
{
    private:
        struct Node { 
            int val;
            Node *left;
            Node *right;
        };

        Node* root;


        Node* insert(Node *node, int x) {
            if (node == nullptr) {
                node = new Node;
                node->val = x;
                node->left = nullptr;
                node->right = nullptr;
            }
            else if (node->val > x)
                node->left = insert(node->left, x);
            else {
                if (node->val < x)
                    node->right = insert(node->right, x);
            }
            return node;
        }

        void preorder(Node* node) { 
            if(node != nullptr) {
                cout << node->val << " ";
                preorder(node->left);
                preorder(node->right);
            }
        }

        void inorder(Node* node) {
            if(node != nullptr) {
                inorder(node->left);
                cout << node->val << " ";
                inorder(node->right);
            }
        }

        void postorder(Node* node) { 
            if(node != nullptr) {
                postorder(node->left);
                postorder(node->right);
                cout << node->val << " ";
            }
        }

        int height (Node* node){
            if(node == nullptr)
                return 0;
            else{
                int maxL = height(node->left);
                int maxR = height(node->right);
                if (maxL > maxR)
                    return maxL + 1;
                else
                    return maxR + 1;
            }
        }

        Node* deleteTree(Node *node) {
            if (node != nullptr) {
                deleteTree(node->left);
                deleteTree(node->right);
                delete node;
            }
            return nullptr;
        }

    public:
        BST(){
            root = nullptr;
        }

        ~BST()
        {
            root = deleteTree(root);
        }

        void insert(int x){
            root = insert(root,x);
        }

        Node* search(int x) {
            Node* ptr = root;
            while(ptr != nullptr) {
                if(x > ptr->val)
                    ptr = ptr->right;
                else if(x < ptr->val)
                    ptr = ptr->left;
                else
                    break;
            }
            return ptr;
        }

        int max ()
        {
            Node* node = root;
            int n = root->val;
            while(node->right != nullptr) {
                node  = node -> right;
                n = node -> val;
            }
            return n;
        }

        int height ()
        {
            return height(root);
        }

        void preorder() {
            preorder(root);
        }

        void inorder() {
            inorder(root);
        }

        void postorder() {
            postorder(root);
        }
};

    int main() {
        ifstream tree_in;
        int x;
        BST tree;
        tree_in.open("data.txt");
        while (tree_in >> x && !tree_in.eof())
            tree.insert(x);
        tree_in.close();
        cout << "Height of BST: " << tree.height() << endl;
        cout << "The biggest element: " << tree.max() << endl;
        cout << "Preorder: ";
        tree.preorder();
        cout << endl << "Inorder: ";
        tree.inorder();
        cout << endl << "Postorder: ";
        tree.postorder();
        cout<< endl << "Right child of 17 is "<<tree.search(17)->right->val;
        return 0;
}
