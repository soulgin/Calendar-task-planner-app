#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TASK_LENGTH 100

typedef struct {
    char tasks[31][MAX_TASK_LENGTH];
} Month;

void add_task(Month* month, int day, const char* task) {
    if (day < 1 || day > 31) {
        printf("Invalid day!\n");
        return;
    }
    strncpy(month->tasks[day - 1], task, MAX_TASK_LENGTH - 1);
    month->tasks[day - 1][MAX_TASK_LENGTH - 1] = '\0';
    printf("Task added for day %d.\n", day);
}

void view_tasks(Month* month, int day) {
    if (day < 1 || day > 31) {
        printf("Invalid day!\n");
        return;
    }
    if (month->tasks[day - 1][0] != '\0') {
        printf("Tasks for day %d: %s\n", day, month->tasks[day - 1]);
    } else {
        printf("No tasks found for day %d.\n", day);
    }
}

void save_tasks(Month* month, const char* filename) {
    FILE* file = fopen(filename, "w");
    if (!file) {
        printf("Error opening file for saving!\n");
        return;
    }
    for (int i = 0; i < 31; i++) {
        if (month->tasks[i][0] != '\0') {
            fprintf(file, "%d,%s\n", i + 1, month->tasks[i]);
        }
    }
    fclose(file);
    printf("Tasks saved to %s.\n", filename);
}

void load_tasks(Month* month, const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        printf("Error opening file for loading!\n");
        return;
    }
    int day;
    char task[MAX_TASK_LENGTH];
    while (fscanf(file, "%d,%[^\n]", &day, task) != EOF) {
        strncpy(month->tasks[day - 1], task, MAX_TASK_LENGTH - 1);
        month->tasks[day - 1][MAX_TASK_LENGTH - 1] = '\0';
    }
    fclose(file);
    printf("Tasks loaded from %s.\n", filename);
}

int main() {
    Month month = {0};
    while (1) {
        printf("\nMenu:\n1. Add Task\n2. View Tasks\n3. Save Tasks\n4. Load Tasks\n0. Exit\n");
        int choice, day;
        char task[MAX_TASK_LENGTH], filename[50];
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter day (1-31): ");
                scanf("%d", &day);
                printf("Enter task: ");
                scanf(" %[^\n]", task);
                add_task(&month, day, task);
                break;
            case 2:
                printf("Enter day (1-31): ");
                scanf("%d", &day);
                view_tasks(&month, day);
                break;
            case 3:
                printf("Enter filename: ");
                scanf("%s", filename);
                save_tasks(&month, filename);
                break;
            case 4:
                printf("Enter filename: ");
                scanf("%s", filename);
                load_tasks(&month, filename);
                break;
            case 0:
                exit(0);
            default:
                printf("Invalid choice.\n");
        }
    }
    return 0;
}
