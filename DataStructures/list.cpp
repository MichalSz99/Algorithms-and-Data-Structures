#include <iostream>
#include <fstream>

using namespace std;

    class List
    {
    private:
        struct Node {
            int val;
            Node *next;
        };

        Node* firstNode;


        void show(Node* node) {
            if(node != nullptr) {
                cout << node->val << " ";
                show(node->next);
            }
        }

        int length (Node* node){
            if(node == nullptr)
                return 0;
            else
               return length(node->next) + 1;
        }

        Node* deleteList() {
            Node *currentNode = firstNode;
            while(currentNode != nullptr)
            {
                firstNode = currentNode -> next;
                free(currentNode);
                currentNode = firstNode;
            }
            return nullptr;
        }


    public:
        List(){
            firstNode = nullptr;
        }

        ~List()
        {
            firstNode = deleteList();
        }

        void insert(int x) {
            Node* newNode = new Node;
            newNode->val = x;
            newNode->next = nullptr;
            if (firstNode == nullptr)
                firstNode = newNode;
            else if (firstNode->val > x) {
                newNode->next = firstNode;
                firstNode = newNode;
            } else {
                Node *currentNode = firstNode;
                Node *nextNode = firstNode->next;
                while (nextNode != nullptr && nextNode->val < x) {
                    currentNode = nextNode;
                    nextNode = nextNode->next;
                }
                newNode->next = nextNode;
                currentNode->next = newNode;
            }
        }

        Node* search(int x) {
            Node *currentNode = firstNode;
            while(currentNode != nullptr && currentNode->val != x)
                currentNode = currentNode ->next;
            return currentNode;
        }

        int max ()
        {
            Node* node = firstNode;
            int n = firstNode->val;
            while(node->next != nullptr)
                node  = node -> next;
            return node->val;
        }


        void show() {
            show(firstNode);
        }

        int length(){
            return length(firstNode);
        }
    };


    int main() {
        ifstream in;
        int x;
        List list;
        in.open("data.txt");
        while (in >> x && !in.eof())
            list.insert(x);
        in.close();
        cout << "The biggest element: "<< list.max() << endl;
        cout << "Next value after 21 is "<< list.search(21)->next->val << endl;
        cout << "Length of list is "<< list.length() << endl;
        cout << "All elements  ";
        list.show();
        return 0;
}
