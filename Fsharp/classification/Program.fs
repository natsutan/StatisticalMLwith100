// Learn more about F# at https://fsharp.org
// See the 'F# Tutorial' project for more help.
open discriminant

let path = @"C:\home\myproj\StatisticalMLwith100\Fsharp\classification\fig\"
let N = 100

[<EntryPoint>]
let main argv =
    
    //sigmoid.plotSigmoid path|> ignore
    let gd1 = {GaussDistri.cx = 2.0; GaussDistri.cy = 2.0; 
               GaussDistri.sigma_1 = 2.0; GaussDistri.sigma_2 = 2.0; 
               GaussDistri.rho = 0.5}
    let gd2 = {GaussDistri.cx = -3.0; GaussDistri.cy = -3.0; 
                GaussDistri.sigma_1 = 1.0; GaussDistri.sigma_2 = 1.0; 
                GaussDistri.rho = -0.8}
 
    let data1 = discriminant.generateData(gd1, N)
    let data2 = discriminant.generateData(gd2, N)

    discriminant.plot(data1, data2, path) |> ignore

    0 // return an integer exit code
