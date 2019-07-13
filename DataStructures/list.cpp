#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

struct list{ //definition of elements of list
	int key;
	struct list *next;
};

struct list *insert(struct list *start, int x) { //insert elements into list

	struct list *newList = (struct list*)malloc(sizeof(struct list));
    newList->key = x;
    newList->next = NULL;

	if(!start) {
		start=newList;
		return start;
	}

    if (start -> key > x)
    {
        newList ->next = start;
        start = newList;
        return start;
    }

    struct list *currentList = start;
    struct list *nextList  = start->next;
	while(nextList !=NULL && nextList->key < x)
	      {
	          currentList = nextList;
	          nextList = nextList -> next;
	      }
	newList ->next = nextList;
	currentList -> next = newList;

	return start;
}

void deleteList(struct list *start) { //deleting list
    struct list *currentList = start;
    while(currentList != NULL)
	{
	    start = currentList -> next;
	    cout << currentList->key << " ";
	    free(currentList);
	    currentList = start;
	}

}

struct list *search(struct list *start, int x) {

	struct list *currentList = start;
	while(currentList !=NULL && currentList->key != x)
	      {
	          currentList = currentList ->next;
	      }
	return(currentList);
}


int main ()
{

    fstream list_in;
	int x;
	struct list *List = NULL;
    list_in.open("dane.txt", ios::in);
    while (list_in>>x && !list_in.eof() )
            	 List = insert(List,x);

    list_in.close();
    cout << endl <<"All elements in list: ";
    deleteList(List);
    return 0;

}
