module Confidence

open MathNet.Numerics.LinearAlgebra
open MathNet.Numerics.Distributions
open FSharp.Charting

let makeData (N:int) =
    let X = DenseMatrix.init N 2 (fun i j -> if j = 0 then 1.0 else lib.randn())
    let beta = vector  [1.0; 1.0]
    let epsilon = Vector<double>.Build.Random(N)

    let y = X * beta + epsilon

    X, y

let fit (X:Matrix<double>, Y:Vector<double>) =
    //U = np.linalg.inv(X.T@X)
    //beta_hat = U@X.T@y
    let U =  (X.Transpose() * X).Inverse() 
    let beta_hat = U * X.Transpose() * Y

    beta_hat, U

let RSE (X:Matrix<double>, Y:Vector<double>, beta_hat:Vector<double>, N:int, p:int) :double = 
    let RSS = (Y - X*beta_hat).L2Norm() ** 2.0
    let RSE = (RSS / float((N-p-1))) ** 0.5

    RSE

let conficeInterval(x, beta_hat:Vector<double>, U:Matrix<double>, prediction:bool, rate:double, rse:double, N, p) = 
    let x2 : Vector<double> =  vector [1.0; x] 
    let x2_t = matrix [[1.0]; [x]]

    let a = if prediction then 1.0 else 0.0
    let tmp1:Vector<double> = x2 * U
    let tmp2:Vector<double> = tmp1 * x2_t 
    let ppf = StudentT.InvCDF(x, 1.0,  float(N - p) - 1.0, rate)
    if ppf < 0.0 then printf "-"


    let r = ppf * rse * ((a + tmp2.[0]) ** 0.5)

    let lower = x2 * beta_hat - r
    let upper = x2 * beta_hat + r
    lower, upper

let pred(x, beta) = 
    let x2 : Vector<double> =  vector [1.0; x] 
    x2 * beta

let plot(path, beta_hat:Vector<double>, U:Matrix<double>, rate:double, rse:double, N, p) =
    let mutable chart_list = []

    let output_file = path + @"ci.png"

    //回帰曲線

    let chart = Chart.Line( [for x in -10.0 .. 0.1 .. 10.0 -> x, pred(x, beta_hat) ], Color=System.Drawing.Color.Black)
    chart_list <- chart :: chart_list

    //信頼区間

    let chart = Chart.Line( [for x in -10.0 .. 0.1 .. 10.0 -> x, fst(conficeInterval(x, beta_hat, U, false, 0.95,rse,  N, p)) ], 
                            Color=System.Drawing.Color.Red)
    chart_list <- chart :: chart_list
    let chart = Chart.Line( [for x in -10.0 .. 0.1 .. 10.0 -> x, snd(conficeInterval(x, beta_hat, U, false, 0.95,rse,  N, p)) ], 
                            Color=System.Drawing.Color.Blue)
    chart_list <- chart :: chart_list

    //予測区間




    let chart_comb = Chart.Combine chart_list
    Chart.Save output_file chart_comb
    None

    //let upper, lower = Confidence.conficeInterval(0.0, beta_hat, U, false, 0.95, RSE, N, p)
    
//    def f(x, a):
//    x = np.array([1, x])
//    r = stats.t.ppf(0.975, df=N-p-1) * RSE *np.sqrt(a+x@U@x.T)
//    lower = x@beta_hat - r
//    upper = x@beta_hat + r
//    return [lower, upper]

