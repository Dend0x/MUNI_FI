module Main (main) where

import Test.HUnit
import MyLZW

tests :: Test
tests = TestList [test1, test2, test3, test4, testLazy]

test1 =
    TestCase
        (assertEqual
            "compress ABAB#"
            [1,2,27,0]
            (compress "ABAB#")
        )

test2 =
    TestCase
        (assertEqual
            "compress ABABABABABAB#"
            [1,2,27,29,28,31,0]
            (compress "ABABABABABAB#")
        )

test3 =
    TestCase
        (assertEqual
            "compress AAAAAAAA#"
            [1,27,28,27,0]
            (compress "AAAAAAAA#")
        )

test4 =
    TestCase
        (assertEqual
            "compress FINRODFINGOLFINANDFINARFIN#"
            [6,9,14,18,15,4,27,14,7,15,12,33,1,14,32,28,1,18,33,0]
            (compress "FINRODFINGOLFINANDFINARFIN#")
        )

testLazy =
    TestCase
        (assertBool
            "lazy compress"
            (length (take 10 (compress (cycle "AB"))) == 10)
        )

main :: IO()
main = do
    _ <- runTestTT tests
    pure ()