#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;


    printf("-----------------\n");

    insert_node(&head, 27);

    print_listint(head);



    printf("-----------------\n");

    insert_node(&head, -2);
    insert_node(&head, 98);
    insert_node(&head, 98);
    insert_node(&head, -2);
    insert_node(&head, -8);

    print_listint(head);




    free_listint(head);

    return (0);
}