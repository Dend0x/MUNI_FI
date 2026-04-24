module Main where

import Calc
import Data.Char (isDigit)
import Data.Ratio (denominator, numerator)

menu :: IO ()
menu = do
    putStrLn "----------------------------------------"
    putStrLn "menu"
    putStrLn "  - prints menu"
    putStrLn "set (expression):"
    putStrLn "  - sets function f to expression"
    putStrLn "get"
    putStrLn "  - prints current function"
    putStrLn "eval (value)"
    putStrLn "  - calculates function with given value"
    putStrLn "exit"
    putStrLn "  closes Calculator"
    putStrLn "----------------------------------------"

{-
    set - sets new function loaded, goes along with rep (represent) that is a string of current input
    get - prints current loaded function, its rep
    menu - prints menu above
    eval - takes an Integer as input and calls eval to calculate the result value of function
    exit - closes app
-}

loop :: Maybe Expr -> String -> IO ()
loop fun rep = do
    input <- getLine
    let sep_input = words input
    case sep_input of
        ("set":rest) -> 
            let new_fun = unwords rest in
                case parseExpr new_fun of
                    Left err -> do
                        putStrLn err
                        loop fun rep
                    Right ex -> do
                        putStrLn $ "f(x) = " ++ new_fun
                        loop (Just ex) new_fun
        ("get":rest) ->
            case fun of
                Nothing -> do
                    putStrLn "Function not set"
                    loop fun rep
                Just _ -> do
                    putStrLn $ "f(x) = " ++ rep
                    loop fun rep
        ("menu":_) -> do
            menu
            loop fun rep
        ("eval":rest) -> 
            case fun of
                Nothing -> do
                    putStrLn "Tried to evaluate without a set function"
                    loop fun rep
                Just ex -> do
                    let val = head rest
                    if all isDigit val then
                        do
                            let x = fromIntegral (read val :: Integer)
                            case eval ex x of
                                Left err -> do
                                    putStrLn "Error while computing"
                                    loop fun rep
                                Right result -> do
                                    putStr $ "f(" ++ val ++ ") = "
                                    if denominator result == 1 then do
                                        putStrLn $ show (numerator result)
                                    else do
                                        putStrLn $ show (numerator result) ++ " / " ++ show (denominator result)
                                    loop fun rep
                    else
                        do
                            putStrLn "Invalid parameter"
                            loop fun rep
        ("exit":_) ->
            do
                putStrLn "Exiting..."

        _ -> do
            putStrLn "Not recognizes command"
            loop fun rep

-- Nothing "" is a starting point for loaded fun
main :: IO ()
main = do
    menu
    loop Nothing ""