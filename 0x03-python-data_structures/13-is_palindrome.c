#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *newhead, *reversed, *tmp, *prev, *fast, *slow;
	if (*head == NULL || head == NULL)
		return (1);
	newhead = *head;
	fast = *head;
	slow = *head;
	prev = NULL;
	while (1)
	{
		if (fast->next)
			fast = fast->next->next;
		if (!fast)
		{
			break;
		}
		slow = slow->next;
		
	}

	reversed = slow->next;
	prev = NULL;
	slow->next = NULL;
	while (reversed)
	{
		tmp = reversed->next;
		reversed->next = prev;
		prev = reversed;
		reversed = tmp;
	}
	reversed = prev;
	while (reversed)
	{
		if (reversed->n != newhead->n)
			return (0);
		reversed = reversed->next;
		newhead = newhead->next;
	}
	return (1);
}
