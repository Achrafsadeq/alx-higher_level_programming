#include "lists.h"

/**
 * reverse_listint - Reverses the order of nodes in a linked list.
 * @head: Address of the pointer to the head node of the list.
 *
 * This function iterates through the linked list, reversing the direction
 * of each node's pointer so that the list is reversed. The new head of the
 * list is pointed to by the original tail of the list.
 *
 * Return: The pointer to the new head of the reversed list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current_node = *head;
	listint_t *next_node = NULL;

	while (current_node)
	{
		next_node = current_node->next;
		current_node->next = previous;
		previous = current_node;
		current_node = next_node;
	}

	*head = previous;
}

/**
 * is_palindrome - Determines if a linked list is a palindrome.
 * @head: Pointer to the pointer of the head node in the list.
 *
 * This function checks if the sequence of values in the linked list reads
 * the same forwards and backwards. It uses a two-pointer technique to 
 * find the middle of the list, reverses the second half, and compares it
 * with the first half to verify if it is a palindrome.
 *
 * Return: 1 if the list is a palindrome, otherwise 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_pointer = *head, *fast_pointer = *head, *temp_pointer = *head, *duplicate = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_pointer = fast_pointer->next->next;
		if (!fast_pointer)
		{
			duplicate = slow_pointer->next;
			break;
		}
		if (!fast_pointer->next)
		{
			duplicate = slow_pointer->next->next;
			break;
		}
		slow_pointer = slow_pointer->next;
	}

	reverse_listint(&duplicate);

	while (duplicate && temp_pointer)
	{
		if (temp_pointer->n == duplicate->n)
		{
			duplicate = duplicate->next;
			temp_pointer = temp_pointer->next;
		}
		else
			return (0);
	}

	if (!duplicate)
		return (1);

	return (0);
}
