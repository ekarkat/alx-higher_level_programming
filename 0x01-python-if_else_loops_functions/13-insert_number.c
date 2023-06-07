#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head;
	listint_t *new;

	if (head == NULL)
	{	
		new = add_nodeint_end(head, 972);
		return (new);
	}
	if (number <= h->n)
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = h;
		*head = new;
		return (new);			
	}
	while (h != NULL && h->next != NULL)
	{
		if (number >= h->n && number < h->next->n)
		{
			new = malloc(sizeof(listint_t));
			new->n = number;
			new->next = h->next;
			h->next = new;
			return (new);
		}
		h = h->next;
	}
	new = add_nodeint_end(head, number);
	return (new);
}