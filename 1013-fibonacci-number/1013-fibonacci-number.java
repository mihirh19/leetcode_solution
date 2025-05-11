class Solution {
    public int fib(int n) {
       return getNthFib(n);
    }
    public int getNthFib(int n){
        if (n==0 || n==1){
            return n;
        }

        return getNthFib(n-1) + getNthFib(n-2);
    }
}