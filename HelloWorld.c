#include "cs50.h"
#include <stdio.h>

int main(void)
{
    string storage_text = get_string("Hello World, tell your name? ");
    printf("Nice to meet ya %s\n", storage_text);
}