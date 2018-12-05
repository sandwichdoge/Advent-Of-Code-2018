#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define INT_MAX 2147483646
#define FSIZE 1024 * 1000 * 2

int react(char *data);
void chr_search_rm(char *out, char *data, char c);


void main()
{
    char *data = calloc(FSIZE, 1);
    FILE *fd = fopen("biginput", "r");
    fread(data, 1, FSIZE, fd);
    fclose(fd);

    int len = react(data);
    printf("PART 1: %d\n", len);
    
    char *old_data = strdup(data);
    char *buf = malloc(FSIZE);
    int min = INT_MAX;
    for (int i = 0; i < 'z' - 'a' + 1; i++) {
        memset(buf, 0, FSIZE);
        chr_search_rm(buf, data, 'a' + i);
        len = react(buf);
        if (len < min) min = len;
    }
    printf("PART 2: %d\n", min);

}


int is_opposite(char c1, char c2)
{
    //if (c1 == '\0' || c2 == '\0') return 0;
    return (tolower(c1) == tolower(c2) && c2 != c1);
}


void chr_search_rm(char *out, char *data, char c)
{
    int n = 0;
    for (int i = 0; data[i]; i++) {
        if (tolower(data[i]) != c) {
            out[n] = data[i];
            n++;
        }
    }
}


void pop(char *stack, int *sp)
{
    (*sp)--;
    stack[*sp] = '\0';
}

void push(char *stack, int *sp, char val)
{
    stack[*sp] = val;
    (*sp)++;
}


int react(char *data)
{
    char *stack = calloc(FSIZE, 1);
    int sp = 0; //stack pointer
    int i = 0;
    for (; data[i]; i++) {
        push(stack, &sp, data[i]);
        while (sp >= 2 && is_opposite(stack[sp - 1], stack[sp - 2])) {
            pop(stack, &sp);
            pop(stack, &sp);
        }
    }

    return strlen(stack);

}