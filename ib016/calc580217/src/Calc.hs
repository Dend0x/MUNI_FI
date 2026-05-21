module Calc where

import Data.Ratio
import Text.Parsec
import Text.Parsec.String (Parser)
import Text.Parsec.Expr

data Expr =
      Val Integer
    | Neg Expr
    | Var
    | Add Expr Expr
    | Sub Expr Expr
    | Mul Expr Expr
    | Div Expr Expr
    deriving (Show)


{-
    Evaluates given expression with a value
-}
eval :: Expr -> Rational -> Either String Rational
eval (Val x) _ = Right (fromIntegral x)
eval (Neg ex) x = do
    a <- eval ex x
    pure (-a)
eval Var x = Right x
eval (Add ex1 ex2) x = do
    a <- eval ex1 x
    b <- eval ex2 x
    pure (a + b)
eval (Sub ex1 ex2) x = do
    a <- eval ex1 x
    b <- eval ex2 x
    pure (a - b)
eval (Mul ex1 ex2) x = do
    a <- eval ex1 x
    b <- eval ex2 x
    pure (a * b)
eval (Div ex1 ex2) x = do
    a <- eval ex1 x
    b <- eval ex2 x
    if b == 0 then
        Left "Zero division Err"
    else
        pure (a / b)

{-
    Represents EBNF given in the source
    expr = term | term + expr | term - expr
    term = factor | factor * term | factor / term
    factor = atom | - atom
    atom = ( expr ) | number | x

    With certain differences:
        Negative values are being done in expr to ensure
        that --9 or 5 + - 9 are not valid, so there is only
        one negation allowed
        Terms and factors are built with left association
-}

minus :: Parser (Expr -> Expr)
minus = do
    string "-"
    spaces
    ter <- term
    spaces
    pure (\x -> Sub x ter)

plus :: Parser (Expr -> Expr)
plus = do
    string "+"
    spaces
    ter <- term
    spaces
    pure (\x -> Add x ter)

{-
    Left association is represented in foldl so the functions
    are evaluated from left to right
    Other than that, there is nothing really different from EBNF
-}

expr :: Parser Expr
expr = do
    ter <- try negative <|> term
    spaces
    ops <- many (plus <|> minus)
    let foldOps = foldl (\accum f -> f accum) ter ops
    pure (foldOps)

divd :: Parser (Expr -> Expr)
divd = do
    string "/"
    spaces
    fac <- factor
    spaces
    pure (\x -> Div x fac)

mult :: Parser (Expr -> Expr)
mult = do
    string "*"
    spaces
    fac <- factor
    spaces
    pure (\x -> Mul x fac)

term :: Parser Expr
term = do
    fac <- factor
    spaces
    ops <- many (mult <|> divd)
    let foldOps = foldl (\accum f -> f accum) fac ops
    pure (foldOps)


negative :: Parser Expr
negative = do
    string "-"
    spaces
    neg <- number <|> variable <|> parens
    pure (Neg neg)

factor :: Parser Expr
factor = atom

parens :: Parser Expr
parens = do
    ex <- between (string "(" >> spaces) (string ")" >> spaces) expr
    pure ex

number :: Parser Expr
number = do
    num <- read <$> many1 digit
    spaces
    pure (Val num)

variable :: Parser Expr
variable = do
    var <- string "x"
    spaces
    pure (Var)

atom :: Parser Expr
atom = parens <|> number <|> variable

{-
    Parses input through made parsers
    Makes sure there is no problem with Either Monad
-}

parseExpr :: String -> Either String Expr
parseExpr input = case (parse (expr <* eof) "" input) of
            Left err  -> Left "Invalid input"
            Right x -> Right x


--    Only my test function when UI wasnt working
{-
calculate :: String -> Rational -> Either String Rational
calculate input x = do
    case (parseExpr input) of
        Left err -> Left (show err)
        Right expr -> eval expr x
-}