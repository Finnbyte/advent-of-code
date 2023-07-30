let readLines (filePath: string) = System.IO.File.ReadLines(filePath)

let data: int array = readLines "input.txt" |> Seq.toArray |> Array.map (fun x -> if x <> "" then int(x) else 0)

let splitOn (predicate: 'T -> bool) (arr: 'a array) : 'a list list =
    let folder (acc: 'a list list) (elem: 'a) =
        match elem with
        | _ when predicate elem -> [] :: acc // Start a new subarray when predicate is true
        | _  -> (List.head acc @ [elem]) :: List.tail acc // Append the element to the current subarray

    Array.fold folder [[]] arr 
    |> List.rev
    |> List.filter (fun subArr -> subArr <> []) // Filter empty subarrays caused by multiple repeating predicates

data 
|> splitOn (fun x -> x = 0) 
|> List.map (fun sub -> List.reduce (fun acc curr -> acc + curr) sub) 
|> List.sortDescending 
|> List.head
|> printfn "%A"
