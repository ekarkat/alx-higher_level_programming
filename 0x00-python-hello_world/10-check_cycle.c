#include "lists.h"

/**
 * check_cycle - finds the loop in a linked list
 * @head: linked list to search for
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	if (!head)
		return (0);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}

	return (0);
}
