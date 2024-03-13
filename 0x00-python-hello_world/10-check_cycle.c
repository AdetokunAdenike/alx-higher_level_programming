#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 otherwise.
 */
typedef struct listint_s {
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list) {
	listint_t *slow_ptr = list, *fast_ptr = list;

	while (slow_ptr && fast_ptr && fast_ptr->next) {
	slow_ptr = slow_ptr->next;
	fast_ptr = fast_ptr->next->next;

	if (slow_ptr == fast_ptr)
		return (1);
	}

	return (0);
