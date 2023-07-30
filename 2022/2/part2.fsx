let readLines (filePath: string) = System.IO.File.ReadLines(filePath)

type Shape (shapeType: string, shapeValue: int) =
    member this.Value = shapeValue
    member this.Type = shapeType
    static member parse (letter: char) =
        match letter with
        | 'A' | 'X' -> Shape("rock", 1)
        | 'B' | 'Y' -> Shape("paper", 2)
        | 'C' | 'Z' -> Shape("scissors", 3)
        | _ -> Shape("", 0)
    member this.wins =
        match this.Type with
        | "rock" -> Shape("scissors", 3)
        | "paper" -> Shape("rock", 1)
        | "scissors" -> Shape("paper", 2)
        | _ -> Shape("", 0)
    member this.loses =
        match this.Type with
        | "rock" -> Shape("paper", 2)
        | "paper" -> Shape("scissors", 3)
        | "scissors" -> Shape("rock", 1)
        | _ -> Shape("", 0)

type Outcome =
    | Win = 6
    | Lose = 0
    | Tie = 3

let outcome (opponent: Shape) (instruction: char) : int =
    match instruction with 
    | 'Y' -> 
        opponent.Value + int Outcome.Tie
    | 'X' -> 
        opponent.wins.Value + int Outcome.Lose
    | 'Z' ->
        opponent.loses.Value + int Outcome.Win
    | _ -> 0

let data: string list = readLines "input.txt" |> Seq.toList
List.map (fun (round: string) -> outcome (Shape.parse(round[0])) round[2]) data |> List.sum |> printfn "%A"
