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
    while(currentNode != NULL && currentNode->val != x)
        currentNode = currentNode ->next;
    return currentNode;
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

int main(){
    FILE *in = fopen("data.txt", "r");
    int x;
    struct list *List = NULL;
    while (fscanf(in, "%d", &x) != EOF)
        List = insert(List, x);
    fclose(in);
    printf("The biggest element: %d \n", max(List));
    printf("Right child of 17 is %d \n", search(List,17)->next->val);
    printf("All elements: ");
    show(List);
    deleteList(List);
}
