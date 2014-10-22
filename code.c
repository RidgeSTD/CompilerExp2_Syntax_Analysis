// int main(){
// int a = 10;
// float b = 10.89;
// int my_var = 89;
// double _my_double1 = 16.78;
// for(int i=0;i<10;i++) {
//     i += 10;
// }
// char *a = "Hello;"
// int c =10;
// while(c--) {
//     a /= (b - c) * 2;
//     a++;
//     b--;
//     if(a>1){
//         if(b<2){
//             a=123;
//         }
            
//     }
    
    
// }

// if (a != b) {
//    c = a + b//there is an error here, which ; is missing
// }
// }
int Add(int x, int y){
    return x+y;
}

int main(){
    int x,y,z;
    x=1;
    y=3;
    while(x<=y){
        if (x==y){
            z=Add(x,y);
        }
        else{
            z=y-x;
        }
    }
    return 0;
}