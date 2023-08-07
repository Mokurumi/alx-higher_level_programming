#include "lists.h"

/**
 * check_cycle - finds the loop in a linked list.
 *
 * @list: pointer to the list node of the linked list.
 *
 * Return: 1 if there is a loop,
 *         or 0 if there is no loop.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			hare = list;

			while (hare != tortoise)
			{
				hare = hare->next;
				tortoise = tortoise->next;
			}

			return (1);
		}
	}

	return (0);
}
