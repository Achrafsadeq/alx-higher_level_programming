#include "lists.h"

listint_t *insert_node(listint_t **head, int number);

/**
 * insert_node - Adds a new element to a sorted singly-linked list.
 * @head: Pointer to the pointer pointing to the head of the list.
 * @number: The integer value to be inserted into the list.
 *
 * This function inserts a new node containing the given number into the
 * appropriate position within a list that is already
 * sorted in ascending order.
 *
 * Return: On success, returns a pointer to the newly created node.
 *         On failure (e.g., memory allocation error), returns NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
