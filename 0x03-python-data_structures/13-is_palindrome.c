#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *first_half;
	listint_t *second_half_reversed;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = slow;
	second_half_reversed = reverse_list(second_half);

	first_half = *head;
	while (second_half_reversed != NULL)
	{
		if (first_half->n != second_half_reversed->n)
		{
			result = 0;
			break;
		}
		first_half = first_half->next;
		second_half_reversed = second_half_reversed->next;
	}

	reverse_list(second_half);

	return (result);
}
