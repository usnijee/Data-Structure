import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.Scanner;

public class bj1158 {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<>();
        List<String> newArray = new ArrayList<>();
        String output;

        String[] input = scanner.nextLine().split(" ");
        int count = Integer.parseInt(input[0]);
        int index = Integer.parseInt(input[1]);

        for (int i = 1; i <= count ; i++) {
            deque.add(i);
        }

        while (true) {
            if (deque.isEmpty()) {
                output = String.format("<" + String.join(", ", newArray) + ">");
                break;
            }
            for (int i = 0; i < index; i++) {
                if (i == index-1) {
                    newArray.add(String.valueOf(deque.peek()));
                    deque.pollFirst();
                }else {
                    Integer e = deque.pollFirst();
                    deque.offerLast(e);
                }
            }
        }
        System.out.println(output);



    }
}
