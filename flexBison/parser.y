%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

%union {
    char *string;
    int integer;
}

/* Structure to store task information */
typedef struct {
    char *name;
    int time;
} Task;

Task tasks[100]; // Assuming a maximum of 100 tasks
int numTasks = 0;
int timeSpentToday = 0; // Variable to keep track of time spent during the day

/* Function to find task by name */
Task* findTaskByName(const char *name) {
    for (int i = 0; i < numTasks; ++i) {
        if (strcmp(tasks[i].name, name) == 0) {
            return &tasks[i];
        }
    }
    return NULL;
}

extern int yylex();
void yyerror(const char *s);

/* Function to handle HABLAR */
void HABLAR(const char *format, ...) {
    va_list args;
    va_start(args, format);
    vprintf(format, args);
    va_end(args);
    /* Consume time from the day's time counter */
    int hablarTime;
    sscanf(format, "%*[^,],%d", &hablarTime); // Extract time from the format string
    timeSpentToday += hablarTime;
    if (timeSpentToday > 24 * 60) { // Ensure time spent during the day does not exceed 24 hours
        yyerror("Time exceeds 24 hours in a day");
    }
}
%}

%token <string> STRING
%token <integer> NUMBER
%token HORA_DE_BRILHAR A_MIMIR SEMPRE_DIVA GRUNIDO ENQUANTO_ELA_NAO_MUDA_DE_IDEIA SE
%token TAREFA_DECLARATION ACAO_DECLARATION

%%

program: blocks
       ;

blocks: blocks block
      | block
      ;

block: HORA_DE_BRILHAR '\n' days SEMPRE_DIVA
      ;

days: days day
    | day
    ;

day: GRUNIDO '\n' { timeSpentToday = 0; } statements A_MIMIR
    ;

statements: statements statement
          | statement
          ;

statement: "λ"
         | TASK_DECLARATION
         | ACTION_DECLARATION
         | WHILE_STATEMENT
         | IF_STATEMENT
         /* Removed HABLAR_STATEMENT */
         ;

TASK_DECLARATION: TAREFA_DECLARATION '(' STRING ',' NUMBER ')' '\n'
                 {
                     /* Store task information */
                     tasks[numTasks].name = strdup($3);
                     tasks[numTasks].time = $5;
                     numTasks++;
                     /* Deduct time from the day's time counter */
                     timeSpentToday += $5;
                     if (timeSpentToday > 24 * 60) { // Ensure time spent during the day does not exceed 24 hours
                         yyerror("Time exceeds 24 hours in a day");
                     }
                 }
                 ;

ACTION_DECLARATION: ACAO_DECLARATION '(' STRING ',' NUMBER ')' '\n'
                   {
                       /* Deduct time from the day's time counter */
                       timeSpentToday += $5;
                       if (timeSpentToday > 24 * 60) { // Ensure time spent during the day does not exceed 24 hours
                           yyerror("Time exceeds 24 hours in a day");
                       }
                   }
                   ;

WHILE_STATEMENT: ENQUANTO_ELA_NAO_MUDA_DE_IDEIA CONDICIONAL ':' statement '\n'
                {
                    Task *task = findTaskByName($<string>3);
                    while (task && task->time >= $<integer>5) {
                        /* Deduct time from the day's time counter */
                        timeSpentToday += task->time;
                        if (timeSpentToday > 24 * 60) { // Ensure time spent during the day does not exceed 24 hours
                            yyerror("Time exceeds 24 hours in a day");
                        }
                        /* Your semantic actions for while statement */
                        $<integer>5 -= task->time; // Reduce the time spent
                    }
                }
                ;

IF_STATEMENT: SE CONDICIONAL ':' statement '\n'
             {
                 Task *task = findTaskByName($<string>3);
                 if (task && task->time >= $<integer>5) {
                     /* Deduct time from the day's time counter */
                     timeSpentToday += task->time;
                     if (timeSpentToday > 24 * 60) { // Ensure time spent during the day does not exceed 24 hours
                         yyerror("Time exceeds 24 hours in a day");
                     }
                     /* Your semantic actions for if statement */
                 } else {
                     yyerror("Time exceeds task duration");
                 }
             }
             ;

CONDICIONAL: TAREFA_DECLARATION '.' STRING '\n'
           {
               Task *task = findTaskByName($3);
               if (!task) {
                   yyerror("Task not found");
               }
               /* Your semantic actions for conditional */
           }
           ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}
