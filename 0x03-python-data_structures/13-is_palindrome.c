#include "lists.h"

/**
 * reverse_listint - Reverses the sequence of nodes in a linked list.
 * @head: Address of the pointer pointing to the first node in the list.
 *
 * This function reverses the linked list by rearranging the pointers 
 * of each node. After the function completes, the head pointer will 
 * point to what was originally the last node in the list.
 *
 * Return: The pointer to the new head of the reversed linked list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Determines if the linked list is a palindrome.
 * @head: Pointer to the head pointer of the linked list.
 *
 * This function assesses whether the linked list forms a palindrome by 
 * comparing the sequence of values from the start and end. It uses a 
 * two-pointer technique to identify the midpoint, reverses the second 
 * half of the list, and checks if the first half matches the reversed 
 * second half.
 *
 * Return: 1 if the list is a palindrome, otherwise 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}

