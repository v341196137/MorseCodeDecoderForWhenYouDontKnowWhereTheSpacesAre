import java.util.*;
class Main{
    static String[] letters = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
    static String[] numbers = {"-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."};
    static ArrayList<String> possible = new ArrayList<String>();
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter some valid Morse code without spaces:");
        String coded = in.next();
        for(int i = 0;i < coded.length();i++){
            if(coded.charAt(i) != '.' && coded.charAt(i) != '-'){
                System.out.println("Invalid Morse Code");
                System.exit(0);
            }
        }
        pain(coded, "");
        in.close();
        Collections.sort(possible);
        for(String s:possible){
            System.out.println(s);
        }
    }
    public static boolean pain(String coded, String curString){
        if(coded.length() == 0){
            possible.add(curString);
            return true;
        }else{
            boolean thing = false;
            for(int i = 0; i < letters.length;i++){
                if((letters[i].length() <= coded.length()) && (coded.substring(0, letters[i].length()).equals(letters[i]))){
                    thing = pain(coded.substring(letters[i].length()), curString + (char)(i + 'A'));
                }
            }
            for(int i = 0; i < numbers.length;i++){
                if((numbers[i].length() <= coded.length()) && (coded.substring(0, numbers[i].length()).equals(numbers[i]))){
                    thing = pain(coded.substring(numbers[i].length()), curString + (char)(i + '0'));
                }
            }
            return thing;
        }
    }
}