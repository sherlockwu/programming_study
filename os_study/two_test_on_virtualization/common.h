#ifndef __common_h__
#define __common_h__

# include <sys/time.h>

double current_time(){
    // get time
    struct timeval t;

    gettimeofday(&t, NULL);

    // change mode

    return (double)t.tv_sec + (double)t.tv_usec/1e6;
}

void Spin(int time){
    // TODO realize a downcount clock
    double t = current_time();
    while (current_time() - t < (double)time){
        ;
    }
    return;
}

#endif
