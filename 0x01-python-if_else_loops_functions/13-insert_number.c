#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 * insert_node - Function that Inserts a number into a sorted list
 * @head: Pointer the head of the linked list.
 * @number: Number to insert.
 *
 * Return: A pointer to the new head.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->i = number;

        if (node == NULL || node->i >= number)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        while (node && node->next && node->next->i < number)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}
