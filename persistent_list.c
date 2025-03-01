/**
 * Example 1: Persistent vs Non-Persistent List in C
 * Demonstrates the difference between a regular list and a persistent list.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure for a regular list
typedef struct {
    int* values;
    size_t size;
    size_t capacity;
} RegularList;

// Structure for persistent list node
typedef struct {
    int value;
    size_t version;
} PersistentNode;

// Structure for persistent list
typedef struct {
    PersistentNode* values;
    size_t size;
    size_t capacity;
    size_t current_version;
} PersistentList;

// Regular List functions
RegularList* regular_list_create() {
    RegularList* list = (RegularList*)malloc(sizeof(RegularList));
    list->capacity = 10;
    list->size = 0;
    list->values = (int*)malloc(sizeof(int) * list->capacity);
    return list;
}

void regular_list_append(RegularList* list, int value) {
    if (list->size >= list->capacity) {
        list->capacity *= 2;
        list->values = (int*)realloc(list->values, sizeof(int) * list->capacity);
    }
    list->values[list->size++] = value;
}

int* regular_list_get_values(RegularList* list, size_t* out_size) {
    int* copy = (int*)malloc(sizeof(int) * list->size);
    memcpy(copy, list->values, sizeof(int) * list->size);
    *out_size = list->size;
    return copy;
}

void regular_list_free(RegularList* list) {
    free(list->values);
    free(list);
}

// Persistent List functions
PersistentList* persistent_list_create() {
    PersistentList* list = (PersistentList*)malloc(sizeof(PersistentList));
    list->capacity = 10;
    list->size = 0;
    list->current_version = 0;
    list->values = (PersistentNode*)malloc(sizeof(PersistentNode) * list->capacity);
    return list;
}

void persistent_list_append(PersistentList* list, int value) {
    if (list->size >= list->capacity) {
        list->capacity *= 2;
        list->values = (PersistentNode*)realloc(list->values, sizeof(PersistentNode) * list->capacity);
    }
    
    list->current_version++;
    list->values[list->size].value = value;
    list->values[list->size].version = list->current_version;
    list->size++;
}

int* persistent_list_get_version(PersistentList* list, size_t version, size_t* out_size) {
    size_t count = 0;
    // First count how many values we need
    for (size_t i = 0; i < list->size; i++) {
        if (list->values[i].version <= version) {
            count++;
        }
    }
    
    // Allocate and fill the array
    int* result = (int*)malloc(sizeof(int) * count);
    size_t j = 0;
    for (size_t i = 0; i < list->size; i++) {
        if (list->values[i].version <= version) {
            result[j++] = list->values[i].value;
        }
    }
    
    *out_size = count;
    return result;
}

void persistent_list_free(PersistentList* list) {
    free(list->values);
    free(list);
}

// Helper function to print arrays
void print_array(int* arr, size_t size) {
    printf("[");
    for (size_t i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

int main() {
    printf("\n=== List Implementation Comparison ===\n");
    
    // Demo with Regular List
    printf("\nRegular List Demo:\n");
    RegularList* regular_list = regular_list_create();
    regular_list_append(regular_list, 1);
    regular_list_append(regular_list, 2);
    regular_list_append(regular_list, 3);
    
    size_t reg_size;
    int* reg_values = regular_list_get_values(regular_list, &reg_size);
    printf("Values: ");
    print_array(reg_values, reg_size);
    free(reg_values);
    
    // Demo with Persistent List
    printf("\nPersistent List Demo:\n");
    PersistentList* persistent_list = persistent_list_create();
    
    persistent_list_append(persistent_list, 1);  // Version 1
    persistent_list_append(persistent_list, 2);  // Version 2
    persistent_list_append(persistent_list, 3);  // Version 3
    
    size_t size;
    int* values;
    
    // Show different versions
    values = persistent_list_get_version(persistent_list, 1, &size);
    printf("Version 1: ");
    print_array(values, size);
    free(values);
    
    values = persistent_list_get_version(persistent_list, 2, &size);
    printf("Version 2: ");
    print_array(values, size);
    free(values);
    
    values = persistent_list_get_version(persistent_list, 3, &size);
    printf("Version 3: ");
    print_array(values, size);
    free(values);
    
    // Cleanup
    regular_list_free(regular_list);
    persistent_list_free(persistent_list);
    
    return 0;
} 