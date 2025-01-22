import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class bj10818 {
    /**
     * N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
     */
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] nums = new int[n];

//        for (int i = 0; i < nums.length; i++) {
//            nums[i] = Integer.parseInt(scanner.next());
//        }
        nums = Arrays.stream(nums).map(x -> Integer.parseInt(scanner.next())).toArray();

        // 버블 정렬
        /**
         * do-while문을 통해 일단 로직을 1회 실행
         * boolean을 활용하여 그 다음 순번부터 true일때만 반복문을 진행하도록 설정
         * do-while문 안에서 while문을 통해 배열을 순회하며 최초 오름차순 정렬을 진행 -> index가 while문을 돌때마다 순차 증가하므로 nums의 크기만큼 순회해도 오름차순 정렬이 안끝날 수 있음
         * 이때 계속해서 오름차순 정렬을 진행하기위해 boolean을 활용한 것,, 오름 차순 조건이 만족할 때 해당 변수를 true로 설정하여 오름차순할 것이 남아 있다면 계속 반복문을 진행하도록 설정
         */
        boolean swaped;

        do {
            swaped = false;
            int idx = 0;
            while (idx < n - 1) {
                if (nums[idx] > nums[idx + 1]) {
                    int num = nums[idx];
                    nums[idx] = nums[idx + 1];
                    nums[idx + 1] = num;

                    swaped = true;
                }
                idx++;
            }
        } while (swaped);

        System.out.printf("%d %d", nums[0], nums[nums.length - 1]);






    }
}
