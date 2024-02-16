#include "fun.h"


void fun(struct Obj *inp) {

    int x_size = sizeof(inp->x) / sizeof(inp->x[0]);

    for (int i=0; i < x_size; i++) {
        inp->y += inp->x[i];
    }
    inp->y /= x_size;

    return;
}
