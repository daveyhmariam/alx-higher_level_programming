#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a node in sorted list
 * @head: address of entry to linked list
 * @number: element to be inserted
 * Return: address of the new node or NULL on failure
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *newhead;

	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	newhead = *head;
	if (new->next == NULL)
	{
		*head = new;
		return (new);
	}
	if (new->n < newhead->n)
	{
		new->next = newhead;
		*head = new;
		return (new);
	}
	if (newhead->n > new->n)
	{
		new->next = newhead;

		return (new);
	}
	while (newhead->next != NULL)
	{
		if ((newhead->next)->n > new->n)
		{
			new->next = newhead->next;
			newhead->next = new;
			return (new);
		}
			newhead = newhead->next;
		}
	newhead->next = new;
	return (new);
}
