# c언어로 작성

#include <stdio.h>
 
# int main() {
#   int a, b, c;
#   scanf("%d %d", &a, &b);
#   c = (a++)*(--b);
#   printf("%d %d %d\n", a, b, c);
#   return 0;
# }