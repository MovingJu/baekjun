#include <iostream>

int main(){

    int user;

    std::cin >> user;

    if(user == 1){
        std::cout << 4;
        return 0;
    }
    if(user == 2){
        std::cout << 6;
        return 0;
    }

    long long n1, n2, n3;

    n1 = 1;
    n2 = 1;
    n3 = 2;

    for(int i = 4; i<user+1; i++){
        if (i%3 == 1){
            n1 = n2 + n3;
        }
        else if(i%3 == 2){
            n2 = n1 + n3;
        }
        else{
            n3 = n1 + n2;
        }
    }

    if (user%3 == 1){
        std::cout << 2*(n1 + n3 + n3 + n2);
        return 0;
    }
    else if(user%3 == 2){
        std::cout << 2*(n2 + n1 + n1 + n3);
        return 0;
    }
    else{
        std::cout << 2*(n3 + n2 + n2 + n1);
        return 0;
    }

    return 0;
}