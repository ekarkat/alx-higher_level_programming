#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if the list is_palindrome
 * @head: list head
 * Return: return 1 if is_palindrome otherwise 0
*/

int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *temp = *head;
	int ln = 0, i = 0, j = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (temp != NULL)
	{
		temp = temp->next;
		ln++;
	}
	while (i < (ln / 2))
	{
		listint_t *last = *head;

		for (j = 0; j < ln - i - 1; j++)
			last = last->next;
		if (first->n == last->n)
			first = first->next;
		else
			return (0);
		i++;
	}
	return (1);
}
