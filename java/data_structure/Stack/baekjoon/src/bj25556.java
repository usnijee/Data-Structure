import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Scanner;

/**
 *  25556. 포스택
 *
 *  문제의 요지 -> 4개의 스택에 주어진 모든 수가 순차적으로 추가 될때 스택의 종류에 상관없이 각 스택의 Last In이 기존의 요소보다 크게
 *  즉, 위에서 아래로 내림 차순을 유지한 상태로 모든 주어진 요소가 주어진 스택에 전부 들어가야 YES가 반환
 *
 *  즉, 각 스택의 내림차순 원칙을 벗어나 스택 안으로 PUSH가 안되는 요소가 있다면 FALSE
 */
public class bj25556 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Deque<Integer> stack1 = new ArrayDeque<>();
        Deque<Integer> stack2 = new ArrayDeque<>();
        Deque<Integer> stack3 = new ArrayDeque<>();
        Deque<Integer> stack4 = new ArrayDeque<>();
        ArrayList<Integer> arrList = new ArrayList<>();
        boolean canSorted = true;

        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            arrList.add(Integer.parseInt(scanner.next()));
        }

        for (Integer i : arrList) {
            if (stack1.isEmpty() || stack1.peek() < i) {
                stack1.push(i);
            } else if (stack2.isEmpty() || stack2.peek() < i) {
                stack2.push(i);
            } else if (stack3.isEmpty() || stack3.peek() < i) {
                stack3.push(i);
            } else if (stack4.isEmpty() || stack4.peek() < i) {
                stack4.push(i);
            } else {
                canSorted = false;
            }
        }

        if (canSorted) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
