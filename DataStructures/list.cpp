#include <iostream>
#include <fstream>

using namespace std;

class Node
{
private:
    int val;
    Node *next;

public:
    Node(int value){
        next = nullptr;
        val = value;
    }

    ~Node()
    {
        delete next;
    }

    Node* insert(int x) {
        Node* newNode = new Node(x);
        if (val > x) {
            newNode->next = this;
            return newNode;
        } else {
            Node *currentNode = this;
            Node *nextNode = this->next;
            while (nextNode != nullptr && nextNode->val < x) {
                currentNode = nextNode;
                nextNode = nextNode->next;
            }
            newNode->next = nextNode;
            currentNode->next = newNode;

            return this;
        }
    }

    Node* search(int x) {
        Node* currentNode = this;
        while (currentNode-> val < x && currentNode->next != nullptr )
            currentNode = currentNode->next;
        if (currentNode->val == x)
            return currentNode;
        else
            return nullptr;
    }

    void show() {
        cout << val << " ";
        if(next != nullptr)
            next->show();
    }

    int length (){
        if(next != nullptr)
            return next->length() + 1;
        else
            return 1;
    }

    int max()
    {
        if(next != nullptr)
            return next->max();
        else
            return val;
    }

    int getValue() {
        return val;
    }

};

int main() {
    ifstream in;
    int x;
    Node* list = nullptr;
    in.open("data.txt");
    while (in >> x)
        if (list == nullptr)
            list = new Node(x);
        else
            list = list->insert(x);
    in.close();
    cout << "The greatest element: "<< list->max() << endl;
    cout <<  list->search(21)->getValue() << endl;
    cout << "Length of list is "<< list->length() << endl;
    cout << "All elements  ";
    list->show();
    delete list;
    return 0;
}
