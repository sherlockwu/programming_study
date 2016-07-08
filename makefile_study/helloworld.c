# include <stdio.h>

int main(){
	
	int c_in;

	printf("Program Start: \n");
	
	int count;

	// 循环
	for (count = 0, c_in = getchar(); c_in != EOF; c_in = getchar(), count++  ) {
	}

	printf("\n count: %5d \n", count);
	return 0; 
}