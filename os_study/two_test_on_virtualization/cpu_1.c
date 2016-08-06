# include<stdio.h>
# include "common.h"

int main(int argc, char ** argv){
    // get the output
    char * c_out;
    c_out = argv[1];

    // print out the output per second
    while(1){
        printf("%s\n", c_out);
        Spin(1);
    }
    return 0;
}

