package lv1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/**
 * 나누어 떨어지는 숫자 배열
 */
public class Lv1_1 {

    public static void main(String[] args) {
        int[] arr = {3, 2, 6};
        int divisor = 10;
        int[] answer = {};
        ArrayList<Integer> save = new ArrayList<>();

        int idx = 0;
        while (idx < arr.length) {
            if (arr[idx] % divisor == 0) {
                save.add(arr[idx]);
            }
            idx++;
        }

        if (save.isEmpty()) 
        }

        Collections.sort(save);
        answer = save.stream().mapToInt(i -> i).toArray(); // mapToInt를 통해 Integer(래퍼 타입) -> int(기본형) 형변환
//        answer = save.toArray(new int[0]);
        System.out.println(Arrays.toString(answer));
    }
}
