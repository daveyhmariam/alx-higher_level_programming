#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *newhead, *reversed, *tmp, *prev;
	if (*head == NULL || head == NULL)
		return (1);
	reversed = *head;
	newhead = *head;
	prev = NULL;
	while (reversed)
	{
		tmp = reversed->next;
		reversed->next = prev;
		prev = reversed;
		reversed = tmp;
	}
	reversed = prev;
	while (reversed && newhead)
	{
		if (reversed->n != newhead->n)
			return (0);
		reversed = reversed->next;
		newhead = newhead->next;
	}
	return (1);
}
