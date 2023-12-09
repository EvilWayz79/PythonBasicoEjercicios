void fizzBuzz(int n) {
    n = 15;
    for(int i = 1; i < n; i++)
    {
        char fizz[4] = "Fizz";
        char buzz[4] = "Buzz";
        char printVal[8];
        
        printVal[0] = i;
        
        if(i%3 == 0 && i%5 == 0)
        {
            strcpy(printVal, strcat(fizz, buzz));
        }
        if(i%3 == 0)
        {
            strcpy(printVal, fizz);
        }
        if(i%5 == 0)
        {
            strcpy(printVal, buzz);
        }
        
        printf(printVal);
    }
}