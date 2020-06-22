module Program



let path = @"C:\home\myproj\StatisticalMLwith100\Fsharp\chap1\LinearRegression\fig\"
let N = 100

let LRrun = false


[<EntryPoint>]
let main argv = 
    // 1.1 線形回帰
    if LRrun then
        let xs, ys = LR.makeData N
        let a, b = LR.min_sq(xs, ys)
        LR.plot_data(xs, ys, a, b, path) |> ignore
        printf "a = %A, b = %A\n" a b

    let X, y = NormalEquation.makedata N
    let beta_hat = NormalEquation.lsm(X, y)

    printf "beta = %A\n" beta_hat

    //  

    0 // return an integer exit code


