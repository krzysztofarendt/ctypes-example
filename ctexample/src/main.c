#include <stdio.h>
#include "fun.h"


// Example program showing how the function fun() works
int main() {

    struct Obj inp;
    inp.x[0] = 1;
    inp.x[1] = 5;
    inp.x[2] = 10;
    inp.y = 0;

    fun(&inp);

    printf("y = %d\n", inp.y);

    return 0;
}
