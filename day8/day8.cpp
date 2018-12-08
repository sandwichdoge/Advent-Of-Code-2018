#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int sum = 0;

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

void print_mem(char *data, int sz)
{
        printf("DATA: ");
        for (int i = 0; i < sz; i++) {
                printf("%d ", data[i]);
        }
}

char *fill(char *data)
{
        print_mem(data, 24);
        puts("");
        char children = *data;
        char entries = *(data + 1);
        data += 2;
        for (int i = 0; i < children; i++) {
                data = fill(data);
        }
        for (int i = 0; i < entries; i++) {
                sum += *(data + i);
        }
	data += entries;
        printf("%d %d\n", entries, sum);
        
        return data;
}


int main()
{
        char buf[1024 * 48];
        FILE *fd = fopen("day8.txt", "r");
        fread(buf, sizeof(buf), 1, fd);
        fclose(fd);
        int n;
        char **data = str_split(buf, " ", &n);
        memset(buf, 0, sizeof(buf));
        for (int i = 0; i < n; i++) {
                buf[i] = atoi((const char*)data[i]);
        }

        fill(buf);
        printf("Sum: %d\n", sum);

        return 0;
}