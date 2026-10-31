using System;

namespace pb006
{
    class Task01
    {
        public static int SigSumRec(int target, int[] seq, int index, int curSum)
        {
            if (index >= seq.Length)
            {
                return curSum;
            }

            int plusS = SigSumRec(target, seq, index + 1, curSum + seq[index]);
            int minusS = SigSumRec(target, seq, index + 1, curSum - seq[index]);

            int plusD = Math.Abs(plusS - target);
            int minusD = Math.Abs(minusS - target);

            if (plusD < minusD)
                return plusS;
            if (plusD > minusD)
                return minusS;
            return Math.Min(plusS, minusS);
        }

        public static int SigSum(int target, int[] seq)
        {
            return SigSumRec(target, seq, 1, seq[0]);
        }
    }

    class Task02
    {
        public static char[] Classify(int from, int to)
        {
            char[] result = new char[to - from + 1];

            for (int i = from; i <= to; i++)
            {
                int divSum = 1;

                for (int div = 2; div * div <= i; div++)
                {
                    if (i % div == 0)
                    {
                        if (div * div != i)
                            divSum += div;
                        divSum += i / div;
                    }
                }

                int index = i - from;

                if (divSum == i)
                    result[index] = 'D';
                else if (divSum < i)
                    result[index] = 'N';
                else
                    result[index] = 'H';
            }

            return result;
        }
    }

    class Task03
    {
        public static string Verbalize(string sentence)
        {
            string[] numsToWords = new string[] {"zero", "one", "two", "three", "four",
                                                "five", "six", "seven", "eight", "nine"};

            string result = "";
            int i = 0;

            while (i < sentence.Length)
            {
                char c = sentence[i++];

                if (c != '#')
                {
                    result += c;
                    continue;
                }

                if (sentence[i] == '#')
                {
                    result += '#';
                    i++;
                    continue;
                }

                while (i < sentence.Length && sentence[i] >= '0' && sentence[i] <= '9')
                {
                    result += numsToWords[sentence[i] - '0'];
                    i++;
                }
            }

            return result;
        }
    }
}
