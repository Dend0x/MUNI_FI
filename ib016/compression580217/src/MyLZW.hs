module MyLZW (Codeword, Encoding, compress, decompress) where

import qualified Data.Map as Map
import qualified Control.Monad.State as State

type Codeword = Int
type Encoding = [Codeword]
type CompressionDict = Map.Map String Codeword
type DecompressionDict = Map.Map Codeword String

{-
    Algorithm works by creating a map of letters of the alphabet + 
    later found substrings of the input

    Every letter (or sequence of letters) found in input has its number (encodeNumber), 
    which will be representing that substring in the output, to make it shorter

    The State monad holds the informations about current dictionary, as it has to lookup
    through found substrings and letters to correctly give a number that is representing it,
    and a nextKey, that is a number (encodeNumber), that will be given to the next newly found
    substring

    During the making of this code I was learning the State Monad from scratch, therefore I
    am using a lot of comments to make it clear to me
-}


-- | CompressionState contains current dictionary and
-- | key, that should be used next
data CompressionState = CompressionState { dictionary :: CompressionDict,
                                           nextKey :: Codeword }

data DecompressionState = DecompressionState { dictionary :: DecompressionDict,
                                               nextKey :: Codeword}

-- map (:[]) converts Char to String, list generator wont work on Strings
compressionDictInit :: CompressionDict
compressionDictInit = Map.fromDistinctAscList $ ("#", 0) : zip (map (:[]) ['A'..'Z']) [1..26]

compressionStateInit :: CompressionState
compressionStateInit = CompressionState compressionDictInit 27

{-

    case 1 - No more letters to work with
        currentState and currentDictionary represent current state of State

        As it is our last iteration through the input, we know, that the substring has to be
        in the dictionary, because of the way how new substrigs were being created, therefore
        I only used Just in pattern to immediattly get the value

        The function returns a State, which is a Monad and because of that I had to pack the value
        of encodeNumber. I preffer pure, as it is less confusing than using return


    case 2
        Getting the current state and newly created substring

        If the created substring is already in the Map, from the algorithm the function
        is just called again with subString as subString + letter 

        If newSubString is not in the Map, then we have to emit the and save the last used subString
        before the new one, that number is represented as encodeNumber

        then we have to update the State that is currently set, that means:
            Adding newSubsString to the dictionary <=> creating new one
            increment encodeNumber, so identifiers are unique
        
        Setting the new State with updated dictionary and nextKey incremented
        State.put removes the previous state and overwrites it with a new one, 
        or simply updates it

        Then is the function recursivily called, on the letters left, [letter] is the
        newly added letter, that is our new start of the substring

        As the encodeNumber is unpacked inside do notation, it has to be packed back, so pure
-}
compressionStep :: String -> String -> State.State CompressionState Encoding
compressionStep subString [] = do
    currentState <- State.get
    let currentDictionary = dictionary currentState
    let Just encodeNumber = Map.lookup subString currentDictionary
    pure [encodeNumber]
compressionStep subString (letter:left) = do
    currentState <- State.get
    let currentDictionary = dictionary currentState
    let newSubString = subString ++ [letter]

    case Map.lookup newSubString currentDictionary of
        Just _ -> compressionStep newSubString left
        Nothing -> do
            let Just encodeNumber = Map.lookup subString currentDictionary
            let newDictionary = Map.insert newSubString (nextKey currentState) currentDictionary
            let newState = CompressionState newDictionary (nextKey currentState + 1)
            State.put newState
            restOfString <- compressionStep [letter] left
            pure (encodeNumber : restOfString)


-- | We simply call a recursive function with "" as the list of current substring
-- | and toEncode as list of what is left to be done
compressionState :: String -> State.State CompressionState Encoding
compressionState toEncode = compressionStep "" toEncode

-- | .evalState - Evaluate a state computation with the given initial state and return
-- | the final value, discarding the final state. - Hoogle
-- | When State is "turned on", it uses CompressionState and returns Encoding
-- | The initial state of State is compressionStateInit
compress :: String -> Encoding
compress toEncode = State.evalState (compressionState toEncode) compressionStateInit

decompressionDictInit :: DecompressionDict
decompressionDictInit = Map.fromDistinctAscList $ (0, "#") : zip (map (:[]) [1..26]) ['A'..'Z']

decompressionStateInit :: DecompressionState
decompressionStateInit = DecompressionState decompressionStateInit 27

decompress :: Encoding -> String
decompress = undefined
