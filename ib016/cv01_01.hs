import Control.Monad

swapWords :: String -> String
swapWords = (unwords . reverse . words)

loadWords :: IO ()
loadWords =
    do  s <- getLine
        (putStrLn . reverse) s
        when (not (null s)) loadWords

wordsBackwards :: IO()
wordsBackwards =
    do  s <- getLine
        (putStrLn . swapWords) s
        when (not (null s)) wordsBackwards