package com.mayankshekhar.adhoc;

import java.util.HashSet;
import java.util.Set;

public class PlaceHolder {

    private static class Wrapper {

        private int[] input;
        private int i;
        private int j;
        private int hashCode;

        public Wrapper(int[] input, int i, int j, int hashCode) {
            this.input = input;
            this.i = i;
            this.j = j;
            this.hashCode = hashCode;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Wrapper wrapper = (Wrapper) o;
            if (j - i != wrapper.j - wrapper.i) return false;
            int currentStart = i;
            int otherStart = wrapper.i;
            for (int k = 0; k < j - i + 1; k++)
                if (input[currentStart + k] != wrapper.input[otherStart + k]) {
                    return false;
                }
            return true;
        }

        @Override
        public int hashCode() {
            return hashCode;
        }
    }

    public static int getMaxKOddSubarrayCount(int[] input, int k) {
        int result = 0;
        if (input == null || input.length == 0) return result;

        int[] prefixCount = new int[input.length];
        prefixCount[0] = (input[0] % 2 == 1) ? 1 : 0;
        for (int i = 1; i < input.length; i++) prefixCount[i] = ((input[i] % 2 == 1) ? 1 : 0) + prefixCount[i - 1];

        Set<Wrapper> set = new HashSet<Wrapper>();
        for (int i = 0; i < input.length; i++) {
            int hash = 0;
            for (int j = i; j < input.length; j++) {
                hash = (hash * 31) + input[j];
                if ((prefixCount[j] - ((i > 0) ? prefixCount[i - 1] : 0)) <= k) {
                    set.add(new Wrapper(input, i, j, hash));
                }
            }
        }
        return set.size();
    }

    public static void main(String[] args) {
        int[] local = new int[]{3, 2, 3, 4};
        System.out.println(getMaxKOddSubarrayCount(local, 1));
    }
}
