#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashtable/hashtable.h"

//gcc bigboi.c hashtable/hashtable.c

#define TABLE_SZ 65536 * 32

typedef struct line_t {
        list_head_t HEAD;
} line_t;


size_t file_get_size(char *path)
{
    FILE *fd = fopen(path, "r");
    if (fd == NULL) return -1;
    fseek(fd, 0L, SEEK_END);
    size_t ret = ftell(fd);
    fclose(fd);
    return ret;
}


int str_count(char* string, const char* substr)  //optimized
{
	int count = 0;
	int sublen = strlen(substr);
	int len = strlen(string);
	for (int i = 0; i < len; i += sublen) {
		string = strstr(string, substr);
		if (string) count++;
		else break;
		string += sublen;
	}
	return count;
}


char **str_split(char *stringf, const char *delim, int *refOcc)  //refOcc = number of segments
{
	int len_prev, index;
	len_prev = index = 0;
	const int delim_size = strlen(delim);

	char *string = strdup(stringf);  //duplicate stringf to mutable array
	char *string_org = string;  //remember org pointer to free() later to avoid mem leak
	
	//strip trailing delimiters, gotta leave at least 1
	//strip_trailing(string, delim);

	int count = str_count(string, delim);
	if (count == 0) {  //no delimiters found
		*refOcc = 0;
		return NULL;
	}
	*refOcc = count + 1;

	char **ret = (char**)malloc((count+1) * sizeof(char*));

	for (int i = 0; i <= count; i++) {
		char *next = strstr(string, delim);
		len_prev = next - string;
		
		if (i == count) len_prev = strlen(string);  //last segment

		//put value in respective array element
		ret[index] = (char*)malloc(len_prev + 1);
		memcpy(ret[index], string, len_prev);
		ret[index][len_prev] = '\0';

		//advance pointer pos to current delimiter
		string += len_prev + delim_size;
		index++;
	}

	free(string_org);
	return ret;
}

char **file_read_to_array(char *path, int *line_count)
{
    size_t sz = file_get_size(path);
    FILE *fd = fopen(path, "r");
    if (fd == NULL) {
        *line_count = -1;
        return NULL;
    }
    
    char* buf = (char*)malloc(sz);
    fread(buf, sz, 1, fd);

    char **lines = str_split(buf, "\n", line_count);
    
    if (*line_count == 0) { //There's only 1 line
        lines = malloc(sizeof(char*));
        lines[0] = malloc(sz + 1);
        strcpy(lines[0], buf);
        *line_count += 1;
    }
    
    free(buf);

    return lines;
}


int mem_cmp(char *s1, char *s2, int len)
{
        int ret = 0;
        for (int i = 0; i < len; i++) {
                if (s1[i] != s2[i]) ret++;
                if (ret > 1) break;
        }
        return ret;
}

/*Remove some character in the middle of a string*/
char *chr_remove(char *str, int pos, int len) //input len
{
        char *ret = malloc(len + 1);
        strncpy(ret, str, len);
        ret[pos] = '_';

        return ret;
}

list_head_t *new_line(char *string)
{
        list_head_t *ret = malloc(sizeof(list_head_t));
        ret->key = string;
        ret->next = NULL;
        return ret;
}


int main()
{
        int line_count = 0;
        char **lines = file_read_to_array("bigboi.in", &line_count);

        int diff = 0;
        int LEN = strlen(lines[0]);

        void **T = table_create(TABLE_SZ);
        for (int i = 0; i < line_count; i++) { //iterate through lines
                for (int c = 0; c < LEN; c++) { //iterate through characters in line
                        char *a = chr_remove(lines[i], c, LEN);
                        if (table_find(T, TABLE_SZ, a) == NULL) {
                                list_head_t *line = new_line(a);
                                table_add(T, TABLE_SZ, line);
                        }
                        else {
                                printf("Part 2:%s\n", a); //found the correct box
                                return 0;
                        }
                }
        }
        table_destroy(T, TABLE_SZ, NULL); //function to free up string here

        return 0;
}