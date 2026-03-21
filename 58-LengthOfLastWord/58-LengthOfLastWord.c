// Last updated: 3/22/2026, 12:46:04 AM
int lengthOfLastWord(char* s) {
    int max=0;
    int cur=0;
    char sp = ' ';
    for(long i=0;s[i]!='\0';i++){
        if(s[i]==sp){
            if(cur>0) max=cur;
            cur=0;
        }else cur++;
    }
    if(cur > 0) max=cur;
    return max;
}