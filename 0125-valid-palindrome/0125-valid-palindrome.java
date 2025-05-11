class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder str = new StringBuilder();

        for(char a : s.toCharArray()){
            if (Character.isLetterOrDigit(a)){
                str.append(Character.toLowerCase(a));
            }
        }
        String r = str.toString();
        int n = r.length();
        for (int i=0; i< n/2; i++){
            if(r.charAt(i) != r.charAt(n-i-1)){
                return false;
            }
        }

        return true;

    }
}