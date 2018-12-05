#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void react(char *data, int len);
void chr_search_rm(char *data, char c);

void main()
{
    char data[65536] = "";
    FILE *fd = fopen("D:\\input.txt", "r");
    fread(data, 1, sizeof(data), fd);
    fclose(fd);
    int len = strlen(data);
    react(data, len);
    printf("PART 1: %d\n", strlen(data));

    char *old_data = strdup(data);
    int min = INT_MAX;
    for (int i = 0; i < 122 - 97 + 1; i++) {
        chr_search_rm(data, 97 + i);
        react(data, strlen(data));
        if (strlen(data) < min) min = strlen(data);
        strcpy(data, old_data);
    }
    printf("PART 2: %d\n", min);

}


int is_opposite(char c1, char c2)
{
    if (c1 == '\0' || c2 == '\0') return 0;
    return (tolower(c1) == tolower(c2) && c2 != c1);
}


void word_remove(char *data, int pos, int len)
{
    char tail[65536] = "";
    strcpy(tail, data + pos + len);
    strcpy(data + pos, tail);
}


void chr_search_rm(char *data, char c)
{
    int i = 0;
    for (; data[i]; i++) {
        if (tolower(data[i]) == c) {
            word_remove(data, i, 1);
            i--;
        }
    }
}


void react(char *data, int len)
{
    int i = 0;
    for (; i < len; i++) {
        if (is_opposite(data[i], data[i+1])) {
            word_remove(data, i, 2);
            len -= 2;
            i -= 2;
        }
    }

}