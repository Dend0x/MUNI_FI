using System;
using System.Globalization;
using System.Runtime.CompilerServices;

namespace ukol1
{
    class Demo
    {
        static void Sum(int first, int second)
        {
            Console.WriteLine(first + second);
        }

        static string UpperString(char[] letters)
        {
            string word = new string(letters).ToUpper();
            return word;
        }

        static bool DivBySeven(int num)
        {
            if (num % 7 == 0)
            {
                Console.WriteLine("{0} is divisible by 7", num);
                return true;
            }

            Console.WriteLine("{0} is not divisible by 7", num);
            return false;
        }

        static void CountDownTwo(int num)
        {
            if (num % 2 == 1)
                num--;
            while (num > 0)
            {
                Console.WriteLine("{0}", num);
                num -= 2;
            }

            Console.WriteLine("0");
        }

        static int CountArr(int[] arr)
        {
            int sum = 0;

            foreach (int num in arr)
            {
                sum += num;
            }

            return sum;
        }

        static bool LeapYear(int year)
        {
            return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
        }

        static void Main(string[] args)
        {
            CountDownTwo(-5);
        }

    }
}
