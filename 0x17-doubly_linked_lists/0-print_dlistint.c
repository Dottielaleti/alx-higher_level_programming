#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * dlistint_len -  returns the number of elements in a linked dlistint_t list
 * @h: name of the list
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h);
 const dlistint_t *current = h;
    size_t count = 0;

    while (current != NULL) {
        printf("%d\n", current->n);
        current = current->next;
        count++;
    }

    return count;
}
