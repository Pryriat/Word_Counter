#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//flag{AD_Simple_Reverse}
//unsigned int flag[] = {102,108,97,103,123,65,68,95,83,105,109,112,108,101,95,82,101,118,101,114,115,101,125}
//Caser Type Encrypt
/*flag{AD_Simple_Reverse}
unsigned int flag[] = {102,108,97,103,123,65,68,95,83,105,109,112,108,101,95,82,101,118,101,114,115,101,125}
Caser Type Encrypt
*/

int change_word(unsigned char src, unsigned int offset, unsigned char cmp)
{
  if(src >= 'A' && src <= 'Z')
  {
    src += offset;
    if(src > 'Z')
      src -= 26;
    if(src < 'A')
      src += 26;
  }
  else if(src >= 'a' && src <= 'z')
  {
    src += offset;
    if(src > 'z')
      src -= 26;
    if(src < 'a')
      src += 26;
  }
  if(src == cmp)
    return 1;
  return 0;
}
int main()
{
  unsigned char flag[] = {'c','h','v','a','{','S','U','_','H','w','z','b','w','o','_','Z','l','b','j','v','v','g','}'};//flag_ascii
  unsigned int flag_size = sizeof(flag);
  printf("Please run in cmd or powershell\nThere is an encrypted flag: chva{SU_Hwzbwo_Zlbjvvg}\n");
  unsigned char* input_char = (unsigned char*)malloc(256);
  memset(input_char,0,256);
  printf("input your flag:\n");
  scanf("%s",input_char);
  unsigned int input_size = 0;
  unsigned char* tmp = input_char;
  while(*tmp++)
    input_size++;
  if(input_size != flag_size)
  {
    printf("flag length error!");
    return 0;
  }
  for(int x = 0;x<input_size;x++)
  {
    ;
    if(!change_word(input_char[x],input_size-x,flag[x]))
    {
      printf("flag error!");
      return 0;
    }
  }
  printf("Your are right!\nFlag is %s",input_char);
  return 0;
}
