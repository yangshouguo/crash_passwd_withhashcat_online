/*************************************************************************
	> File Name: my_encrypt.c
	> Author:yangshouguo 
	> Mail: 
	> Created Time: 2017年08月19日 星期六 10时33分44秒

    该程序可以通过输入 加盐后的哈希串 （例如shadow文件中的hash） 和 字典文件名，
    暴力破解密码
 ************************************************************************/

#include<stdio.h>
#include <string.h>
#include<unistd.h>
#include<stdlib.h>
#define _XOPEN_SOURCE


char salt[20];
char *  get_salt_hash_splited(char * hashstring){
    int string_len = strlen(hashstring);
    int num = 0 , i;
    for (i=0 ; i < string_len ;++i){
        if(hashstring[i] == '$')
            num++;
        if(num >=3)
            break;
    }
    num = i+1;
    strncpy(salt , hashstring , i+1);
    return salt;
}

void print_help(){
    char *x = "please use this command as : my_encrypt 'hashstring'(salt+hashvalue) dic_file";
    char y[] = "./myencrypt '$6$9WbBd61T$bGOeNO09qbTDxsLLghNqoKPRlA.BzZQVOwvCs7CtfhX5y/lP8BHcgC8YO8W.RH4L9dpYA1' 1.dic ";
    printf("%s\n %s\n",x,y);
}


int is_right_passwd(char * salt ,char * pass_text , char * wholepass){
    char *passwd ;
    passwd = (crypt(pass_text,salt));
    //printf("%s with salt: %s get %s \n",pass_text , salt , passwd);
    if(!strcmp(wholepass , passwd)){
        return 1;
    }
    return 0;
}

int main(int argc ,char* argv[]){

    char hashstring[100] , * filename ;
    char *salt ;
    FILE *fp;
    int i , j;
    char pass_text[50];
    if (argc < 2){//parameters not enough
        print_help();
        return 1;
    }

    strcpy(hashstring,argv[1]);
    filename = argv[2];
    // printf("hashstring : %s \n , filename = %s \n",hashstring , filename);
    salt = get_salt_hash_splited(hashstring);
    //printf("salt is :%s \n hash is : %s \n ",struct_h.salt , struct_h.phashstring);
    if ((fp = fopen(filename,"r")) == NULL){
        printf("not found dic file");
        return -1;
    }
    while (!feof(fp)){
        fgets(pass_text,50,fp);//read line
        for (i = 0 ; i < strlen(pass_text); ++i){
            if (pass_text[i] < 32){
                pass_text[i] = '\0';
                break;
            }
        }/*
        for (i = 0 ; i < strlen(pass_text); ++i){
            printf("%c%d",pass_text[i],pass_text[i]);
        }*/
        //printf("pass_text_length : %d\n", strlen(pass_text ));
        if(is_right_passwd(salt ,pass_text, hashstring)){
            printf("%s\n",pass_text);
            break;
        }
    }

    return 0;
    

    
}


