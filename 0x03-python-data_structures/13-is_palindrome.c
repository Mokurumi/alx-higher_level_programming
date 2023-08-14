#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list.
 *
 * @head: pointer to the head node of the linked list.
 *
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	return (prev);
}

/**
 * is_palindrome - check if it is similar front and back
 *i
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if true or 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *original = *head;
	listint_t *reversed = reverse_listint(head);

	/* Compare the original list with its reversed version */
	while (original != NULL && reversed != NULL)
	{
		if (original->n != reversed->n)
			return (0); /* Not a palindrome */
		
		original = original->next;
		reversed = reversed->next;
	}

	/* If one of the lists is longer than the other */
	if (original != NULL || reversed != NULL)
		return (0); /* Not a palindrome */

	return (1); /* Palindrome */
}
