import java.util.*;
class Main{
    static String[] letters = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
    static String[] numbers = {"-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."};
    static Set<String> possible = new HashSet<String>();
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String coded = in.next();
        pain(coded);
        in.close();
    }
    public static boolean pain(String coded){
        if(coded.length() == 0){
            return true;
        }else{
            //TODO: loop through letters and numbers, then do recursive calls to find stuff and hope DFS is
        }
        return false;
    }
}