#include <stdio.h>
#include <stdlib.h>


struct list{
    int val;
    struct list *next;
};

struct list *insert(struct list *firstNode, int x) {

    struct list *newNode = (struct list*)malloc(sizeof(struct list));
    newNode->val = x;
    newNode->next = NULL;
    if(!firstNode)
        return newNode;
    else if (firstNode->val > x)
    {
        newNode->next = firstNode;
        return newNode;
    } else {
        struct list *currentNode = firstNode;
        struct list *nextNode = firstNode->next;
        while (nextNode != NULL && nextNode->val < x) {
            currentNode = nextNode;
            nextNode = nextNode->next;
        }
        newNode->next = nextNode;
        currentNode->next = newNode;
        return firstNode;
    }

}

struct list *search(struct list *firstNode, int x) {
    struct list *currentNode = firstNode;
    while(currentNode->val < x && currentNode->next != NULL )
        currentNode = currentNode ->next;
    if (currentNode->val == x)
        return currentNode;
    else
        return NULL;
}

void show(struct list *firstNode) {
    struct list *currentNode = firstNode;
    while(currentNode != NULL)
    {
        printf("%d  ",currentNode->val);
        currentNode = currentNode ->next;
    }
}

int max (struct list *firstNode) {

    struct list *currentNode = firstNode;
    while(currentNode->next != NULL )
        currentNode = currentNode ->next;
    return currentNode->val;
}

void deleteList(struct list *firstNode) {
    struct list *currentNode = firstNode;
    while(currentNode != NULL)
    {
        firstNode = currentNode -> next;
        free(currentNode);
        currentNode = firstNode;
    }
}

int length (struct list* node){
    if(node == NULL)
        return 0;
    else
        return length(node->next) + 1;
}

int main(){
    FILE *in = fopen("data.txt", "r");
    int x;
    struct list *List = NULL;
    while (fscanf(in, "%d", &x) != EOF)
        List = insert(List, x);
    fclose(in);
    printf("The biggest element: %d \n", max(List));
    printf("Next value after 21 is %d \n", search(List,21)->next->val);
    printf("Length of list is %d \n", length(List));
    printf("All elements: ");
    show(List);
    deleteList(List);
}
