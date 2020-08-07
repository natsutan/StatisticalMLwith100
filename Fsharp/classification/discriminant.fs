module discriminant
open MathNet.Numerics.Distributions
open FSharp.Charting

type GaussDistri = 
    { cx :float
      cy :float
      sigma_1 :float
      sigma_2 :float
      rho: float
        }

//Pythonのrandn
let randn():double = 
    Normal(mean=0.0, stddev=1.0).Sample()


let createGD(x:float, y:float,  s1:float,  s2:float,  rho:float ) : GaussDistri =
    {cx = x; cy = y; sigma_1 = s1; sigma_2 = s2; rho = rho}


let generateData(gd:GaussDistri, N:int) = 
    [| for _ in 1 .. N -> (gd.sigma_1 * randn() + gd.cx, gd.sigma_2 * randn() + gd.cy ) |]
    

let plot(data1:System.Tuple<double, double>[], data2:System.Tuple<double, double>[], path) = 
    let chart1 = Chart.Point data1
    let chart2 = Chart.Point data2

    let chart = Chart.Combine [chart1; chart2]
    let output_file = path + @"discri.png"    
    Chart.Save output_file chart
    
    printf "%s\n"  output_file

    None
    