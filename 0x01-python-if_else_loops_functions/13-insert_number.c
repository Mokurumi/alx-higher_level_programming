#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted singly linked list
 *
 * @head: pointer to the first node of the list
 * @number: number to insert
 *
 * Return: The address of the new node
 * or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	/* Create a new node */
	listint_t *current, *new_node = malloc(sizeof(listint_t));
	
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	/* If the list is empty or the new node should be the new head */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Find the appropriate position to insert the new node */
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	/* Insert the new node */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
