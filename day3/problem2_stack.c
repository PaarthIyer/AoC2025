#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

#define MAX_LINE_LENGTH 1024
#define NUM_BATTS 12

long long largest_joltage(int *bank, int bank_len) {
    int stack[NUM_BATTS];  
    int stack_top = 0;     
    int can_reject = bank_len - NUM_BATTS;
    
    for (int i = 0; i < bank_len; i++) {
        int bat = bank[i];
        
        while (stack_top > 0 && can_reject > 0 && bat > stack[stack_top - 1]) {
            stack_top--;
            can_reject--;
        }
        
        if (can_reject == 0) {
            int remaining = NUM_BATTS - stack_top;
            for (int j = 0; j < remaining && i + j < bank_len; j++) {
                stack[stack_top + j] = bank[i + j];
            }
            break;
        }
        
        if (stack_top < NUM_BATTS) {
            stack[stack_top] = bat;
            stack_top++;
        } else {
            can_reject--;
        }
    }
    
    long long joltage = 0;
    int final_size = (can_reject > 0) ? stack_top : NUM_BATTS;
    for (int j = 0; j < final_size; j++) {
        joltage = joltage * 10 + stack[j];
    }
    
    return joltage;
}

int main() {
    clock_t start = clock();
    FILE *file = fopen("day3/input.in", "r");
    
    char line[MAX_LINE_LENGTH];
    long long total = 0;
    
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = 0;
        
        int len = strlen(line);
        // Convert string of digits to array of integers
        int *bank = malloc(len * sizeof(int));
        for (int i = 0; i < len; i++) {
            bank[i] = line[i] - '0';
        }
        
        long long joltage = largest_joltage(bank, len);
        total += joltage;
        
        free(bank);
    }
    
    fclose(file);
    
    clock_t end = clock();
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
    
    printf("\nAnswer : %lld\n", total);
    printf("Time: %.6f seconds\n\n", time_spent);
    
    return 0;
}