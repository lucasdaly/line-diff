public int factorial(int number){

    int value = 0;
    System.out.println("Calculate sum of numbers");
    for( int i=2; i<number; i++){
        value = value * i;
    }

    return value;
}