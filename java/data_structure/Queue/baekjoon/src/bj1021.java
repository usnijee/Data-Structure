import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Scanner;

public class bj1021 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<>();

        int n = Integer.parseInt(scanner.next());
        int m = Integer.parseInt(scanner.next());
        scanner.nextLine();
        String[] nums = scanner.nextLine().split(" ");

        for (int i = 1; i <= n; i++) {
            deque.offerLast(i);
        }

        int idx = 0;
        int minSum = 0;
        boolean isCloseFirst;

        while (idx < m) {
            int selectNum = Integer.parseInt(nums[idx]);
            isCloseFirst = compareMidOf(selectNum, deque);
            int cnt1 = 0;
            int cnt2 = 0;

            if (isCloseFirst) {
                while (true) {
                    if (deque.getFirst() == selectNum) {
                        deque.pollFirst();
                        break;
                    }
                    makeCW(deque);
                    cnt1++;
                }
            } else if (!isCloseFirst) {

                while (true) {
                    if (deque.getFirst() == selectNum) {
                        deque.pollFirst();
                        break;
                    }
                    makeCounterCW(deque);
                    cnt2++;
                }
            }

            minSum += cnt1 > cnt2 ? cnt1 : cnt2;
            idx++;
        }
        System.out.println(minSum);
    }

    private static boolean compareMidOf(int selectNum, Deque<Integer> deque) {
        ArrayList<Integer> dequeAsList = new ArrayList<>(deque);
        int middleValueIdx = deque.size() / 2;
        int selectNumIdx = dequeAsList.indexOf(selectNum);

        // selectNum 즉, 대상이 deque의 중앙보다 앞에 존재시 true 반환
        if (selectNumIdx <= middleValueIdx) {
            return true;
        } else {
            return false;
        }
    }

    private static void makeCW(Deque<Integer> deque) {
        int num = deque.pollFirst();
        deque.offerLast(num);
    }

    private static void makeCounterCW(Deque<Integer> deque) {
        int num = deque.pollLast();
        deque.offerFirst(num);
    }



}
