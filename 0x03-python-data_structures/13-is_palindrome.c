#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *newhead, *reversed, *tmp;
	if (*head == NULL || head == NULL)
		return (1);
	reversed = *head;
	newhead = *head;
	tmp = reversed;
	tmp->next = NULL;
	while (reversed->next)
	{
		reversed = reversed->next;
		reversed->next = tmp;
		tmp = reversed;
	}
	while (reversed && newhead)
	{
		if (reversed->n != newhead->n)
			return (0);
		reversed = reversed->next;
		newhead = newhead->next;
	}
	return (1);
}
