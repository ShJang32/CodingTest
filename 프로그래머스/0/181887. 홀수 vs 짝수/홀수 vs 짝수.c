#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int answer = 0;
    int i, j;
    int sum_even = 0;
    int sum_odd = 0;
    
    for(i=0; i < num_list_len; i++) {
        if (i % 2 == 0)
            sum_odd += num_list[i];
        else
            sum_even += num_list[i];
    }
    answer = sum_odd >= sum_even ? sum_odd : sum_even;
    return answer;
}