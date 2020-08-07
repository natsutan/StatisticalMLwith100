// Learn more about F# at https://fsharp.org
// See the 'F# Tutorial' project for more help.


[<EntryPoint>]
let main argv =
    let path = @"C:\home\myproj\StatisticalMLwith100\Fsharp\classification\fig\"
    
    //sigmoid.plotSigmoid path|> ignore
    let gd1 = discriminant_analysis.createGD(2.0, 2.0, 2.0, 2.0, 0.5)
    let gd2 = discriminant_analysis.createGD(-3.0, -3.0, 1.0, 1.0, -0.8)
    


    0 // return an integer exit code
