import Data.Char (isAlpha)

decodeRLE :: [(Int, Char)] -> IO ()
decodeRLE xs = putStrLn (concat (map (\x -> replicate (fst x) (snd x)) xs))

printAsItWas :: IO ()
printAsItWas = getLine >>= putStrLn

printReversed :: IO ()
printReversed = getLine >>= (putStrLn . reverse)

printBlank :: IO()
printBlank = getLine >>= putStrLn . (\x -> if x == [] then "empty" else x)

printAndSave :: IO String
printAndSave = getLine >>= \s -> putStrLn s >> pure s

getInteger :: IO Integer
getInteger = getLine >>= (\x -> pure (read x :: Integer))

loopecho :: IO ()
loopecho = getLine >>= (\x -> if x == [] then putStrLn x else putStrLn x >> loopecho)

getSanitized :: IO String
getSanitized = getLine >>= (pure . (filter isAlpha))
