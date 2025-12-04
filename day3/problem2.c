#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <time.h>

#define MAX_LINE_LENGTH 1024
#define NUM_BATTS 12

long long largest_joltage(int *bank, int bank_len) {
    long long joltage = 0;
    int ibs = -1;
    
    for (int bat = 0; bat < NUM_BATTS; bat++) {
        int start = ibs + 1;
        int end = (bat == NUM_BATTS - 1) ? bank_len : bank_len - (NUM_BATTS - 1 - bat);
        
        // Find max in range [start, end)
        int max_val = INT_MIN;
        int max_idx = start;
        for (int i = start; i < end; i++) {
            if (bank[i] > max_val) {
                max_val = bank[i];
                max_idx = i;
            }
        }
        
        joltage = joltage*10 + max_val;
        ibs = max_idx;
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