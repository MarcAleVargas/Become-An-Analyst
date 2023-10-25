#include <stdio.h>

int main(void)
{
    FILE *file = fopen("Introducing Power BI.pdf", "r");
    if (file != NULL)
    {
        fprintf(file, "This is CS50\n");
        fclose(file);
    }
}