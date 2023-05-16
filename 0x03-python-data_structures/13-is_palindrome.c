#include "lists.h"
#include <stdlib.h>

/**
 * listint_revs - reverses a linked list
 * @head: pointer to node in list
 * Return: ptr to node in new list
 */
void listint_revs(listint_t **head)
{
	listint_t *_previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = _previous;
		_previous = current;
		current = next;
	}

	*head = _previous;
}

/**
 * is_palindrome - checks linkedlist is palindrome
 * @head: pointer to linkedlist
 *
 * Return: 1 if, or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *quick = *head, *temp = *head, *_daplicate = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		quick = quick->next->next;
		if (!quick)
		{
			_daplicate = slow->next;
			break;
		}
		if (!quick->next)
		{
			_daplicate = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	listint_revs(&_daplicate);

	while (_daplicate && temp)
	{
		if (temp->n == _daplicate->n)
		{
			_daplicate = _daplicate->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!_daplicate)
		return (1);

	return (0);
}
