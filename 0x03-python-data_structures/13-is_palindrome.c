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

	while (fast && fast->next && fast->next->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (slow->next == NULL)
		return (1);
	reversed = slow->next;

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
