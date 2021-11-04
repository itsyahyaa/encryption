//Simple C program to encrypt and decrypt a string

#include <stdio.h>

int main()
{
   int i,j,a;
   char str[100];

   printf("\nPlease enter a string:\t");
   gets(str);
   printf("\nPlease enter a key:\t");
   scanf("%d",&a);
   
    if(strlen(str) > 0){
      for(i = 0; (i < 100 && str[i] != '\0'); i++)
        str[i] = str[i] + a; //the key for encryption is key that is added to ASCII value

      printf("\nEncrypted string: %s\n", str);
      for(j = 0; (j < 100 && str[j] != '\0'); j++)
        str[j] = str[j] - a; //the key for encryption is key that is subtracted to ASCII value

      printf("\nDecrypted string: %s\n", str);
    }
    else{
        printf("\nEnter Valid String\n");
        
    }
  
    return 0;
}