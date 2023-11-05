#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *newhead, *reversed, *tmp;
	if (*head == NULL || head == NULL)
		return (1);

	newhead = *head;
	reversed = (listint_t *) malloc(sizeof(listint_t));
	if (reversed == NULL)
		return (0);
	reversed->n = newhead->n;
	reversed->next = NULL;
	while (newhead->next != NULL)
	{
		newhead = newhead->next;
		tmp = reversed;
		reversed = (listint_t *) malloc(sizeof(listint_t));
		if (reversed == NULL)
			return (0);
		reversed->n = newhead->n;
		reversed->next = tmp;
	}

	newhead = *head;
	while(reversed != NULL && newhead != NULL)
	{
		if (reversed->n != newhead->n)
			return (0);
		reversed = reversed->next;
		newhead = newhead->next;
	}
	return (1);
}
