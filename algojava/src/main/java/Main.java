import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Arrays;
import java.util.Random;

public class Main {

    static int N = 100000000;

    static int[] input = new int[N];

    public static void straightInsertionSort(int[] input) {
        for (int i = 1; i < input.length; i++) {
            int key = input[i];
            int j = i - 1;
            while (j >= 0 && input[j] > key) {
                input[j + 1] = input[j];
                j = j - 1;
            }
            input[j + 1] = key;
        }
    }

    public static void straightSelectionSort(final int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minElementIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[minElementIndex] > arr[j]) {
                    minElementIndex = j;
                }
            }

            if (minElementIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minElementIndex];
                arr[minElementIndex] = temp;
            }
        }
    }

    static void bubbleSort(int[] arr)
    {
        int n = arr.length;
        for (int i = 0; i < n-1; i++)
            for (int j = 0; j < n-i-1; j++)
                if (arr[j] > arr[j+1])
                {
                    // swap temp and arr[i]
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
    }

    static void shakerSort(int[] a)
    {
        boolean swapped = true;
        int start = 0;
        int end = a.length;

        while (swapped == true) {
            // reset the swapped flag on entering the
            // loop, because it might be true from a
            // previous iteration.
            swapped = false;

            // loop from bottom to top same as
            // the bubble sort
            for (int i = start; i < end - 1; ++i) {
                if (a[i] > a[i + 1]) {
                    int temp = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = temp;
                    swapped = true;
                }
            }

            // if nothing moved, then array is sorted.
            if (swapped == false)
                break;

            // otherwise, reset the swapped flag so that it
            // can be used in the next stage
            swapped = false;

            // move the end point back by one, because
            // item at the end is in its rightful spot
            end = end - 1;

            // from top to bottom, doing the
            // same comparison as in the previous stage
            for (int i = end - 1; i >= start; i--) {
                if (a[i] > a[i + 1]) {
                    int temp = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = temp;
                    swapped = true;
                }
            }

            // increase the starting point, because
            // the last stage would have moved the next
            // smallest number to its rightful spot.
            start = start + 1;
        }
    }

    public static void main(String[] args) {
        Random random = new Random();

        for (int i = 0; i < N; i++)
            input[i] = Math.abs(random.nextInt(100));

        callMethodWithTime("straightInsertionSort", false);
        callMethodWithTime("straightSelectionSort", false);
        callMethodWithTime("bubbleSort", false);
        callMethodWithTime("shakerSort", false);
    }

    private static void callMethodWithTime(String algorithm, boolean print) {
        int[] temp = input;
        long startTime = System.nanoTime();
        try {
            Method method = Main.class.getMethod(algorithm);
            method.invoke(temp);
            if(print){
                System.out.println(algorithm + Arrays.toString(temp));
            }

        } catch (IllegalAccessException | InvocationTargetException | NoSuchMethodException e) {
            System.out.println(e.getMessage());
        }
        long endTime   = System.nanoTime();
        long totalTime = endTime - startTime;
        System.out.println(algorithm + " :: " + totalTime + " nanoseconds");    }
}
