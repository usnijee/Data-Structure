import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.stream.IntStream;

/**
 * 요세푸스 링크드리스트로 구현하기
 */
public class bj1158 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        LinkedList<Integer> list = new LinkedList<>();
        ArrayList<Integer> result = new ArrayList<>();

        int n = Integer.parseInt(scanner.next());
        int k = Integer.parseInt(scanner.next());

//        for (int i = 1; i <= n; i++) {
//            list.add(i);
//        }

        IntStream.range(1, n + 1).forEach(list::add);

        k -= 1;
        for (int i = 0; i < n; i++) {
            int loop = k;
            while (loop-- > 0) { // 이 부분이 관건 -> 각 i 마다 한바퀴씩 돌릴것
                list.add(list.remove(0));
            }
            result.add(list.remove(0));
        }

        System.out.println(result);

    }
}
