#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list contains a cycle.
 * @list: Pointer to the first node of the linked list.
 *
 * Return: 1 if the linked list has a cycle, 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
