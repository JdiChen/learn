
package oj;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class A3381 {

    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            String str = scanner.nextLine().trim().replaceAll("-", "").replaceAll(" ", "");
            List<String> list = new ArrayList<>();
            /*
            1.先判断输入字串总长是否大于4
            2.取前3位子串添加到列表中
            3.去掉前3位取的子串重新赋值，重新计算，直到子串长度小于等于4
            */
            while (str.length() > 4) {
                list.add(str.substring(0, 3));
                str = str.substring(3);
            }
            StringBuilder sb = new StringBuilder();
            /*
            * 小于4时，不会向列表添加子串，下方for也就不会执行添加
            * 如果大于4，说明3位子串后肯定会有字符
            * 所以可以直接在每一项后加 -
            * */
            for (String item : list) {
                sb.append(item).append("-");
            }
            /*
            * 这里是长度小于等于4时的输出，拼接前面
            * */
            if (str.length() == 4) {
                sb.append(str, 0, 2).append("-").append(str, 2, 4);
            } else {
                sb.append(str);
            }
            System.out.println(sb);

    }
}

