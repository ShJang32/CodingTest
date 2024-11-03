#include <stdio.h>
#define LEN_INPUT 10

int main(void) {
    char s1[LEN_INPUT];
    int a;
    scanf("%s", s1);
    
    for (int i = 0; i < strlen(s1); i++) {
        if ('A' <= s1[i] && s1[i] <= 'Z') { // 소문자 변환
            s1[i] = s1[i] + 32;
        } else if ('a' <= s1[i] && s1[i] <= 'z') {
            s1[i] = s1[i] - 32;
        }
    }
    printf("%s", s1);
    
    return 0;
}
