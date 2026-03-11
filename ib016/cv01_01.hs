import Control.Monad

swapWords :: String -> String
swapWords = (unwords . reverse . words)

loadWords :: IO ()
loadWords =
    do  s <- getLine
        (putStrLn . reverse) s
        when (not (null s)) loadWords

loadWords' :: IO()
loadWords' = interact (\s -> reverse s)

wordsBackwards :: IO()
wordsBackwards =
    do  s <- getLine
        (putStrLn . swapWords) s
        when (not (null s)) wordsBackwards

getInteger :: IO Integer
getInteger = getLine >>= (\s -> pure (read s :: Integer))

main' :: IO ()
main' =
    do  putStrLn "Enter number:"
        x <- getInteger
        y <- getInteger
        z <- getInteger
        if x + y > z && x + z > y && y + z > x then putStrLn "Ano" else putStrLn "Ne"

sumNums :: IO ()
sumNums = sumNums' 0

sumNums' :: Integer -> IO ()
sumNums' x =
    do  s <- getInteger
        if s == 0 then putStrLn (show x) else sumNums' (x + s)

sumNums2 :: IO()
sumNums2 = 
    do  s <- getIntegers
        putStrLn (show (sum s))

getIntegers :: IO [Integer]
getIntegers =
    do  s <- getInteger
        if s == 0 then pure [] else
            do  rest <- getIntegers
                pure (s : rest)

fill :: Integer -> Integer -> Integer -> Integer -> IO()
fill x y w h = if x == w then putStrLn "" >> (fill 0 (y + 1) w h) else
               if y == h then putStrLn "" else
               putStr "#" >> (fill (x + 1) y w h)

rectangleFill :: IO ()
rectangleFill =
    do  w <- getInteger
        h <- getInteger
        fill 0 0 w h
