import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class bj10828 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Deque<Integer> stack = new ArrayDeque<>();

        int count = scanner.nextInt();
        scanner.nextLine();
        for (int i = 0; i < count; i++) {
            String orders = scanner.nextLine();
            if (orders.contains("push")) {
                String[] ordersArray = orders.split(" ");
                int num = Integer.parseInt(ordersArray[1]);
                stack.push(num);
            } else if (orders.contains("pop")) {
                if (!stack.isEmpty()) {
                    System.out.println(stack.peek());
                    stack.pop();
                } else {
                    System.out.println(-1);
                }
            } else if (orders.contains("size")) {
                System.out.println(stack.size());
            } else if (orders.contains("empty")) {
                if (!stack.isEmpty()) {
                    System.out.println(0);
                } else {
                    System.out.println(1);
                }
            } else if (orders.contains("top")) {
                if (!stack.isEmpty()) {
                    System.out.println(stack.peek());
                } else {
                    System.out.println(-1);
                }
            } else {
                System.out.println("잘못 입력하셨습니다");
            }
        }
    }
}
