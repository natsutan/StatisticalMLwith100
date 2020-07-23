// Learn more about F# at https://fsharp.org
// See the 'F# Tutorial' project for more help.

let path = @"C:\home\myproj\StatisticalMLwith100\Fsharp\classification\fig\"

[<EntryPoint>]
let main argv =
    
    sigmoid.plotSigmoid path|> ignore

    0 // return an integer exit code
