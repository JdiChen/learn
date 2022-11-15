package oj;

import java.util.Scanner;

public class A3380 {
    /*输入一个整数数组和一个目标值。数组和目标值以空格分开。
    请在对数组进行排序后，
    找出给定目标值在数组中的开始位置和结束位置（如果只有一个则返回排序后的位置。
    如果数组中不存在目标值 ，则返回排序后的数组最后一个值；
    如果数组或目标值为空，返回-1*/
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] lines = scanner.nextLine().trim().split(" ");
        /*
        拆分字符串后，如果正确拆分则会有两个元素，
        当只有一个元素时，说明数组或者元素有一个缺少
        则返回-1，即出程序
        */
        if (lines.length == 1) {
            System.out.println(-1);
            return;
        }

        int traget = Integer.parseInt(lines[lines.length - 1]);
        String[] nums = lines[0].split(",");

        //转为整形数组
        int[] numsInt = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numsInt[i] = Integer.parseInt(nums[i]);
        }

        //排序
        for (int i = 0; i < numsInt.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (numsInt[i] < numsInt[j]) {
                    int t = numsInt[i];
                    numsInt[i] = numsInt[j];
                    numsInt[j] = t;
                }
            }
        }

        /*
        * count统计出现的次数
        * start为第一次出现的位置
        * end为最后一次出现的位置
        * */
        int count = 0, start = 0, end = 0;
        for (int i = 0; i < numsInt.length; i++) {
            if (traget == numsInt[i]) {
                if (count == 0) {
                    count++;
                    start = i;
                } else {
                    count++;
                    end = i;
                }
            }
        }
        /*count为0 说明没有数组内没有目标值
        * 为1只需要输出首个
        * 大于1则需要输出start和end*/
        if (count == 0) {
            System.out.println(numsInt[numsInt.length - 1]);
        } else if (count == 1) {
            System.out.format("%d", start);
        } else {
            System.out.format("%d,%d", start, end);
        }
    }
}
